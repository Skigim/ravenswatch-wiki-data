"""Build the readable Markdown pages in browse/ from the TSV tables in data/.

Run from the repository root:  python tools/build_browse.py

The TSVs stay the canonical source. This script only reads them and rewrites
browse/ from scratch, so never edit browse/ by hand.
"""

import csv
import re
import shutil
import sys
from collections import OrderedDict, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
OUT = ROOT / "browse"
REPO_URL = "https://github.com/Skigim/ravenswatch-wiki-data/blob/main"

csv.field_size_limit(sys.maxsize if sys.maxsize < 2**31 else 2**31 - 1)

# Hero file ids in the order the game lists them is not in the data, so use
# alphabetical order of the display name (worked out after loading).
HERO_IDS = [
    "Aladdin", "Beowulf", "Carmilla", "Geppetto", "Juliet", "Kintaro",
    "Melusine", "Merlin", "Piper", "RED", "Romeo", "Snow_Queen", "SunWukong",
]

GENERATED_NOTE = (
    "*This page is generated from the TSV files in [data/](../data/) by "
    "`tools/build_browse.py`. Do not edit it by hand; fix the data and "
    "re-run the script.*"
)


# ---------------------------------------------------------------- reading

def read_table(name):
    """Return (meta, rows) for data/<name>. meta holds the '# key<TAB>value' lines."""
    meta = OrderedDict()
    lines = []
    with open(DATA / name, encoding="utf-8", newline="") as f:
        for line in f:
            if not lines and line.startswith("#"):
                key, _, value = line[1:].strip().partition("\t")
                meta[key.strip()] = value.strip()
            else:
                lines.append(line)
    rows = list(csv.DictReader(lines, delimiter="\t"))
    return meta, rows


def text_by_key(name):
    _, rows = read_table(name)
    return {r["key"]: r["text_en"] for r in rows if r.get("key")}


# ---------------------------------------------------------------- formatting

MARKUP = re.compile(
    r"#(?P<hl>[^#@]+?)@"        # #term@      highlighted term
    r"|&(?P<pos>[^&~]+?)~"      # &text~      positive value
    r"|\$(?P<neg>[^$*]+?)\*"    # $text*      negative value
    r"|\\(?!n)(?P<alt>[^\\§]+?)§"  # \term§  alternate highlight
    r"|(?P<nl>\\n)"             # literal \n  line break
    r"|(?P<ph>\{\d*\})"         # {0} or {}   runtime placeholder
)

MD_SPECIAL = re.compile(r"([\\`*_\[\]<>|])")


def esc(text):
    """Escape characters Markdown would otherwise treat as formatting."""
    return MD_SPECIAL.sub(r"\\\1", text)


def game_text(text, newline="<br>"):
    """Turn game markup into Markdown. Placeholders stay visible as {0}."""
    if text is None:
        return ""
    out = []
    pos = 0
    for m in MARKUP.finditer(text):
        out.append(esc(text[pos:m.start()]))
        if m.group("nl"):
            out.append(newline)
        elif m.group("ph"):
            out.append("`" + m.group("ph") + "`")
        else:
            inner = m.group("hl") or m.group("pos") or m.group("neg") or m.group("alt")
            inner = game_text(inner, newline).strip()
            out.append("**" + inner + "**" if inner else "")
        pos = m.end()
    out.append(esc(text[pos:]))
    return "".join(out).strip()


def plain(text):
    return esc((text or "").replace("\\n", " ")).strip()


def table(headers, rows):
    if not rows:
        return "_No rows._\n"
    lines = ["| " + " | ".join(headers) + " |",
             "|" + "|".join("---" for _ in headers) + "|"]
    for row in rows:
        cells = [(c if c not in (None, "") else " ") for c in row]
        lines.append("| " + " | ".join(cells) + " |")
    return "\n".join(lines) + "\n"


def slug(name):
    s = name.replace("ō", "o").replace("Ō", "O")
    s = re.sub(r"[^A-Za-z0-9]+", "_", s).strip("_")
    return s


def source_line(*files):
    links = ", ".join(f"[`{f}`](../data/{f})" for f in files)
    return f"Source: {links}."


