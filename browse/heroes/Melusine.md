# Melusine

[All tables](../README.md)

[Abilities](#abilities) · [Ability values](#ability-values) · [Talents](#talents) · [Outfits](#outfits) · [Memoir](../memoirs/Melusine.md)

Melusine was already a dangerous siren before the Nightmares impregnated her with a mysterious child. She uses powerful water magic and charming song to summon will-o-wisps to drown anyone with plans to harm her precious cargo. Melusine's atypical fighting style is unsettling to behold. Monsters, fill your ears with wax, lest the melodious mother fill your lungs with brine.

## Abilities

| Slot | Name | Description |
|---|---|---|
| Trait | Siren's Call | • Switch between **SING STANCE** and **MOVE STANCE**<br>• **SING STANCE** casts a controllable **WISP** but immobilizes the Hero<br>• **MOVE STANCE** revokes **WISP** and restores control to the Hero |
| Attack | Wisp Attack | • **WISP** suddenly dashes forward, dealing **`{0}`** damage to all enemies passed<br>• Automatically enter **SING STANCE** when cast |
| Power | Splatter | • **WISP** pulses a splash of water, dealing **`{0}`** damage to all enemies around<br>• Automatically enter **SING STANCE** when cast |
| Special | Torrent | • Send waves of water forward, dealing up to **`{0}`** damage |
| Defense | Dive | • Dive into a pool of water, turning **INTANGIBLE** for a short time<br>• Reemerge in **MOVE STANCE** |
| Ultimate 1 | Water Bomb | • `{0}` wraps herself in a water sphere and turns **INVINCIBLE**<br>• After a short time or if triggered, the sphere explodes and deals **`{1}`** damage to all nearby enemies |
| Ultimate 2 | Wisp Ballet | • Summon **`{0}`** autonomous **WISPS** that pursue and attack nearby enemies<br>• After **`{1}`** seconds, the **WISPS** cast **`{2}`** and then disappear |

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
| Siren's Call | cooldown | 0 | seconds | Decoded |   |
| Siren's Call | charges | 1 | charges | Decoded (baseline) |   |
| Siren's Call | active duration | *not decoded* | seconds | Not decoded |   |
| Siren's Call | resource cost | *not decoded* | resource | Not decoded |   |

### Attack

| Name | Stat | Value | Unit | Status | In-game check |
|---|---|---|---|---|---|
| Wisp Attack | damage per dash | 21 | damage | Decoded (baseline) |   |
| Wisp Attack | hit count | *not decoded* | hits | Not decoded |   |
| Wisp Attack | hit damage sequence | *not decoded* | damage | Not decoded |   |
| Wisp Attack | attack timing | *not decoded* | seconds | Not decoded |   |

### Power

| Name | Stat | Value | Unit | Status | In-game check |
|---|---|---|---|---|---|
| Splatter | cooldown | 4 | seconds | Decoded |   |
| Splatter | charges | 1 | charges | Decoded (baseline) |   |
| Splatter | damage | 50 | damage | Decoded (baseline) |   |
| Splatter | active duration | *not decoded* | seconds | Not decoded |   |
| Splatter | resource cost | *not decoded* | resource | Not decoded |   |

### Special

| Name | Stat | Value | Unit | Status | In-game check |
|---|---|---|---|---|---|
| Torrent | cooldown | 8 | seconds | Decoded |   |
| Torrent | charges | 1 | charges | Decoded (baseline) |   |
| Torrent | max total damage | 100 | damage | Decoded (baseline) |   |
| Torrent | active duration | *not decoded* | seconds | Not decoded |   |
| Torrent | resource cost | *not decoded* | resource | Not decoded |   |

### Defense

| Name | Stat | Value | Unit | Status | In-game check |
|---|---|---|---|---|---|
| Dive | cooldown | 8 | seconds | Decoded |   |
| Dive | charges | 1 | charges | Decoded (baseline) |   |
| Dive | intangible duration | *not decoded* | seconds | Not decoded |   |
| Dive | active duration | *not decoded* | seconds | Not decoded |   |
| Dive | resource cost | *not decoded* | resource | Not decoded |   |

### Ultimate 1

| Name | Stat | Value | Unit | Status | In-game check |
|---|---|---|---|---|---|
| Water Bomb | cooldown | 90 | seconds | Decoded |   |
| Water Bomb | charges | 1 | charges | Decoded (baseline) |   |
| Water Bomb | explosion damage | 400 | damage | Decoded (baseline) |   |
| Water Bomb | active duration | *not decoded* | seconds | Not decoded |   |
| Water Bomb | resource cost | *not decoded* | resource | Not decoded |   |
| Water Bomb | automatic explosion delay | 2 | seconds | Decoded |   |

### Ultimate 2

| Name | Stat | Value | Unit | Status | In-game check |
|---|---|---|---|---|---|
| Wisp Ballet | cooldown | *not decoded* | seconds | Not decoded | Second decoding pass: 60 |
| Wisp Ballet | charges | 1 | charges | Decoded (baseline) |   |
| Wisp Ballet | wisp count | 6 | wisps | Decoded |   |
| Wisp Ballet | duration | 4 | seconds | Decoded |   |
| Wisp Ballet | final cast ability name | Splatter |   | Fixed text |   |
| Wisp Ballet | active duration | *not decoded* | seconds | Not decoded |   |
| Wisp Ballet | resource cost | *not decoded* | resource | Not decoded |   |
| Wisp Ballet | damage per wisp attack | *not decoded* | damage | Not decoded |   |
| Wisp Ballet | wisp attack frequency | *not decoded* | per second | Not decoded |   |
| Wisp Ballet | final cast damage per wisp | *not decoded* | damage | Not decoded |   |

## Talents

Values separated by / are for Common / Rare / Epic / Legendary.

**Unlocks at rank** is the hero rank, not the level reached in a run.

### Ultimates

The talent tables do not include the base ultimates or their unlock ranks; this text is from the hero's text table.

| Ultimate | Description |
|---|---|
| Water Bomb | • Warp into a movable water sphere then release a giant splash, dealing huge damage to all nearby enemies |
| Wisp Ballet | • Channel several autonomous **WISPS** that track and attack all nearby enemies |

### Ultimate upgrades

| Talent | Upgrades | Unlocks at rank | Effect |
|---|---|---|---|
| Vortex Bomb | Water Bomb | 1 | ULTIMATE water sphere attracts nearby enemies and deals 40 / 50 / 60 / 70 damage per second to enemies hit |
| Healing Blast | Water Bomb | 9 | ULTIMATE explosion restores 60 / 75 / 90 / 105 health to all Heroes around and grants them REGENERATION +5 |
| Crescendo | Wisp Ballet | 6 | While ULTIMATE is channeled, Melusine gradually summons up to 3 / 4 / 5 / 6 additional WISPS |
| Overtone Singing | Wisp Ballet | 9 | When entering SING STANCE, Melusine casts an additional ULTIMATE autonomous WISP that deals 40 / 50 / 60 / 70% damage |

### Other talents

| Talent | Unlocks at rank | Effect |
|---|---|---|
| Aftershock | 1 | POWER leaves a water core at the casting location that triggers POWER again after 1.5 seconds for 40 / 50 / 60 / 70% of its damage |
| Backwash | 1 | When SPECIAL ends, add 3 additional waves that travel backwards and deal 50 / 65 / 80 / 95% damage each |
| Bewitching Song | 1 | When entering SING STANCE, apply WEAK to all nearby enemies for 3 / 4 / 5 / 6 seconds |
| Deep Beat | 1 | For every 4 ATTACKS that hit an enemy, generate a blast all around that deals 100 / 120 / 140 / 160% of ATTACK's damage<br>Counter resets when exiting SING STANCE |
| Freezing Splash | 1 | POWER applies CHILLED to all enemies hit and gains +15 / 20 / 25 / 30% range |
| Power Dive | 1 | DEFENSE triggers POWER's effect with a +20 / 25 / 30 / 35% damage increase when Melusine dives underwater |
| Protective Flow | 1 | Heroes passed by ATTACK gain 8 / 10 / 12 / 14 SHIELD for 6 seconds |
| Spring Water | 1 | Each wave from SPECIAL that hits an enemy restores 2 / 2.5 / 3 / 3.5 Health to all Heroes within the area of effect |
| Tidal Wave | 1 | SPECIAL's waves are 20 / 25 / 30 / 35% wider and longer |
| Water Bubble | 1 | After DEFENSE is triggered, Melusine is surrounded by a bubble for 4 seconds, absorbing damage for one hit<br>The bubble then explodes and deals 60 / 75 / 90 / 105 area damage |
| Submerging Attack | 2 | ATTACK damage increases by 8 / 9 / 10 / 11% for each enemy hit (up to 6 hits, +48 / 54 / 60 / 66%)<br>Resets if Melusine takes damage or exits SING STANCE |
| Underwater Predation | 2 | DEFENSE can be held to move more quickly underwater<br>All enemies passed become VULNERABLE for 4 / 5 / 6 / 7 seconds |
| Geyser | 3 | POWER deals +50 / 60 / 70 / 80% damage at its center |
| Water Communion | 3 | DEFENSE removes SPECIAL's cooldown and increases next SPECIAL's damage within 3 seconds by +40 / 50 / 60 / 70% |
| Razor Tail | 4 | DEFENSE makes Melusine strike with her tail, dealing 400 / 500 / 600 / 700% of ATTACK damage |
| Soothing Presence | 4 | When in combat, passively heal 4 / 5 / 6 / 7 Hit Points for all Heroes in the area every 5 seconds |
| Sea Dance | 5 | In SING STANCE, the CONTEXTUAL ACTION allows for quick teleportation to the WISP (5 seconds cooldown)<br>Performing this action in combat restores 8 / 10 / 12 / 14 health to all nearby Heroes |
| Wisp Surge | 5 | After casting SPECIAL, gain +40 / 50 / 60 / 70% ATTACK SPEED for 3 seconds |
| Final Burst | 7 | After 3 successful attacks, WISP explodes when it disappears, dealing 40 / 50 / 60 / 70 area damage |
| Waterlogging | 7 | WISP gains 2 growth charges for each wave of SPECIAL that hits it (up to a maximum of 12 charges)<br>Each charge increases the damage of the ATTACK by 20 / 25 / 30 / 35%, with each ATTACK consuming one charge |
| Enduring Wisp | 8 | When Melusine leaves the SING STANCE, WISP remains active and automatically attacks surrounding enemies up to 4 / 5 / 6 / 7 times before then disappearing |
| Shimmering Scales | 8 | In SING STANCE, Melusine gains temporary ARMOR every second, up to a maximum of 40 / 60 / 80 / 100 |

## Outfits

| Outfit | How to unlock | Description |
|---|---|---|
| Signature Outfit | Healed 4 times or more in a single activation of Singing Stance with 'Sea Danse' Talent | Unlocked by Healing 4 times or more in a single activation of Singing Stance with 'Sea Dance' Talent |
| Traveler Outfit | Reached Chapter 3 | Unlocked by reaching Chapter 3 |
| Master Outfit | Completed the game in Darkness Difficulty | Unlocked by completing the game  in Darkness Difficulty |
| Hidden Outfit | Water Brings Life | Hidden Requirements |
| Ravens Outfit | Ravens Skin Pack Acquired | Available in the Ravens Skin Pack |
| Nightmares Outfit | Nightmares Skin Pack Acquired | Available in the Nightmares Skin Pack |
| Timeless Outfit | Timeless Skin Pack Acquired | Available in the Timeless Skin Pack |


**How to read the text**

- **Bold** words are highlighted in the game.
- `{0}`, `{1}` and so on are numbers or names the game fills in while you play.

Source: [`Hero_Melusine_Common.LangEN.tsv`](../../data/Hero_Melusine_Common.LangEN.tsv), [`Hero_Melusine_Abilities.tsv`](../../data/Hero_Melusine_Abilities.tsv), [`Hero_Melusine_Talents.tsv`](../../data/Hero_Melusine_Talents.tsv), [`Hero_Melusine_Skins.LangEN.tsv`](../../data/Hero_Melusine_Skins.LangEN.tsv).
Game version: Game build 1.06 (Steam build ID 25174305); the displayed version string is unverified. See VERSION.json.

*This page is generated from the TSV files in [data/](../../data/) by `tools/build_browse.py`. Do not edit it by hand; fix the data and re-run the script.*
