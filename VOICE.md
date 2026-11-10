# Voice lines and audio

[Voice_Lines_Audio.tsv](data/Voice_Lines_Audio.tsv) pairs each spoken line in [Dialogue_Lines.tsv](data/Dialogue_Lines.tsv), and each narrated hero memoir chapter, with its recording in the game's English voice bank. It also lists every recording that no text names. It was read on November 10, 2026 from the same Steam install as the 1.06 tables (Steam build ID `25174305`). The voice bank was last written by the 1.06 update on October 12, 2026.

| `audio_status` | Rows | Meaning |
|---|---:|---|
| `clip found` | 5,371 | A clip in the speaker's folder has the line's name |
| `clip found, name spelled differently` | 3 | The names differ only in spelling or spacing: `Gepetto` in two Carmilla keys, a trailing space in one Sinbad key |
| `clip found, clip name adds _1` | 4 | The clip name ends in `_1` and the key does not: Merlin's three `Collecting_` lines and Kintarō's `Ultimate1_Upgrade1` |
| `memoir narration` | 91 | A hero memoir chapter (`Hero_<Hero>_Memoirs`, `_Memoir<N>_Desc`); seven for each of the 13 heroes |
| `no clip with this name` | 469 | No clip has the line's name (see below) |
| `clip has no text row` | 54 | A clip that no dialogue or memoir key names |
| Total | 5,992 | |

Six clips whose names refer to unreleased content are held back.

## Where the audio is

All recorded speech is in one file, `Audio/Voice_EN.bank`, an FMOD Studio 2.02 bank. In the install's cooked folder its file name is enciphered, as all cooked file names are. No other voice-language bank is installed. The bank holds 5,571 Ogg Vorbis clips at 48 kHz, about 6.9 hours, in two FSB5 sound chunks:

- `fsb_chunk` 1 holds 5,548 clips in an FMOD audio table: the game plays them by key from code. The table stores its keys hashed; the hash form was not identified.
- `fsb_chunk` 0 holds 23 clips that events inside the bank play. Their names begin with the three pigs' names (`Cynric_`, `Godric_`, `Alaric_`), the speakers of the `Story_3Pigs_` lines. Their names do not match those text keys, for example `Godric_Accept_EA_Like_1`, so none is paired with a line.

`fsb_index` is the clip's position in its chunk. `byte_offset` and `byte_length` give the clip's encoded data in the bank file. `seconds` is the clip's length from its sample count.

## How lines and clips are paired

A clip name is the text key without the speaker prefix: the key `SnowQueen_Ally_KillStreak_Dislike_1` plays the clip `Ally_KillStreak_Dislike_1`. The same clip name occurs once per speaker, so the speaker is needed to find a clip.

Chunk 1 stores its clips in speaker folders. Inside each folder the names are in sorted order, and a new folder starts wherever that order resets. This gives 21 folders:

- the 13 heroes, plus `Wolf` for Scarlet's wolf form;
- `BabaYaga`, `Castaway`, `Jack`, `Morgan`, `Refugee`, `Sandman` and `Sinbad`.

Each folder is named after the `speaker_prefix` in [Dialogue_Lines.tsv](data/Dialogue_Lines.tsv) whose keys match its clip names most often. The margins are wide, for example 342 matching names against 232 for the runner-up. Within a folder no two clips share a name. The folder names are inferred this way; the bank does not store them in readable form. Memoir clips carry the full memoir key and are matched to the memoir tables directly.

## Lines with no clip

The 469 `no clip with this name` rows group as follows. The absence of a same-named clip does not show that a line is never voiced.

| Lines | Rows |
|---|---:|
| `Command_` lines, every hero except Kintarō (Kintarō's are recorded) | 236 |
| `AFK` and `Ally_AFK` lines, every hero except Kintarō | 104 |
| `Menu_Validation`, `Menu_Victory` and `Menu_Defeat` | 41 |
| `Story_3Pigs_` lines (see chunk 0 above) | 23 |
| Other heroes' lines that name Kintarō | 20 |
| `Wish` | 12 |
| Merlin's `Nature_`, `Arcanic_`, `Divine_` and `Ultimate_2_` spell lines | 12 |
| Romeo and Juliet `SpecialCalled_by_` | 4 |
| Others | 17 |

Some clips with no text row have names close to these lines. They are not paired, because the names do not match and the clips were not listened to:

| Line keys | Clips (folder) |
|---|---|
| `Juliet_SpecialCalled_by_Juliet_1`, `_2` | `Special_1` to `Special_3` (Juliet) |
| `Romeo_SpecialCalled_by_Romeo_1`, `_2` | `Special_1` to `Special_3` (Romeo) |
| `Kintaro_Defense__1` to `_3` | `Defense_B_1` to `_3` (Kintaro) |
| `Merlin_Ultimate1_1`, `Merlin_Ultimate2_1` | `Ultimate_1`, `Ultimate_2` (Merlin) |
| `Kintaro_Spawn_(Scarlet,Kintaro)_H2` | `Spawn_H2` (Kintaro) |
| `Morgan_Weeping_Loop_1` | `Mordred_Weeping_Loop_2`, `_3` (Morgan) |

## Limits

- Nothing was checked by listening or in game. The game's FMOD library loaded ten clips under the names this table gives them, with matching lengths.
- Speaker folders are inferred from clip order and name matches, as described above.
- Hero banks (`Hero_<Hero>.bank`) hold combat sounds; they were not searched for speech.
