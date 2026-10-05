# Contributing

This repository shares selected decoded tables used to work on the Ravenswatch Wiki. Changes should help contributors trace a wiki statement to its evidence.

## Report a problem

Include the file, key or entity, current value, proposed correction, and supporting evidence. Record the game version and test conditions when known. Distinguish a decoded value from an observation and an inference. If a name or mapping is unresolved, say so rather than treating an internal identifier as a game display name.

## Change a table

Work directly in this repository or its Git checkout. Keep the existing TSV columns, UTF-8 encoding, original text keys, row indices, and blank rows. Preserve every tooltip bullet, game markup, and unresolved placeholder. Do not silently replace source text with a prose paraphrase or fill unknown cells with zero. Explain the source of changed values and refresh the corresponding row count and SHA-256 entry in TABLES.md. Follow [VERSIONING.md](VERSIONING.md) to update game-version evidence and handle partial refreshes without relabeling older tables.

Submit new table selections separately for review before adding them. The initial publication contains 43 decoded exports; TABLES.md also identifies later selected tables separately. The six numerical talent tables retain decoded traces, interpretation history, compendium confirmations and unlock ranks in derived columns, while the original text exports stay verbatim. The Git ignore rules explicitly allow those filenames; a new file requires a deliberate allowlist change.

## Repository contents

Keep this repository limited to selected TSV tables and the documentation and Git configuration needed to use them. Do not commit images, icons, portraits, audio, video, fonts, binaries, game archives, raw decoded game files, game installations, screenshots, upload bundles, credentials, private notes, or local machine paths.

Use the wiki for article prose and uploaded assets. This repository is the reference for the selected data tables.
