# Juliet

[All tables](../README.md)

[Abilities](#abilities) · [Ability values](#ability-values) · [Talents](#talents) · [Outfits](#outfits) · [Memoir](../memoirs/Juliet.md)

Juliet's dreams of happily-ever-after were dashed when Romeo awakened, unable to form new memories, and "'til death do us part" took on a whole new meaning. Determined to make the most of their second shot at love, Juliet has honed her skills so her shooting is as devastating as her beauty.

## Abilities

| Slot | Name | Description |
|---|---|---|
| Trait | Until death do us part | • **Passive:** If `{0}` definitely dies, `{1}` dies too<br>• **Active:** Consume Health equivalent to **`{2}`%** of Maximum Health to make `{0}` heal for **`{3}`%** of the amount (healing above Maximum Health is converted into **SHIELD**) |
| Attack | Pistol Shot | • Shoot with pistol, dealing **`{0}`** damage<br>• Shots consume **AMMO** which reloads after a period of time without shooting<br>• **DASH** instantly reloads all **AMMO** |
| Power | Power Shot | • Hold then release to shoot a piercing bullet dealing **`{0}`** damage (requires one **AMMO**)<br>• Release at key moment to trigger a **PERFECT SHOT** dealing **+`{1}`%** damage<br>• Shooting a `{2}`'s Rose makes it explode, dealing **`{3}`** damage all around |
| Special | Passionate Kiss | • Call `{0}` during **`{1}`** seconds or answer `{0}`'s call<br>• Answering the call makes both heroes dash towards each other and kiss at half-distance dealing **`{2}`** area damage, then they move back in opposite directions |
| Defense | Strafe | • `{0}` becomes **INTANGIBLE** and triggers a barrage of **ATTACK**’s bullets on nearby enemies consuming all remaining **AMMO** |
| Ultimate 1 | Wild Waltz | • `{2}` rushes towards `{0}` to perform an **INTANGIBLE** dance for **`{1}`** seconds<br>• Both Heroes influence moving direction during dance. The more identical the directions, the faster the movement<br>• Deal between **`{3}`** and **`{4}`** area damage per second (according to their movement speed) |
| Ultimate 2 | Poison Flask | • Throw a poison flask in the air<br>• Trigger **ULTIMATE** again at the right time to shoot the flask and make it explode, dealing **`{0}`** to **`{1}`** damage in a wide area |
| Trait Solo | Broken Heart | • Consume Health equivalent to **`{0}`%** of Maximum Health to gain **+`{1}`** **REGENERATION** |

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
| Until death do us part (Paired) | cooldown | 15 | seconds | Decoded |   |
| Until death do us part (Paired) | charges | 1 | charges | Decoded (baseline) |   |
| Until death do us part (Paired) | health sacrifice | 15 | percent | Decoded |   |
| Until death do us part (Paired) | heal ratio | *not decoded* | percent | Not decoded | Second decoding pass: 200 |
| Broken Heart (Solo) | cooldown | *not decoded* | seconds | Not decoded | Second decoding pass: 15 |
| Broken Heart (Solo) | health sacrifice | 15 | percent | Decoded |   |
| Broken Heart (Solo) | regeneration rate | 6 | health per second | Decoded |   |
| Until death do us part (Paired) | active duration | *not decoded* | seconds | Not decoded |   |
| Until death do us part (Paired) | resource cost | *not decoded* | resource | Not decoded |   |
| Broken Heart (Solo) | charges | *not decoded* | charges | Not decoded |   |
| Broken Heart (Solo) | active duration | *not decoded* | seconds | Not decoded |   |
| Broken Heart (Solo) | resource cost | *not decoded* | resource | Not decoded |   |
| Broken Heart (Solo) | solo trait selection condition | *not decoded* |   | Not decoded |   |

### Attack

| Name | Stat | Value | Unit | Status | In-game check |
|---|---|---|---|---|---|
| Pistol Shot | damage per shot | 20 | damage | Decoded (baseline) |   |
| Pistol Shot | hit count | *not decoded* | hits | Not decoded |   |
| Pistol Shot | hit damage sequence | *not decoded* | damage | Not decoded |   |
| Pistol Shot | attack timing | *not decoded* | seconds | Not decoded |   |
| Pistol Shot | reload behavior | *not decoded* |   | Not decoded |   |
| Pistol Shot | ammo capacity | 6 | ammo | Decoded (baseline) |   |
| Pistol Shot | reload progression interval configuration | 0.4 | seconds | Decoded |   |
| Pistol Shot | no shooting reload delay | 0.2 | seconds | Decoded |   |

### Power

| Name | Stat | Value | Unit | Status | In-game check |
|---|---|---|---|---|---|
| Power Shot | cooldown | 4 | seconds | Decoded |   |
| Power Shot | charges | 1 | charges | Decoded (baseline) |   |
| Power Shot | base damage | 80 | damage | Decoded (baseline) |   |
| Power Shot | perfect shot bonus | *not decoded* | percent | Not decoded | Second decoding pass: 50 |
| Power Shot | rose explosion damage | 80 | damage | Decoded (baseline) |   |
| Power Shot | active duration | *not decoded* | seconds | Not decoded |   |
| Power Shot | resource cost | *not decoded* | resource | Not decoded |   |
| Power Shot | hold release timing window | 0.1 | seconds | Decoded |   |

### Special

| Name | Stat | Value | Unit | Status | In-game check |
|---|---|---|---|---|---|
| Passionate Kiss | cooldown | 9 | seconds | Decoded |   |
| Passionate Kiss | charges | 1 | charges | Decoded (baseline) |   |
| Passionate Kiss | call window | 3 | seconds | Decoded |   |
| Passionate Kiss | kiss area damage | *not decoded* | damage | Not decoded | Second decoding pass: 125 |
| Passionate Kiss | active duration | *not decoded* | seconds | Not decoded |   |
| Passionate Kiss | resource cost | *not decoded* | resource | Not decoded |   |

### Defense

| Name | Stat | Value | Unit | Status | In-game check |
|---|---|---|---|---|---|
| Strafe | cooldown | 6 | seconds | Decoded |   |
| Strafe | charges | 1 | charges | Decoded (baseline) |   |
| Strafe | ammo consumed | all remaining Ammo |   | Fixed text |   |
| Strafe | active duration | *not decoded* | seconds | Not decoded |   |
| Strafe | resource cost | *not decoded* | resource | Not decoded |   |
| Strafe | fire cadence | *not decoded* | shots per second | Not decoded |   |
| Strafe | bullet damage reference | *not decoded* | damage | Not decoded |   |

### Ultimate 1

| Name | Stat | Value | Unit | Status | In-game check |
|---|---|---|---|---|---|
| Wild Waltz | cooldown | *not decoded* | seconds | Not decoded | Second decoding pass: 90 |
| Wild Waltz | charges | 1 | charges | Decoded (baseline) |   |
| Wild Waltz | duration | 7 | seconds | Decoded |   |
| Wild Waltz | active duration | *not decoded* | seconds | Not decoded |   |
| Wild Waltz | resource cost | *not decoded* | resource | Not decoded |   |
| Wild Waltz | min area dps | *not decoded* | damage per second | Not decoded | Second decoding pass: 130 |
| Wild Waltz | max area dps | *not decoded* | damage per second | Not decoded | Second decoding pass: 260 |
| Wild Waltz | movement speed damage formula | *not decoded* |   | Not decoded |   |

### Ultimate 2

| Name | Stat | Value | Unit | Status | In-game check |
|---|---|---|---|---|---|
| Poison Flask | cooldown | *not decoded* | seconds | Not decoded | Second decoding pass: 60 |
| Poison Flask | charges | 1 | charges | Decoded (baseline) |   |
| Poison Flask | min damage | 300 | damage | Decoded (baseline) |   |
| Poison Flask | max damage | 600 | damage | Decoded (baseline) |   |
| Poison Flask | active duration | *not decoded* | seconds | Not decoded |   |
| Poison Flask | resource cost | *not decoded* | resource | Not decoded |   |
| Poison Flask | range timing rule | *not decoded* | seconds | Not decoded |   |

## Talents

Values separated by / are for Common / Rare / Epic / Legendary.

### Starting talents

Talents unlocked at rank 1, not counting ultimate upgrades.

| Talent | Effect |
|---|---|
| Bullet Ballet | DEFENSE shots can ricochet to hit nearby targets, dealing 60 / 75 / 90 / 105% ATTACK damage |
| Defensive Reload | Reload 3 / 4 / 5 / 6 AMMO after using DEFENSE |
| Hot Shots | ATTACKS triggered within 2 second(s) after a POWER apply IGNITE to hit enemies and deal +20 / 25 / 30 / 35% damage |
| Kiss the Groom | Quest (x20): Hitting at least one enemy with SPECIAL grants +0.5 Crit Chance<br>Complete: Any enemy hit by SPECIAL has a 40 / 50 / 60 / 70% chance to grant Juliet 2 Dream Shard(s) |
| Large Chambers | Maximum amount of AMMO is increased by 2<br>ATTACK and POWER damage are increased by 3 / 3.5 / 4 / 4.5% for each missing AMMO |
| Longshot | POWER gains +50% range and deals +20 / 25 / 30 / 35% damage to enemies hit beyond half the maximum range |
| Overflowing Passion | SPECIAL restores 6 / 7.5 / 9 / 10.5 Health to all Heroes around whenever it hits at least an enemy |
| Shadow Round | PERFECT SHOT applies VULNERABLE for 2 / 2.5 / 3 / 3.5 second(s) to hit enemies |
| Valiant Hearts | TRAIT grants both Romeo and Juliet +20% MOVE SPEED and STRENGTH for 5 / 6.25 / 7.5 / 8.75 second(s) |
| Volcanic Shots | ATTACK triggered right after DASH shoots 3 / 4 / 5 / 6 times in a row, consuming 3 AMMO |

### Ultimates

The talent tables do not include the base ultimates or their unlock ranks; this text is from the hero's text table.

| Ultimate | Description |
|---|---|
| Wild Waltz | • `{0}` rushes towards `{1}` to perform an **INTANGIBLE** dance dealing area damage |
| Poison Flask | • Throw a poison flask in the air<br>• Trigger **ULTIMATE** again at the right time to shoot the flask and make it explode, dealing damage in a wide area |

### Ultimate upgrades

| Talent | Upgrades | Unlocks at rank | Effect |
|---|---|---|---|
| Passion Dance | Wild Waltz | 1 | Restore between 4–8 / 5–10 / 6–12 / 7–14 Health per seconds to all Heroes nearby during ULTIMATE’s dance (depending on dance movement speed) |
| Flashy Ending | Wild Waltz | 9 | Dancing gauge can be filled up according to the synchronization of Romeo and Juliet's movements during ULTIMATE<br>Trigger an explosion at the end of the dance dealing from 270 / 337.5 / 405 / 472.5 to 540 / 675 / 810 / 945 area damage (based on dancing gauge level) |
| Plague Flask | Poison Flask | 6 | ULTIMATE’s explosion applies MARKED to hit enemies for 4 / 5 / 6 / 7 second(s) |
| Unstable Concoction | Poison Flask | 9 | Using DASH makes Juliet drop a flask of poison to the ground, dealing 30 / 40 / 50 / 60 damage in a zone |

### Other talents

| Talent | Unlocks at rank | Effect |
|---|---|---|
| Double Tap | 2 | Hold POWER to trigger 2 shots in a row<br>The second shot deals 60 / 75 / 90 / 105% damage |
| Guns & Roses | 2 | Quest (x10): Hitting an enemy by exploding Romeo's Rose with a PERFECT SHOT grants +1 DMG<br>Complete: Rose explosions triggered with a PERFECT SHOT gain +50% range and deals +28 / 35 / 42 / 49% damage |
| Love Sparks | 3 | SPECIAL fires 4 / 5 / 6 / 7 homing projectiles towards nearby enemies, each one dealing 18.75 damage |
| Swirling Rose | 3 | ATTACKS hitting Romeo's Roses make them spin, dealing 60 / 75 / 100 / 115% of Juliet's ATTACK damage all around |
| Comforting Presence | 4 | Crossing through a Hero using DASH grants 20 / 25 / 30 / 35 SHIELD for 6 seconds to Juliet and all Heroes crossed |
| Knockout | 4 | When Juliet is very close to an enemy, ATTACK turns into a strike using her pistol's butt dealing 400 / 500 / 600 / 700% damage at close range without consuming AMMO (4 seconds cooldown) |
| Explosive Backstep | 5 | While holding POWER, using ATTACK makes Juliet step back and shoot to the ground, dealing 100 / 125 / 150 / 175% POWER’s damage in a zone |
| Wedding Gifts | 5 | Whenever they obtain a Magical Object, Juliet and Romeo have a 25 / 30 / 35 / 40%/12 / 15 / 17 / 19%/6 / 7 / 8 / 9% chance to gift the other the same common, rare or epic Magical Object |
| Blind Shots | 7 | DEFENSE fires 3 / 4 / 5 / 6 more shot(s) than the number of AMMO remaining |
| Heartbeat | 7 | Using TRAIT or receiving Romeo’s TRAIT triggers a sonic wave dealing 100 / 125 / 150 / 175 damage all around Juliet |
| Lucky Shot | 8 | ATTACKS have a 4 / 5 / 6 / 7% chance to turn into a POWER shot |
| Shrapnel | 8 | Using POWER also triggers a shrapnel burst dealing 40 / 50 / 60 / 70% damage in a cone |

## Outfits

| Outfit | How to unlock | Description |
|---|---|---|
| Signature Outfit | Completed ‘Kiss the Groom' Talent Quest | Unlocked by completing 'Kiss the Groom' Talent Quest |
| Traveler Outfit | Reached Chapter 3 | Unlocked by reaching Chapter 3 |
| Master Outfit | Completed the game in Darkness Difficulty | Unlocked by completing the game  in Darkness Difficulty |
| Hidden Outfit | Bull’s Eye | Hidden Requirements |
| Romance Outfit | Romance Skin Pack Acquired | Available in the Romance Skin Pack |
| Ravens Outfit |   |   |
| Nightmares Outfit |   |   |
| Eternal Love Outfit |   |   |
|   | Romeo & Juliet Skin Pack Acquired | Available in the Romeo & Juliet Skin Pack |


**How to read the text**

- **Bold** words are highlighted in the game.
- `{0}`, `{1}` and so on are numbers or names the game fills in while you play.

Source: [`Hero_Juliet_Common.LangEN.tsv`](../../data/Hero_Juliet_Common.LangEN.tsv), [`Hero_Juliet_Abilities.tsv`](../../data/Hero_Juliet_Abilities.tsv), [`Hero_Juliet_Talents.tsv`](../../data/Hero_Juliet_Talents.tsv), [`Hero_Juliet_Skins.LangEN.tsv`](../../data/Hero_Juliet_Skins.LangEN.tsv).
Game version: Game build 1.06 (Steam build ID 25174305); the displayed version string is unverified. See VERSION.json.

*This page is generated from the TSV files in [data/](../../data/) by `tools/build_browse.py`. Do not edit it by hand; fix the data and re-run the script.*
