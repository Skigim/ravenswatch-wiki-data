# Contributing

This repository shares selected decoded tables used to work on the Ravenswatch Wiki. Changes should help contributors trace a wiki statement to its evidence.

## Report a problem

Include the file, key or entity, current value, proposed correction, and supporting evidence. Record the game version and test conditions when known. Distinguish a decoded value from an observation and an inference. If a name or mapping is unresolved, say so rather than treating an internal identifier as a game display name.

## Change a table

Work directly in this repository or its Git checkout. Keep the existing TSV columns, UTF-8 encoding, original text keys, row indices, and blank rows. Preserve every tooltip bullet, game markup, and unresolved placeholder. Do not silently replace source text with a prose paraphrase or fill unknown cells with zero. Explain the source of changed values and refresh the corresponding row count and SHA-256 entry in TABLES.md. Follow [VERSIONING.md](VERSIONING.md) to update game-version evidence and handle partial refreshes without relabeling older tables.

Submit new table selections separately for review before adding them. TABLES.md lists the 46 decoded text and index exports and the derived tables separately. The 13 numerical talent tables retain decoded traces, interpretation history, compendium confirmations and unlock ranks in derived columns, while the original text exports stay verbatim. The one exception is the spelling corrections to the hero memoir tables; record any new one in `data/Hero_Memoirs_Corrections.tsv` and the table's header note. The 18 numerical value tables are described in [VALUES.md](VALUES.md); when correcting one, keep the decoded columns and the check columns distinct and say whether a new figure was decoded or read in the game. The Git ignore rules explicitly allow those filenames; a new file requires a deliberate allowlist change.

## Repository contents

Keep this repository limited to selected TSV tables and the documentation and Git configuration needed to use them. Do not commit images, icons, portraits, audio, video, fonts, binaries, game archives, raw decoded game files, game installations, screenshots, upload bundles, credentials, private notes, or local machine paths.

Use the wiki for article prose and uploaded assets. This repository is the reference for the selected data tables.


Gameplay-note imports are documented in [ENEMIES.md](ENEMIES.md),
[COMBAT.md](COMBAT.md), and [MAP_GENERATION.md](MAP_GENERATION.md). Keep
localized names distinct from descriptive labels, fallback values distinct
from referenced constants, and configuration distinct from inferred models
and observations. A dated note without game-version evidence must receive
an unverified table override rather than inheriting the default 1.06 label.
