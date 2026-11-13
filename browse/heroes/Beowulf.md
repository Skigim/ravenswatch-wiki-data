# Beowulf

[All tables](../README.md)

[Abilities](#abilities) · [Ability values](#ability-values) · [Talents](#talents) · [Outfits](#outfits) · [Memoir](../memoirs/Beowulf.md)

Beowulf's renown was earned slaying the vile Grendel, Grendel's mother, and a dragon. Honour-bound to raise the spawn of his cursed victim, he trains his drake pup ward in the arts of war. Together a gruesome pair, the sword-and-shield warrior and the toddling fire breather are a force to be feared, even by Nightmares. Their bark is hotter than their bite.

## Abilities

| Slot | Name | Description |
|---|---|---|
| Trait | Last Wyrm | • Call **Wyrm** to empower next **POWER**, **SPECIAL** or **DEFENSE** |
| Attack | Runic Sword | • Chain together a series of attacks with the sword. Last attack deals **+`{0}`%** damage<br>• Whole combo deals a total of **`{1}`** damage |
| Power | Shockwave | • Scrape the sword on the floor to project a shockwave in front that deals **`{0}`** damage along its path<br>• **+WYRM**: Deals **+`{1}`%** damage and applies **IGNITE** to all enemies hit |
| Special | Whirlwind | • Spin with the sword, briefly becoming **INTANGIBLE** and dealing **`{0}`** damage all around then finish with a swing that deals **`{1}`** damage all around<br>• **+WYRM**: Deals **+`{2}`%** damage and finisher applies **IGNITE** to all enemies hit |
| Defense | Shield | • Hold to raise shield and block all incoming damage. Release to bash with shield and deal **`{0}`** damage<br>• **+WYRM**: Deals **+`{1}`%** damage. Each attack blocked heals all nearby Heroes by **`{2}`%** of damage blocked |
| Ultimate 1 | Dragon Flight | • Wyrm takes off and tracks enemies, continuously breathing fire during its flight and dealing **`{0}`** damage per second and applying **IGNITE** to all enemies hit<br>• **TRAIT** is disabled during this time |
| Ultimate 2 | Raging Chain | •  Rush forward, then chain together a series of attacks with the sword and Wyrm, dealing up to **`{0}`** damage<br>• `{1}` is **INTANGIBLE** during the whole abillity |

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
| Last Wyrm | cooldown | 6 | seconds | Decoded (baseline) | Matches the game |
| Last Wyrm | charges | 1 | charges | Decoded (baseline) |   |
| Last Wyrm | active duration | *not decoded* | seconds | Not decoded |   |
| Last Wyrm | resource cost | *not decoded* | resource | Not decoded |   |

### Attack

| Name | Stat | Value | Unit | Status | In-game check |
|---|---|---|---|---|---|
| Runic Sword | final hit bonus | 200 | percent | Decoded | Matches the game |
| Runic Sword | full combo damage | *not decoded* | damage | Not decoded | Game shows 70 |
| Runic Sword | hit count | *not decoded* | hits | Not decoded |   |
| Runic Sword | hit damage sequence | *not decoded* | damage | Not decoded |   |
| Runic Sword | attack timing | *not decoded* | seconds | Not decoded |   |

### Power

| Name | Stat | Value | Unit | Status | In-game check |
|---|---|---|---|---|---|
| Shockwave | cooldown | 5 | seconds | Decoded | Matches the game |
| Shockwave | charges | 1 | charges | Decoded (baseline) |   |
| Shockwave | damage | *not decoded* | damage | Not decoded | Game showed 50 on 1.05; changed in 1.06 |
| Shockwave (Wyrm-empowered) | wyrm bonus damage | 50 | percent | Decoded | Matches the game |
| Shockwave | active duration | *not decoded* | seconds | Not decoded |   |
| Shockwave | resource cost | *not decoded* | resource | Not decoded |   |

### Special

| Name | Stat | Value | Unit | Status | In-game check |
|---|---|---|---|---|---|
| Whirlwind | cooldown | 8 | seconds | Decoded | Matches the game |
| Whirlwind | charges | 1 | charges | Decoded (baseline) |   |
| Whirlwind | spin damage | 15 | damage | Decoded (baseline) | Matches the game |
| Whirlwind | finisher damage | 60 | damage | Decoded (baseline) | Matches the game |
| Whirlwind (Wyrm-empowered) | wyrm bonus damage | 50 | percent | Decoded | Matches the game |
| Whirlwind | active duration | *not decoded* | seconds | Not decoded |   |
| Whirlwind | resource cost | *not decoded* | resource | Not decoded |   |

### Defense

| Name | Stat | Value | Unit | Status | In-game check |
|---|---|---|---|---|---|
| Shield | cooldown | 6 | seconds | Decoded | Matches the game |
| Shield | charges | 1 | charges | Decoded (baseline) |   |
| Shield | bash damage | 30 | damage | Decoded (baseline) | Matches the game |
| Shield (Wyrm-empowered) | wyrm bonus damage | 50 | percent | Decoded | Matches the game |
| Shield (Wyrm-empowered) | nearby hero heal | 30 | percent | Decoded | Matches the game |
| Shield | active duration | *not decoded* | seconds | Not decoded |   |
| Shield | resource cost | *not decoded* | resource | Not decoded |   |

### Ultimate 1

| Name | Stat | Value | Unit | Status | In-game check |
|---|---|---|---|---|---|
| Dragon Flight | cooldown | 60 | seconds | Decoded | Matches the game |
| Dragon Flight | charges | 1 | charges | Decoded (baseline) |   |
| Dragon Flight | damage per second | *not decoded* | damage per second | Not decoded | Game shows 200 |
| Dragon Flight | active duration | *not decoded* | seconds | Not decoded |   |
| Dragon Flight | resource cost | *not decoded* | resource | Not decoded |   |
| Dragon Flight | flight duration | *not decoded* | seconds | Not decoded |   |

### Ultimate 2

| Name | Stat | Value | Unit | Status | In-game check |
|---|---|---|---|---|---|
| Raging Chain | cooldown | *not decoded* | seconds | Not decoded | Game shows 45 |
| Raging Chain | charges | 1 | charges | Decoded (baseline) |   |
| Raging Chain | max total damage | *not decoded* | damage | Not decoded | Game shows 400 |
| Raging Chain | active duration | *not decoded* | seconds | Not decoded |   |
| Raging Chain | resource cost | *not decoded* | resource | Not decoded |   |
| Raging Chain | hit channel breakdown | *not decoded* | damage | Not decoded |   |

## Talents

Values separated by / are for Common / Rare / Epic / Legendary.

**Unlocks at rank** is the hero rank, not the level reached in a run.

### Starting talents

The talents offered at level 1 of a run. A starting talent not yet unlocked at your hero rank can still fill an empty card. The Lack of Inspiration modifier lowers the offer to 3 cards. See [TALENTS.md](../../TALENTS.md).

| Talent | Unlocks at rank | Effect |
|---|---|---|
| Explosive Fire | 1 | IGNITED enemies explode when they die, dealing 20 / 25 / 30 / 35 damage and applying IGNITE to all nearby enemies |
| Shield Charge | 1 | DEFENSE makes Beowulf dash forward and deal +150 / 187.5 / 225 / 262.5% damage along the path |
| Rampart | 2 | Quest (x20): blocking at least one attack during Defense grants +1.5 Armor<br>Complete: Wyrm Defense heals 50 / 60 / 70 / 80% more in a larger radius |
| Draconic Binds | 5 | Quest (x20): Hit at least 2 enemies with a single Wyrm ability to earn +0.5 DMG<br>Complete: Reduces Trait cooldown by 20 / 25 / 30 / 35% and increases Wyrm ability damage by 10 / 12.5 / 15 / 17.5% |

### Ultimates

The talent tables do not include the base ultimates or their unlock ranks; this text is from the hero's text table.

| Ultimate | Description |
|---|---|
| Dragon Flight | • **Wyrm** takes off and flies around, continuously breathing fire<br>• Deals damage and applies **IGNITE** to all enemies hit. `{0}` can act at the same time |
| Raging Chain | • Rush forward, then chain together a series of attacks with the sword and Wyrm |

### Ultimate upgrades

| Talent | Upgrades | Unlocks at rank | Effect |
|---|---|---|---|
| Immolation | Dragon Flight | 1 | During ULTIMATE, Beowulf deals 40 / 50 / 60 / 70 damage per second to nearby enemies, and all abilities function as if they were Wyrm Empowered |
| Sudden Growth | Dragon Flight | 9 | During ULTIMATE, the Wyrm grows and breathes fire in a wider zone, dealing +40 / 50 / 60 / 70% damage |
| Volcanic Rage | Raging Chain | 6 | Each ULTIMATE fireball throws 4 / 5 / 6 / 7 fiery rocks into the surrounding area, dealing 50% damage each |
| Fireball | Raging Chain | 9 | In Combat, DASH makes the Wyrm throw a Fireball towards a close enemy, dealing 40 / 50 / 60 / 70 area damage |

### Other talents

| Talent | Unlocks at rank | Effect |
|---|---|---|
| Blademaster | 1 | After each TRAIT activation, next 3 ATTACKS gain +100% Crit Chance<br>Permanently gain +10 / 12 / 14 / 16% ATTACK speed |
| Bladestorm | 1 | Special performs 2 / 3 / 4 / 5 additional spins for 100% damage each<br>Beowulf remains INTANGIBLE throughout additional spins |
| Breath of Fire | 1 | Wyrm breathes a cone of fire during ATTACK finisher, dealing 200 / 250 / 300 / 350% damage and applying IGNITE to enemies hit |
| Double Shock | 1 | POWER sends out two successive shockwaves, each one dealing -30 / 25 / 20 / 15% damage |
| Eruption | 1 | POWER's shockwaves explode at the end and deal 60 / 75 / 90 / 105% additional damage all around |
| Fiery Seismo | 1 | Wyrm SPECIAL's finisher strikes 3 times with a growing radius for 45 / 50 / 55 / 60% damage each |
| Furnace | 1 | IGNITE effects last 2 more seconds and deal +32 / 40 / 48 / 56% damage |
| Heavy Strikes | 1 | ATTACK is slower but cleaves across a wide area and deals +50 / 60 / 70 / 80% damage |
| Blazing Runes | 2 | ATTACK and SPECIAL gain +40 / 50 / 60 / 70% Crit Chance against IGNITED enemies |
| Fire Wings | 3 | Activating TRAIT deals 30 / 35 / 40 / 45 damage all around and applies IGNITE to all enemies hit |
| Scorched Earth | 3 | Wyrm POWER leaves a trail of fire that deals 40 / 50 / 60 / 70 damage over time to enemies standing on it |
| Retaliation | 4 | After using DEFENSE, the next ATTACK within 2 seconds triggers a two-strike retaliation, with each one dealing 360 / 450 / 540 / 630% damage |
| Sparkling Shield | 4 | Each attack blocked during DEFENSE inflicts 120 / 150 / 180 / 210% of blocked damage to what is in front of Beowulf. |
| Fiery Slash | 5 | ATTACK triggered right after DASH deals 400 / 500 / 600 / 700% damage and applies IGNITE to enemies |
| Battle Cry | 7 | TRAIT increases Move Speed by 15% and grants 12 / 15 / 18 / 21 SHIELD to all Heroes in the area for 6 seconds |
| Maelstrom | 7 | SPECIAL's final hit deals +24 / 30 / 36 / 42% damage for each different enemy already hit (up to +120 / 150 / 180 / 210%) |
| Furious Blows | 8 | After a SPECIAL, the next ATTACK triggers a series of 3 strikes dealing 100 / 125 / 150 / 175% damage each<br>If the SPECIAL was reinforced by the Wyrm, the attacks apply an IGNITE status to enemies and inflict +50% damage |
| Runes of War | 8 | After hitting an enemy with DEFENSE, runes appear around Beowulf dealing 16 / 20 / 24 / 28 area damage per second for 5 seconds |

## Outfits

| Outfit | How to unlock | Description |
|---|---|---|
| Signature Outfit | Completed 'Rampart' Talent Quest | Unlocked by completing the  'Rampart' Talent Quest |
| Traveler Outfit | Reached Chapter 3 | Unlocked by reaching Chapter 3 |
| Master Outfit | Completed the game  in Darkness Difficulty | Unlocked by completing the game  in Darkness Difficulty |
| Hidden Outfit | Bringer of Boom | Hidden Requirements |
| Ravens Outfit | Ravens Skin Pack Acquired | Available in the Ravens Skin Pack |
| Nightmares Outfit | Nightmares Skin Pack Acquired | Available in the Nightmares Skin Pack |
| Fairytales Outfit | Fairytales Skin Pack Acquired | Available in the Fairytales Skin Pack |
| Unleashed Outfit | Unleashed Skin Pack acquired | Available from the Unleashed Skin Pack |


**How to read the text**

- **Bold** words are highlighted in the game.
- `{0}`, `{1}` and so on are numbers or names the game fills in while you play.

Source: [`Hero_Beowulf_Common.LangEN.tsv`](../../data/Hero_Beowulf_Common.LangEN.tsv), [`Hero_Beowulf_Abilities.tsv`](../../data/Hero_Beowulf_Abilities.tsv), [`Hero_Beowulf_Talents.tsv`](../../data/Hero_Beowulf_Talents.tsv), [`Hero_Beowulf_Skins.LangEN.tsv`](../../data/Hero_Beowulf_Skins.LangEN.tsv).
Game version: Game build 1.06 (Steam build ID 25174305); the displayed version string is unverified. See VERSION.json.

*This page is generated from the TSV files in [data/](../../data/) by `tools/build_browse.py`. Do not edit it by hand; fix the data and re-run the script.*
