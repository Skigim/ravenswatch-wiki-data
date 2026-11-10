# Voice lines and audio

[Voice_Lines_Audio.tsv](data/Voice_Lines_Audio.tsv) pairs each spoken line in [Dialogue_Lines.tsv](data/Dialogue_Lines.tsv), and each narrated hero memoir chapter, with its recording in the game's audio banks. It also lists the recordings that no text names. It was read on November 10, 2026 from the same Steam install as the 1.06 tables, which was still on Steam build ID `25174305`.

| `audio_status` | Rows | Meaning |
|---|---:|---|
| `clip found` | 5,429 | A clip has the line's name: 5,371 in `Voice_EN.bank`, 58 in a hero bank or `Maps.bank` |
| `clip found, name spelled differently` | 3 | The names differ only in spelling or spacing: `Gepetto` in two Carmilla keys, a trailing space in one Sinbad key |
| `clip found, clip name adds _1` | 4 | The clip name ends in `_1` and the key does not: Merlin's three `Collecting_` lines and Kintarō's `Ultimate1_Upgrade1` |
| `memoir narration` | 91 | A hero memoir chapter (`Hero_<Hero>_Memoirs`, `_Memoir<N>_Desc`); seven for each of the 13 heroes |
| `no clip with this name` | 411 | No clip in any bank has the line's name (see below) |
| `clip has no text row` | 66 | A clip that no dialogue or memoir key names: 54 in `Voice_EN.bank`, 12 alternate takes in hero banks |
| Total | 6,004 | |

Six clips whose names refer to unreleased content are held back.

## Where the audio is

`bank` names the file. All are FMOD Studio 2.02 banks in the install's `Audio` folder; on disk their file names are enciphered, as all cooked file names are. No other voice-language bank is installed. The clips are Ogg Vorbis at 48 kHz.

- **`Voice_EN.bank`** holds almost all speech: 5,571 clips, about 6.9 hours, in two FSB5 sound chunks.
  - `fsb_chunk` 1 holds 5,548 clips in an FMOD audio table: the game plays them by key from code. The table stores its keys hashed; the hash form was not identified.
  - `fsb_chunk` 0 holds 23 clips that events inside the bank play. Their names begin with the three pigs' names (`Cynric_`, `Godric_`, `Alaric_`), the speakers of the `Story_3Pigs_` lines. Their names do not match those text keys, for example `Godric_Accept_EA_Like_1`, so none is paired with a line.
- **`Hero_<Hero>.bank`** (12 banks; Romeo and Juliet share `Hero_RomeoJuliet.bank`) holds each hero's menu lines (`Menu_Validation`, `Menu_Victory`, `Menu_Defeat`). `Hero_RomeoJuliet.bank` also holds Romeo's and Juliet's `SpecialCalled_by_` lines and the `Ally_Death_` lines each says when the other dies. Extra takes, such as `SpecialCalled_by_Romeo_3_bis` and `Carmilla_Menu_Validation_2`, have no text row.
- **`Maps.bank`** holds the `Wish` lines of Carmilla, Juliet, Kintarō, Romeo and Sun Wukong.

`fsb_index` is the clip's position in its chunk. `byte_offset` and `byte_length` give the clip's encoded data in the bank file. `seconds` is the clip's length from its sample count. The hero banks also hold combat sounds and short voice efforts (`Juliet_Voice_Hurt_04` and the like); those are not lines and are not listed.

## How lines and clips are paired

In `Voice_EN.bank` a clip name is the text key without the speaker prefix: the key `SnowQueen_Ally_KillStreak_Dislike_1` plays the clip `Ally_KillStreak_Dislike_1`. The same clip name occurs once per speaker, so the speaker is needed to find a clip.

Chunk 1 stores its clips in speaker folders. Inside each folder the names are in sorted order, and a new folder starts wherever that order resets. This gives 21 folders:

- the 13 heroes, plus `Wolf` for Scarlet's wolf form;
- `BabaYaga`, `Castaway`, `Jack`, `Morgan`, `Refugee`, `Sandman` and `Sinbad`.

Each folder is named after the `speaker_prefix` in [Dialogue_Lines.tsv](data/Dialogue_Lines.tsv) whose keys match its clip names most often. The margins are wide, for example 342 matching names against 232 for the runner-up. Within a folder no two clips share a name. The folder names are inferred this way; the bank does not store them in readable form. Memoir clips carry the full memoir key and are matched to the memoir tables directly. `speaker_folder` is filled for `Voice_EN.bank` clips only.

Lines left without a clip are then looked up in the other banks:

- A clip named with the full key, prefix included (`Juliet_Menu_Victory_1`, `Romeo_Wish_1`), pairs in any bank.
- A clip named with the key minus its prefix (`SpecialCalled_by_Romeo_2`) pairs only in the speaker's own hero bank, and only when a single line of that bank's speakers has that name. For example, `Ally_Death_Romeo_1` in `Hero_RomeoJuliet.bank` is Juliet's line, because Romeo has no `Ally_Death_Romeo` line.
- Kintarō's hero bank also holds copies of his ability lines under the names of clips already paired in `Voice_EN.bank`. Those copies are not listed.

## Lines with no clip

The 411 `no clip with this name` rows group as follows. The absence of a same-named clip does not show that a line is never voiced.

| Lines | Rows |
|---|---:|
| `Command_` lines, every hero except Kintarō (Kintarō's are recorded) | 236 |
| `AFK` and `Ally_AFK` lines, every hero except Kintarō | 104 |
| `Story_3Pigs_` lines (see chunk 0 above) | 23 |
| Other heroes' lines that name Kintarō | 20 |
| Merlin's `Nature_`, `Arcanic_`, `Divine_` and `Ultimate_2_` spell lines | 12 |
| `Kintaro_Menu_Validation_1`, `Wolf_Menu_Victory_1`, `Wolf_Menu_Defeat_1` | 3 |
| Merlin's `Wish` lines | 2 |
| Others | 11 |

Some clips with no text row have names close to these lines. They are not paired, because the names do not match and the clips were not listened to:

| Line keys | Clips (bank, folder) |
|---|---|
| `Kintaro_Defense__1` to `_3` | `Defense_B_1` to `_3` (`Voice_EN.bank`, Kintaro) |
| `Merlin_Ultimate1_1`, `Merlin_Ultimate2_1` | `Ultimate_1`, `Ultimate_2` (`Voice_EN.bank`, Merlin) |
| `Kintaro_Spawn_(Scarlet,Kintaro)_H2` | `Spawn_H2` (`Voice_EN.bank`, Kintaro) |
| `Morgan_Weeping_Loop_1` | `Mordred_Weeping_Loop_2`, `_3` (`Voice_EN.bank`, Morgan) |

Romeo and Juliet also have untexted clips named `Special_1` to `Special_3` in `Voice_EN.bank`. They are not the `SpecialCalled_by_` lines, which are in `Hero_RomeoJuliet.bank`.

## Limits

- Nothing was checked by listening or in game. The game's FMOD library loaded 21 clips from `Voice_EN.bank` and `Hero_RomeoJuliet.bank` under the names this table gives them, with matching lengths.
- Speaker folders are inferred from clip order and name matches, as described above.
- `Master.bank` and `Music.bank` hold no clip named after a dialogue key and were not searched further.

## Corrections

The first version of this table (`2026-11-10-voice-audio`) read `Voice_EN.bank` only and said all speech is there. The 58 lines found in hero banks and `Maps.bank` were listed as `no clip with this name`, and the table had no `bank` column.
