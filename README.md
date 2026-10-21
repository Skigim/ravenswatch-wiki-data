# Ravenswatch wiki data

Selected decoded tables prepared for contributors to the [Ravenswatch Wiki](https://ravenswatch.wiki.gg/).

This repository is the canonical source for 91 selected TSV tables used to write and check wiki articles: 46 decoded text and index exports, 13 numerical talent tables, 18 numerical value tables, 3 enemy reference tables, 3 combat-configuration tables, 7 map-generation tables and 1 dialogue table. It does not contain game assets, raw game files, archives, decoding tools, or a complete export of the game.

## Game version

The current publication, `2026-10-20-dialogue`, adds a dialogue table decoded from the 1.06 extraction: spoken lines with their speaker, target and trigger. The previous publication, `2026-10-20-memoir-corrections`, corrects 17 spelling errors in eight hero memoir tables of the 1.06 extraction; nothing was re-extracted. Before that, `2026-10-16-gameplay-notes` added thirteen gameplay-reference tables converted from existing notes: three enemy-roster tables, three combat-configuration tables and seven map-generation tables. These imports have unverified source game versions. The earlier `2026-10-12-1.06` extraction comes from **Steam (PC), version `1.06.00.04.27511`**, with the displayed build date `2026/09/07` and revision marker `#16d45d2f01`. Its Steam build ID is `25174305`. The tables were extracted on October 12, 2026, the day 1.06 shipped with the Kintarō DLC. The maintainer confirmed the displayed version string the same day.

Of the 77 tables in that earlier extraction, every table was re-extracted from 1.06 except two. `In_Game_Observations.tsv` and `Fill_Pass_Values.tsv` hold readings and a decoding pass made on Steam (PC) version `1.05.01.01.27384` (displayed build date `2026/06/16`, revision `#773b656a63`), and they keep that attribution. [CHANGES-1.06.md](CHANGES-1.06.md) lists every row that changed between the two versions.

[VERSION.json](VERSION.json) records the game version and its evidence separately from the snapshot date. [VERSIONING.md](VERSIONING.md) explains how to confirm a version, record updates, and cite a fixed snapshot. The October 5 and 6 snapshots came from version 1.05. Tags `snapshot-2026-10-05` and `snapshot-2026-10-05.2` fix the first two, and commit `1118de2` holds `2026-10-06-values`. Cite a commit or snapshot tag when documenting a wiki claim.

## Tables

| Group | Files | Purpose |
|---|---:|---|
| Hero Common text | 13 | Hero names, abilities, talent text, backgrounds, and some unlock descriptions |
| Hero Memoirs text | 13 | Hero memoir titles and story text |
| Hero Skins text | 13 | Outfit names and descriptions |
| General and section text | 4 | Common UI, enemy, Magical Objects, and Melodies text |
| Object and melody indexes | 2 | Entity-to-text-key mappings for the selected objects and melodies |
| Magical Object sources | 1 | Rarity chances explicitly set on decoded source entities |
| Numerical talents | 13 | All 13 heroes: 26 talents each, with effects, unlock ranks, and source traces |
| Hero ability values | 13 | Trait, ability, ultimate and dash values and cooldowns for each hero, with source traces and the October 6 check |
| Object, melody and mechanics values | 3 | Magical Object and Melody effect values and shared mechanics settings |
| In-game readings | 1 | 94 values read by the maintainer in the Compendium on October 6, 2026, on version 1.05 |
| Fill pass | 1 | Second decoding pass over 65 values the 1.05 corrected table lacked |
| Enemy reference | 3 | Definition names and evidence, tribe/map references, and explicitly documented flags; source version unverified |
| Enemy combat configuration | 3 | Stored constants, picker roles and authored difficulty factors; no validated final-damage formula |
| Map generation | 7 | Resource roles, weights, quotas, caps, tier bands, probability models and limited observations |
| Dialogue | 1 | 5,847 spoken lines from hero barks, NPCs, quest dialogs and refugees, with speaker, target and trigger from game data, or the situation the key names |

See [TABLES.md](TABLES.md) for the exact files, declared row counts, source identifiers, and SHA-256 hashes. Tables are in [data/](data/).

## Talent publication status

All twelve hero talent pages were published and verified on October 5, 2026 across four batches, from the 1.05 tables: 312 talent rows in total. Each page has Icon, Name, Unlocks at and Effect columns, 26 loaded 48px icons, and no table redlinks. All parent hero pages link to their talent pages. [TALENTS.md](TALENTS.md) lists the published pages and verification history.

Build 1.06 replaces five talents and changes the effects of others. Those pages need updating from the 1.06 tables. Kintarō's talent table is new and has no page yet.

## Reading the tables

Open a TSV as UTF-8 text or import it into a spreadsheet with a tab delimiter. The opening lines beginning with `#` describe the source and row count; the following line contains the column names.

Text tables have `index`, `key`, and `text_en` columns. Their `index` is the original zero-based row index. Match index-table keys to the `key` column of the corresponding text table rather than guessing from display names. Internal hero identifiers include `RED` for Scarlet, `Piper` for The Pied Piper, `Snow_Queen` for The Snow Queen and `Kintaro` for Kintarō.

The exports preserve blank rows, original spelling, game markup, and literal `\n` escapes. The exception is eight hero memoir tables, where 17 spelling errors were corrected on October 20, 2026. [Hero_Memoirs_Corrections.tsv](data/Hero_Memoirs_Corrections.tsv) lists each change. A `\n` in a text cell represents a line break in the game text. Read every bullet before drafting an effect description.

| Markup | Meaning |
|---|---|
| `#term@` | Highlighted term |
| `&text~` | Positive value or effect |
| `$text*` | Negative value or effect |
| `\term§` | Alternate highlighted-term markup |
| `{0}`, `{1}`, etc. | Runtime substitutions, which can be values or names |

Replace markup with wiki formatting when drafting prose. Runtime placeholders are unresolved in these text exports; do not invent numbers to fill them. The separate [numerical talent tables](TALENTS.md) retain the decoded calculations, Common / Rare / Epic / Legendary order, baseline conditions and verification notes. Their `effect_en` and `notes` columns use literal `\n` line breaks; `tooltip_arguments_json` preserves the traced argument graph in each row. They do not replace the original tooltip text.

The [numerical value tables](VALUES.md) hold the numbers for ability, Magical Object and Melody tooltips. Each row keeps its decoded value, its evidence status and the result of the October 6 in-game check in separate columns. A blank value there means not decoded, not zero.

## Evidence limits

A snapshot date is the date the snapshot was published, not necessarily a game release or extraction date. See VERSION.json for version attribution; this repository does not claim to represent the latest game state.

The Magical Object index records 58 selected objects and the melody index records 12 melodies. Text tables can also contain blank, unused, or retired entries; a text row alone does not establish that an entry ships. In 1.06, replaced talent text often sits under a new `_Update6` key while the old key stays in the table. The recorded LiveOps6 manifest label applies to the Magical Object index and is distinct from the game version.

In `Magical_Objects_Sources.tsv`, numeric chances are fractions: `0.5` means 50%. A blank means the entity does not explicitly set that chance; it does not mean zero. Inherited values and Drop Chance Selectors are not decoded. Shops, the Sandman, and camp rewards are outside that table's coverage. Source rows include templates and do not establish which sources are active in-game.

These source tables describe rarity chances, not the probability of each named object within a rarity. The internal entry `Rare_Chest` has not been matched to a verified in-game chest name. Talent unlock ranks are recorded separately in the numerical talent tables from decoded hero progression definitions. Other runtime mechanics require their own evidence.

## Contributing

Read [CONTRIBUTING.md](CONTRIBUTING.md) before submitting changes. Use an issue to report a questionable mapping or value, or submit a pull request with the source, game version when known, and relevant conditions. Coordinate article work through the wiki's [contributor guide](https://ravenswatch.wiki.gg/wiki/Help:Contributing).

Ravenswatch game text belongs to its respective rights holders. This repository does not grant an open-source license over extracted game text.

## Enemy reference selection

The three enemy reference tables, converted from existing maintainer
Markdown notes, are described in [ENEMIES.md](ENEMIES.md). They preserve
name uncertainty and distinguish map references from spawn restrictions.
Their source game version is unverified; the original 77 tables keep their
previous attribution and, apart from the memoir spelling corrections, exact bytes.

## Combat and map-generation references

[COMBAT.md](COMBAT.md) distinguishes named constants from picker fallbacks
and configured difficulty factors. [MAP_GENERATION.md](MAP_GENERATION.md)
distinguishes quotas, caps and relative weights from inferred probabilities
and the single recorded run observation. Neither conversion gathers new
game data. The existing 77 text, talent and value tables were not changed by them.

## Dialogue

[DIALOGUE.md](DIALOGUE.md) describes the dialogue table. Its speaker, target
and trigger columns come from the game's bark players and bark setups; where
no trigger was decoded, `trigger_situation` gives the situation the key names,
with its basis. A blank cell means neither establishes it. Trigger chains name
developer components, not player-facing text, and give no chances or delays.
