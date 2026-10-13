# Game versions and data snapshots

VERSION.json is the version record for the tables in this repository. A game version identifies the source game; a snapshot identifies a particular publication of the selected tables. Git commits identify the exact repository contents.

## Current record

The current snapshot is `2026-10-12-1.06`, published October 12, 2026. It re-extracts 75 of the 77 tables from the Steam (PC) install after the 1.06 update, Steam build ID `25174305`, on the same day. The top-level fields of VERSION.json are the attribution for those 75 tables.

The top-level `version_status` is `maintainer-confirmed`. On October 12, 2026, the maintainer read the displayed version string `1.06.00.04.27511 2026/09/07 #16d45d2f01` on the install used for the exports. The record separates the game version `1.06.00.04.27511`, displayed build date `2026-09-07` and displayed revision marker `16d45d2f01`, and keeps the full string in `version_display`. The Steam build ID `25174305` and the "Version 1.06" patch notes are recorded as further evidence.

The confirmation came after the tables were published. Their `# source_version` header lines still say the displayed version string is unverified. VERSION.json is the version record; correcting the attribution didn't change the table bytes or their hashes.

`In_Game_Observations.tsv` and `Fill_Pass_Values.tsv` were not re-extracted. They hold readings and a decoding pass made on version 1.05, and their `table_overrides` entries keep that attribution: Steam (PC) `1.05.01.01.27384`, displayed build date `2026-06-16`, revision marker `773b656a63`, maintainer-confirmed.

Earlier snapshots came from version 1.05:

| Snapshot | Published | Contents | Fixed by |
|---|---|---|---|
| `2026-10-05-initial` | October 5, 2026 | 43 text and index exports | Tag `snapshot-2026-10-05` |
| `2026-10-05-talents-verified` | October 5, 2026 | Adds 12 numerical talent tables | Tag `snapshot-2026-10-05.2` |
| `2026-10-06-values` | October 6, 2026 | Adds 17 numerical value tables | Commit `1118de2` |

The recorded `LiveOps6` label applies to the Magical Object index's selected entry list. It does not establish a public patch number, the source version of every table, or the current version of the installed game.

## Confirm a source version

Record the displayed game version in `game_version` exactly as shown and preserve the complete label in `version_display`. Record `platform` and `store` separately, and put a store build identifier in `build_id` when known. A displayed date and revision marker can be recorded as `build_date` and `build_revision`. Build IDs, revision markers, and displayed game versions are distinct identifiers. Leave unavailable fields as `null`.

Add a `version_evidence` entry with `kind`, `reference`, and `note`. For example, the kind can describe an extraction record or build metadata, the reference can be a public source or a reproducible identifier, and the note should explain how that evidence links the exported tables to that game build. Keep private machine paths and game files out of the repository.

Use `unverified` when source attribution is unresolved, `maintainer-confirmed` when the maintainer identifies the version used for the exports, and `verified` when recorded extraction or build evidence independently ties the tables to the stated version or build. An observation of today's installed version alone does not identify the version of an older export. Correcting version attribution without changing table contents does not require changing their SHA-256 hashes or inventing a new extraction date.

## Updating tables

The top-level version fields are the default source attribution for tables without an override. If all tables are refreshed from the same confirmed build, update those fields and their evidence together.

For a partial refresh, retain the default attribution for unchanged tables. Add entries to `table_overrides`, keyed by repository path, such as `data/Melodies.LangEN.tsv`. Each entry records `game_version`, `version_display`, `platform`, `store`, `build_id`, `build_date`, `build_revision`, `version_status`, `version_evidence`, and `extracted_on` for that table. Unknown values remain `null`; a partial refresh must not relabel older tables as coming from the new build.

When table bytes change, update the affected row counts and SHA-256 entries in TABLES.md. Assign a new `snapshot_id` and `snapshot_published_on` when publishing a new data snapshot. Snapshot IDs use a date and a descriptive suffix, for example `2026-10-05-initial`; the date does not imply a game release date.

## Tags and wiki citations

Use annotated tags named `snapshot-YYYY-MM-DD` for published data snapshots. Add `.2`, `.3`, and so on for additional snapshots on the same date. Keep published tags fixed; issue a new snapshot rather than moving a tag.

For a wiki source, link to the relevant file at the full commit SHA or a fixed snapshot tag, and name the text key, row index, or entity used. Include the recorded game version and preserve its attribution status: maintainer-confirmed, independently verified, or unverified. The TABLES.md hashes identify table bytes but do not prove a game version.

Read and edit tables through the repository or its Git checkout. Pull updates before starting new work, commit changes in the repository, and use a fixed revision when reproducing an earlier finding.
