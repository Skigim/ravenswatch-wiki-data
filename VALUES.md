# Numerical value tables

The `2026-10-06-values` snapshot adds seventeen tables holding the numbers behind ability, Magical Object and Melody tooltips, plus shared mechanics settings. They combine three kinds of evidence, which stay in separate columns: values decoded from game configuration, values the maintainer read in the game, and a second decoding pass over the values that were still missing.

| Table | Rows | Contents |
|---|---:|---|
| `Hero_<id>_Abilities.tsv` (12 files) | 871 | Trait, ability, ultimate and dash values and cooldowns for each hero |
| `Magical_Objects_Values.tsv` | 315 | Object effects and collection bonuses, grouped by rarity |
| `Melodies_Values.tsv` | 21 | Melody effects |
| `Mechanics_Values.tsv` | 240 | Shared settings: reward sources, difficulties, drops, status effects, prices, resources, stats and timers. Nearly half are unresolved |
| `In_Game_Observations.tsv` | 94 | Each value read in the game, beside the decoded entry it was compared with |
| `Fill_Pass_Values.tsv` | 65 | The second decoding pass, with its formulas and evidence notes |

Hero files use the internal hero identifiers listed in the README (`RED`, `Piper`, `Snow_Queen`).

## Columns of the fifteen page tables

Each row is one field of one ability, object, melody or setting. The first sixteen columns are the decoded record and were not changed by the check.

| Column | Meaning |
|---|---|
| `section`, `form_or_condition`, `name` | Where the row belongs: ability slot or object rarity, the form or condition it applies to, and the game's display name |
| `text_table`, `text_key`, `source_row_index` | The text export, key and row holding the description this value fills |
| `field`, `value`, `unit` | What the number is, the decoded value (blank when not decoded) and its unit |
| `formula`, `baseline` | The decoded expression and the conditions the value was computed under |
| `status` | Evidence status of the decoded value, defined below |
| `notes`, `source_path`, `source_property`, `reference_chain` | Qualifications and the game-relative source trace |
| `check_id` | Identifier of the check row this field belongs to. It matches the `id` column of `In_Game_Observations.tsv` and `Fill_Pass_Values.tsv`. Blank when the field was not on the check list |
| `checked_value` | The figure after the October 6 check: the in-game reading where there is one, otherwise the decoded value, otherwise the fill pass value |
| `checked_value_source` | `in-game reading`, `decoded`, `decoded-baseline`, or `fill pass (decoded-baseline)` |
| `maintainer_check` | `read in game: match`, `read in game: differs from decoded value`, `read in game: no decoded value`, or `accepted without reading` |
| `check_note` | The maintainer's note on that reading, when there is one |

Rows that share a `check_id` are variants of one displayed figure, such as Merlin's cooldowns by selected spell state. Their `checked_value` is the combined figure, with the variants separated by slashes in row order.

## Evidence statuses

| Status | Meaning |
|---|---|
| `decoded` | A typed literal or configuration value with a source trace |
| `decoded-baseline` | A value computed at the stated baseline or for a stated condition. Keep the baseline and condition with the value |
| `unresolved` | Not decoded. The value is blank and the notes name what blocks it |
| `static-text` | Description text or a textual result kept for reference |
| `symbolic` | An expression whose runtime variables are not bound to one number |
| `existing-table` | A value already recorded in another table of this repository, with that table's coverage limits |

A blank `value` is not zero. An `unresolved` row can still have a `checked_value` when the figure was read in the game or filled by the second pass.

## Baseline

Damage, healing and shield amounts are the figures the Compendium shows at level 1: character damage 10, healing 10, no talents and no Magical Objects. Object values are for one copy with no collection bonus applied. Values in a run differ with level, talents and objects.

## The October 6 check

The maintainer compared 390 tooltip values and cooldowns with the game on Steam (PC) version `1.05.01.01.27384 2026/06/16 #773b656a63`.

- 94 were read in the Compendium: all values and cooldowns for Scarlet, The Snow Queen, Beowulf and The Pied Piper, and eight single values elsewhere. 57 matched the decoded value, 36 supplied a value the decoded table lacked, and 1 differed.
- The one difference is The Snow Queen's Ice Skating cooldown: 8 seconds in the game, 6 in the decoded table. The second decoding pass found that her component labels are rotated relative to her ability keys. Read by ability key, the decoded cooldown is also 8.
- 296 values for the other eight heroes, Magical Objects and Melodies were accepted by the maintainer without reading them in the game. They are marked `accepted without reading` and keep `decoded`, `decoded-baseline` or `fill pass` as their source.

Nothing in `Mechanics_Values.tsv` was checked in the game.

## The fill pass

`Fill_Pass_Values.tsv` covers the 65 checked values that had neither a decoded value nor a reading when it was run. It decoded 57 and left 8 unresolved. The same method reproduced the 86 in-game readings available at the time, which is why its values are used where nothing else exists. 83 of those 86 are derived from source alone. The other three (Scarlet's Lycanthrope cooldown and two Ice Crown values) rest on rules supported only by the readings themselves, and none of the three is used for a filled value. The 8 unresolved values were then read in the game: Geppetto's Meca-Puppet damage per second, Romeo's Rapier combo damage, Dreamcatcher's price reduction, and the cooldown reductions of the five Raven objects.

The `evidence` column of that table names working files kept by the maintainer. Those files are not part of this repository.

## Source version

The hero tables were decoded from source files whose hashes match the earlier exports attributed to version `1.05.01.01.27384`. The decoding record for Magical Objects, Melodies and mechanics leaves the source version unconfirmed. Each row's `game_version` wording from the decoding record is summarised in the file's `# source_version` header line, and VERSION.json records the attribution per table. The in-game readings were taken on the version named above.

## Limits

- Cooldowns that depend on run state are recorded as observed, with the condition in `check_note`. Scarlet's Lycanthrope has no cooldown unless the Shapeshifter starting trait is taken; In the Belly has a base cooldown that scales with the eaten enemy's level.
- The night descriptions of The Pied Piper's Flute and Solo have no decoded argument order. Their readings are attached to the rows whose fields match the placeholders in the game text.
- Difficulty modifiers, chapter timers and stat formulas are not decoded.
- These tables do not establish drop rates of named objects or which reward sources are active in the game.
