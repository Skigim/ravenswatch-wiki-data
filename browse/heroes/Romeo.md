# Romeo

[All tables](../README.md)

[Abilities](#abilities) · [Ability values](#ability-values) · [Talents](#talents) · [Outfits](#outfits) · [Memoir](../memoirs/Romeo.md)

Awakening every day with no memories of the day before, Romeo still remembers that he is in love with Juliet who quickly informs him that they are intrepid agents of the Ravenswatch. Quick with his rapier and quicker with his verse, the legendary hero of clan Montague is most powerful when marrying his skills with his equally deadly paramour.

## Abilities

| Slot | Name | Description |
|---|---|---|
| Trait | Until death do us part | • **Passive:** If `{0}` definitely dies, `{1}` dies too<br>• **Active:** Consume Health equivalent to **`{2}`%** of Maximum Health to make `{0}` heal for **`{3}`%** of the amount (healing above Maximum Health is converted into **SHIELD**) |
| Attack | Rapier | • Chain together a series of attacks with the rapier, last attack deals **+`{0}`%** damage<br>• Whole combo deals a total of **`{2}`** damage<br>• Use **DASH** during or right after **ATTACK** to perform a dash attack dealing **`{1}`** damage |
| Power | Red Rose | • Hold then release to throw a Rose that deals damage along path, then stops to spin dealing area damage for **`{0}`** seconds<br>• The Rose can deal up to **`{1}`** damage in total <br>• `{2}` can use **POWER** to shoot the Rose and make it explode, dealing damage all around |
| Special | Passionate Kiss | • Call `{0}` during **`{1}`** seconds or answer `{0}`'s call<br>• Answering the call makes both heroes dash towards each other and kiss at half-distance dealing **`{2}`** area damage, then they move back in opposite directions |
| Defense | Deflect | • Perform an **INTANGIBLE** series of deflections, blocking any enemy attack<br>• **ATTACK** used during or right after **DEFENSE** triggers an **INTANGIBLE** **Ripost** launching a flurry of attacks, dealing up to **`{1}`** damage |
| Ultimate 1 | Wild Waltz | • `{2}` rushes towards `{0}` to perform an **INTANGIBLE** dance for **`{1}`** seconds<br>• Both Heroes influence moving direction during dance. The more identical the directions, the faster the movement<br>• Deal between **`{3}`** and **`{4}`** area damage per second (according to their movement speed) |
| Ultimate 2 | Black Roses | • Send **`{0}`** black Roses, piercing through enemies and dealing **`{1}`** damage each |

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
| Until death do us part (Paired) | active duration | *not decoded* | seconds | Not decoded |   |
| Until death do us part (Paired) | resource cost | *not decoded* | resource | Not decoded |   |

### Attack

| Name | Stat | Value | Unit | Status | In-game check |
|---|---|---|---|---|---|
| Rapier | final hit bonus | 200 | percent | Decoded |   |
| Rapier | full combo damage | *not decoded* | damage | Not decoded | Game shows 67 |
| Rapier | dash attack damage | 30 | damage | Decoded (baseline) |   |
| Rapier | hit count | *not decoded* | hits | Not decoded |   |
| Rapier | hit damage sequence | *not decoded* | damage | Not decoded |   |
| Rapier | attack timing | *not decoded* | seconds | Not decoded |   |

### Power

| Name | Stat | Value | Unit | Status | In-game check |
|---|---|---|---|---|---|
| Red Rose | cooldown | 7 | seconds | Decoded |   |
| Red Rose | charges | 1 | charges | Decoded (baseline) |   |
| Red Rose | spin duration | 3 | seconds | Decoded |   |
| Red Rose | max total damage | *not decoded* | damage | Not decoded | Second decoding pass: 70 |
| Red Rose | juliet explosion damage | 80 | damage | Decoded (baseline) |   |
| Red Rose | active duration | *not decoded* | seconds | Not decoded |   |
| Red Rose | resource cost | *not decoded* | resource | Not decoded |   |

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
| Deflect | cooldown | 6 | seconds | Decoded |   |
| Deflect | charges | 1 | charges | Decoded (baseline) |   |
| Deflect | riposte damage | *not decoded* | damage | Not decoded | Second decoding pass: 80 |
| Deflect | active duration | *not decoded* | seconds | Not decoded |   |
| Deflect | resource cost | *not decoded* | resource | Not decoded |   |
| Deflect | deflection window | *not decoded* | seconds | Not decoded |   |
| Deflect | followup window | 1 | seconds | Decoded |   |

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
| Black Roses | cooldown | *not decoded* | seconds | Not decoded | Game showed 75 on 1.05; changed in 1.06 |
| Black Roses | charges | 1 | charges | Decoded (baseline) |   |
| Black Roses | rose count | 42 | roses | Decoded |   |
| Black Roses | damage per rose | 13 | damage | Decoded (baseline) |   |
| Black Roses | active duration | *not decoded* | seconds | Not decoded |   |
| Black Roses | resource cost | *not decoded* | resource | Not decoded |   |

## Talents

Values separated by / are for Common / Rare / Epic / Legendary.

### Starting talents

Talents unlocked at rank 1, not counting ultimate upgrades.

| Talent | Effect |
|---|---|
| Burning Kiss | SPECIAL's area of effect gains +25% range, +40 / 50 / 60 / 70% damage and applies IGNITE to hit enemies |
| Floral Dodge | DEFENSE now creates a POWER Rose dealing 40 / 50 / 60 / 70% damage |
| Healing Rose | Every 2 times the POWER Rose hits an enemy, it restores 2 / 2.5 / 3 / 3.5 Health to all Heroes around |
| Kick | Adds a kick to ATTACK combo, dealing 48.4 / 60.5 / 72.6 / 84.7 damage and pushing light enemies back |
| Kiss the Bride | Quest (x20): Hitting at least one enemy with SPECIAL grants +0.5 Crit Chance<br>Complete: Any enemy hit by SPECIAL has a 40 / 50 / 60 / 70% chance to grant Romeo 2 Dream Shard(s) |
| Panache | Hitting an enemy with any additional ATTACK move, such as DASH attack or DEFENSE's Ripost, grants one Panache token (up to 3)<br>Each Panache token increases ATTACK damage by 20% and grants +4 / 5 / 6 / 7% ATTACK SPEED, all Panache tokens are lost when Romeo is hit |
| Relentless Assaults | ATTACK used right after POWER triggers DEFENSE's Ripost launching a flurry of attacks, dealing up to 11 damage |
| Surge of bravery | After SPECIAL's kiss, next 6 / 8 / 10 / 12 ATTACKS gain +30% range and deal +30% damage |
| Thorns Aura | After using TRAIT or receiving Juliet's TRAIT, an aura of thorns appears around Romeo, dealing 120 / 150 / 180 / 210 area damage per second for 6 seconds |
| Thorny Rose | When POWER Rose blooms, 5 paths of thorns spread around, dealing 40 / 50 / 60 / 70 damage per second to enemies crossing through |

### Ultimates

The talent tables do not include the base ultimates or their unlock ranks; this text is from the hero's text table.

| Ultimate | Description |
|---|---|
| Wild Waltz | • `{0}` rushes towards `{1}` to perform an **INTANGIBLE** dance dealing area damage |
| Black Roses | • Send **`{0}`** black Roses, piercing through enemies and dealing **`{1}`** damage each |

### Ultimate upgrades

| Talent | Upgrades | Unlocks at rank | Effect |
|---|---|---|---|
| Burning Dance | Wild Waltz | 1 | ULTIMATE applies IGNITE to hit enemies and deals +40 / 50 / 60 / 70% damage |
| Explosive Performance | Wild Waltz | 9 | During ULTIMATE's dance, launch 24 / 30 / 36 / 42 firework rockets all around, exploding on impact and dealing 17 damage each |
| Funeral Bouquet | Black Roses | 6 | ATTACKS throw ULTIMATE's Black Roses, dealing 3 / 3.75 / 4.5 / 5.25 damage each |
| Tempestuous Roses | Black Roses | 9 | Romeo throws 56 / 64 / 72 / 80 Black Roses in a wide cone dealing 13 damage each and is now surrounded by a tempest dealing 10 area damage per second |

### Other talents

| Talent | Unlocks at rank | Effect |
|---|---|---|
| Love Thread | 2 | Using TRAIT casts a beam towards Juliet for 6 second(s), dealing 265 / 330 / 395 / 460 damage per second to crossed enemies |
| Secret Weapon | 2 | Quest(x20): Blocking at least once during DEFENSE grants +0.5 DMG<br>Complete: Ripost ATTACK after DEFENSE deals +40 / 50 / 60 / 70% damage per successful block (up to 4 times) |
| Flash of Steel | 3 | Holding DASH during a dash attack makes Romeo rush back towards his starting location, dealing 120 / 150 / 180 / 210% damage on its path |
| Selfless Defender | 3 | Blocking at least one attack during DEFENSE grants 12 / 15 / 18 / 21 SHIELD for 8 second(s) to all Heroes around |
| Deadly Brambles | 4 | 4th strike of ATTACK combo implants brambles on enemies, dealing 40 / 50 / 60 / 70 damage over 5 seconds<br>Brambles explode when Romeo implants again on affected enemy or on enemy death, dealing 200 / 250 / 300 / 350% area damage |
| Fencing Reflex | 4 | Basic ATTACKS can turn into a block when Romeo gets hit (every 5 seconds max)<br>After it blocks, Romeo gains +40 / 50 / 60 / 70% Crit Chance for 4 second(s) |
| Ice Rose | 5 | POWER now throws ice Roses, applying CHILLED to hit enemies<br>POWER deals +32 / 40 / 48 / 56% damage |
| Swarm of Petals | 5 | Using POWER also launches a swarm of petals in a cone, pushing back light enemies and dealing 40 / 50 / 60 / 70% damage |
| Broad Stroke | 7 | ATTACK used right after DASH triggers a broad stroke, dealing 400 / 500 / 600 / 700% damage all around |
| Wind Spiral | 7 | DEFENSE creates a wind spiral around Romeo dealing up to 60 / 75 / 90 / 105 area damage |
| Bursting Bloom | 8 | When POWER Rose blooms, trigger a burst of petals dealing 40 / 50 / 60 / 70% area damage |
| Love Shield | 8 | After SPECIAL's kiss, Romeo and Juliet are surrounded by a Love Shield, making them INVINCIBLE for 4 seconds (every 14 / 12 / 10 / 8 seconds max) |

## Outfits

| Outfit | How to unlock | Description |
|---|---|---|
| Signature Outfit | Completed ‘Kiss the Bride' Talent Quest | Unlocked by completing 'Kiss the Bride' Talent Quest |
| Traveler Outfit | Reached Chapter 3 | Unlocked by reaching Chapter 3 |
| Master Outfit | Completed the game in Darkness Difficulty | Unlocked by completing the game  in Darkness Difficulty |
| Hidden Outfit | Untouchable Duelist | Hidden Requirements |
| Romance Outfit | Romance Skin Pack Acquired | Available in the Romance Skin Pack |
| Ravens Outfit |   |   |
| Nightmares Outfit |   |   |
| Eternal Love Outfit |   |   |
|   | Romeo & Juliet Skin Pack Acquired | Available in the Romeo & Juliet Skin Pack |


**How to read the text**

- **Bold** words are highlighted in the game.
- `{0}`, `{1}` and so on are numbers or names the game fills in while you play.

Source: [`Hero_Romeo_Common.LangEN.tsv`](../../data/Hero_Romeo_Common.LangEN.tsv), [`Hero_Romeo_Abilities.tsv`](../../data/Hero_Romeo_Abilities.tsv), [`Hero_Romeo_Talents.tsv`](../../data/Hero_Romeo_Talents.tsv), [`Hero_Romeo_Skins.LangEN.tsv`](../../data/Hero_Romeo_Skins.LangEN.tsv).
Game version: Game build 1.06 (Steam build ID 25174305); the displayed version string is unverified. See VERSION.json.

*This page is generated from the TSV files in [data/](../../data/) by `tools/build_browse.py`. Do not edit it by hand; fix the data and re-run the script.*
