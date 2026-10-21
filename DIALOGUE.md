# Dialogue lines

[Dialogue_Lines.tsv](data/Dialogue_Lines.tsv) lists every non-blank spoken line in the game's dialogue text tables, one row per line. Each row gives the line, who says it, who it is said to or about when the game data names that, and the game components that play it. It was decoded on October 20, 2026 from the same 1.06 extraction as the text tables: re-exporting `Common`, `Enemy_Common`, `Hero_RED_Common`, `Hero_Kintaro_Common` and `Melodies` from that tree reproduces the published files byte for byte.

| Source table | Rows | Lines tied to a bark setup | Key named directly by an entity | Situation read from the key | Not found |
|---|---:|---:|---:|---:|---:|
| 13 `Hero_<Hero>_Barks` tables | 5,196 | 4,384 | 0 | 800 | 12 |
| `NPC_Sandman` | 176 | 58 | 0 | 112 | 6 |
| `NPC_Sinbad` | 174 | 160 | 1 | 13 | 0 |
| `NPC_Morgan` | 96 | 95 | 0 | 1 | 0 |
| `NPC_BabaYaga` | 83 | 80 | 0 | 3 | 0 |
| `Map_Dark_Hills_Dialogs` | 57 | 34 | 21 | 2 | 0 |
| `Refugees` (spoken rows only) | 65 | 65 | 0 | 0 | 0 |
| Total | 5,847 | 4,876 | 22 | 931 | 18 |

The total counts the two Baba Yaga lines whose bark name differs only in letter case (see below) as tied to a bark setup.

## What is included

All non-blank rows of the 13 hero bark tables, the four `NPC_` tables and `Map_Dark_Hills_Dialogs` are included. Six blank rows (three each in the Carmilla and Merlin bark tables) are left out. 54 non-blank hero bark rows are held back for now and are not in this table. `Refugees` also holds choice labels, reward text and names. Only the 65 rows that a refugee bark setup plays are included: each refugee's opening line and the answer to each choice.

Hero memoirs are letters, not speech, and are already published as their own tables. Tutorials, quest-log labels and notifications are left out. `Common` has a `Sandman_Quote` row with the same text as `Sandman_First_Opening_1`; only the `NPC_Sandman` row is included.

`text_en` is the game text exactly as exported: spelling, game markup and literal `\n` escapes are unchanged. One key, `Sinbad_Roc_Boss_Failed_FollowUp_1 `, ends with a space in the game data and keeps it.

## How the columns are filled

A hero, NPC or refugee speaks through a bark player. Each bark player names a text table, a key prefix and the text key for the speaker's display name. A line's key is the prefix, a bark name and a variant, for example `Scarlet` + `Kill_Crab` + `1`. A bark setup elsewhere in the game data plays a bark name.

| Column | Contents |
|---|---|
| `source_table`, `index`, `key`, `text_en` | The text row, as in the text exports |
| `speaker_prefix` | The bark player's key prefix that starts the key. Scarlet's table has two, `Scarlet` and `Wolf` |
| `speaker`, `speaker_name_key` | The display name the bark player uses, and its text key. A refugee's name comes from its own scenario entity |
| `bark` | The bark name: the bark setup's name when one matches, otherwise the key without prefix and variant |
| `variant` | The suffix after the bark name: a number, or a letter and line number in a conversation (`A1`, `B3`) |
| `conversation` | The participants named in brackets in a conversation key, for example `Scarlet,Piper` |
| `target`, `target_basis` | Who the line is said to or about, and where that came from (see below) |
| `trigger_status` | `bark setup`, `key referenced`, `key name`, `not found`, or `bark setup (letter case differs)` |
| `trigger_situation`, `situation_basis` | For `key name` rows only: the situation the key names, and where that reading comes from (see below) |
| `trigger_entities`, `trigger_setups` | The entities that hold the matching bark setups, and each setup's group path and name |
| `trigger_chain` | The nearest components upstream of each bark setup (see below) |

`target_basis` is one of three sources, tried in this order:

- `key conversation`: the other participants in a conversation key.
- `listener flag`: the flags on the game event listener that starts the bark. These name a hero (`Beowulf`, `Red`, `Snow_Queen`), a relationship (`Liked_Ally`, `Disliked_Hero`), or, for kill lines, the enemy group (`Crabs`, `Nightmare_Cultists`). `Elite` is not copied into `target`, because the data does not show whether it includes or excludes elites. It stays in `trigger_chain`.
- `key`: a hero name at the end of the bark name, such as `Ally_Fall_Merlin` or `Revived_by_Juliet`, or the enemy tribe named by a `key name` kill or last-death line (see below).

A blank `target` means none of these name one.

## Trigger chains

