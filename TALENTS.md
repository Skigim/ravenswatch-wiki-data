# Numerical talent tables

The initial Scarlet and Snow Queen pilot was saved at [revision 755](https://ravenswatch.wiki.gg/wiki/User:Skigim/Talent_pilot?oldid=755). The current snapshot, `2026-10-12-1.06`, contains 13 numerical tables, one for each hero including Kintarō, with 26 talents each (338 rows total). They were re-extracted from build 1.06; see [Build 1.06 re-extraction](#build-106-re-extraction). The `2026-11-12-starting-talents` snapshot adds two columns that mark the starting talents; see [Starting talents](#starting-talents). Icons are referenced by wiki filename; no images are included.

## Extraction and interpretation

The numeric sources are cooked entity definitions. Each row records original roster order, localization keys and row indices, the controller, unlock rank, whether it is a starting talent and where that was read, plain English numerical effect, unresolved-value notes, tooltip component and byte offset, traced argument graph as JSON, and wiki icon filename. Roster order is not an unlock-rank claim. The JSON records literals, selector properties/values and operation inputs; these are decoded evidence, while the interpretations below remain explicitly identified.

The `2026-10-05-talents-verified` tables came from Steam (PC) `1.05.01.01.27384`, displayed build date `2026/06/16`, revision `#773b656a63`, as the maintainer confirmed on October 5, 2026. The 1.06 tables come from Steam (PC) `1.06.00.04.27511`, displayed build date `2026/09/07`, revision `#16d45d2f01`, Steam build ID `25174305`, as the maintainer confirmed on October 12, 2026. The tables' `# source_version` header lines predate that confirmation; VERSION.json is the record.

- Literal union types 0/1/2 are decoded as float/int/bool, with byte offsets. Values are rounded to remove float32 representation noise.
- Rarity conditions 0x15fc6bf7 / 0x15fc6bf1 / 0x15fc6bf9 are interpreted as Rare / Epic / Legendary, with the unconditional fallback as Common. This ordering is inferred from consistent four-step selector progression across both heroes. UI localized labels independently establish the Common / Rare / Epic / Legendary order, but do not prove the controller flag identities. The published slash-separated values use this order; the October 5 compendium checks resolved the flagged displayed-value cases. Decoded flag identities remain an interpretation of the source graph.
- Operation 0x17b29be2 is interpreted as multiplication, 0x17b29bec as division and 0x17af9527 as addition. These interpretations are corroborated by named shared operations such as Life + Shield, Life + Shield to Max HP Ratio, and damage multiplier operations. The actual implementation is absent.
- Percentage arguments using format 1/5 are interpreted as ratios and multiplied by 100; negative reductions use magnitude. Format 8 in Shadow Strikes already multiplies 0.005 by 100 in its value graph: its final increment is 0.5%, not 50%.
- Damage and healing baseline use a source basis of 10 with no added ability modifiers. Runtime character damage/healing properties and ability modifier inputs remain represented in the trace. The wiki distinguishes baseline arithmetic from current in-run values. Pack Leader's Legendary minimum shield coefficient is stored as 1.63 (16.3 baseline), rather than assuming 1.625 from the earlier progression.
- Pirouette's Chilled bonus has a base 0.5 plus an optional Frostbite operand. The row gives 50% and states that Frostbite adds its own bonus.
- Snowball divides 1 by the initial size (8 / 10 / 12 / 14) for its per-hit reduction. Initial baseline damage multiplies 10 * 5 * size * 0.05.
- Snow Queen overrides the inherited Shatter Damage Multiplier Default GUID with value 6. Shattering Storm baseline uses 10 * 6 * (1.2 / 1.5 / 1.8 / 2.1).
- In 1.06, rarity condition 0x15fc6beb is an explicit Common entry. Double Shock uses it: Common -30%, with a default of 0.

## Build 1.06 re-extraction

On October 12, 2026, all twelve tables were rebuilt from build 1.06 and Kintarō's table was added. [CHANGES-1.06.md](CHANGES-1.06.md) lists every changed row.

**Override files.** Build 1.06 doesn't rewrite most hero definitions. Its version manifest maps each hero to a sparse `Hero_<id>_Update6` definition that overrides components by name or GUID. The tooltip traces read the override first and the base definition second. A node read from an override file is tagged with a `source` key in `tooltip_arguments_json`.

**Roster lookup by GUID.** Each roster entry in a hero definition names its talent controller and gives a 16-byte GUID for it. When the name doesn't match a component, the GUID is used. One Kintarō entry needs this: the roster says "Skill Controller Skill Defense Summon Spirit", and the GUID resolves it to "Skill Controller Defense Summon Spirit" (Forest Spirits).

**Unlock ranks.** Ranks are decoded from hero progression definitions, as for 1.05. Three replacement talents (Deadly Combo, Jinn Charge and Spectral Blades) have an unlock condition at level 0, which is met from the start. They're listed at rank 1, like the other talents that are unlocked from the start. Focus unlocks at rank 9 and Maelstrom at rank 7. Kintarō has the same rank layout as the other heroes.

**Which rows keep the compendium check.** A row whose `effect_en` is unchanged since 1.05 keeps it, along with the October 5 compendium check: 267 of the 312 rows for the twelve earlier heroes. The other 45 are datamined only:

- 33 were rendered from the 1.06 trace with the same baseline and order as before.
- 12 were written by hand, where a value needs interpretation or can't be resolved from the data. Their `notes` say why.

All 26 Kintarō rows are datamined only and haven't been checked in the compendium: 23 rendered and 3 written by hand. Two of his values stay unresolved: Targeted Bite's damage and Skewer's maximum.

**Default values of engine-fed operands.** Some operands are filled in by the engine at runtime; the definition stores a default. In the 1.05 tables, 57 of the 201 compendium-checked rows that match the default render pass through such an operand. So `effect_en` uses the default render, as the compendium does. The value tables are stricter and leave these values unresolved; see [VALUES.md](VALUES.md).

**Trace-only changes.** Byte offsets, roster order and internal operand indices change in almost every row because the files were rebuilt. Merlin's table changes only in these columns.

## Starting talents

Two columns follow `unlock_rank`:

- `starting_talent`: `yes` for the talents dealt into the level 1 offer of a run, `no` for the rest. Every row has a value; none is blank.
- `starting_talent_source`: the entity file, the skill controller component, its tier value and the byte offset of that value in the cooked entity, for example `Hero_Aladdin.entity, Skill Controller Trait Extra Wish, tier 0 @0x57c24`. Where a `Hero_<id>_Update6` override replaces the component, the override is the source.

Each hero has exactly 4 starting talents: two at rank 1, one at rank 2 and one at rank 5. The other 9 rank 1 talents are unlocked from the start but are not starting talents.

**How the game picks them.** Read from `Ravenswatch.exe` of build 1.06 (Steam build ID `25174305`), in the decompiler unless marked otherwise:

- Every skill controller has a tier: a u32 that `oCDtEntityCpntSkillControllerSettings` reads into `+0x178` (`FUN_1402e6db0`), right after its first two child objects. The deserializer rejects values above 3. The engine names the tiers in a table at `0x140ed54e0`: 0 "Tier I", 1 "Tier II", 2 "Tier Ultimate", 3 "Tier III". In the tables, tier 1 covers the 18 regular talents, tier 3 the 4 ultimate upgrades and tier 0 the 4 starting talents. Both base ultimates are tier 2.
- An activated skill controller adds itself to one of four pools on the hero controller, picked by its tier (`FUN_1402e8250`).
- The hero controller has 10 talent slots with fixed tiers, set in its constructor (`FUN_140397250`): slot 0 is tier 0, slots 1–3 and 5–8 are tier 1, slot 4 is tier 2 and slot 9 is tier 3. A run starts with no talents, so the first offer fills slot 0 from the tier 0 pool.
- The offer builder (`FUN_1403b27e0`) deals `Extra skill choice + 4` cards for a tier 0 slot and `Extra skill choice + 2` for the others, at least 1 (confirmed in the assembly at `0x1403b29aa`–`0x1403b29c9`). `Extra skill choice` is the entity value `0x1a7a3166`, registered with a default of 0 in `FUN_1401d0030`.
- The builder draws unlocked talents at random. A talent whose hero-rank lock isn't met yet goes to a fallback list instead. For a tier 0 slot, the fallback list fills any remaining cards, sorted by unlock rank (`FUN_1402e9850`, `FUN_1403178f0`). The lock comes from the hero definition entry with the same GUID (`FUN_1402e80c0`).

So with default settings, the level 1 offer is all 4 starting talents, whatever the hero's rank. The data doesn't show how the game displays a starting talent that is still locked.

**What changes it.** The only cooked data that touches `Extra skill choice` is `LessChoices LessSkill Modifier` in `Hero_Common.entity` (int `-1` @`0x9b23c`), part of the Lack of Inspiration game modifier. With it, the level 1 offer is 3 cards: unlocked starting talents at random, then locked ones by unlock rank. The same builder handles rerolls; a reroll leaves out the previous cards when enough others remain.

**Talents that are never offered.** Some heroes have tier 0 controllers that aren't in the hero definition, for example Aladdin's `Skill Controller Trait Fourth Wish`. They aren't in these tables. In every one of them, the byte after the component name is 0; in every roster controller in the hero entity files it is 1. The 1.06 `_Update6` overrides set it to 0 on four controllers that the 1.06 roster no longer uses. This byte reads as the component's enabled flag, which would keep those controllers out of the pools. That reading is inferred from this pattern; the code that checks the flag wasn't traced.

## Compendium verification completed October 5, 2026

The maintainer manually checked the flagged tooltips in the Antigravity session. These confirmations are applied in the current tables and drafts:

1. Scarlet, On the Hunt: a flat +25% damage increase at every rarity; duration 4 / 6 / 8 / 10 seconds.
2. Scarlet, Devourer, and The Snow Queen, Rupture: quest target 20 at every rarity. Earlier stored selector branches do not alter the confirmed displayed target.
3. The Snow Queen, Freezing Stars: 32 / 40 / 48 / 56 area damage. The unresolved source GUID remains in the trace, but the displayed value is settled by the compendium check.

Unlock ranks were subsequently decoded from hero progression definitions and added to all twelve tables. Base ultimates are excluded from talent tables; ultimate upgrade talents are included. `unlock_rank` is the hero rank that unlocks a talent. Each hero has 11 talents at rank 1, which are unlocked from the start, two at each rank 2–5, one at rank 6, two at each rank 7–8, and two at rank 9. Rank 1 doesn't make a talent a starting talent: only 2 of the 11 are. See [Starting talents](#starting-talents).

Source traces preserve the original graph and interpretation history. Historical unresolved operands are not current publication blockers when the displayed value has been confirmed.

## Numerical source hashes

Paths below are game-relative asset identifiers, not distributed source files. They pin the entity snapshot used by the existing pilot trace.

| Source identifier | SHA-256 |
|---|---|
| `EntitySettings/Heroes/Hero_Red!Hero_Red.entity.ot.EntitySettingsResource.gen` | `7b2908fe07deb129d34f2935c65f69c764364973b8ad471e0c76198ceacb7080` |
| `EntitySettings/Heroes/Hero_Snow_Queen!Hero_Snow_Queen.entity.ot.EntitySettingsResource.gen` | `7d39818f124967d8a40fe1bc4a35f45bb4a5d7e393a0a1cd598fbdbe5cecf5c1` |
| `EntitySettings/Heroes/Hero_Common!Hero_Common.entity.ot.EntitySettingsResource.gen` | `b976168090fec1d419bea6ed4549f2b77782ba38692b99860686cbac27c742a2` |
| `EntitySettings/Character_Common/Character_Common.entity.ot.EntitySettingsResource.gen` | `46651291a24fd7f2a2a2e3a2bde86a3b99d76168649c58780519e5a851c6d047` |
| `EntitySettings/GameUis/Items!Skill_Description.entity.ot.EntitySettingsResource.gen` | `a672e76d7a7b957fdf8a0a65ac78fc5000b522744fecd0dbbe94ba94b262a5c7` |

## Publication and display checks

Historical pilot checks: all 52 Scarlet and Snow Queen effects were verified against the local authored numerical draft. The wiki was previewed through DevTools at 1920, 1366, 768 and 390 pixels. Both tables fit without clipped cells at each width; the shared desktop navigation overflows at 768px. The small layout collapses the sidebar. Screenshots and raw entity files are not part of this repository.

All four publication batches completed on October 5, 2026. Scarlet and The Snow Queen were updated; the remaining ten hero talent pages were created. Each of the twelve live tables was checked for 26 talent rows, four columns, 26 loaded 48px icons and zero redlinks. All twelve parent hero pages link to their corresponding talent pages. Romeo, Juliet and Merlin parent-page caches were refreshed after publication to remove cached redlinks.

## Published talent pages

| Hero | Batch | Data table | Wiki page | Status |
|---|---:|---|---|---|
| Scarlet | 1 | [Hero_RED_Talents.tsv](data/Hero_RED_Talents.tsv) | [Talents](https://ravenswatch.wiki.gg/wiki/Scarlet/Talents) | Published and verified |
| The Snow Queen | 1 | [Hero_Snow_Queen_Talents.tsv](data/Hero_Snow_Queen_Talents.tsv) | [Talents](https://ravenswatch.wiki.gg/wiki/The_Snow_Queen/Talents) | Published and verified |
| Beowulf | 2 | [Hero_Beowulf_Talents.tsv](data/Hero_Beowulf_Talents.tsv) | [Talents](https://ravenswatch.wiki.gg/wiki/Beowulf/Talents) | Published and verified |
| The Pied Piper | 2 | [Hero_Piper_Talents.tsv](data/Hero_Piper_Talents.tsv) | [Talents](https://ravenswatch.wiki.gg/wiki/The_Pied_Piper/Talents) | Published and verified |
| Aladdin | 2 | [Hero_Aladdin_Talents.tsv](data/Hero_Aladdin_Talents.tsv) | [Talents](https://ravenswatch.wiki.gg/wiki/Aladdin/Talents) | Published and verified |
| Melusine | 2 | [Hero_Melusine_Talents.tsv](data/Hero_Melusine_Talents.tsv) | [Talents](https://ravenswatch.wiki.gg/wiki/Melusine/Talents) | Published and verified |
| Geppetto | 3 | [Hero_Geppetto_Talents.tsv](data/Hero_Geppetto_Talents.tsv) | [Talents](https://ravenswatch.wiki.gg/wiki/Geppetto/Talents) | Published and verified |
| Sun Wukong | 3 | [Hero_SunWukong_Talents.tsv](data/Hero_SunWukong_Talents.tsv) | [Talents](https://ravenswatch.wiki.gg/wiki/Sun_Wukong/Talents) | Published and verified |
| Carmilla | 3 | [Hero_Carmilla_Talents.tsv](data/Hero_Carmilla_Talents.tsv) | [Talents](https://ravenswatch.wiki.gg/wiki/Carmilla/Talents) | Published and verified |
| Romeo | 4 | [Hero_Romeo_Talents.tsv](data/Hero_Romeo_Talents.tsv) | [Talents](https://ravenswatch.wiki.gg/wiki/Romeo/Talents) | Published and verified |
| Juliet | 4 | [Hero_Juliet_Talents.tsv](data/Hero_Juliet_Talents.tsv) | [Talents](https://ravenswatch.wiki.gg/wiki/Juliet/Talents) | Published and verified |
| Merlin | 4 | [Hero_Merlin_Talents.tsv](data/Hero_Merlin_Talents.tsv) | [Talents](https://ravenswatch.wiki.gg/wiki/Merlin/Talents) | Published and verified |

The only image warning was an exact duplicate of Melusine Freezing Splash; the existing identical image was retained without overriding the warning. Batch 3 and Batch 4 had no filename or duplicate-image warnings. An automatic Cloudflare check during Batch 4 cleared without interaction before publication continued.
