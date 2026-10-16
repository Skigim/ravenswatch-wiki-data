# Enemy reference tables

The `2026-10-16-enemies` snapshot adds three selected TSV tables converted
from the existing enemy note on 2026-10-16. The earlier 77 tables retain
their exact bytes and source attribution. No game files were decoded, no
manifest was rebuilt, and no game process was inspected during conversion.

| Table | Rows | What belongs here |
|---|---:|---|
| [Enemy_Definitions.tsv](data/Enemy_Definitions.tsv) | 81 | Definition IDs, readable labels, established localization references, and tribe affiliations |
| [Enemy_Tribe_Map_References.tsv](data/Enemy_Tribe_Map_References.tsv) | 75 | Each of 25 tribes against each of the three chapter map definitions |
| [Enemy_Definition_Flags.tsv](data/Enemy_Definition_Flags.tsv) | 6 | The explicitly documented DarkHills, ChapterBoss, and Standard flags |

## How to read the names

`readable_label` always preserves the label in the source note.
`localized_name` is populated only when the note establishes a localization
reference. There are 15 `localized-reference` names, 3 `probable-mapping`
labels, and 63 `descriptive-label` labels. Probable and descriptive rows
have a blank `localized_name`; they must not be published as verified game
display names. `name_text_table`, `name_text_keys`, and `name_evidence`
preserve the recorded trace. A localization reference is not a new in-game
check. Existing Enemy_Common text keys were cross-checked separately for
spelling; that does not establish the version of the definition corpus.

For example, Boss_Crab has the established localized name Karkinos, Scourge
of the Reefs. Ogre_Cyclop retains Steropes, the Cyclop as a probable label.
Baba_Yaga_House retains a descriptive label and no tribe reference.

## How to read the map references and flags

`listed` means that the chapter map definition references the tribe.
`absent` means that the reference is absent. Neither is a complete spawn
whitelist: scripted encounters and summons require separate evidence. The
Baba Yaga map is outside this selection. Tribe counts include bosses,
summons, eggs and detached entities, not just distinct species.

The three maps list 10, 9 and 11 tribes respectively for Dark Hills, Storm
Island and Avalon. 80 of the 81 enemy definitions have a tribe reference;
Baba_Yaga_House has none. Boss_Roc_Bird references Jinns, which is preserved.

The flag table is a selection of six documented flags, not a complete flag
census. DarkHills enforcement as a spawn restriction is unestablished.
ChapterBoss identifies no particular chapter. Elite_Witch_Stake carries a
Standard tag despite its filename; filename prefixes are not a complete
rank taxonomy.

## Provenance and version

The source note is `datamining/enemy_list.md` in the maintainer's private
research repository, at commit `77b9e0416a01146a08d232ca465dd1b4b4756aa8`. Its canonical Git-byte
SHA-256 is `9d2371c28d2b657f0090deef16758ad0e09eab57f0b441d9dd1b0fd501124762`. Every row records the source document, line,
SHA-256 and revision. The note is not copied into this repository.
Definition and map resource paths are preserved for independent tracing.

The source note records a check on 2026-10-13 against an existing decoded
corpus. That date is neither a fresh extraction nor proof of a particular
game build. The new tables therefore have unverified source-version
overrides in VERSION.json, with unavailable fields left null. They must
not inherit the 1.06 attribution of the existing published tables.

The original Markdown remains in the private research repository. This
selection transfers reusable gameplay facts, not research plans, binary
format documentation, raw game files, or application source.

The later combat tables are documented in [COMBAT.md](COMBAT.md). They are a
separate bounded evidence selection and do not supply final stats for all
81 definitions.
