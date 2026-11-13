# Carmilla

[All tables](../README.md)

[Abilities](#abilities) · [Ability values](#ability-values) · [Talents](#talents) · [Outfits](#outfits) · [Memoir](../memoirs/Carmilla.md)

Separated from the love of her eternal life in the war against darkness, Carmilla now fights to extinguish those she holds responsible for destroying her happily-ever-after. She is a dhampir, a day-walking vampire, drinking blood to strengthen her powers while taking care to control the monster within. Carmilla is physically fast and ferocious – but her wit also has fangs of its own.

## Abilities

| Slot | Name | Description |
|---|---|---|
| Trait | Dhampir | • `{0}` uses **BLOOD** to fuel some of her abilities, or health when there is no more left<br>• Activate to enter **Winged Form**, draining **`{1}`** **BLOOD** per second to gain **+`{2}`% MOVE SPEED** and **BLOOD**-free abilities<br>• **DAY**: Every **`{3}`** second(s), restore **`{4}`** health to all nearby heroes<br>• **NIGHT**: Gain **+`{5}`%** **Crit Chance** |
| Attack | Tearing | • Chain a series of **`{0}`** attacks with clawed hands, with the last attack dealing **+`{1}`%** damage<br>• The combo overall deals a total of **`{2}`** damage and earns **`{3}`** **BLOOD point(s)** |
| Power | Blood Orb | • `{0}` sends a blood orb forward; holding the action consumes **BLOOD** to fuel it, dealing **`{2}`** area damage per second<br>• Upon release, the blood orb explodes and deals **`{1}`** area damage |
| Special | Death Kiss | • Hold then release – `{0}` launches herself at the target location, then turns **INTANGIBLE** and bites the closest enemy, dealing **`{1}`** damage<br>• Each successful bite earns **`{2}`** **BLOOD point(s)** |
| Defense | Bat Swarm | • `{0}` transforms into an **INTANGIBLE** bat swarm, dealing **`{1}`** damage to enemies passed through as **BLEED**<br>• Holding the action consumes **BLOOD** to keep this form active for up to **`{2}`** seconds |
| Ultimate 1 | Impalement | • Consume all **BLOOD** to launch a series of blood spikes errupting from the ground in front, dealing **`{0}`** damage per second to enemies in the area<br>• Each **BLOOD point** consumed increases damage by **`{1}`%** |
| Ultimate 2 | Blood Lash | • Summon a whip of blood, dealing **`{0}`** area damage<br>• Next **`{1}`** **ATTACKS** use the whip to strike in large areas, with the combo overall dealing a total of **`{2}`** damage |

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
| Dhampir | cooldown | 15 | seconds | Decoded |   |
| Dhampir | blood drain per second | 10 | blood per second | Decoded |   |
| Dhampir | movement speed bonus | *not decoded* | percent | Not decoded | Second decoding pass: 30 |
| Dhampir | daytime heal interval | 1 | seconds | Decoded |   |
| Dhampir | daytime heal amount | 2 | health | Decoded (baseline) |   |
| Dhampir | nighttime crit chance bonus | 30 | percent | Decoded |   |
| Dhampir | charges | 1 | charges | Decoded (baseline) |   |
| Dhampir | active duration | *not decoded* | seconds | Not decoded |   |
| Dhampir | resource cost | *not decoded* | resource | Not decoded |   |
| Dhampir | blood cap | *not decoded* | blood | Not decoded |   |
| Dhampir | blood base cap configuration | 100 | blood | Decoded |   |
| Dhampir | health substitution cost | *not decoded* | health | Not decoded |   |
| Dhampir | health substitution ratio configuration | 0.015 | ratio | Decoded |   |

### Attack

| Name | Stat | Value | Unit | Status | In-game check |
|---|---|---|---|---|---|
| Tearing | combo hit count | 5 | hits | Decoded |   |
| Tearing | final hit bonus | *not decoded* | percent | Not decoded | Second decoding pass: 300 |
| Tearing | full combo damage | *not decoded* | damage | Not decoded | Second decoding pass: 48 |
| Tearing | blood earned | *not decoded* | blood | Not decoded | Second decoding pass: 12 |
| Tearing | hit count | *not decoded* | hits | Not decoded |   |
| Tearing | hit damage sequence | *not decoded* | damage | Not decoded |   |
| Tearing | attack timing | *not decoded* | seconds | Not decoded |   |

### Power

| Name | Stat | Value | Unit | Status | In-game check |
|---|---|---|---|---|---|
| Blood Orb | cooldown | 8 | seconds | Decoded |   |
| Blood Orb | charges | 1 | charges | Decoded (baseline) |   |
| Blood Orb | held damage per second | *not decoded* | damage per second | Not decoded | Second decoding pass: 80 |
| Blood Orb | explosion damage | 40 | damage | Decoded (baseline) |   |
| Blood Orb | active duration | *not decoded* | seconds | Not decoded |   |
| Blood Orb | blood drain per second | *not decoded* | blood per second | Not decoded |   |
| Blood Orb | max hold duration | *not decoded* | seconds | Not decoded |   |
| Blood Orb | resource cost | *not decoded* | blood | Not decoded |   |

### Special

| Name | Stat | Value | Unit | Status | In-game check |
|---|---|---|---|---|---|
| Death Kiss | cooldown | 6 | seconds | Decoded |   |
| Death Kiss | charges | 1 | charges | Decoded (baseline) |   |
| Death Kiss | bite damage | 100 | damage | Decoded (baseline) |   |
| Death Kiss | blood earned | 30 | blood | Decoded |   |
| Death Kiss | active duration | *not decoded* | seconds | Not decoded |   |
| Death Kiss | resource cost | *not decoded* | resource | Not decoded |   |

### Defense

| Name | Stat | Value | Unit | Status | In-game check |
|---|---|---|---|---|---|
| Bat Swarm | cooldown | 8 | seconds | Decoded |   |
| Bat Swarm | charges | 1 | charges | Decoded (baseline) |   |
| Bat Swarm | bleed damage | *not decoded* | damage | Not decoded | Second decoding pass: 30 |
| Bat Swarm | duration | 3 | seconds | Decoded |   |
| Bat Swarm | resource cost | *not decoded* | resource | Not decoded |   |
| Bat Swarm | blood drain per second | *not decoded* | blood per second | Not decoded |   |
| Bat Swarm | bleed total damage | *not decoded* | damage | Not decoded |   |
| Bat Swarm | bleed tick damage | *not decoded* | damage | Not decoded |   |
| Bat Swarm | bleed tick interval | *not decoded* | seconds | Not decoded |   |
| Bat Swarm | active duration | 3 | seconds | Decoded |   |

### Ultimate 1

| Name | Stat | Value | Unit | Status | In-game check |
|---|---|---|---|---|---|
| Impalement | cooldown | *not decoded* | seconds | Not decoded | Second decoding pass: 60 |
| Impalement | charges | *not decoded* | charges | Not decoded |   |
| Impalement | damage per second | *not decoded* | damage per second | Not decoded | Second decoding pass: 450 |
| Impalement | damage bonus per blood | *not decoded* | percent | Not decoded | Second decoding pass: 1 |
| Impalement | active duration | *not decoded* | seconds | Not decoded |   |
| Impalement | resource cost | *not decoded* | resource | Not decoded |   |

### Ultimate 2

| Name | Stat | Value | Unit | Status | In-game check |
|---|---|---|---|---|---|
| Blood Lash | cooldown | 60 | seconds | Decoded |   |
| Blood Lash | charges | 1 | charges | Decoded (baseline) |   |
| Blood Lash | initial area damage | 100 | damage | Decoded (baseline) |   |
| Blood Lash | empowered attacks count | 12 | attacks | Decoded (baseline) |   |
| Blood Lash (empowered attack) (Empowered Whip) | whip combo attacks | 3 | attacks | Decoded |   |
| Blood Lash (empowered attack) (Empowered Whip) | final hit bonus | *not decoded* | percent | Not decoded | Second decoding pass: 100 |
| Blood Lash (empowered attack) (Empowered Whip) | combo damage | *not decoded* | damage | Not decoded | Second decoding pass: 140 |
| Blood Lash | active duration | *not decoded* | seconds | Not decoded |   |
| Blood Lash | resource cost | *not decoded* | resource | Not decoded |   |
| Blood Lash (empowered attack) (Empowered Whip) | hit count | *not decoded* | hits | Not decoded |   |
| Blood Lash (empowered attack) (Empowered Whip) | hit damage sequence | *not decoded* | damage | Not decoded |   |
| Blood Lash (empowered attack) (Empowered Whip) | attack timing | *not decoded* | seconds | Not decoded |   |
| Blood Lash | empowered combo total damage | *not decoded* | damage | Not decoded | Second decoding pass: 140 |

## Talents

Values separated by / are for Common / Rare / Epic / Legendary.

**Unlocks at rank** is the hero rank, not the level reached in a run.

### Starting talents

The talents offered at level 1 of a run. A starting talent not yet unlocked at your hero rank can still fill an empty card. The Lack of Inspiration modifier lowers the offer to 3 cards. See [TALENTS.md](../../TALENTS.md).

| Talent | Unlocks at rank | Effect |
|---|---|---|
| Bat Master | 1 | When not in combat, DEFENSE grants STEALTH and can be held without consuming BLOOD<br>DEFENSE deals +20 / 25 / 30 / 35% damage<br>STEALTH make Carmilla undetectable by enemies |
| Life Essence | 1 | Quest (x30): Killing an enemy with SPECIAL's bite earns VITALITY +1<br>Complete: Repeating this action restores 20 / 25 / 30 / 35 health to Carmilla |
| Blood Rage | 2 | Quest(x20): Hitting an enemy with the POWER held for at least 1 second to gain +0.5 DMG<br>Complete: Repeating this action increases POWER explosion damage by +80 / 100 / 120 / 140% |
| Life Tap | 5 | In Winged Form, activating TRAIT again consumes 15% of maximum health to recover up to 40 / 50 / 60 / 70 BLOOD points.<br>Cannot be used below the health cost; has a 10-second cooldown. |

### Ultimates

The talent tables do not include the base ultimates or their unlock ranks; this text is from the hero's text table.

| Ultimate | Description |
|---|---|
| Impalement | • Consume all **BLOOD** to launch a series of blood spikes errupting from the ground in front, dealing damage to enemies passed |
| Blood Lash | • Summon a whip of blood, dealing area damage<br>• Next **`{0}`** **ATTACKS** use the whip to strike in large areas |

### Ultimate upgrades

| Talent | Upgrades | Unlocks at rank | Effect |
|---|---|---|---|
| Torture of the Pale | Impalement | 1 | At the end of their course, ULTIMATE blood spikes return toward Carmilla, dealing 40 / 50 / 60 / 70% damage |
| Heartbreak | Impalement | 9 | Add a fourth move to ATTACK combo, impaling enemies in front, dealing 40 / 50 / 60 / 70% ULTIMATE damage |
| Mistress of Pain | Blood Lash | 6 | Increase maximum number of ATTACKS transformed by ULTIMATE by 6 / 8 / 10 / 12 |
| Mass Punishment | Blood Lash | 9 | Add a fourth ATTACK to ULTIMATE combo, dealing 240 / 300 / 360 / 420% area damage |

### Other talents

| Talent | Unlocks at rank | Effect |
|---|---|---|
| Boiling Blood | 1 | After consuming Health for at least 1 second(s) to fuel an ability, gain REGENERATION +3 / 4 / 5 / 6 |
| Dispersion | 1 | After DEFENSE, bats disperse around Carmilla, dealing 20 / 25 / 30 / 35 area damage as BLEED |
| Furious Tempest | 1 | Consuming BLOOD to fuel POWER gradually increases its damage, up to +40 / 50 / 60 / 70% after 3 seconds of holding |
| Go for the Throat | 1 | Distance covered before SPECIAL's bite increases its damage and Crit Chance, up to +40 / 50 / 60 / 70% |
| Puncture | 1 | Each enemy passed through while using DASH earns 8 / 10 / 12 / 14 BLOOD |
| Razor Claws | 1 | ATTACK deals +40 / 50 / 60 / 70% damage as BLEED |
| Sadism | 1 | Critical Hits deal +40 / 60 / 80 / 100% damage on enemies affected by BLEED |
| Victimization | 1 | SPECIAL applies MARKED to bitten enemy for 4 / 6 / 8 / 10 seconds<br>MARKED targets take +25% damage and spread this status to another nearby enemy when they die |
| Gust | 2 | TRAIT pushes back nearby enemies and deals 80 / 100 / 120 / 140 area damage |
| Aggressive Flock | 3 | During DEFENSE, Carmilla casts a bat every 0.5 / 0.35 / 0.3 / 0.25 second(s) that seeks out nearby enemies and pierces through them, dealing 10 damage |
| Blood Reserve | 3 | Increase maximum BLOOD reserve by 20 / 25 / 30 / 35% |
| Flesh Rip | 4 | POWER has +40 / 50 / 60 / 70% Crit Chance on enemies affected by BLEED |
| Onslaught | 4 | After a SPECIAL, the next ATTACK makes Carmilla rush forward, dealing 800 / 1000 / 1200 / 1400% ATTACK damage to enemies passed through |
| Seductive Provocation | 5 | Using DASH without specifying a move direction makes Carmilla seduce up to 4 non-boss enemies in front of her, applying WEAKENED and VULNERABLE to them for 6 / 7.5 / 9 / 10.5 seconds (every 6 seconds max) |
| Angel and Demon | 7 | When using TRAIT:<br>Day: Restores 20 / 25 / 30 / 35 health to all nearby heroes.<br>Night: Grants STRENGTH to all nearby heroes for 4 / 5 / 6 / 7 seconds. |
| Cruel Strike | 7 | After DASH or DEFENSE, the next ATTACK starts with a combo finishing move, dealing +100 / 125 / 150 / 175% damage |
| Injection | 8 | SPECIAL implants a blood seed into the bitten enemy that shortly after triggers an explosion of POWER, dealing 80 / 100 / 120 / 140% area damage |
| Wild Heart | 8 | POWER's orb move speed is increased by 100%<br>POWER explosion gains +20 / 25 / 30 / 35% range |

## Outfits

| Outfit | How to unlock | Description |
|---|---|---|
| Signature Outfit | Completed 'Life Essence' Talent Quest | Unlocked by completing 'Life Essence' Talent Quest |
| Traveler Outfit | Reached Chapter 3 | Unlocked by reaching Chapter 3 |
| Master Outfit | Completed the game in Darkness Difficulty | Unlocked by completing the game  in Darkness Difficulty |
| Hidden Outfit | Wings of Desire | Hidden Requirements |
| Ravens Outfit | Ravens Skin Pack Acquired | Available in the Ravens Skin Pack |
| Nightmares Outfit | Nightmares Skin Pack Acquired | Available in the Nightmare Skin Pack |
| Unleashed Outfit | Unleashed Skin Pack Acquired | Available in the Unleashed Skin Pack |


**How to read the text**

- **Bold** words are highlighted in the game.
- `{0}`, `{1}` and so on are numbers or names the game fills in while you play.

Source: [`Hero_Carmilla_Common.LangEN.tsv`](../../data/Hero_Carmilla_Common.LangEN.tsv), [`Hero_Carmilla_Abilities.tsv`](../../data/Hero_Carmilla_Abilities.tsv), [`Hero_Carmilla_Talents.tsv`](../../data/Hero_Carmilla_Talents.tsv), [`Hero_Carmilla_Skins.LangEN.tsv`](../../data/Hero_Carmilla_Skins.LangEN.tsv).
Game version: Game build 1.06 (Steam build ID 25174305); the displayed version string is unverified. See VERSION.json.

*This page is generated from the TSV files in [data/](../../data/) by `tools/build_browse.py`. Do not edit it by hand; fix the data and re-run the script.*
