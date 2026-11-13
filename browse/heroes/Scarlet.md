# Scarlet

[All tables](../README.md)

[Abilities](#abilities) · [Ability values](#ability-values) · [Talents](#talents) · [Outfits](#outfits) · [Memoir](../memoirs/Scarlet.md)

Scarlet discovered she was cursed with lycanthropy while covered in her grandmother's remains. The Little Red of legend grew up in the blink of two very big eyes. A revenge-seeking hunter by day, wielding an arsenal of knives and the occasional bomb, at night she is a brutal monster whose pounce is just as mean as her bite. Oh, what big claws she has.

## Abilities

| Slot | Name | Description |
|---|---|---|
| Trait | Lycanthrope | • **NIGHT**: At nightfall, transform into a werewolf with new abilities<br>• **DAY**: At dawn, regain human form |
| Human Attack | Daggers | • Chain together a series of dagger slashes, each one dealing **`{0}`** damage<br>• Every two consecutive attacks that hit an enemy, one **COMBO POINT** is generated (up to **`{1}`** can be stored) |
| Human Power | Swift Strike | • Rush forward while **INTANGIBLE**, dealing **`{0}`** damage along the way<br>• Spends all **COMBO POINTS**. Damage is increased by **`{1}`%** for each point spent |
| Human Special | Bomb | • Drops a bomb that triggers a delayed explosion<br>• Deals **`{0}`** damage to enemies and stuns `{1}` if she is within the area of effect |
| Human Defense | Cloak | • Hide under the cloak and turn **INTANGIBLE** for **`{0}`** second(s)<br>• **ATTACK** or **POWER** triggered during this effect gain #+`{1}`%~ Crit Chance<br>• While hidden Scarlet gain **STEALTH** |
| Human Ultimate 1 | Hunter's Souvenir | • Shoot with the shotgun, dealing **`{0}`** damage in a wide cone<br>• Stores **`{1}` charges** |
| Human Ultimate 2 | Grandmother's Souvenir | • Throw a pinch of ashes that creates a clouded area lasting **`{0}`** seconds<br>• During this time, all Heroes standing in the area of effect are **INTANGIBLE** |
| Wolf Attack | Claws | • Chain together a series of claw swipes, each one dealing **`{0}`** damage<br>• Every two consecutive attacks that hit an enemy, one **COMBO POINT** is generated (up to **`{1}`** can be stored) |
| Wolf Power | Bite | • Rush towards the closest enemy while **INTANGIBLE** to bite it and deal **`{0}`** damage<br>• Spends all **COMBO POINTS**. Damage is increased by **`{1}`%** for each point spent |
| Wolf Special | Leap | • An **INTANGIBLE** jump followed by a ground strike, dealing **`{0}`** damage around the landing zone |
| Wolf Defense | Howl | • Gain **`{0}` ARMOR**. **ATTACK** and **POWER** gain **`{1}`%** **LIFE ON HIT**<br>• Lasts **`{2}`** seconds |
| Wolf Ultimate 1 | Gusting Roar | • Deal **`{0}`** damage per second in a wide cone for **`{1}`** seconds |
| Wolf Ultimate 2 | In the Belly | • Eat the closest non-boss enemy, instantly killing it<br>• Cooldown is proportional to the eaten enemy's level |

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

### Human / Trait

| Name | Stat | Value | Unit | Status | In-game check |
|---|---|---|---|---|---|
| Lycanthrope (Human) | cooldown | *not decoded* | seconds | Not decoded | Game shows none |
| Lycanthrope (Human) | charges | 1 | charges | Decoded (baseline) |   |
| Lycanthrope (Human) | active duration | *not decoded* | seconds | Not decoded |   |
| Lycanthrope (Human) | resource cost | *not decoded* | resource | Not decoded |   |

### Human / Attack

| Name | Stat | Value | Unit | Status | In-game check |
|---|---|---|---|---|---|
| Daggers (Human) | damage per hit | 15 | damage | Decoded (baseline) | Matches the game |
| Daggers (Human) | max combo points | 3 | combo points | Decoded (baseline) | Matches the game |
| Daggers (Human) | hit count | *not decoded* | hits | Not decoded |   |
| Daggers (Human) | hit damage sequence | *not decoded* | damage | Not decoded |   |
| Daggers (Human) | attack timing | *not decoded* | seconds | Not decoded |   |

### Human / Power

| Name | Stat | Value | Unit | Status | In-game check |
|---|---|---|---|---|---|
| Swift Strike (Human) | cooldown | 4 | seconds | Decoded | Matches the game |
| Swift Strike (Human) | charges | 1 | charges | Decoded (baseline) |   |
| Swift Strike (Human) | damage | 40 | damage | Decoded (baseline) | Matches the game |
| Swift Strike (Human) | bonus damage per combo point | 50 | percent | Decoded | Matches the game |
| Swift Strike (Human) | active duration | *not decoded* | seconds | Not decoded |   |
| Swift Strike (Human) | resource cost | *not decoded* | resource | Not decoded |   |

### Human / Special

| Name | Stat | Value | Unit | Status | In-game check |
|---|---|---|---|---|---|
| Bomb (Human) | cooldown | 10 | seconds | Decoded | Matches the game |
| Bomb (Human) | charges | 1 | charges | Decoded (baseline) |   |
| Bomb (Human) | damage | 60 | damage | Decoded (baseline) | Matches the game |
| Bomb (Human) | explosion delay | *not decoded* | seconds | Not decoded |   |
| Bomb (Human) | self stun duration | *not decoded* | seconds | Not decoded |   |
| Bomb (Human) | active duration | *not decoded* | seconds | Not decoded |   |
| Bomb (Human) | resource cost | *not decoded* | resource | Not decoded |   |

### Human / Defense

| Name | Stat | Value | Unit | Status | In-game check |
|---|---|---|---|---|---|
| Cloak (Human) | cooldown | 8 | seconds | Decoded | Matches the game |
| Cloak (Human) | charges | 1 | charges | Decoded (baseline) |   |
| Cloak (Human) | duration | 2 | seconds | Decoded (baseline) | Matches the game |
| Cloak (Human) | crit chance bonus | 100 | percent | Decoded | Matches the game |
| Cloak (Human) | active duration | *not decoded* | seconds | Not decoded |   |
| Cloak (Human) | resource cost | *not decoded* | resource | Not decoded |   |

### Human / Ultimate 1

| Name | Stat | Value | Unit | Status | In-game check |
|---|---|---|---|---|---|
| Hunter's Souvenir (Human) | cooldown | 90 | seconds | Decoded | Matches the game |
| Hunter's Souvenir (Human) | charges | *not decoded* | charges | Not decoded | Game shows 2 |
| Hunter's Souvenir (Human) | damage | *not decoded* | damage | Not decoded | Game shows 250 |
| Hunter's Souvenir (Human) | active duration | *not decoded* | seconds | Not decoded |   |
| Hunter's Souvenir (Human) | resource cost | *not decoded* | resource | Not decoded |   |

### Human / Ultimate 2

| Name | Stat | Value | Unit | Status | In-game check |
|---|---|---|---|---|---|
| Grandmother's Souvenir (Human) | cooldown | 90 | seconds | Decoded | Matches the game |
| Grandmother's Souvenir (Human) | charges | 1 | charges | Decoded (baseline) |   |
| Grandmother's Souvenir (Human) | cloud duration | 8 | seconds | Decoded | Matches the game |
| Grandmother's Souvenir (Human) | active duration | *not decoded* | seconds | Not decoded |   |
| Grandmother's Souvenir (Human) | resource cost | *not decoded* | resource | Not decoded |   |

### Werewolf / Attack

| Name | Stat | Value | Unit | Status | In-game check |
|---|---|---|---|---|---|
| Claws (Werewolf) | damage per swipe | 15 | damage | Decoded (baseline) | Matches the game |
| Claws (Werewolf) | max combo points | 3 | combo points | Decoded (baseline) | Matches the game |
| Claws (Werewolf) | hit count | *not decoded* | hits | Not decoded |   |
| Claws (Werewolf) | hit damage sequence | *not decoded* | damage | Not decoded |   |
| Claws (Werewolf) | attack timing | *not decoded* | seconds | Not decoded |   |

### Werewolf / Power

| Name | Stat | Value | Unit | Status | In-game check |
|---|---|---|---|---|---|
| Bite (Werewolf) | cooldown | 4 | seconds | Decoded | Matches the game |
| Bite (Werewolf) | charges | 1 | charges | Decoded (baseline) |   |
| Bite (Werewolf) | damage | 60 | damage | Decoded (baseline) | Matches the game |
| Bite (Werewolf) | bonus damage per combo point | 50 | percent | Decoded | Matches the game |
| Bite (Werewolf) | active duration | *not decoded* | seconds | Not decoded |   |
| Bite (Werewolf) | resource cost | *not decoded* | resource | Not decoded |   |

### Werewolf / Special

| Name | Stat | Value | Unit | Status | In-game check |
|---|---|---|---|---|---|
| Leap (Werewolf) | cooldown | 8 | seconds | Decoded | Matches the game |
| Leap (Werewolf) | charges | 1 | charges | Decoded (baseline) |   |
| Leap (Werewolf) | landing damage | 60 | damage | Decoded (baseline) | Matches the game |
| Leap (Werewolf) | active duration | *not decoded* | seconds | Not decoded |   |
| Leap (Werewolf) | resource cost | *not decoded* | resource | Not decoded |   |

### Werewolf / Defense

| Name | Stat | Value | Unit | Status | In-game check |
|---|---|---|---|---|---|
| Howl (Werewolf) | cooldown | 14 | seconds | Decoded | Matches the game |
| Howl (Werewolf) | charges | 1 | charges | Decoded (baseline) |   |
| Howl (Werewolf) | armor | 50 | armor | Decoded | Matches the game |
| Howl (Werewolf) | life on hit | 15 | percent | Decoded | Matches the game |
| Howl (Werewolf) | duration | 5.5 | seconds | Decoded (baseline) | Matches the game |
| Howl (Werewolf) | active duration | *not decoded* | seconds | Not decoded |   |
| Howl (Werewolf) | resource cost | *not decoded* | resource | Not decoded |   |

### Werewolf / Ultimate 1

| Name | Stat | Value | Unit | Status | In-game check |
|---|---|---|---|---|---|
| Gusting Roar (Werewolf) | cooldown | *not decoded* | seconds | Not decoded | Game showed 60 on 1.05; changed in 1.06 |
| Gusting Roar (Werewolf) | charges | 1 | charges | Decoded (baseline) |   |
| Gusting Roar (Werewolf) | damage per second | *not decoded* | damage per second | Not decoded | Game shows 200 |
| Gusting Roar (Werewolf) | duration | 3 | seconds | Decoded (baseline) | Matches the game |
| Gusting Roar (Werewolf) | active duration | *not decoded* | seconds | Not decoded |   |
| Gusting Roar (Werewolf) | resource cost | *not decoded* | resource | Not decoded |   |

### Werewolf / Ultimate 2

| Name | Stat | Value | Unit | Status | In-game check |
|---|---|---|---|---|---|
| In the Belly (Werewolf) | cooldown | *not decoded* | seconds | Not decoded | Game shows 10 |
| In the Belly (Werewolf) | charges | 1 | charges | Decoded (baseline) |   |
| In the Belly (Werewolf) | active duration | *not decoded* | seconds | Not decoded |   |
| In the Belly (Werewolf) | resource cost | *not decoded* | resource | Not decoded |   |

## Talents

Values separated by / are for Common / Rare / Epic / Legendary.

| Talent | Unlocks at rank | Effect |
|---|---|---|
| Adrenaline | 7 | Each time you spend COMBO POINTS, each point spent:<br>Human: restores 2 / 2.5 / 3 / 3.5 health<br>Werewolf: increases ATTACK SPEED by 4 / 5 / 6 / 7% for 6 seconds |
| Aggressive Defense | 1 | Deal 60 / 75 / 90 / 105 damage all around when triggering DEFENSE |
| Armor Break | 2 | SPECIAL applies VULNERABLE to all enemies hit for 3 / 4 / 5 / 6 seconds |
| Bone Cracker | 6 | Human: Ash cloud deals 20 / 25 / 30 / 35 damage per second to enemies inside<br>Werewolf: Devouring an enemy causes it to explode, dealing 50 / 62.5 / 75 / 87.5 to 150 / 187.5 / 225 / 262.5 area damage (depending on its size) |
| Cleave | 1 | ATTACK has a 25% chance to cleave all around and deal +120 / 150 / 180 / 210% damage |
| Deadly Combo | 1 | POWER ends with an area attack dealing 40 / 50 / 60 / 70% damage |
| Devourer | 1 | Repeatable Quest: Each kill with Werewolf POWER earns +0.4 / 0.5 / 0.6 / 0.7 DMG |
| Distant Explosions | 1 | SPECIAL now targets a farther location and deals +40 / 50 / 60 / 70% damage<br>Human: SPECIAL no longer affects Scarlet and bomb explodes as soon as it hits the ground |
| Double Strike | 4 | ATTACK triggered right after DASH triggers a double strike, dealing 400 / 500 / 600 / 700% damage and generating one Combo Point |
| Energy | 1 | Maximum Combo Points is increased by 2<br>POWER has +4 / 5 / 6 / 7% Crit Chance per Combo Point stored |
| Evisceration | 1 | Each Combo Point spent by POWER applies 16 / 20 / 24 / 28% damage dealt in the form of BLEED |
| Explosive Rush | 5 | When at 3 Combo Points or above, POWER triggers SPECIAL effect upon use, dealing 40 / 50 / 60 / 70% of its normal damage amount |
| Fan of Spikes | 7 | When in combat, DASH can consume a COMBO POINT to send 4 / 5 / 6 / 7 spikes, with each one dealing 100% ATTACK damage to enemies hit |
| Fiery Maw | 1 | ULTIMATE gains +30% range, deals +20 / 25 / 30 / 35% damage and applies IGNITE to enemies hit |
| Focus | 9 | Human: The shotgun fires piercing bullets with greater range, dealing 350 / 437.5 / 525 / 612.5 damage<br>Werewolf: The gust summons a tornado that remains on the ground, dealing 70 / 87.5 / 105 / 122 damage per second |
| Murderous Intent | 1 | DEFENSE instantly bestows 3 Combo Points and lasts 20 / 25 / 30 / 35% longer |
| On the Hunt | 8 | DEFENSE applies MARKED to the nearest enemy for 4 / 6 / 8 / 10 seconds<br>MARKED targets take +25% increased damage and spread this status to another nearby enemy when they die |
| Pack Leader | 9 | Human: Ash cloud restores 5 / 6.25 / 7.5 / 8.7 hit points per second to all Heroes within<br>Werewolf: Eating an enemy applies a 15 / 18.75 / 22.5 / 26.2 to 28 / 35 / 42 / 49 SHIELD to all heroes around (depending on its size) |
| Pulverize | 4 | SPECIAL hits enemies 30% farther<br>SPECIAL can consume a COMBO POINT to deal +40 / 50 / 60 / 70% damage |
| Pyromania | 1 | SPECIAL applies IGNITE to all enemies hit and gains +40 / 50 / 60 / 70% Crit Chance |
| Savagery | 8 | Each time Scarlet earns or spends COMBO POINTS, she gains a charge of Savagery (up to 20), each granting +1 / 1.2 / 1.4 / 1.6 DMG<br>Savagery stacks disappear after 5 seconds if no new stacks are gained |
| Shadow Strikes | 2 | Quest (x30): ATTACK or POWER triggered during Human DEFENSE gain +0.5% Crit Chance per enemy hit<br>Complete: +20 / 25 / 30 / 35% Crit Damage |
| Shapeshifter | 5 | TRAIT becomes active (with a 30 / 26 / 22 / 18 seconds cooldown) and heals 20% of Maximum Health when used<br>Maximum Health is reduced by 20% |
| Slash Flurry | 1 | After using POWER, the next ATTACK within 3 seconds delivers a flurry of 5 slashes with +20 / 30 / 40 / 50% increased damage |
| True Instincts | 3 | In Human Form, gain +10 / 12 / 14 / 16% Move Speed<br>In Werewolf Form, gain +20 / 25 / 30 / 35% Maximum Health |
| Wide Attacks | 3 | ATTACK gains +40% range and deals +20 / 25 / 30 / 35% damage |

## Outfits

| Outfit | How to unlock | Description |
|---|---|---|
| Signature Outfit | Completed the 'Devourer' Talent Quest | Unlocked by completing the 'Devourer' Talent Quest |
| Traveler Outfit | Reached Chapter 3 | Unlocked by reaching Chapter 3 |
| Master Outfit | Completed the game in Darkness Difficulty | Unlocked by completing the game  in Darkness Difficulty |
| Hidden Outfit | Human after all | Hidden Requirements |
| Ravens Outfit | Ravens Skin Pack Acquired | Available in the Ravens Skin Pack |
| Nightmares Outfit | Nightmares Skin Pack Acquired | Available in the Nightmares Skin Pack |
| Fairytales Outfit | Fairytales Skin Pack Acquired | Available in the Fairytales Skin Pack |
| Timeless Outfit | Timeless Skin Pack Acquired | Available in the Timeless Skin Pack |


**How to read the text**

- **Bold** words are highlighted in the game.
- `{0}`, `{1}` and so on are numbers or names the game fills in while you play.

Source: [`Hero_RED_Common.LangEN.tsv`](../../data/Hero_RED_Common.LangEN.tsv), [`Hero_RED_Abilities.tsv`](../../data/Hero_RED_Abilities.tsv), [`Hero_RED_Talents.tsv`](../../data/Hero_RED_Talents.tsv), [`Hero_RED_Skins.LangEN.tsv`](../../data/Hero_RED_Skins.LangEN.tsv).
Game version: Game build 1.06 (Steam build ID 25174305); the displayed version string is unverified. See VERSION.json.

*This page is generated from the TSV files in [data/](../../data/) by `tools/build_browse.py`. Do not edit it by hand; fix the data and re-run the script.*
