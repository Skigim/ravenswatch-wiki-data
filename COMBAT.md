# Enemy combat configuration

These three tables transcribe the existing bounded combat note. They cover
Tentacle Master Nightmare, three comparison enemies, their shared settings,
and the four documented chapter damage selectors. They are not an enemy-wide
stat census or a validated table of final HP and damage.

| Table | Rows | Contents |
|---|---:|---|
| [Enemy_Combat_Values.tsv](data/Enemy_Combat_Values.tsv) | 24 | Named constants, inherited health settings, and two cooked NGP defaults |
| [Enemy_Combat_Picker_Values.tsv](data/Enemy_Combat_Picker_Values.tsv) | 9 | Fallbacks, unnamed picker literals, and conditional-selector operands |
| [Enemy_Chapter_Damage_Factors.tsv](data/Enemy_Chapter_Damage_Factors.tsv) | 16 | Four difficulty indices across four chapter selectors |

## Stored values and active values

`stored_value` is a number recorded in configuration, with f32 values rounded
as in the source note. It is not measured player damage or effective enemy HP.
`inheritance` distinguishes a local override, parent/model setting, shared
baseline, or cooked global default. `source_path` and file offsets preserve
the trace; offsets are in the resource file, not a live process.

The boss's Fast Slam references a named 1.5 multiplier while the picker's
embedded fallback is 3. Those are separate records in separate tables.
The wolf's 100 raw health is inherited from its model. The elite crab's 90
overrides its model's 70, and Mother Ghoul's 200 overrides its parent's 100.
No inheritance sum or final combat formula is calculated during conversion.

The two NGP globals have stored defaults of 0. Their active values at a
selected difficulty are unknown. Their exact source files and offsets were
not recorded in the note, so those cells stay blank. `unit` also stays blank
where the note did not establish one; a field name is not a unit measurement.

## Picker interpretation

`semantic_status` keeps `embedded-fallback`, `inferred-multiplier-role`,
`unresolved-runtime-role`, and `conditional-selector-operand` distinct.
The shared Tentacle Shockwave/Swipe slots contain 2 and 3, but their role
is inferred from an analogous layout. Rain's first-picker literal 10 is not
validated Rain hit damage. The literal field `Attack Shot Damage Multiplier`
is preserved under its original name rather than relabeled as Rain damage.

Ring and Final Ring named 0.8 values are selected conditionally. The
Attraction selectors also contain a literal 1 and an enraged-state reference.
Their branch evaluation and runtime result remain unvalidated. A fallback
or selector operand must not replace a referenced value unconditionally.

## Difficulty configuration

`configured_damage_factor` preserves the authored switch-selector entries.
The selectors read global ID `0x18700873`, identified in the note as
Game Difficulty. No difficulty display-name mapping was checked, so that
column remains blank. The note records a prior test where writing the
chapter-scaling globals had no observed effect on existing or newly spawned
enemies. Consumption therefore remains unproven. Do not multiply these
factors by Raw Damage and an attack coefficient and call the result a
validated per-hit damage value.

## Provenance

This publication converts an existing note checked on 2026-10-16. It does
not perform that check again, extract game files, inspect an executable or
process, or establish a game version. Each row records the original note,
line, canonical Git-byte SHA-256 and source revision. Unknown game-version
and extraction fields stay null in VERSION.json; the old 1.06 table default
does not apply to these imports. The original private note remains evidence.

Source note: `datamining/docs/enemy_combat_fields.md` at `0ae8f70b327a3b37b615babd9bd50f1281ac7acc`.
Canonical source SHA-256: `62c381674bd5de17c8a988aaac762b4f1e49465d3b1ba41011f5964ac8312b8b`.