`trigger_chain` follows references backwards from the bark setup to the nearest game event listener, named event listener, counter, detector or mode state. It keeps only listeners, states, timers, counters, detectors, testers and random selectors, with their names as authored. A listener's flags or named event follow it in brackets, for example `Level_Up Event Listener [HERO_XP_LEVEL_UP]`. Alternative paths are separated by `||`.

The names are the developers' component names, not player-facing text. They show which event, state or condition leads to the line. They do not give chances, cooldowns or delays; those values were not decoded. The chain is read from the order of records in each resource file, so treat it as a lead and check it against the setup name and group in `trigger_setups`. Cinematics, refugee scenarios and some quest dialogs play their setups from a sequence or choice the reader does not follow; their chain is blank and `trigger_entities` names the cinematic or scenario.

## Situations read from key names

949 lines have no bark setup or direct key reference. No trigger for their bark names was found in any decoded resource folder (searched ignoring letter case, including level streams, 3D, video and fonts), in the install's asset map, in the game executable (as text, or as CRC-32, FNV-1, FNV-1a or djb2 hashes), or in the game's log files. The executable holds no bark names at all, including ones the data does trigger, such as `Kill_Crab`, so these lines are most likely started from compiled game code, which was not decoded. The English voice bank has clips with the same names, for example `Command_Bark_1` to `Command_Bark_10`, so the lines were recorded.

For 931 of them the key names a situation clearly enough to use, for example `Open_Chest`, `Menu_Victory` or `Opening_LastDeath_Gnoll`. These rows have the status `key name`, and `trigger_situation` gives that situation. Their `trigger_entities`, `trigger_setups` and `trigger_chain` stay blank. `situation_basis` says where the reading comes from:

| Basis | Meaning |
|---|---|
| `key` | The key names the situation, for example `Open_Lock` or `Opening_Comeback_Week` |
| `owner` | The wiki editors' reading of a key that is less explicit, for example `Dodge`, `Defense_Mounted` or `Command_Bark` |
| `key + owner` | The key, with the wiki editors' confirmation of what it means (`Menu_Validation`: the hero is confirmed in the menu). `Roc_On_The_Move` and `Weeping_Loop` are also placed by where they sit in the text table: Sinbad's between the triggered `Roc_Escort_Start` and `Roc_Approach_Deposit`, Morgan's right after her `Quest_Failed` lines, matching `Mordred_Weeping_Loop`, which plays when the Mordred quest fails. `Weeping_Loop` has no clip in the voice bank |
| `owner + game text` | The wiki editors' reading, with ability and spell names from the game's text tables, for example Merlin's Nature, Arcane, Sacred and Forbidden Spells, or Kintarō's Giant Carp with Rain of Fish |
| `key + game text` | The key, with a name from the game's text tables (`Baba Yaga's Mortar`) |
| `key + enemy tables` | The key, with the enemy tribe from [Enemy_Definitions.tsv](data/Enemy_Definitions.tsv). The token is paired with the tribe the same way the game's `Kill_` listener flags pair them, for example `MarshGhoul` with `Marsh_Ghouls` |
| `key + game data` | The key, with a listener flag that is not an enemy tribe (`Boss`, `Nightmare_Creature`) |
| `key + line text` | The key, read with what the line says (`Opening_LastDeath_Rich`: the lines mourn unspent dream shards; `Opening_SameDeath`: "Twice?" and "nearly the exact same thing last time", read with the other openings that name the cause of the last death) |

For kill and last-death lines, `target` holds the enemy tribe or flag, with `target_basis` `key`. Keys marked `OLD` (`Trait_3_OLD`, `Roc_OLD_Quest_Start`) have the situation "Key marked OLD; may be unused". None of these situations were checked in game, and a key name does not show chance, cooldown or whether the line plays at all.

## Limits

- `not found` (18 rows) means no trigger was decoded and the key does not name a clear situation: `Wish` (six heroes) and the Sandman's `Approching`.
- The Sandman has bark setups for Geppetto and Sun Wukong openings and farewells, but no text lines for them. The `Quit_without_Buying_Melusine` setup plays the bark name `Quit_after_Buying_Melusine`, so the `Sandman_Quit_without_Buying_Melusine_1` line is `not found`.
- Baba Yaga's `Final_Hero_Dies` lines match the setup bark `Final_Hero_dies` only when letter case is ignored. Their status says so; whether the game matches them this way was not checked in game.
- The three pigs in `Map_Dark_Hills_Dialogs` play their lines through dialog components on the pig houses that name the text key directly. Those rows are `key referenced`, with the house entity in `trigger_entities`, and have no speaker: the dialog components name no bark player or speaker name.
- Castaway lines in `NPC_Sinbad` have a bark player with no speaker-name key, so `speaker` is blank.
- `Wolf` lines use Scarlet's bark player name key, so their `speaker` is `Scarlet`; `speaker_prefix` keeps them apart.
- Nothing here was checked in game.
