# Contributing

This repository shares selected decoded tables used to work on the Ravenswatch Wiki. Changes should help contributors trace a wiki statement to its evidence.

## Report a problem

Include the file, key or entity, current value, proposed correction, and supporting evidence. Record the game version and test conditions when known. Distinguish a decoded value from an observation and an inference. If a name or mapping is unresolved, say so rather than treating an internal identifier as a game display name.

## Change a table

Keep the existing TSV columns, UTF-8 encoding, original text keys, row indices, and blank rows. Preserve every tooltip bullet, game markup, and unresolved placeholder. Do not silently replace source text with a prose paraphrase or fill unknown cells with zero. Explain the source of changed values and refresh the corresponding row count and SHA-256 entry in TABLES.md.

Submit new table selections separately for review before adding them. The initial publication contains exactly the 43 files listed in TABLES.md. The Git ignore rules explicitly allow those filenames; a new file requires a deliberate allowlist change.

## Repository contents

Keep this repository limited to selected TSV tables and the documentation and Git configuration needed to use them. Do not commit images, icons, portraits, audio, video, fonts, binaries, game archives, raw decoded game files, game installations, screenshots, upload bundles, credentials, private notes, or local machine paths.

Use the wiki for article prose and uploaded assets. This repository is the reference for the selected data tables.