def write(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8", newline="\n")


def rel_source(files, depth):
    up = "../" * depth
    links = ", ".join(f"[`{f}`]({up}data/{f})" for f in files)
    return f"Source: {links}."


def note(depth):
    return GENERATED_NOTE.replace("](../data/)", "](" + "../" * depth + "data/)")


# ---------------------------------------------------------------- values tables

STATUS = {
    "decoded": "Decoded",
    "decoded-baseline": "Decoded (baseline)",
    "static-text": "Fixed text",
    "symbolic": "Formula",
    "existing-table": "Earlier table",
    "unresolved": "Not decoded",
}


def show_value(r):
    value = r.get("value", "")
    if value == '""':
        return "*(empty)*"
    if value == "" and r.get("status") == "unresolved":
        return "*not decoded*"
    if value == "" and r.get("formula"):
        return "`" + r["formula"].replace("|", "\\|") + "`"
    if r.get("unit") == "text":
        return game_text(value)
    return plain(value)


def show_unit(unit):
    if unit in ("", "text", "unknown", "rule", "notes", "condition", "formula"):
        return ""
    return plain(unit.replace("_", " "))


def show_field(field):
    words = [w for w in field.split("_") if w != "pct"]
    return plain(" ".join(words))


def show_check(r):
    check = r.get("maintainer_check", "")
    cv = plain(r.get("checked_value", ""))
    src = r.get("checked_value_source", "")
    if check == "read in game: match":
        return "Matches the game"
    if check in ("read in game: differs from decoded value", "read in game: no decoded value"):
        return f"Game shows {cv}"
    if check.startswith("stale"):
        return f"Game showed {cv} on 1.05; changed in 1.06"
    if src.startswith("fill pass") and r.get("value", "") == "" and cv:
        return f"Second decoding pass: {cv}"
    return ""


def values_section(rows, group_key="section"):
    """Group a values table by section and render one table per section."""
    out = []
    groups = OrderedDict()
    for r in rows:
        if r.get("field") == "tooltip_binding_coverage":
            continue  # a copy of the tooltip text, already shown above
        groups.setdefault(r.get(group_key) or "Other", []).append(r)
    for section, items in groups.items():
        out.append(f"### {plain(section)}\n")
        body = []
        for r in items:
            name = plain(r.get("name", ""))
            form = r.get("form_or_condition", "")
            if form and form not in ("Base", "main effect"):
                name += f" ({plain(form)})"
            body.append([name, show_field(r["field"]), show_value(r),
                         show_unit(r.get("unit", "")), STATUS.get(r["status"], plain(r["status"])),
                         show_check(r)])
        out.append(table(["Name", "Stat", "Value", "Unit", "Status", "In-game check"], body))
    return "\n".join(out)


VALUES_KEY = """\
**How to read the values**

- **Decoded** values come straight from the game files.
- **Decoded (baseline)** values assume a level 1 hero with damage 10, healing 10, no talents and no Magical Objects.
- **Not decoded** means nobody has found the number yet. It does not mean zero.
- **In-game check** shows what the maintainer read in the game's Compendium, when that was checked.
"""

TEXT_KEY = """\
**How to read the text**

- **Bold** words are highlighted in the game.
- `{0}`, `{1}` and so on are numbers or names the game fills in while you play.
"""


# ---------------------------------------------------------------- heroes

def ability_rows(common):
    """Return [(slot, name, description)] for the hero's abilities."""
    slots = OrderedDict()
    for key in common:
        m = re.match(r"Ability_(.+)_Name$", key)
        if m:
            slots[m.group(1)] = key
    rows = []
    for slot, name_key in slots.items():
        desc = common.get(f"Ability_{slot}_Update6_Desc") or common.get(f"Ability_{slot}_Desc", "")
        rows.append((slot.replace("_", " "), common[name_key], desc))
    return rows


def rank(t):
    try:
        return int(t["unlock_rank"])
    except (KeyError, ValueError):
        return 99


def ultimate_number(t):
    """Which ultimate (1 or 2) an upgrade talent belongs to, from its text key or controller."""
    m = re.match(r"Skill_Ultimate_(\d)_", t["name_key"]) or re.search(r"U\w*timate (\d)", t["controller"])
    return m.group(1) if m else ""


def talents_section(common, talents):
    upgrades = [t for t in talents if t["name_key"].startswith("Skill_Ultimate")]
    rest = [t for t in talents if t not in upgrades]
    # The tables do not record which talents are offered at level 1 of a run,
    # so there is no Starting talents group until an export provides that.
    others = sorted(rest, key=lambda t: (rank(t), t["name"]))

    def row(t):
        return [game_text(t["name"]), plain(t["unlock_rank"]), game_text(t["effect_en"])]

    ult_names = {}
    ultimates = []
    for n in ("1", "2"):
        name = common.get(f"Skill_Ultimate_{n}_Name") or common.get(f"Ability_Ultimate_{n}_Name")
        if not name:
            continue
        ult_names[n] = game_text(name)
        desc = (common.get(f"Skill_Ultimate_{n}_Update6_Desc") or common.get(f"Skill_Ultimate_{n}_Desc")
                or common.get(f"Ability_Ultimate_{n}_Desc", ""))
        ultimates.append([ult_names[n], game_text(desc)])

    upgrades.sort(key=lambda t: (ultimate_number(t), rank(t), t["name"]))

    out = ["## Talents\n",
           "Values separated by / are for Common / Rare / Epic / Legendary.\n",
           "**Unlocks at rank** is the hero rank, not the level reached in a run.\n",
           "### Ultimates\n",
           "The talent tables do not include the base ultimates or their unlock ranks; this text is from the hero's text table.\n",
           table(["Ultimate", "Description"], ultimates),
           "### Ultimate upgrades\n",
           table(["Talent", "Upgrades", "Unlocks at rank", "Effect"],
                 [[game_text(t["name"]), ult_names.get(ultimate_number(t), ""), plain(t["unlock_rank"]),
                   game_text(t["effect_en"])] for t in upgrades]),
           "### Other talents\n",
           table(["Talent", "Unlocks at rank", "Effect"], [row(t) for t in others])]
    return "\n".join(out)


def skins(skin_text):
    groups = OrderedDict()
    for key, text in skin_text.items():
        m = re.match(r"(.+)_(Title|Description|UnlockCondition)$", key)
        if m:
            groups.setdefault(m.group(1), {})[m.group(2)] = text
    return [[game_text(g.get("Title", "")), game_text(g.get("UnlockCondition", "")),
             game_text(g.get("Description", ""))] for g in groups.values()]


def memoir_page(hero_name, memoir_text, file):
    out = [f"# {hero_name}: memoir\n", f"[← {hero_name}](../heroes/{slug(hero_name)}.md) · [All tables](../README.md)\n"]
    title = next((t for k, t in memoir_text.items() if re.match(r".+_Memoir_Title$", k)), "")
    if title:
        out.append(f"## {plain(title)}\n")
    chapters = OrderedDict()
    for key, text in memoir_text.items():
        m = re.match(r".+_Memoir(\d+)_(Title|Desc)$", key)
        if m:
            chapters.setdefault(int(m.group(1)), {})[m.group(2)] = text
    for n in sorted(chapters):
        ch = chapters[n]
        out.append(f"### {plain(ch.get('Title', f'Chapter {n}'))}\n")
        out.append(game_text(ch.get("Desc", ""), newline="\n") + "\n")
    out.append(TEXT_KEY)
    out.append(rel_source([file], 2) + "\n")
    out.append(note(2))
    return "\n".join(out)


def hero_page(hid, name, common, talents_meta, talents, abilities_meta, abilities, skin_rows, has_memoir):
    s = slug(name)
    out = [f"# {name}\n", "[All tables](../README.md)\n"]
    links = ["[Abilities](#abilities)", "[Ability values](#ability-values)", "[Talents](#talents)", "[Outfits](#outfits)"]
    if has_memoir:
        links.append(f"[Memoir](../memoirs/{s}.md)")
    out.append(" · ".join(links) + "\n")

    if common.get("Hero_Desc"):
        out.append(game_text(common["Hero_Desc"], newline="\n\n") + "\n")

    out.append("## Abilities\n")
    out.append(table(["Slot", "Name", "Description"],
                     [[plain(slot), game_text(n), game_text(d)] for slot, n, d in ability_rows(common)]))
    dash = common.get("Ability_Dash_Desc")
    if dash:
        out.append(f"\n**Dash:** {game_text(dash)}\n")

    out.append("## Ability values\n")
    out.append(VALUES_KEY)
    if abilities_meta.get("baseline"):
        out.append(f"Baseline for this hero: {plain(abilities_meta['baseline'])}\n")
    out.append(values_section(abilities))

    out.append(talents_section(common, talents))

    out.append("## Outfits\n")
    out.append(table(["Outfit", "How to unlock", "Description"], skin_rows))

    out.append("\n" + TEXT_KEY)
    files = [f"Hero_{hid}_Common.LangEN.tsv", f"Hero_{hid}_Abilities.tsv",
             f"Hero_{hid}_Talents.tsv", f"Hero_{hid}_Skins.LangEN.tsv"]
    out.append(rel_source(files, 2))
    version = talents_meta.get("source_version") or abilities_meta.get("source_version")
    if version:
        out.append(f"Game version: {plain(version)}\n")
    out.append(note(2))
    return "\n".join(out)


def build_heroes():
    heroes = []
    for hid in HERO_IDS:
        common = text_by_key(f"Hero_{hid}_Common.LangEN.tsv")
        name = common.get("Hero_Name", hid)
        heroes.append((name, hid, common))
    heroes.sort(key=lambda h: h[0].removeprefix("The "))

    for name, hid, common in heroes:
        t_meta, talents = read_table(f"Hero_{hid}_Talents.tsv")
        a_meta, abilities = read_table(f"Hero_{hid}_Abilities.tsv")
        skin_rows = skins(text_by_key(f"Hero_{hid}_Skins.LangEN.tsv"))
        memoir_file = f"Hero_{hid}_Memoirs.LangEN.tsv"
        memoir = text_by_key(memoir_file)
        write(OUT / "heroes" / f"{slug(name)}.md",
              hero_page(hid, name, common, t_meta, talents, a_meta, abilities, skin_rows, bool(memoir)))
        if memoir:
            write(OUT / "memoirs" / f"{slug(name)}.md", memoir_page(name, memoir, memoir_file))
    return [name for name, _, _ in heroes]


# ---------------------------------------------------------------- objects and melodies

def build_objects():
    text = text_by_key("Magical_Objects.LangEN.tsv")
    _, index = read_table("Magical_Objects_Index.tsv")
    _, values = read_table("Magical_Objects_Values.tsv")
    out = ["# Magical Objects\n", "[All tables](README.md)\n"]
    by_rarity = OrderedDict()
    for r in index:
        by_rarity.setdefault(r["rarity"], []).append(r)
    out.append(" · ".join(f"[{plain(k)}](#{slug(k).lower()})" for k in by_rarity) + " · [Values](#values)\n")
    for rarity, items in by_rarity.items():
        out.append(f"## {plain(rarity)}\n")
        rows = []
        for r in items:
            rows.append([game_text(text.get(r["name_key"], "")),
                         game_text(text.get(r["description_key"], "")),
                         game_text(text.get(r["supereffect_key"], ""))])
        out.append(table(["Object", "Effect", "Collection bonus"], rows))
    out.append("## Values\n")
    out.append(VALUES_KEY)
    out.append(values_section(values))
    out.append("\n" + TEXT_KEY)
    out.append(rel_source(["Magical_Objects_Index.tsv", "Magical_Objects.LangEN.tsv", "Magical_Objects_Values.tsv"], 1))
    out.append(note(1))
    write(OUT / "magical-objects.md", "\n".join(out))


def build_melodies():
    text = text_by_key("Melodies.LangEN.tsv")
    _, index = read_table("Melodies_Index.tsv")
    _, values = read_table("Melodies_Values.tsv")
    out = ["# Melodies\n", "[All tables](README.md)\n"]
    out.append(table(["Melody", "Effect"],
                     [[game_text(text.get(r["name_key"], "")), game_text(text.get(r["description_key"], ""))]
                      for r in index]))
    out.append("## Values\n")
    out.append(VALUES_KEY)
    out.append(values_section(values))
    out.append("\n" + TEXT_KEY)
    out.append(rel_source(["Melodies_Index.tsv", "Melodies.LangEN.tsv", "Melodies_Values.tsv"], 1))
    out.append(note(1))
    write(OUT / "melodies.md", "\n".join(out))


def build_mechanics():
    meta, rows = read_table("Mechanics_Values.tsv")
    out = ["# Shared mechanics\n", "[All tables](README.md)\n",
           "Settings shared by all heroes: reward sources, difficulties, drops, status effects, prices, resources, stats and timers.\n"]
    out.append(VALUES_KEY)
    out.append(values_section(rows))
    out.append(rel_source(["Mechanics_Values.tsv"], 1))
    out.append(note(1))
    write(OUT / "mechanics.md", "\n".join(out))


# ---------------------------------------------------------------- enemies and other reference tables

TECH_COLUMNS = re.compile(
    r"^(source_.*|.*_offset|.*_sha256|.*_path|reference_chain|definition_path|"
    r"map_definition_path|name_text_table|name_text_keys|global_id|selector_offset)$"
)


def generic_table(rows, rename=None, drop=()):
    if not rows:
        return "_No rows._\n"
    cols = [c for c in rows[0].keys() if c and not TECH_COLUMNS.match(c) and c not in drop and c != "limits"]
    rename = rename or {}
    headers = [rename.get(c, c.replace("_", " ").capitalize()) for c in cols]
    body = [[game_text(r.get(c, "")) for c in cols] for r in rows]
    return table(headers, body)


def build_enemies():
    _, defs = read_table("Enemy_Definitions.tsv")
    _, tribes = read_table("Enemy_Tribe_Map_References.tsv")
    _, flags = read_table("Enemy_Definition_Flags.tsv")
    out = ["# Enemies\n", "[All tables](README.md)\n",
           "The game version of these tables is unverified. See [ENEMIES.md](../ENEMIES.md).\n",
           "## Enemies\n",
           "**In-game name** is filled only where the game's own text names the enemy. "
           "**Label** is a description written by the data maintainer, not a game name.\n"]
    out.append(table(["In-game name", "Label", "Tribe", "Internal id"],
                     [[plain(r["localized_name"]), plain(r["readable_label"]),
                       plain(r["tribe_id"].replace("_", " ")), "`" + r["definition_id"] + "`"] for r in defs]))
    out.append("## Tribes by map\n")
    out.append(generic_table(tribes, drop=("limits",)))
    out.append("## Flags\n")
    out.append(generic_table(flags))
    out.append(rel_source(["Enemy_Definitions.tsv", "Enemy_Tribe_Map_References.tsv", "Enemy_Definition_Flags.tsv"], 1))
    out.append(note(1))
    write(OUT / "enemies.md", "\n".join(out))


def build_reference(title, intro, doc, files, out_name):
    out = [f"# {title}\n", "[All tables](README.md)\n", intro + f" See [{doc}](../{doc}) for what each column means and what the data cannot show.\n"]
    for f in files:
        _, rows = read_table(f)
        heading = f.removesuffix(".tsv").replace("_", " ")
        out.append(f"## {heading}\n")
        out.append(generic_table(rows))
    out.append(rel_source(files, 1))
    out.append(note(1))
    write(OUT / out_name, "\n".join(out))


# ---------------------------------------------------------------- dialogue

def build_dialogue(hero_names):
    _, rows = read_table("Dialogue_Lines.tsv")
    by_speaker = defaultdict(list)
    for r in rows:
        by_speaker[(r.get("speaker") or "").strip() or "Unknown speaker"].append(r)

    def lines_table(items, with_speaker=False):
        body = []
        for r in items:
            row = [game_text(r["text_en"]), plain(r.get("trigger_situation", "")), plain(r.get("target", ""))]
            if with_speaker:
                row.insert(0, plain(r["speaker"]) or "*unknown*")
            body.append(row)
        headers = ["Line", "When", "Said to"]
        if with_speaker:
            headers.insert(0, "Speaker")
        return table(headers, body)

    index = ["# Dialogue\n", "[All tables](../README.md)\n",
             "Spoken lines from the game, grouped by speaker. **When** describes the situation that triggers the line; "
             "see [DIALOGUE.md](../../DIALOGUE.md) for how it was worked out.\n",
             "## Heroes\n"]
    hero_set = set(hero_names)
    for name in hero_names:
        items = by_speaker.get(name, [])
        if items:
            index.append(f"- [{name}]({slug(name)}.md) ({len(items)} lines)")
            page = [f"# {name}: dialogue\n", "[All dialogue](README.md) · "
                    f"[{name}](../heroes/{slug(name)}.md)\n", lines_table(items), "\n" + TEXT_KEY,
                    rel_source(["Dialogue_Lines.tsv"], 2), note(2)]
            write(OUT / "dialogue" / f"{slug(name)}.md", "\n".join(page))
    others = [(k, v) for k, v in by_speaker.items() if k not in hero_set]
    others.sort(key=lambda kv: (-len(kv[1]), kv[0]))
    index.append("\n## Other characters\n")
    small = []
    for speaker, items in others:
        if len(items) >= 20:
            index.append(f"- [{plain(speaker)}]({slug(speaker)}.md) ({len(items)} lines)")
            page = [f"# {plain(speaker)}: dialogue\n", "[All dialogue](README.md)\n", lines_table(items),
                    "\n" + TEXT_KEY, rel_source(["Dialogue_Lines.tsv"], 2), note(2)]
            write(OUT / "dialogue" / f"{slug(speaker)}.md", "\n".join(page))
        else:
            small.extend(items)
    if small:
        index.append(f"- [Everyone else](Others.md) ({len(small)} lines)")
        page = ["# Other speakers: dialogue\n", "[All dialogue](README.md)\n",
                "Speakers with fewer than 20 lines.\n", lines_table(small, with_speaker=True),
                "\n" + TEXT_KEY, rel_source(["Dialogue_Lines.tsv"], 2), note(2)]
        write(OUT / "dialogue" / "Others.md", "\n".join(page))
    index += ["", rel_source(["Dialogue_Lines.tsv"], 2), note(2)]
    write(OUT / "dialogue" / "README.md", "\n".join(index))


# ---------------------------------------------------------------- index

def build_index(hero_names):
    out = ["# Browse the data\n",
           "Readable versions of the tables in [data/](../data/). Pick a page below. "
           "To cite a fact on the wiki, cite the TSV file and commit listed at the bottom of each page.\n",
           "## Heroes\n",
           "Each page has the hero's abilities, ability values, talents and outfits.\n",
           " · ".join(f"[{n}](heroes/{slug(n)}.md)" for n in hero_names) + "\n",
           "Memoirs: " + " · ".join(f"[{n}](memoirs/{slug(n)}.md)" for n in hero_names
                                     if (OUT / "memoirs" / f"{slug(n)}.md").exists()) + "\n",
           "## Items and effects\n",
           "- [Magical Objects](magical-objects.md)",
           "- [Melodies](melodies.md)",
           "- [Shared mechanics](mechanics.md)\n",
           "## World\n",
           "- [Enemies](enemies.md)",
           "- [Enemy combat settings](combat.md)",
           "- [Map generation](map-generation.md)\n",
           "## Dialogue\n",
           "- [Spoken lines by speaker](dialogue/README.md)\n",
           "## Not shown here\n",
           "These tables are for checking the data and have no readable page. Open the TSV directly:\n",
           "- [`Voice_Lines_Audio.tsv`](../data/Voice_Lines_Audio.tsv): where each line's recording sits in the audio files",
           "- [`In_Game_Observations.tsv`](../data/In_Game_Observations.tsv) and [`Fill_Pass_Values.tsv`](../data/Fill_Pass_Values.tsv): the evidence behind the **In-game check** column",
           "- [`Magical_Objects_Sources.tsv`](../data/Magical_Objects_Sources.tsv): rarity chances set on reward sources",
           "- [`Common.LangEN.tsv`](../data/Common.LangEN.tsv) and [`Enemy_Common.LangEN.tsv`](../data/Enemy_Common.LangEN.tsv): general interface and enemy text",
           "- [`Hero_Memoirs_Corrections.tsv`](../data/Hero_Memoirs_Corrections.tsv): spelling fixes made to the memoirs\n",
           note(1)]
    write(OUT / "README.md", "\n".join(out))


def main():
    if OUT.exists():
        shutil.rmtree(OUT)
    hero_names = build_heroes()
    build_objects()
    build_melodies()
    build_mechanics()
    build_enemies()
    build_reference("Enemy combat settings",
                    "Stored combat constants, picker roles and difficulty damage factors. "
                    "There is no confirmed final-damage formula.",
                    "COMBAT.md",
                    ["Enemy_Combat_Values.tsv", "Enemy_Combat_Picker_Values.tsv", "Enemy_Chapter_Damage_Factors.tsv"],
                    "combat.md")
    build_reference("Map generation",
                    "Resource roles, weights, quotas, caps, tier bands and probability models used when maps are built.",
                    "MAP_GENERATION.md",
                    ["Map_Generation_References.tsv", "Map_Generation_Weights.tsv", "Map_Generation_Quotas.tsv",
                     "Map_Generation_Caps.tsv", "Map_Tile_Tier_Bands.tsv", "Map_Stash_Models.tsv",
                     "Map_Generation_Observations.tsv"],
                    "map-generation.md")
    build_dialogue(hero_names)
    build_index(hero_names)
    print(f"Wrote {sum(1 for _ in OUT.rglob('*.md'))} pages to {OUT}")


if __name__ == "__main__":
    main()
