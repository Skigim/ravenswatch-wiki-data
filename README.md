# Ravenswatch wiki data

Selected decoded tables prepared for contributors to the [Ravenswatch Wiki](https://ravenswatch.wiki.gg/).

This repository is the canonical source for 43 selected decoded TSV exports and two derived numerical talent tables used to write and check wiki articles. It does not contain game assets, raw game files, archives, decoding tools, or a complete export of the game.

## Game version

The initial 43 text and index exports come from **Steam (PC), version `1.05.01.01.27384`**, with the displayed build date `2026/06/16` and revision marker `#773b656a63`. This source attribution was confirmed by the maintainer on October 5, 2026. Its data snapshot ID is `2026-10-05-initial`; the Steam numeric build ID has not been recorded.

[VERSION.json](VERSION.json) records the game version and its evidence separately from the data snapshot date. [VERSIONING.md](VERSIONING.md) explains how to confirm a version, record updates, and cite a fixed snapshot. The numerical talent tables have separate, unverified source-version overrides. The current snapshot ID is `2026-10-05-talent-pilot`. Use these repository tables directly; cite a commit or snapshot tag when documenting a wiki claim.

## Tables

| Group | Files | Purpose |
|---|---:|---|
| Hero Common text | 12 | Hero names, abilities, talent text, backgrounds, and some unlock descriptions |
| Hero Memoirs text | 12 | Hero memoir titles and story text |
| Hero Skins text | 12 | Outfit names and descriptions |
| General and section text | 4 | Common UI, enemy, Magical Objects, and Melodies text |
| Object and melody indexes | 2 | Entity-to-text-key mappings for the selected objects and melodies |
| Magical Object sources | 1 | Rarity chances explicitly set on decoded source entities |
| Numerical talent pilot | 2 | Scarlet and Snow Queen: 26 interpreted talent rows each, with source bindings and unresolved-value notes |

See [TABLES.md](TABLES.md) for the exact files, declared row counts, source identifiers, and SHA-256 hashes. Tables are in [data/](data/).

## Reading the tables

Open a TSV as UTF-8 text or import it into a spreadsheet with a tab delimiter. The opening lines beginning with `#` describe the source and row count; the following line contains the column names.

Text tables have `index`, `key`, and `text_en` columns. Their `index` is the original zero-based row index. Match index-table keys to the `key` column of the corresponding text table rather than guessing from display names. Internal hero identifiers include `RED` for Scarlet, `Piper` for The Pied Piper, and `Snow_Queen` for The Snow Queen.

The exports preserve blank rows, original spelling, game markup, and literal `\n` escapes. A `\n` in a text cell represents a line break in the game text. Read every bullet before drafting an effect description.

| Markup | Meaning |
|---|---|
| `#term@` | Highlighted term |
| `&text~` | Positive value or effect |
| `$text*` | Negative value or effect |
| `\term§` | Alternate highlighted-term markup |
| `{0}`, `{1}`, etc. | Runtime substitutions, which can be values or names |

Replace markup with wiki formatting when drafting prose. Runtime placeholders are unresolved in these text exports; do not invent numbers to fill them. The separate [numerical talent tables](TALENTS.md) retain the pilot calculations, inferred rarity order, baseline conditions and source exceptions. Their `effect_en` and `notes` columns use literal `\n` line breaks; `tooltip_arguments_json` preserves the traced argument graph in each row. They do not replace the original tooltip text.

## Evidence limits

The initial data snapshot was published on October 5, 2026. That date is the snapshot publication date, not a game release or extraction date. See VERSION.json for version attribution; this repository does not claim to represent the latest game state.

The Magical Object index records 58 selected objects and the melody index records 12 melodies. Text tables can also contain blank, unused, or retired entries; a text row alone does not establish that an entry ships. The recorded LiveOps5 manifest label applies to the Magical Object index and is distinct from the maintainer-confirmed game version.

In `Magical_Objects_Sources.tsv`, numeric chances are fractions: `0.5` means 50%. A blank means the entity does not explicitly set that chance; it does not mean zero. Inherited values and Drop Chance Selectors are not decoded. Shops, the Sandman, and camp rewards are outside that table's coverage. Source rows include templates and do not establish which sources are active in-game.

These source tables describe rarity chances, not the probability of each named object within a rarity. The internal entry `Rare_Chest` has not been matched to a verified in-game chest name. Runtime scaling, talent unlock ranks, and other unresolved mechanics need separate evidence.

## Contributing

Read [CONTRIBUTING.md](CONTRIBUTING.md) before submitting changes. Use an issue to report a questionable mapping or value, or submit a pull request with the source, game version when known, and relevant conditions. Coordinate article work through the wiki's [contributor guide](https://ravenswatch.wiki.gg/wiki/Help:Contributing).

Ravenswatch game text belongs to its respective rights holders. This repository does not grant an open-source license over extracted game text.
