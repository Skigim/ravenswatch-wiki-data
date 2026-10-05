# Ravenswatch wiki data

Selected decoded tables prepared for contributors to the [Ravenswatch Wiki](https://ravenswatch.wiki.gg/).

This repository contains the 43 existing TSV tables selected from the wiki working folder, copied without changing their contents. It is a reference snapshot for writing and checking articles. It does not contain game assets, raw game files, archives, decoding tools, or a complete export of the game.

## Tables

| Group | Files | Purpose |
|---|---:|---|
| Hero Common text | 12 | Hero names, abilities, talent text, backgrounds, and some unlock descriptions |
| Hero Memoirs text | 12 | Hero memoir titles and story text |
| Hero Skins text | 12 | Outfit names and descriptions |
| General and section text | 4 | Common UI, enemy, Magical Objects, and Melodies text |
| Object and melody indexes | 2 | Entity-to-text-key mappings for the selected objects and melodies |
| Magical Object sources | 1 | Rarity chances explicitly set on decoded source entities |

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

Replace markup with wiki formatting when drafting prose. Runtime placeholders are unresolved in these text exports; do not invent numbers to fill them.

## Evidence limits

The tables were already present in the wiki working folder when this repository was assembled on October 5, 2026. That date is the repository assembly date, not a game release or extraction date. The files do not establish a precise game build or patch version, and this repository does not claim to represent the latest game state.

The Magical Object index records 58 selected objects and the melody index records 12 melodies. Text tables can also contain blank, unused, or retired entries; a text row alone does not establish that an entry ships. The saved index provenance describes a LiveOps5 manifest, which is not a precise public patch identifier.

In `Magical_Objects_Sources.tsv`, numeric chances are fractions: `0.5` means 50%. A blank means the entity does not explicitly set that chance; it does not mean zero. Inherited values and Drop Chance Selectors are not decoded. Shops, the Sandman, and camp rewards are outside that table's coverage. Source rows include templates and do not establish which sources are active in-game.

These source tables describe rarity chances, not the probability of each named object within a rarity. The internal entry `Rare_Chest` has not been matched to a verified in-game chest name. Runtime scaling, talent unlock ranks, and other unresolved mechanics need separate evidence.

## Contributing

Read [CONTRIBUTING.md](CONTRIBUTING.md) before submitting changes. Use an issue to report a questionable mapping or value, or submit a pull request with the source, game version when known, and relevant conditions. Coordinate article work through the wiki's [contributor guide](https://ravenswatch.wiki.gg/wiki/Help:Contributing).

Ravenswatch game text belongs to its respective rights holders. This repository does not grant an open-source license over extracted game text.
