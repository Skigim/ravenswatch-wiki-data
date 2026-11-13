# Melodies

[All tables](README.md)

| Melody | Effect |
|---|---|
| The Goose Girl Melody | In combat, every **`{0}`** seconds, each hero unleashes a powerful wind that blows around them, dealing **`{1}`** area damage |
| Galahad Melody | Grants **`{0}`** Raven's Feather(s) and fully heals all Heroes at the start of each day or night |
| Hansel and Gretel Melody | When the Master Nightmare is awakened, grants **`{0}`** **DMG** every **`{1}`** seconds until the final showdown begins |
| Lady of the Lake Melody | Healing Foutains and Sacrificial Idols grant **+`{0}`%** **VITALITY** or **DMG** |
| Tortoise Melody | Increases move speed for all Heroes by **`{0}`%** |
| Fairy Godmother Melody | The group of heroes instantly levels up |
| The Little Tailor Melody | Grants **`{0}`** consumables each time the group of Heroes reaches a level above `{1}` |
| Lucky Hans Melody | Magical Object collections require **`{0}`** item less to be considered completed |
| Sheherazad Melody | Dreams obtained from the Sandman are restocked **`{0}`** time(s) after being purchased |
| Merry Men Melody | The locks no longer need keys to be opened; keys now grant **`{0}` Dream Shards** each |
| Long John Silver Melody | Reveals all Raven Marks on the map |
| Otohime Melody | The Hourglass of Dreams empties **`{0}`%** slower |

## Values

**How to read the values**

- **Decoded** values come straight from the game files.
- **Decoded (baseline)** values assume a level 1 hero with damage 10, healing 10, no talents and no Magical Objects.
- **Not decoded** means nobody has found the number yet. It does not mean zero.
- **In-game check** shows what the maintainer read in the game's Compendium, when that was checked.

### Melody effect

| Name | Stat | Value | Unit | Status | In-game check |
|---|---|---|---|---|---|
| The Goose Girl Melody | wind trigger interval | 10.0 | seconds | Decoded | Game showed 15 on 1.05; changed in 1.06 |
| The Goose Girl Melody | area damage | *not decoded* | damage | Not decoded | Game showed 150 on 1.05; changed in 1.06 |
| Galahad Melody | raven feathers granted | 1 | Raven Feathers | Decoded |   |
| Hansel and Gretel Melody | damage gained per trigger | 8.0 | DMG | Decoded |   |
| Hansel and Gretel Melody | trigger interval | 20.0 | seconds | Decoded |   |
| Lady of the Lake Melody | extra fountain vitality or idol damage | 100.0 | percent | Decoded |   |
| Tortoise Melody | move speed bonus | 20.0 | percent | Decoded |   |
| Fairy Godmother Melody | static description | The group of heroes instantly levels up |   | Fixed text |   |
| The Little Tailor Melody | consumables per qualifying level | 1 | consumables | Decoded | Game showed 3 on 1.05; changed in 1.06 |
| The Little Tailor Melody | exclusive level threshold | 6 | level | Decoded | Game showed 10 on 1.05; changed in 1.06 |
| Lucky Hans Melody | collection copy reduction | 1 | copies | Decoded |   |
| Sheherazad Melody | sandman restocks after purchase | 1 | restocks | Decoded |   |
| Merry Men Melody | dream shards per key | 150 | Dream Shards | Decoded |   |
| Long John Silver Melody | static description | Reveals all Raven Marks on the map |   | Fixed text |   |
| Otohime Melody | hourglass drain slowdown | 25.0 | percent | Decoded |   |
| The Goose Girl Melody | damage scaling rule | *not decoded* |   | Not decoded |   |
| Galahad Melody | feather grant vs day night heal trigger | *not decoded* |   | Not decoded |   |
| Hansel and Gretel Melody | trigger cap and showdown condition | *not decoded* |   | Not decoded |   |
| Tortoise Melody | day night condition implementation | *not decoded* |   | Not decoded |   |
| The Little Tailor Melody | strict level comparison implementation | *not decoded* |   | Not decoded |   |
| Otohime Melody | hourglass rate and duration formula | *not decoded* |   | Not decoded |   |


**How to read the text**

- **Bold** words are highlighted in the game.
- `{0}`, `{1}` and so on are numbers or names the game fills in while you play.

Source: [`Melodies_Index.tsv`](../data/Melodies_Index.tsv), [`Melodies.LangEN.tsv`](../data/Melodies.LangEN.tsv), [`Melodies_Values.tsv`](../data/Melodies_Values.tsv).
*This page is generated from the TSV files in [data/](../data/) by `tools/build_browse.py`. Do not edit it by hand; fix the data and re-run the script.*
