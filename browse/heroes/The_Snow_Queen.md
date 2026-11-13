# The Snow Queen

[All tables](../README.md)

[Abilities](#abilities) · [Ability values](#ability-values) · [Talents](#talents) · [Outfits](#outfits) · [Memoir](../memoirs/The_Snow_Queen.md)

Once loved by her people as a warm and caring sovereign sorceress, Nyss left and joined the Ravenswatch when Nightmares corrupted her healing powers, making her touch deadly and her gaze bitter. The Snow Queen freezes enemies at a distance before crushing them with destructive spells. Nothing shatters more completely than a monster turned to ice.

## Abilities

| Slot | Name | Description |
|---|---|---|
| Trait | Ice Crown | • **Passive:** Some abilities apply **CHILLED** to enemies hit, decreasing their move speed by **`{0}`%** for **`{1}`** seconds<br>• **Active:** Briefly becomes **INTANGIBLE** and shatter all **CHILLED** enemies, dealing **`{2}`** damage to them and removing their **CHILLED** status |
| Attack | Ice Lances | • Shoot out ice lances that deal **`{0}`** damage and pierce through enemies<br>• Ice lances deal **+`{1}`%** damage to **CHILLED** targets |
| Power | Frost Blast | • Create a large area of frost, dealing **`{0}`** damage to enemies in the area and inflicting them with **CHILLED** |
| Special | Ice Shards | • Throw a volley of ice shards at a short range, dealing up to **`{0}`** damage<br>• Ice Shards deal **+`{1}`%** damage to **CHILLED** enemies |
| Defense | Ice Skating | • Boost own movement speed and create frost underfoot, dealing **`{0}`** damage to enemies and inflicting them with **CHILLED**<br>• Briefly grants **INTANGIBLE** at the start of the ability |
| Ultimate 1 | Frost Ray | • Channel a Frost Ray to the ground, dealing **`{0}`** damage per second and applying **CHILLED** to hit enemies |
| Ultimate 2 | Snowstorm | • Summon a snow storm to deal **`{0}`** damage per second, inflicting all enemies within range with **CHILLED**<br>• The effect lasts **`{1}`** seconds |

## Ability values

**How to read the values**

- **Decoded** values come straight from the game files.
- **Decoded (baseline)** values assume a level 1 hero with damage 10, healing 10, no talents and no Magical Objects.
- **Not decoded** means nobody has found the number yet. It does not mean zero.
- **In-game check** shows what the maintainer read in the game's Compendium, when that was checked.

Baseline for this hero: Compendium level 1 figures: character damage 10, healing 10, no talents, no Magical Objects.

### Dash

| Name | Stat | Value | Unit | Status | In-game check |
|---|---|---|---|---|---|
| Dash | cooldown | 3 | seconds | Decoded |   |
| Dash | charges | 1 | charges | Decoded (baseline) |   |
| Dash | duration | 0.25 | seconds | Decoded (baseline) |   |
| Dash | resource cost | *not decoded* | resource | Not decoded |   |
| Dash | active duration | 0.25 | seconds | Decoded (baseline) |   |

### Trait

| Name | Stat | Value | Unit | Status | In-game check |
|---|---|---|---|---|---|
| Ice Crown | cooldown | *not decoded* | seconds | Not decoded | Game shows 6 |
| Ice Crown | charges | 1 | charges | Decoded (baseline) |   |
| Ice Crown | slow | *not decoded* | percent | Not decoded | Game shows 40 |
| Ice Crown | chilled duration | *not decoded* | seconds | Not decoded | Game shows 5 |
| Ice Crown | shatter damage | 60 | damage | Decoded (baseline) | Matches the game |
| Ice Crown | active duration | *not decoded* | seconds | Not decoded |   |
| Ice Crown | resource cost | *not decoded* | resource | Not decoded |   |

### Attack

| Name | Stat | Value | Unit | Status | In-game check |
|---|---|---|---|---|---|
| Ice Lances | damage per lance | 15 | damage | Decoded (baseline) | Matches the game |
| Ice Lances | bonus damage vs chilled | 50 | percent | Decoded (baseline) | Matches the game |
| Ice Lances | hit count | *not decoded* | hits | Not decoded |   |
| Ice Lances | hit damage sequence | *not decoded* | damage | Not decoded |   |
| Ice Lances | attack timing | *not decoded* | seconds | Not decoded |   |

### Power

| Name | Stat | Value | Unit | Status | In-game check |
|---|---|---|---|---|---|
| Frost Blast | cooldown | 10 | seconds | Decoded | Matches the game |
| Frost Blast | charges | 1 | charges | Decoded (baseline) |   |
| Frost Blast | damage | 50 | damage | Decoded (baseline) | Matches the game |
| Frost Blast | active duration | *not decoded* | seconds | Not decoded |   |
| Frost Blast | resource cost | *not decoded* | resource | Not decoded |   |

### Special

| Name | Stat | Value | Unit | Status | In-game check |
|---|---|---|---|---|---|
| Ice Shards | cooldown | 6 | seconds | Decoded | Matches the game |
| Ice Shards | charges | 1 | charges | Decoded (baseline) |   |
| Ice Shards | damage | 80 | damage | Decoded (baseline) | Game showed 65 on 1.05; changed in 1.06 |
| Ice Shards | bonus damage vs chilled | 50 | percent | Decoded (baseline) | Game showed 50 on 1.05; changed in 1.06 |
| Ice Shards | active duration | *not decoded* | seconds | Not decoded |   |
| Ice Shards | resource cost | *not decoded* | resource | Not decoded |   |
| Ice Shards | shard count | *not decoded* | shards | Not decoded |   |
| Ice Shards | damage per shard | *not decoded* | damage | Not decoded |   |

### Defense

| Name | Stat | Value | Unit | Status | In-game check |
|---|---|---|---|---|---|
| Ice Skating | cooldown | 6 | seconds | Decoded | Game shows 8 |
| Ice Skating | charges | 1 | charges | Decoded (baseline) |   |
| Ice Skating | damage | 30 | damage | Decoded (baseline) | Matches the game |
| Ice Skating | intangible duration | *not decoded* | seconds | Not decoded |   |
| Ice Skating | active duration | *not decoded* | seconds | Not decoded |   |
| Ice Skating | resource cost | *not decoded* | resource | Not decoded |   |
| Ice Skating | movement speed bonus | *not decoded* | percent | Not decoded |   |
| Ice Skating | frost duration | *not decoded* | seconds | Not decoded |   |

### Ultimate 1

| Name | Stat | Value | Unit | Status | In-game check |
|---|---|---|---|---|---|
| Frost Ray | cooldown | *not decoded* | seconds | Not decoded | Game shows 60 |
| Frost Ray | charges | 1 | charges | Decoded (baseline) |   |
| Frost Ray | damage per second | *not decoded* | damage per second | Not decoded | Game shows 160 |
| Frost Ray | active duration | *not decoded* | seconds | Not decoded |   |
| Frost Ray | resource cost | *not decoded* | resource | Not decoded |   |
| Frost Ray | channel duration limit | *not decoded* | seconds | Not decoded |   |

### Ultimate 2

| Name | Stat | Value | Unit | Status | In-game check |
|---|---|---|---|---|---|
| Snowstorm | cooldown | 60 | seconds | Decoded | Matches the game |
| Snowstorm | charges | 1 | charges | Decoded (baseline) |   |
| Snowstorm | damage per second | *not decoded* | damage per second | Not decoded | Game shows 5 |
| Snowstorm | duration | 10 | seconds | Decoded | Matches the game |
| Snowstorm | active duration | *not decoded* | seconds | Not decoded |   |
| Snowstorm | resource cost | *not decoded* | resource | Not decoded |   |

## Talents

Values separated by / are for Common / Rare / Epic / Legendary.

### Starting talents

Talents unlocked at rank 1, not counting ultimate upgrades.

| Talent | Effect |
|---|---|
| Cold Heart | Gain +4 / 5 / 6 / 7% Crit Chance for each CHILLED enemy nearby (can stack up to 5 times) |
| Flurry of Shards | SPECIAL can be held to hit up to 2 / 3 / 4 / 5 more time(s) |
| Frost Surge | POWER can be held to store up to 3 levels of charge before being released<br>Each charge level increases damage dealt by 20 / 25 / 30 / 35% and the effect radius by 10% |
| Hailstorm | After using POWER, 3 / 4 / 5 / 6 waves of ice strike the area and deal 20 damage each |
| Ice Clone | DEFENSE leaves an ice clone with 40% of Hero's Maximum Health, attracting enemies' attention<br>When destroyed or after 10 seconds have passed, it deals 40 / 60 / 80 / 100 area damage and inflicts CHILLED to enemies hit |
| Lance Burst | TRAIT sends 3 / 4 / 5 / 6 ATTACKS forward in a cone-shaped burst |
| Rupture | Quest (x20): SHATTER 2 enemies with a single TRAIT to earn +0.5 DMG<br>Complete: SHATTER leaves affected enemies VULNERABLE for 4 / 5 / 6 / 7 seconds |
| Slide | DASH creates frost underfoot, dealing 100 / 125 / 150 / 175% of DEFENSE damage to enemies passed |
| Snowball | POWER sends a snowball that deals 20 / 25 / 30 / 35 damage per second to enemies in its path and inflicts them with CHILLED<br>Each enemy hit reduces the size and damage of the snowball by 12.5 / 10 / 8.3333 / 7.1429% |
| Windy Lances | ATTACK's lances can curve to seek out targets, and their duration resets whenever they hit an enemy, up to 3 / 4 / 5 / 6 times |

### Ultimates

The talent tables do not include the base ultimates or their unlock ranks; this text is from the hero's text table.

| Ultimate | Description |
|---|---|
| Frost Ray | • Channel a frost ray to the ground that deals damage over time and creates **FROST** in a targetable area |
| Snowstorm | • Summon a snow storm that deals damage over time, inflicting all enemies within range with **CHILLED** |

### Ultimate upgrades

| Talent | Upgrades | Unlocks at rank | Effect |
|---|---|---|---|
| Royal Ray | Frost Ray | 1 | ULTIMATE triggers TRAIT at its start and deals +8 / 10 / 12 / 14% damage for each shattered enemy (up to +40 / 50 / 60 / 70%) |
| Ice Beam | Frost Ray | 9 | ULTIMATE now channels an ice beam, dealing 180 / 225 / 270 / 315% damage and inflicting CHILLED to first enemy hit |
| Rending Storm | Snowstorm | 6 | Each time The Snow Queen casts TRAIT, POWER or SPECIAL within the ULTIMATE zone, the storm unleashes a burst dealing 20 / 25 / 30 / 35 damage |
| Shattering Storm | Snowstorm | 9 | When ULTIMATE effect ends, zone explodes and SHATTERS all enemies insides, dealing 72 / 90 / 108 / 126 damage |

### Other talents

| Talent | Unlocks at rank | Effect |
|---|---|---|
| Frost Queen | 2 | Frost generated by your abilities remains on the ground for 2 / 3 / 4 / 5 seconds<br>Enemies CHILLED by The Snow Queen suffer 5 damage per second |
| Radiant Crown | 2 | Gain +1 TRAIT charge<br>Any Shatter effect deals +20 / 25 / 30 / 35% damage |
| Ice Spray | 3 | SPECIAL sprays two bursts of ice shards in opposite directions, dealing +32 / 40 / 48 / 56% damage to CHILLED enemies. |
| Strafe | 3 | DEFENSE sends up to 5 / 6 / 7 / 8 successive ATTACKS to nearby enemies |
| Ice Shield | 4 | DEFENSE grants a 16 / 20 / 24 / 28 SHIELD to The Snow Queen and all Heroes passed for 6 seconds |
| Shattering Blast | 4 | POWER triggers SHATTER when hitting enemies that are already CHILLED<br>Each SHATTER deals +20 / 25 / 30 / 35% damage |
| Dual Lances | 5 | ATTACK sends forth two lances side by side but their maximum range is reduced by 45%<br>Each lance deals 70 / 80 / 90 / 100% damage |
| Freezing Stars | 5 | DASH leaves behind an ice star that explodes due to a Shattering effect or after 10 seconds<br>The ice star's explosion deals 32 / 40 / 48 / 56 area damage and inflicts CHILLED to enemies hit |
| Ice Cores | 7 | Each enemy hit by POWER summons 2 cores of ice (up to 6)<br>The SPECIAL consumes each core to fire an ATTACK dealing 80 / 100 / 120 / 140% damage |
| Protective Crown | 7 | TRAIT grants 4 / 5 / 6 / 7 SHIELD for 6 seconds to all Heroes around for each enemy hit (up to 4 times) |
| Frostbite | 8 | All abilities that deal extra damage to CHILLED enemies deal +20 / 25 / 30 / 35% extra damage |
| Pirouette | 8 | Retriggering DEFENSE while it is in progress triggers a spin dealing 40 / 50 / 60 / 70 area damage, +50% to CHILLED enemies |

## Outfits

| Outfit | How to unlock | Description |
|---|---|---|
| Signature Outfit | Completed the 'Rupture' Talent Quest | Unlocked by completing the 'Rupture' Talent Quest |
| Traveler Outfit | Reached Chapter 3 | Unlocked by reaching Chapter 3 |
| Master Outfit | Completed the game on Darkness Difficulty | Unlocked by completing the game on Darkness Difficulty |
| Hidden Outfit | Ice Breaker | Hidden Requirements |
| Ravens Outfit | Ravens Skin Pack Acquired | Available in the Ravens Skin Pack |
| Nightmares Outfit | Nightmares Skin Pack Acquired | Available in the Nightmares Skin Pack |
| Fairytales Outfit | Fairytales Skin Pack Acquired | Available in the Fairytales Skin Pack |
| Unleashed Outfit | Unleashed Skin Pack Acquired | Available in the Unleashed Skin Pack |
| Mercenaries Outfit | Mercenaries Skin Pack Acquired | Available in the Mercenaries Skin Pack |


**How to read the text**

- **Bold** words are highlighted in the game.
- `{0}`, `{1}` and so on are numbers or names the game fills in while you play.

Source: [`Hero_Snow_Queen_Common.LangEN.tsv`](../../data/Hero_Snow_Queen_Common.LangEN.tsv), [`Hero_Snow_Queen_Abilities.tsv`](../../data/Hero_Snow_Queen_Abilities.tsv), [`Hero_Snow_Queen_Talents.tsv`](../../data/Hero_Snow_Queen_Talents.tsv), [`Hero_Snow_Queen_Skins.LangEN.tsv`](../../data/Hero_Snow_Queen_Skins.LangEN.tsv).
Game version: Game build 1.06 (Steam build ID 25174305); the displayed version string is unverified. See VERSION.json.

*This page is generated from the TSV files in [data/](../../data/) by `tools/build_browse.py`. Do not edit it by hand; fix the data and re-run the script.*
