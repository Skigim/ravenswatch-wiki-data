# Aladdin

[All tables](../README.md)

[Abilities](#abilities) · [Ability values](#ability-values) · [Talents](#talents) · [Outfits](#outfits) · [Memoir](../memoirs/Aladdin.md)

Once a happy-go-lucky thief until his happily-ever-after princess got stuck in a lamp, Aladdin now pledges his rogue skills to the protection of Reverie. A master thief, sporting formidable magical powers from his ring and lamp, Aladdin makes for quite the sneaky and unpredictable guardian. Funny things can happen on the way to one's potential.

## Abilities

| Slot | Name | Description |
|---|---|---|
| Trait | Jinniya of the Lamp | • Call Jinniya of the lamp for a wish. Next ability grants the wish<br>• **POWER**: Deals **`{0}`** damage all around<br>• **SPECIAL**: Makes **`{1}`** to **`{2}` Dream Shards** and **`{3}` Consumable(s)** appear<br>• **DEFENSE**: Revives all nearby Heroes or fully heals them with a permanent **`{4}` SHIELD** |
| Attack | Scimitars | • Chain together a series of attacks with the scimitars, each one dealing **`{0}`** damage. Last attack hits all around<br>• Each attack can consume **ENCHANTMENT** points so you can strike twice with increased damage |
| Power | Ring Jinn | • Summon Jinn of the Ring to fly forward and deliver a powerful blow that deals **`{0}`** damage<br>• Can be held to move farther and increase damage up to **+`{1}`%** |
| Special | Enchanted Blades | • Throw scimitars: They move forward, stop to spin, then return to `{0}`, dealing up to **`{1}`** damage<br>• Scimitars gain **ENCHANTMENT** points for each enemy hit<br>• Blades can be recalled sooner by triggering **SPECIAL** again |
| Defense | Somersault | • Jump quickly to turn **INTANGIBLE**<br>• Enemies passed become **VULNERABLE** for **`{0}`** second(s) |
| Ultimate 1 | Dream Wish | • Consume **`{0}` Dream Shards** to earn an additional **TRAIT** charge |
| Ultimate 2 | Magic Carpet | • Ride the Magic Carpet, turning **INTANGIBLE** and dealing **`{0}`** damage to enemies passed<br>• Movement is forced but the direction can be controlled |

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
| Jinniya of the Lamp | starting charges | *not decoded* | charges | Not decoded |   |
| Jinniya of the Lamp (Power Wish) | power wish damage | *not decoded* | damage | Not decoded | Second decoding pass: 250 |
| Jinniya of the Lamp (Special Wish) | special wish min shards | 15 | dream shards | Decoded |   |
| Jinniya of the Lamp (Special Wish) | special wish max shards | 25 | dream shards | Decoded |   |
| Jinniya of the Lamp (Special Wish) | special wish consumable count | 1 | consumables | Decoded |   |
| Jinniya of the Lamp (Defense Wish) | defense wish permanent shield | *not decoded* | shield | Not decoded | Second decoding pass: 30 |
| Jinniya of the Lamp | cooldown | 0 | seconds | Decoded |   |
| Jinniya of the Lamp | charges | *not decoded* | charges | Not decoded |   |
| Jinniya of the Lamp | active duration | *not decoded* | seconds | Not decoded |   |
| Jinniya of the Lamp | resource cost | *not decoded* | resource | Not decoded |   |

### Attack

| Name | Stat | Value | Unit | Status | In-game check |
|---|---|---|---|---|---|
| Scimitars | damage per attack | 16 | damage | Decoded (baseline) |   |
| Scimitars | enchantment cost | *not decoded* | enchantment | Not decoded |   |
| Scimitars | enchanted damage bonus | *not decoded* | percent | Not decoded |   |
| Scimitars | hit count | *not decoded* | hits | Not decoded |   |
| Scimitars | hit damage sequence | *not decoded* | damage | Not decoded |   |
| Scimitars | attack timing | *not decoded* | seconds | Not decoded |   |

### Power

| Name | Stat | Value | Unit | Status | In-game check |
|---|---|---|---|---|---|
| Ring Jinn | cooldown | 6 | seconds | Decoded |   |
| Ring Jinn | charges | 1 | charges | Decoded (baseline) |   |
| Ring Jinn | base damage | 80 | damage | Decoded (baseline) |   |
| Ring Jinn | max held damage bonus | 50 | percent | Decoded (baseline) |   |
| Ring Jinn | active duration | *not decoded* | seconds | Not decoded |   |
| Ring Jinn | resource cost | *not decoded* | resource | Not decoded |   |
| Ring Jinn | time to max charge | 0.65 | seconds | Decoded |   |

### Special

| Name | Stat | Value | Unit | Status | In-game check |
|---|---|---|---|---|---|
| Enchanted Blades | cooldown | 8 | seconds | Decoded |   |
| Enchanted Blades | charges | 1 | charges | Decoded (baseline) |   |
| Enchanted Blades | max total damage | *not decoded* | damage | Not decoded | Second decoding pass: 90 |
| Enchanted Blades | enchantment cap | *not decoded* | enchantment | Not decoded |   |
| Enchanted Blades | active duration | *not decoded* | seconds | Not decoded |   |
| Enchanted Blades | resource cost | *not decoded* | resource | Not decoded |   |
| Enchanted Blades | enchantment per hit | *not decoded* | enchantment | Not decoded |   |

### Defense

| Name | Stat | Value | Unit | Status | In-game check |
|---|---|---|---|---|---|
| Somersault | cooldown | 6 | seconds | Decoded |   |
| Somersault | charges | 1 | charges | Decoded (baseline) |   |
| Somersault | vulnerable duration | 3 | seconds | Decoded |   |
| Somersault | active duration | *not decoded* | seconds | Not decoded |   |
| Somersault | resource cost | *not decoded* | resource | Not decoded |   |

### Ultimate 1

| Name | Stat | Value | Unit | Status | In-game check |
|---|---|---|---|---|---|
| Dream Wish | cooldown | 90 | seconds | Decoded |   |
| Dream Wish | charges | 1 | charges | Decoded (baseline) |   |
| Dream Wish | dream shard cost | *not decoded* | dream shards | Not decoded | Second decoding pass: 150 |
| Dream Wish | active duration | *not decoded* | seconds | Not decoded |   |
| Dream Wish | resource cost | *not decoded* | resource | Not decoded |   |

### Ultimate 2

| Name | Stat | Value | Unit | Status | In-game check |
|---|---|---|---|---|---|
| Magic Carpet | cooldown | *not decoded* | seconds | Not decoded | Second decoding pass: 90 |
| Magic Carpet | charges | 1 | charges | Decoded (baseline) |   |
| Magic Carpet | damage | 100 | damage | Decoded (baseline) |   |
| Magic Carpet | resource cost | *not decoded* | resource | Not decoded |   |
| Magic Carpet | active duration | 5 | seconds | Decoded |   |

## Talents

Values separated by / are for Common / Rare / Epic / Legendary.

**Unlocks at rank** is the hero rank, not the level reached in a run.

### Starting talents

The talents offered at level 1 of a run. A starting talent not yet unlocked at your hero rank can still fill an empty card. The Lack of Inspiration modifier lowers the offer to 3 cards. See [TALENTS.md](../../TALENTS.md).

| Talent | Unlocks at rank | Effect |
|---|---|---|
| Aerial Catch | 1 | Quest (x15): After they hit an enemy, retrieving SPECIAL blades during DEFENSE grants +2 ARMOR<br>Complete: Doing it again grants 12 / 15 / 18 / 21 SHIELD to all nearby Heroes for 6 seconds |
| Jinniya's Gift | 1 | Gain +1 TRAIT charge<br>Future Talents have a +15 / 25 / 35 / 45% chance of being Rare or above |
| Jinn's Might | 2 | Quest (x20): Hitting an enemy with POWER at maximum charge grants +0.5 DMG<br>Complete: Increases POWER's bonus damage from charge by 40 / 50 / 60 / 70% |
| Wish of Omnipotence | 5 | Casting wishes grant OMNIPOTENCE to all nearby Heroes for 8 / 10 / 12 / 14 seconds<br>During OMNIPOTENCE, Heroes POWER, SPECIAL and DEFENSE have a 0.5 second(s) cooldown |

### Ultimates

The talent tables do not include the base ultimates or their unlock ranks; this text is from the hero's text table.

| Ultimate | Description |
|---|---|
| Dream Wish | • Consume **`{0}` Dream Shards** to earn an additional **TRAIT** charge |
| Magic Carpet | • Ride the Magic Carpet, turning **INTANGIBLE** and dealing damage to enemies passed |

### Ultimate upgrades

| Talent | Upgrades | Unlocks at rank | Effect |
|---|---|---|---|
| Wondrous Wishes | Dream Wish | 1 | All wishes are improved:<br>POWER: deals +50 / 75 / 100 / 125% damage<br>SPECIAL: 40 / 60 / 80 / 100% chance to generate 2 consumables<br>DEFENSE: +100 / 125 / 150 / 175% SHIELD gained |
| Infinite Wishes | Dream Wish | 9 | Gain +3 TRAIT charges<br>Dream Shards cost for ULTIMATE is reduced by 20 / 30 / 40 / 50% |
| Dream Stride | Magic Carpet | 6 | Each time ULTIMATE hits an enemy, Aladdin gains 8 / 10 / 12 / 14 Dream Shards<br>ULTIMATE has no cooldown if no enemies are hit |
| Quick Ride | Magic Carpet | 9 | DASH uses Magic Carpet to deal 40 / 50 / 60 / 70 damage to enemies passed and can be held for up to 1 second(s) |

### Other talents

| Talent | Unlocks at rank | Effect |
|---|---|---|
| Air Dash | 1 | DASH can be triggered during DEFENSE's air time <br>Doing so increases ATTACK speed by 15% for 4 / 5 / 6 / 7 second(s) |
| Healing Blades | 1 | When retrieved, SPECIAL's blades heal all Heroes nearby for each enemy hit, up to 7.5 / 9 / 10.5 / 12 Health |
| Jinn Charge | 1 | DASH used after POWER summons the Jinn to charge through enemies and deal 25 / 31.25 / 37.5 / 43.7 damage |
| Jinn's Fury | 1 | POWER strikes 3 times, each one dealing 40 / 45 / 50 / 55% damage |
| Major Enchantment | 1 | While NOT using ATTACK, passively generate 1 ENCHANTMENT points every 3 / 2.5 / 2.25 / 2 seconds |
| Shard Blades | 1 | While ENCHANTMENT is active on blades, ATTACKS have their range increased by 20 / 25 / 30 / 35% and deal +20% damage |
| Slide Attack | 1 | Using ATTACK while the blades are flying makes you slide and deal 400 / 500 / 600 / 700% of ATTACK's damage along the path |
| Spectral Blades | 1 | Retrieving SPECIAL's blades before they return to Aladdin triggers a flurry of attacks that can deal up to 44 / 55 / 66 / 77 area damage |
| Dive | 2 | Using ATTACK during DEFENSE's jump makes Aladdin dive to the ground, dealing 400 / 500 / 600 / 700% of ATTACK's damage all around |
| Acrobatics | 3 | Each enemy passed during DEFENSE grants 3 / 4 / 5 / 6 ENCHANTMENT points |
| Spinning Strikes | 3 | After retrieving SPECIAL's blades, next ATTACK within 2 second(s) spins 2 times (twice as many with ENCHANTMENT) and deals +80 / 100 / 120 / 140% damage |
| Leaping Strike | 4 | ATTACK used right after DASH deals 200 / 250 / 300 / 350% damages and strikes twice with ENCHANTMENT |
| Swordjinn | 4 | POWER Jinn can catch SPECIAL's blades and deal +80 / 120 / 140 / 160% damage in a wider range |
| Tornado Jump | 5 | DEFENSE casts a tornado that moves toward Aladdin and deals 40 / 50 / 60 / 70 damage per second for 4 seconds |
| Dream Scimitars | 7 | While ENCHANTMENT is active on blades, ATTACK has a 40 / 50 / 60 / 70% chance of earning Aladdin a Dream Shard upon enemy hit |
| Sand Vortex | 7 | SPECIAL's blades, when stationary, pull in enemies around them<br>SPECIAL deals +40 / 50 / 60 / 70% damage |
| Enchanted Jinn | 8 | POWER can consume up to 5 ENCHANTMENT points to increase its Crit Chance by 10% per point<br>The maximum number of ENCHANTMENT points is increased by 5 / 10 / 15 / 20 |
| Master Thief | 8 | Whenever you choose a Common, Rare or Epic Magical Object, you have a 40 / 50 / 60 / 70%/20 / 25 / 30 / 35%/10 / 12 / 14 / 16% chance to get another copy of it |

## Outfits

| Outfit | How to unlock | Description |
|---|---|---|
| Signature Outfit | Completed 'Aerial Catch' Talent Quest | Unlocked by completing  'Aerial Catch' Talent Quest |
| Traveler Outfit | Reached Chapter 3 | Unlocked by reaching Chapter 3 |
| Master Outfit | Completed the game in Darkness Difficulty | Unlocked by completing the game  in Darkness Difficulty |
| Hidden Outfit | Wish Rainbow | Hidden requirements |
| Ravens Outfit | Ravens Skin Pack Acquired | Available in the Ravens Skin Pack |
| Nightmares Outfit | Nightmares Skin Pack Acquired | Available in the Nightmares Skin Pack |
| Timeless Outfit | Timeless Skin Pack Acquired | Available in the Timeless Skin Pack |
| Mercenaries Outfit | Mercenaries Skin Pack Acquired | Available in the Mercenaries Skin Pack |


**How to read the text**

- **Bold** words are highlighted in the game.
- `{0}`, `{1}` and so on are numbers or names the game fills in while you play.

Source: [`Hero_Aladdin_Common.LangEN.tsv`](../../data/Hero_Aladdin_Common.LangEN.tsv), [`Hero_Aladdin_Abilities.tsv`](../../data/Hero_Aladdin_Abilities.tsv), [`Hero_Aladdin_Talents.tsv`](../../data/Hero_Aladdin_Talents.tsv), [`Hero_Aladdin_Skins.LangEN.tsv`](../../data/Hero_Aladdin_Skins.LangEN.tsv).
Game version: Game build 1.06 (Steam build ID 25174305); the displayed version string is unverified. See VERSION.json.

*This page is generated from the TSV files in [data/](../../data/) by `tools/build_browse.py`. Do not edit it by hand; fix the data and re-run the script.*
