# Geppetto

[All tables](../README.md)

[Abilities](#abilities) · [Ability values](#ability-values) · [Talents](#talents) · [Outfits](#outfits) · [Memoir](../memoirs/Geppetto.md)

After losing his son to Nightmares, Geppetto set his mind to the invention of deadly automatons: squadrons of killing machines, messengers of booming doom. The once-upon-a-time puppet maker now works to bring about the destruction of the horrors invading Reverie as efficiently as possible. Geppetto's minions know no fear and never tell lies.

## Abilities

| Slot | Name | Description |
|---|---|---|
| Trait | Dummy | • Build a **DUMMY** that draws enemies' attention and attacks them for **`{0}`** damage<br>• `{1}` can have up to **`{2}` DUMMIES** built at the same time<br>• **DUMMIES** can be dismantled using **Contextual Action** and will self destroy if they are too far from `{3}` |
| Attack | Hammer | • Attack with a hammer at close quarters, dealing **`{0}`** damage<br>• **DUMMIES** hit are healed for **`{1}`%** of their Maximum Health |
| Power | Uppercut | • Perform a powerful hammer strike that deals **`{0}`** damage<br>• Closest **DUMMY** hit is displaced and deals **`{1}`** damage along its path |
| Special | Cogsplosion | • Hold then release to roll a bomb that explodes after a short duration, dealing **`{0}`** damage all around<br>• **DUMMIES** hit are healed for **`{1}`%** of their Maximum Health |
| Defense | Defibrillation | • Apply a **`{0}`** **SHIELD** on `{1}` and all **DUMMIES** for **`{2}`** seconds<br>• Briefly grants **INTANGIBLE** at the start of the ability |
| Ultimate 1 | Meca-Puppet | • Create an autonomous **PUPPET** that will attack the closest target and deal up to **`{0}`** damage per second<br>• **PUPPET** follows `{1}` if no target is nearby and lasts up to **`{2}`** seconds |
| Ultimate 2 | Overclock | • Make all **DUMMIES** spin around and track nearby enemies, each one dealing **`{0}`** damage per second all around |

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
| Dummy | cooldown | 4 | seconds | Decoded |   |
| Dummy | charges | 1 | charges | Decoded (baseline) |   |
| Dummy | attack damage | 40 | damage | Decoded (baseline) |   |
| Dummy | max dummies | 3 | dummies | Decoded (baseline) |   |
| Dummy | active duration | *not decoded* | seconds | Not decoded |   |
| Dummy | resource cost | *not decoded* | resource | Not decoded |   |
| Dummy | dummy max health formula | *not decoded* | health | Not decoded |   |
| Dummy | self destruct distance | *not decoded* | meters | Not decoded |   |

### Attack

| Name | Stat | Value | Unit | Status | In-game check |
|---|---|---|---|---|---|
| Hammer | damage | 15 | damage | Decoded (baseline) |   |
| Hammer | dummy repair | 15 | percent | Decoded |   |
| Hammer | hit count | *not decoded* | hits | Not decoded |   |
| Hammer | hit damage sequence | *not decoded* | damage | Not decoded |   |
| Hammer | attack timing | *not decoded* | seconds | Not decoded |   |

### Power

| Name | Stat | Value | Unit | Status | In-game check |
|---|---|---|---|---|---|
| Uppercut | cooldown | 3 | seconds | Decoded |   |
| Uppercut | charges | 1 | charges | Decoded (baseline) |   |
| Uppercut | hammer damage | 25 | damage | Decoded (baseline) |   |
| Uppercut | launched dummy damage | 50 | damage | Decoded (baseline) |   |
| Uppercut | active duration | *not decoded* | seconds | Not decoded |   |
| Uppercut | resource cost | *not decoded* | resource | Not decoded |   |

### Special

| Name | Stat | Value | Unit | Status | In-game check |
|---|---|---|---|---|---|
| Cogsplosion | cooldown | 7 | seconds | Decoded |   |
| Cogsplosion | charges | 1 | charges | Decoded (baseline) |   |
| Cogsplosion | explosion damage | 40 | damage | Decoded (baseline) |   |
| Cogsplosion | dummy repair | 40 | percent | Decoded |   |
| Cogsplosion | active duration | *not decoded* | seconds | Not decoded |   |
| Cogsplosion | resource cost | *not decoded* | resource | Not decoded |   |
| Cogsplosion | explosion delay | *not decoded* | seconds | Not decoded |   |

### Defense

| Name | Stat | Value | Unit | Status | In-game check |
|---|---|---|---|---|---|
| Defibrillation | cooldown | 12 | seconds | Decoded |   |
| Defibrillation | charges | 1 | charges | Decoded (baseline) |   |
| Defibrillation | shield amount | 20 | shield | Decoded (baseline) |   |
| Defibrillation | duration | 6 | seconds | Decoded |   |
| Defibrillation | active duration | *not decoded* | seconds | Not decoded |   |
| Defibrillation | resource cost | *not decoded* | resource | Not decoded |   |
| Defibrillation | intangible duration | *not decoded* | seconds | Not decoded |   |
| Defibrillation | hero dummy scaling distinction | *not decoded* |   | Not decoded |   |

### Ultimate 1

| Name | Stat | Value | Unit | Status | In-game check |
|---|---|---|---|---|---|
| Meca-Puppet | cooldown | 90 | seconds | Decoded |   |
| Meca-Puppet | charges | 1 | charges | Decoded (baseline) |   |
| Meca-Puppet | damage per second | *not decoded* | damage per second | Not decoded | Game shows 77 |
| Meca-Puppet | lifetime | 40 | seconds | Decoded |   |
| Meca-Puppet | active duration | *not decoded* | seconds | Not decoded |   |
| Meca-Puppet | resource cost | *not decoded* | resource | Not decoded |   |

### Ultimate 2

| Name | Stat | Value | Unit | Status | In-game check |
|---|---|---|---|---|---|
| Overclock | cooldown | *not decoded* | seconds | Not decoded | Second decoding pass: 70 |
| Overclock | charges | 1 | charges | Decoded (baseline) |   |
| Overclock | damage per second | *not decoded* | damage per second | Not decoded | Second decoding pass: 50 |
| Overclock | resource cost | *not decoded* | resource | Not decoded |   |
| Overclock | duration | 6 | seconds | Decoded |   |
| Overclock | active duration | 6 | seconds | Decoded |   |

## Talents

Values separated by / are for Common / Rare / Epic / Legendary.

| Talent | Unlocks at rank | Effect |
|---|---|---|
| Bomb Reserve | 1 | When in combat, the Meca-Puppet sends a bomb around itself every 1 second(s), dealing 40 / 50 / 60 / 70 area damage |
| Clockwork Medicine | 3 | DUMMIES healed by SPECIAL also gain +8 / 10 / 12 / 14 REGENERATION |
| Dummyball | 1 | SPECIAL creates a DUMMY when it explodes and deals 155 / 170 / 185 / 200% damage<br>Has no effect if max number of DUMMIES are already active |
| Explosive Builds | 1 | When built by TRAIT, DUMMIES emit a blast, dealing 40 / 50 / 60 / 70 area damage |
| Family Meeting | 4 | When three or more DUMMIES are active, Geppetto and DUMMIES gain +20 / 25 / 30 / 35% ATTACK SPEED |
| Fireworks | 3 | Each time a DUMMY regains 30 / 25 / 20 / 15% of its Maximum Health, it shoots a homing missile that deals 15 damage to a nearby enemy |
| Flash of Genius | 8 | First time this Talent is chosen, instantly create 1 / 2 / 3 / 4 random magical object(s) <br>Each upgrade to this Talent will create an additional item once |
| Flux Capacitor | 2 | While Geppetto has SHIELD, POWER affects all DUMMIES within range and deals +20 / 25 / 30 / 35% damage |
| Forked Lightning | 1 | DEFENSE sends bolts of lightning toward DUMMIES, each dealing 40 / 50 / 60 / 70 damage |
| Heart Ties | 1 | DUMMIES gain 40 / 50 / 60 / 70% of Geppetto's VITALITY<br>Geppetto gains +5 ARMOR per active DUMMY |
| High Voltage | 6 | After a DUMMY is displaced by POWER, it activates the Overclock effect of the ULTIMATE for 1 / 1.5 / 2 / 2.5 second(s) |
| Hyperclock | 9 | DUMMIES under the Overclock effect overheat, applying IGNITE to hit enemies, and lastly explode to deal 80 / 100 / 120 / 140 area damage |
| Large Family | 1 | Increase maximum active DUMMIES by 1<br>TRAIT has a 10 / 15 / 20 / 25% reduced cooldown |
| Laser Lenses | 4 | When the DEFENSE effect is applied, DUMMIES' next attack shoots lasers from their eyes, dealing 200 / 250 / 300 / 350% ranged damage |
| Lightning Rod Dummies | 8 | A short time after the DEFENSE effect is applied, DUMMIES are struck by lightning and deal 36 / 45 / 54 / 63 damage around |
| Magnetic Hammer | 7 | Holding POWER allows Geppetto to pull in a DUMMY in front of him<br>Upon release, the DUMMY that has been pulled in deals +40 / 50 / 60 / 70% damage across a 100% wider area |
| Master Puppet | 9 | When the Meca-Puppet is built, it consumes any DUMMY built around to gain 32 / 40 / 48 / 56% max. health and deal 16 / 20 / 24 / 28% more damage per DUMMY consumed |
| Mourning Rage | 1 | Whenever a DUMMY is destroyed, Geppetto and other DUMMIES gain STRENGTH for 4 / 6 / 8 / 10 seconds |
| Nailing Strike | 1 | Adds an additional strike to the ATTACK combo, dealing 400 / 500 / 600 / 700% damage |
| Oiled Mechanisms | 1 | DUMMIES hit by Geppetto's ATTACK immediately attack in their current position, dealing 50 / 60 / 70 / 80% damage |
| Pogo-Hoppers | 1 | DUMMIES move 100 / 133.3 / 166.6 / 200% farther when attacking |
| Rocket Science | 1 | DASH can be held for up to 1 second(s), dealing 32 / 40 / 48 / 56 damage along its path and applying IGNITE to all enemies hit.<br>Crossed DUMMIES catch fire and their attacks deal +25 / 25 / 30 / 35% damage for 5 seconds |
| Sharp Noses | 7 | DUMMIES have a 50% chance of attacking with their nose, dealing 160 / 200 / 240 / 280% damage on all enemies they hit |
| Twin Dummies | 2 | TRAIT has a 55 / 70 / 85 / 100% chance to build two DUMMIES at once |
| Unstable Cores | 5 | 3 seconds after their creation, DUMMIES become unstable<br>If an unstable DUMMY is hit with POWER - or if it is destroyed or dismantled - this will cause it to explode, dealing 70 / 87.5 / 105 / 122.5 area damage |
| Vacuum Capsule | 5 | DUMMIES hit by SPECIAL are jerked toward the center of the explosion, dealing 40 / 50 / 60 / 70% of POWER damage along the way |

## Outfits

| Outfit | How to unlock | Description |
|---|---|---|
| Signature Outfit | Blew up 3 dummies in less than a second with 'Unstable Cores' talent in combat | Unlocked by Blowing up 3 dummies in less than a second with 'Unstable Cores' talent in combat |
| Traveler Outfit | Reached Chapter 3 | Unlocked by reaching Chapter 3 |
| Master Outfit | Completed the game in Darkness Difficulty | Unlocked by completing the game  in Darkness Difficulty |
| Hidden Outfit | One Man Army | Hidden Requirements |
| Ravens Outfit | Ravens Skin Pack Acquired | Available in the Ravens Skin Pack |
| Nightmares Outfit | Nightmares Skin Pack Acquired | Available in the Nightmares Skin Pack |
| Timeless Outfit | Timeless Skin Pack Acquired | Available in the Timeless Skin Pack |
| Mercenaries Outfit | Mercenaries Skin Pack Acquired | Available in the Mercenaries Skin Pack |


**How to read the text**

- **Bold** words are highlighted in the game.
- `{0}`, `{1}` and so on are numbers or names the game fills in while you play.

Source: [`Hero_Geppetto_Common.LangEN.tsv`](../../data/Hero_Geppetto_Common.LangEN.tsv), [`Hero_Geppetto_Abilities.tsv`](../../data/Hero_Geppetto_Abilities.tsv), [`Hero_Geppetto_Talents.tsv`](../../data/Hero_Geppetto_Talents.tsv), [`Hero_Geppetto_Skins.LangEN.tsv`](../../data/Hero_Geppetto_Skins.LangEN.tsv).
Game version: Game build 1.06 (Steam build ID 25174305); the displayed version string is unverified. See VERSION.json.

*This page is generated from the TSV files in [data/](../../data/) by `tools/build_browse.py`. Do not edit it by hand; fix the data and re-run the script.*
