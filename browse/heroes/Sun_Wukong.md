# Sun Wukong

[All tables](../README.md)

[Abilities](#abilities) · [Ability values](#ability-values) · [Talents](#talents) · [Outfits](#outfits) · [Memoir](../memoirs/Sun_Wukong.md)

Sun Wukong, the Monkey King and Heaven's Equal, lost his power of immortality during a great celebration at the hands of uninvited Nightmares. Still formidable, he relies on his alternating postures, embracing a balanced strategy of Yin and Yang to pound out all ideas of resistance from his foolish foes. One should expect no less from a god.

## Abilities

| Slot | Name | Description |
|---|---|---|
| Trait | Taiji | • Switch between **YIN STANCE** and **YANG STANCE**<br>• **YIN:** All abilities gain **`{0}`%** **LIFE ON HIT**, all heroes around gain **`{1}`** **SHIELD** for **`{2}`** seconds<br>• **YANG:** `{3}` Deals **and takes** **`{4}`%** more damage, all heroes around gain **STRENGTH** for **`{5}`** seconds |
| Attack | Ruyi Jingu Bang | • Chain attacks with the staff, with each successive move increasing its range as well as its power<br>• The full chain deals a total of **`{0}`** damage |
| Power | Jindou Yun | • Rush toward a nearby enemy then strike it for **`{0}`** damage<br>• If other enemies are nearby, `{1}` can follow up with **`{2}`** other targets while being **INTANGIBLE** |
| Special | Mantra | • Launch prayer beads that orbit `{0}` for **`{1}`** second(s), dealing **`{2}`** damage per second to enemies affected |
| Defense | Empty Palm | • Block any attack for **`{0}`** second(s)<br>• If an attack is blocked, the blocking time is reset and `{1}` has no cooldown |
| Ultimate 1 | Monkey Clones | • Summons **`{0}`** clones in the area, which will fight nearby enemies and attract their attention<br>• Clones copy `{1}`'s **VITALITY** and **DMG** and disappear after **`{2}`** seconds |
| Ultimate 2 | Transfiguration | • `{0}` transforms for **`{1}`** seconds into a copy of another random hero, with all their standard Talents activated, of Epic quality |

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
| Taiji (Yin Stance) | cooldown | 7 | seconds | Decoded |   |
| Taiji (Yin Stance) | charges | 1 | charges | Decoded (baseline) |   |
| Taiji (Yin Stance) | life on hit | 10 | percent | Decoded |   |
| Taiji (Yin Stance) | nearby hero shield | *not decoded* | shield | Not decoded | Second decoding pass: 15 |
| Taiji (Yin Stance) | shield duration | *not decoded* | seconds | Not decoded | Second decoding pass: 6 |
| Taiji (Yang Stance) | damage dealt increase | 100 | percent | Decoded |   |
| Taiji (Yang Stance) | damage taken increase | 100 | percent | Decoded |   |
| Taiji (Yang Stance) | strength buff duration | *not decoded* | seconds | Not decoded | Second decoding pass: 4 |
| Taiji (Yin Stance) | active duration | *not decoded* | seconds | Not decoded |   |
| Taiji (Yin Stance) | resource cost | *not decoded* | resource | Not decoded |   |

### Attack

| Name | Stat | Value | Unit | Status | In-game check |
|---|---|---|---|---|---|
| Ruyi Jingu Bang | combo sequence damage | *not decoded* | damage | Not decoded | Second decoding pass: 81 |
| Ruyi Jingu Bang | hit count | *not decoded* | hits | Not decoded |   |
| Ruyi Jingu Bang | hit damage sequence | *not decoded* | damage | Not decoded |   |
| Ruyi Jingu Bang | attack timing | *not decoded* | seconds | Not decoded |   |

### Power

| Name | Stat | Value | Unit | Status | In-game check |
|---|---|---|---|---|---|
| Jindou Yun | cooldown | 6 | seconds | Decoded |   |
| Jindou Yun | charges | 1 | charges | Decoded (baseline) |   |
| Jindou Yun | damage per strike | 30 | damage | Decoded (baseline) |   |
| Jindou Yun | additional targets | 2 | targets | Decoded (baseline) |   |
| Jindou Yun | active duration | *not decoded* | seconds | Not decoded |   |
| Jindou Yun | resource cost | *not decoded* | resource | Not decoded |   |

### Special

| Name | Stat | Value | Unit | Status | In-game check |
|---|---|---|---|---|---|
| Mantra | cooldown | 11 | seconds | Decoded |   |
| Mantra | charges | 1 | charges | Decoded (baseline) |   |
| Mantra | damage per second | *not decoded* | damage per second | Not decoded | Second decoding pass: 16 |
| Mantra | duration | 5 | seconds | Decoded |   |
| Mantra | active duration | *not decoded* | seconds | Not decoded |   |
| Mantra | resource cost | *not decoded* | resource | Not decoded |   |

### Defense

| Name | Stat | Value | Unit | Status | In-game check |
|---|---|---|---|---|---|
| Empty Palm | cooldown | 5 | seconds | Decoded |   |
| Empty Palm | charges | 1 | charges | Decoded (baseline) |   |
| Empty Palm | parry window | 0.5 | seconds | Decoded |   |
| Empty Palm | active duration | *not decoded* | seconds | Not decoded |   |
| Empty Palm | resource cost | *not decoded* | resource | Not decoded |   |
| Empty Palm | cooldown removed ability | Empty Palm |   | Fixed text |   |

### Ultimate 1

| Name | Stat | Value | Unit | Status | In-game check |
|---|---|---|---|---|---|
| Monkey Clones | cooldown | 90 | seconds | Decoded |   |
| Monkey Clones | charges | 1 | charges | Decoded (baseline) |   |
| Monkey Clones | clone count | 6 | clones | Decoded |   |
| Monkey Clones | lifetime | 10 | seconds | Decoded |   |
| Monkey Clones | active duration | *not decoded* | seconds | Not decoded |   |
| Monkey Clones | resource cost | *not decoded* | resource | Not decoded |   |
| Monkey Clones | copied vitality formula | *not decoded* | vitality | Not decoded |   |
| Monkey Clones | copied dmg formula | *not decoded* | DMG | Not decoded |   |

### Ultimate 2

| Name | Stat | Value | Unit | Status | In-game check |
|---|---|---|---|---|---|
| Transfiguration | cooldown | 90 | seconds | Decoded |   |
| Transfiguration | charges | 1 | charges | Decoded (baseline) |   |
| Transfiguration | duration | 20 | seconds | Decoded |   |
| Transfiguration | active duration | *not decoded* | seconds | Not decoded |   |
| Transfiguration | resource cost | *not decoded* | resource | Not decoded |   |

## Talents

Values separated by / are for Common / Rare / Epic / Legendary.

| Talent | Unlocks at rank | Effect |
|---|---|---|
| Airbender | 1 | POWER can strike up to 1 / 2 / 3 / 4 more time(s) |
| Army of Monkeys | 1 | ULTIMATE summons 3 / 4 / 5 / 6 additional clones |
| Celestial Pillar | 1 | Adds a crushing blow to the ATTACK combo, dealing 40 / 50 / 60 / 70 damage around the point of impact |
| Ch'i Outburst | 8 | After POWER hits at least one enemy, the next ATTACK can be held down to store power then released to deliver an energy beam dealing up to 100 / 125 / 150 / 175% POWER damage to all enemies it passes through |
| Divine Beverage | 9 | ULTIMATE transformation grants all heroes around OMNIPOTENCE for 8 / 10 / 12 / 14 seconds<br>During OMNIPOTENCE, Heroes' POWER, SPECIAL and DEFENSE have a 0.5 second cooldown |
| Divine Palm | 5 | Blocking with DEFENSE less than 0.2 second(s) after its activation triggers a perfect block:<br>YIN: restores 4 / 5 / 6 / 7 health to all nearby heroes<br>YANG: deals 40 / 50 / 60 / 70 area damage |
| Fiery Dragon | 4 | Adds an explosion of fire to the activation effects of YANG STANCE, dealing 55 / 68 / 82 / 96 area damage and inflicting enemies with IGNITE |
| Fiery Golden Eyes | 8 | At the start of each DAY or NIGHT, reveal 2 point(s) of interest on the map<br>Personal Dream Shards gains are increased by 20 / 25 / 30 / 35% |
| Focused Strikes | 7 | POWER can be held down to deliver the next strike to the same target and deals +8 / 10 / 12 / 14% damage |
| Frost Tiger | 4 | Adds an explosion of frost to the activation effects of YIN STANCE, dealing 44 / 55 / 66 / 77 area damage and inflicting enemies with CHILLED |
| Mantra of Balance | 1 | When SPECIAL is triggered, it applies a negative status effect to enemies within range:<br>YIN: VULNERABLE for 4 / 5 / 6 / 7 second(s)<br>YANG: WEAKENED for 6 / 8 / 10 / 12 second(s) |
| Mantra of Replication | 9 | Whenever SPECIAL is casted, summon 3 Monkey Clone that fight for 8 / 10 / 12 / 14 seconds |
| Mind Fortress | 3 | SHIELD and STRENGTH effects triggered upon TRAIT activation last 60 / 75 / 90 / 100% longer |
| One-Inch Punch | 3 | ATTACK triggered after a successful DEFENSE launches a powerful punch, dealing 600 / 750 / 900 / 1050% damage |
| Perfect Copy | 6 | During the ULTIMATE transformation, Sun Wukong can use a random ULTIMATE ability of the Hero copied<br>Transfiguration lasts 4 / 5 / 6 / 7 more seconds |
| Resonance | 1 | When the SPECIAL effect expires, all the activation effects of the current STANCE are restarted<br>SPECIAL deals +20 / 25 / 30 / 35% damage |
| Ringing Beads | 1 | While SPECIAL is active, ATTACK makes beads ring, dealing 30 / 35 / 40 / 45% ATTACK damage all around |
| Sacred Seal | 7 | When SPECIAL ends, orbs sink into the ground to draw a sacred pattern that explodes after a short time, dealing 50 / 62.5 / 75 / 87.5 area damage |
| Sprint | 1 | Bestows +10 / 12 / 14 / 16% Move Speed<br>DASH can be held for up to 3 seconds to sprint at high speed |
| Stick Twirl | 1 | ATTACK triggered after a DASH launches a rapid series of 5 strikes, each dealing 60 / 75 / 90 / 105% area damage |
| Stone Monkey | 1 | Quest (x40): Each successful DEFENSE grants +0.5 ARMOR<br>Complete: Each block triggers an attack dealing 100 / 125 / 150 / 175% of the blocked damage as area damage |
| Supreme Polarity | 2 | Switching STANCE increases the power of the new STANCE for 7 seconds:<br>YIN: +4 / 5 / 6 / 7% LIFE ON HIT<br>YANG: deals +20 / 25 / 30 / 35% damage |
| Thirst for Immortality | 1 | Quest (x7): Obtaining a Magical Object with an Epic quality or better grants +2 DMG<br>Complete: Grants +1 / 1.25 / 1.5 / 1.75 VITALITY, but now only Hero or Magical Object heals are effective |
| Thundercloud | 2 | Enemies hit by POWER are soon afterwards struck by lightning, dealing 20 / 25 / 30 / 35% damage all around the point of impact |
| Way of Awakening | 5 | After 7 successful DEFENSE actions, the next TRAIT activates AWAKENED STANCE for 12 / 15 / 18 / 21 seconds<br>AWAKENED STANCE grants both YIN and YANG effects, without taking any additional damage |
| Ōm | 1 | While SPECIAL is active, beads gradually increase their action radius, up to +24 / 30 / 36 / 42%, and hit all enemies present in the area |

## Outfits

| Outfit | How to unlock | Description |
|---|---|---|
| Signature Outfit | Completed the 'Thirst of Immortality' Talent Quest | Unlocked by completing the 'Thirst of Immortality' Talent Quest |
| Traveler Outfit | Reached Chapter 3 | Unlocked by reaching Chapter 3 |
| Master Outfit | Completed the game in Darkness Difficulty | Unlocked by completing the game  in Darkness Difficulty |
| Hidden Outfit | Master of Disguise | Hidden Requirements |
| Ravens Outfit | Ravens Skin Pack Acquired | Available in the Ravens Skin Pack |
| Nightmares Outfit | Nightmares Skin Pack Acquired | Available in the Nightmares Skin Pack |
| Unleashed Outfit | Unleashed Skin Pack Acquired | Available in the Unleashed Skin Pack |
| Mercenaries Outfit | Mercenaries Skin Pack Acquired | Available in the Mercenaries Skin Pack |


**How to read the text**

- **Bold** words are highlighted in the game.
- `{0}`, `{1}` and so on are numbers or names the game fills in while you play.

Source: [`Hero_SunWukong_Common.LangEN.tsv`](../../data/Hero_SunWukong_Common.LangEN.tsv), [`Hero_SunWukong_Abilities.tsv`](../../data/Hero_SunWukong_Abilities.tsv), [`Hero_SunWukong_Talents.tsv`](../../data/Hero_SunWukong_Talents.tsv), [`Hero_SunWukong_Skins.LangEN.tsv`](../../data/Hero_SunWukong_Skins.LangEN.tsv).
Game version: Game build 1.06 (Steam build ID 25174305); the displayed version string is unverified. See VERSION.json.

*This page is generated from the TSV files in [data/](../../data/) by `tools/build_browse.py`. Do not edit it by hand; fix the data and re-run the script.*
