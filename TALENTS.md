# Numerical talent tables

The initial Scarlet and Snow Queen pilot was saved at [revision 755](https://ravenswatch.wiki.gg/wiki/User:Skigim/Talent_pilot?oldid=755). The current snapshot, `2026-10-05-talents-verified`, contains twelve numerical tables covering all released heroes, with 26 talents each (312 rows total). These include the October 5 compendium corrections and decoded unlock ranks. Icons are referenced by wiki filename; no images are included.

## Extraction and interpretation

The numeric sources are cooked entity definitions. Each row records original roster order, localization keys and row indices, the controller, plain English numerical effect, unresolved-value notes, tooltip component and byte offset, traced argument graph as JSON, and wiki icon filename. Roster order is not an unlock-rank claim. The JSON records literals, selector properties/values and operation inputs; these are decoded evidence, while the interpretations below remain explicitly identified.

The maintainer confirmed on October 5, 2026 that the current game version for these talent tables is the last documented repository version: Steam (PC) `1.05.01.01.27384`, displayed build date `2026/06/16`, revision `#773b656a63`. This is maintainer attribution, not an independent binary build identification. VERSION.json records this evidence for all twelve tables.

- Literal union types 0/1/2 are decoded as float/int/bool, with byte offsets. Values are rounded to remove float32 representation noise.
- Rarity conditions 0x15fc6bf7 / 0x15fc6bf1 / 0x15fc6bf9 are interpreted as Rare / Epic / Legendary, with the unconditional fallback as Common. This ordering is inferred from consistent four-step selector progression across both heroes. UI localized labels independently establish the Common / Rare / Epic / Legendary order, but do not prove the controller flag identities. The published slash-separated values use this order; the October 5 compendium checks resolved the flagged displayed-value cases. Decoded flag identities remain an interpretation of the source graph.
- Operation 0x17b29be2 is interpreted as multiplication, 0x17b29bec as division and 0x17af9527 as addition. These interpretations are corroborated by named shared operations such as Life + Shield, Life + Shield to Max HP Ratio, and damage multiplier operations. The actual implementation is absent.
- Percentage arguments using format 1/5 are interpreted as ratios and multiplied by 100; negative reductions use magnitude. Format 8 in Shadow Strikes already multiplies 0.005 by 100 in its value graph: its final increment is 0.5%, not 50%.
- Damage and healing baseline use a source basis of 10 with no added ability modifiers. Runtime character damage/healing properties and ability modifier inputs remain represented in the trace. The wiki distinguishes baseline arithmetic from current in-run values. Pack Leader's Legendary minimum shield coefficient is stored as 1.63 (16.3 baseline), rather than assuming 1.625 from the earlier progression.
- Pirouette's Chilled bonus has a base 0.5 plus an optional Frostbite operand. The row gives 50% and states that Frostbite adds its own bonus.
- Snowball divides 1 by the initial size (8 / 10 / 12 / 14) for its per-hit reduction. Initial baseline damage multiplies 10 * 5 * size * 0.05.
- Snow Queen overrides the inherited Shatter Damage Multiplier Default GUID with value 6. Shattering Storm baseline uses 10 * 6 * (1.2 / 1.5 / 1.8 / 2.1).

## Compendium verification completed October 5, 2026

The maintainer manually checked the flagged tooltips in the Antigravity session. These confirmations are applied in the current tables and drafts:

1. Scarlet, On the Hunt: a flat +25% damage increase at every rarity; duration 4 / 6 / 8 / 10 seconds.
2. Scarlet, Devourer, and The Snow Queen, Rupture: quest target 20 at every rarity. Earlier stored selector branches do not alter the confirmed displayed target.
3. The Snow Queen, Freezing Stars: 32 / 40 / 48 / 56 area damage. The unresolved source GUID remains in the trace, but the displayed value is settled by the compendium check.

Unlock ranks were subsequently decoded from hero progression definitions and added to all twelve tables. Base ultimates are excluded from talent tables; ultimate upgrade talents are included. Each hero has 11 Starting talents, two at each rank 2–5, one at rank 6, two at each rank 7–8, and two at rank 9.

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
