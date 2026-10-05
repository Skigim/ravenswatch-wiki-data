# Numerical talent tables

Saved [revision 755](https://ravenswatch.wiki.gg/wiki/User:Skigim/Talent_pilot?oldid=755). The existing Scarlet and Snow Queen tables retain all 52 talents and icons. [Hero_RED_Talents.tsv](data/Hero_RED_Talents.tsv) and [Hero_Snow_Queen_Talents.tsv](data/Hero_Snow_Queen_Talents.tsv) each publish 26 rows from that revision. Icons are referenced by wiki filename; no images are included.

## Extraction and interpretation

The numeric sources are cooked entity definitions. Each row records original roster order, localization keys and row indices, the controller, plain English numerical effect, unresolved-value notes, tooltip component and byte offset, traced argument graph as JSON, and wiki icon filename. Roster order is not an unlock-rank claim. The JSON records literals, selector properties/values and operation inputs; these are decoded evidence, while the interpretations below remain explicitly identified.

The numeric entity sources are not independently tied to a confirmed build. VERSION.json uses unverified overrides for these two tables, preserving the maintainer-confirmed attribution of the original exports.

- Literal union types 0/1/2 are decoded as float/int/bool, with byte offsets. Values are rounded to remove float32 representation noise.
- Rarity conditions 0x15fc6bf7 / 0x15fc6bf1 / 0x15fc6bf9 are interpreted as Rare / Epic / Legendary, with the unconditional fallback as Common. This ordering is inferred from consistent four-step selector progression across both heroes. UI localized labels independently establish the Common / Rare / Epic / Legendary order, but do not prove the controller flag identities. The page explicitly keeps runtime verification pending.
- Operation 0x17b29be2 is interpreted as multiplication, 0x17b29bec as division and 0x17af9527 as addition. These interpretations are corroborated by named shared operations such as Life + Shield, Life + Shield to Max HP Ratio, and damage multiplier operations. The actual implementation is absent.
- Percentage arguments using format 1/5 are interpreted as ratios and multiplied by 100; negative reductions use magnitude. Format 8 in Shadow Strikes already multiplies 0.005 by 100 in its value graph: its final increment is 0.5%, not 50%.
- Damage and healing baseline use a source basis of 10 with no added ability modifiers. Runtime character damage/healing properties and ability modifier inputs remain represented in the trace. The wiki distinguishes baseline arithmetic from current in-run values. Pack Leader's Legendary minimum shield coefficient is stored as 1.63 (16.3 baseline), rather than assuming 1.625 from the earlier progression.
- Pirouette's Chilled bonus has a base 0.5 plus an optional Frostbite operand. The row gives 50% and states that Frostbite adds its own bonus.
- Snowball divides 1 by the initial size (8 / 10 / 12 / 14) for its per-hit reduction. Initial baseline damage multiplies 10 * 5 * size * 0.05.
- Snow Queen overrides the inherited Shatter Damage Multiplier Default GUID with value 6. Shattering Storm baseline uses 10 * 6 * (1.2 / 1.5 / 1.8 / 2.1).

## Unresolved source behavior (visible on the page)

1. On the Hunt: the tooltip and modifier reference a literal 10.0 with percentage formatting. The conversion/display semantics cannot be settled from this asset alone. Duration 4 / 6 / 8 / 10 seconds is extracted; a guessed damage percentage is not published.
2. Devourer and Rupture: both quest target selectors place a true -> 20 entry before rarity-conditioned 35 / 30 / 25 entries. Under first-match evaluation these stay 20. Runtime selector priority is not supplied. The page records the first unconditional value and all later stored values, with a confirmation note.
3. Freezing Stars: a multiplicative tooltip operand uses GUID 02b44ade992bed44a205c17398bfbf8f, no component path, and a zero fallback. It is unresolved in the hero and shared component files. The available coefficient 3.2 / 4 / 4.8 / 5.6 and conditional 32 / 40 / 48 / 56 arithmetic are recorded, but final displayed damage is left unresolved.

These are source limitations, not a claim that the live game necessarily behaves incorrectly. No runtime game session or current patch verification was performed.


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

All 52 pilot effects were verified against the local authored numerical draft. The wiki was previewed through DevTools at 1920, 1366, 768 and 390 pixels. Both tables fit without clipped cells at each width; the shared desktop navigation overflows at 768px. The small layout collapses the sidebar. Screenshots and raw entity files are not part of this repository.
