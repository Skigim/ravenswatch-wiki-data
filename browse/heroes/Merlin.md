# Merlin

[All tables](../README.md)

[Abilities](#abilities) · [Ability values](#ability-values) · [Talents](#talents) · [Outfits](#outfits) · [Memoir](../memoirs/Merlin.md)

Merlin's mysterious release from his eternal prison cell has him now using his wizardly magic to obliterate the darkness clouding both Reverie and his own mind. Bereft of his powers of prophecy, he relies on his druidly elemental powers to clear the world of monsters and find the missing Lady of the Lake.

## Abilities

| Slot | Name | Description |
|---|---|---|
| Trait | Celestial Potency | • **Passive:** `{0}` can conjure runes of **POTENCY** (up to **`{1}`**) that are consumed by his next Spell to enhance its effects<br>• **Active:** `{0}` briefly turns **INTANGIBLE** and instantly conjures the maximum amount of runes of **POTENCY** |
| Attack | Magic Strikes | • Chains a series of magic strikes, dealing a total of **`{0}`** damage<br>• The final attack conjures a rune of **POTENCY** provided it hits at least one enemy |
| Power | Nature Spells | • Prepares a **Nature Spell**, to be cast as the next Ability used:<br>• **POWER:** `{0}`<br>• **SPECIAL:** `{1}`<br>• **DEFENSE:** `{2}`<br>• Using **CONTEXTUAL ACTION** will cancel this preparation action |
| Power Power | Giant Brambles | • Causes two giant brambles to grow and hit one another, dealing **`{0}`** damage |
| Power Special | Starfall | • Causes stars to fall from the sky on up to **`{0}`** nearby enemies, with each one dealing **`{1}`** damage |
| Power Defense | Stone Shield | • `{0}` surrounds himself with stones to **BLOCK** any incoming damage<br>• Stones deal **`{1}`** damage per second then explode after a short duration, dealing **`{2}`** damage all around |
| Special | Arcane Spells | • Prepares an **Arcane Spell**, to be cast as the next Ability used:<br>• **POWER:** `{0}`<br>• **SPECIAL:** `{1}`<br>• **DEFENSE:** `{2}`<br>• Using **CONTEXTUAL ACTION** will cancel this preparation action |
| Special Power | Fork of Lightning | • Channels a lightning attack for up to **`{0}`** seconds, dealing **`{1}`** damage per second to all enemies passed through |
| Special Special | Fireball | • Launches a fireball that explodes on contact or after a small delay, dealing **`{0}`** area damage each and applying **IGNITE** to enemies hit<br>• Damage increases based on distance traveled, up to a maximum of **+`{1}`%** |
| Special Defense | Frost Orb | • Sends out a Frost Orb that tracks nearby enemies for **`{0}`** seconds<br>• The orb deals **`{1}`** damage every **`{2}`** seconds and applies **CHILLED** to enemies hit |
| Defense | Sacred Spells | • Prepares a **Sacred Spell**, to be cast as the next Ability used:<br>• **POWER:** `{0}`<br>• **SPECIAL:** `{1}`<br>• **DEFENSE:** `{2}`<br>• Using **CONTEXTUAL ACTION** will cancel this preparation action |
| Defense Power | Blessing | • Grants **REGENERATION** **+`{0}`** to the most heavily wounded nearby Hero |
| Defense Special | Light Nova | • Unleashes a burst of light, stunning enemies or inflicting **`{0}`** points of stagger to them<br>• If the burst hits at least one enemy, it also applies a **`{1}`** **SHIELD** to all nearby Heroes for **`{2}`** seconds |
| Defense Defense | Blink | • `{0}` turns **INTANGIBLE** and quickly teleports forward at a medium range<br>• Does not consume runes of **POTENCY** |
| Ultimate 1 | Standing Stone | • Pulls a standing stone out of the ground, drawing the attention of enemies<br>• The stone passively loses health and explodes when this reaches zero, dealing **`{0}`** area damage |
| Ultimate 2 | Forbidden Spells | • Prepares a **Forbidden Spell**, to be cast as the next Ability used:<br>• **POWER:** `{0}`<br>• **SPECIAL:** `{1}`<br>• **DEFENSE:** `{2}`<br>• Using **CONTEXTUAL ACTION** will cancel this preparation action |
| Ultimate 2 Power | Cataclysm | • Summons a meteorite from the sky, the impact area of which can be moved around for a short time before it hits<br>• The meteorite then strikes the targeted location, dealing **`{0}`** damage in a large area surrounding it |
| Ultimate 2 Special | Unholy Strikes | • The next **`{0}`** **ATTACKS** send out a corrupted projectile, piercing through enemies and dealing **`{1}`** damage<br>• Each one that hits at least one enemy conjures a rune of **POTENCY** |
| Ultimate 2 Defense | Blood Ritual | • Sacrifices health equivalent to **`{0}`%** of maximum health, resulting in other nearby Heroes being revived and healed for **`{1}`%** of the amount of health lost<br>• Nearby enemies take damage equivalent to **`{2}`** times the amount of health lost |

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
| Celestial Potency | max potency runes | 3 | runes | Decoded (baseline) |   |
| Celestial Potency | enhancement per rune | *not decoded* | percent | Not decoded |   |
| Celestial Potency (Base; Second Ability Selected Selector{\[State\] Hero\_Merlin\\Ability Primary/Primary Primary\\State Ability Primary Primary =\> 1; \[State\] Hero\_Merlin\\Ability Primary/Primary Secondary\\State Ability Primary Secondary =\> 2; \[State\] Hero\_Merlin\\Ability Primary/Primary Defense\\State Ability Primary Defense =\> 3; \[State\] Hero\_Merlin\\Ability Secondary/Secondary Primary\\State Ability Secondary Primary =\> 1; \[State\] Hero\_Merlin\\Ability Secondary/Secondary Secondary\\State Ability Secondary Secondary =\> 2; \[State\] Hero\_Merlin\\Ability Secondary/Secondary Defense\\State Ability Secondary Defense =\> 3; \[State\] Hero\_Merlin\\Ability Defense/Defense Primary\\State Ability Defense Primary =\> 1; \[State\] Hero\_Merlin\\Ability Defense/Defense Secondary\\State Ability Defense Secondary =\> 2; \[State\] Hero\_Merlin\\Ability Defense/Defense Defense\\State Ability Defense Defense =\> 3; \[State\] Hero\_Merlin\\Ability Ultimate 2/Ultimate 2 Primary\\State Ability Ultimate 2 Primary =\> 1; \[State\] Hero\_Merlin\\Ability Ultimate 2/Ultimate 2 Secondary\\State Ability Ultimate 2 Secondary =\> 2; \[State\] Hero\_Merlin\\Ability Ultimate 2/Ultimate 2 Defense\\State Ability Ultimate 2 Defense =\> 3; True =\> 0}=0) | cooldown | 0 | seconds | Decoded |   |
| Celestial Potency (Base; Second Ability Selected Selector{\[State\] Hero\_Merlin\\Ability Primary/Primary Primary\\State Ability Primary Primary =\> 1; \[State\] Hero\_Merlin\\Ability Primary/Primary Secondary\\State Ability Primary Secondary =\> 2; \[State\] Hero\_Merlin\\Ability Primary/Primary Defense\\State Ability Primary Defense =\> 3; \[State\] Hero\_Merlin\\Ability Secondary/Secondary Primary\\State Ability Secondary Primary =\> 1; \[State\] Hero\_Merlin\\Ability Secondary/Secondary Secondary\\State Ability Secondary Secondary =\> 2; \[State\] Hero\_Merlin\\Ability Secondary/Secondary Defense\\State Ability Secondary Defense =\> 3; \[State\] Hero\_Merlin\\Ability Defense/Defense Primary\\State Ability Defense Primary =\> 1; \[State\] Hero\_Merlin\\Ability Defense/Defense Secondary\\State Ability Defense Secondary =\> 2; \[State\] Hero\_Merlin\\Ability Defense/Defense Defense\\State Ability Defense Defense =\> 3; \[State\] Hero\_Merlin\\Ability Ultimate 2/Ultimate 2 Primary\\State Ability Ultimate 2 Primary =\> 1; \[State\] Hero\_Merlin\\Ability Ultimate 2/Ultimate 2 Secondary\\State Ability Ultimate 2 Secondary =\> 2; \[State\] Hero\_Merlin\\Ability Ultimate 2/Ultimate 2 Defense\\State Ability Ultimate 2 Defense =\> 3; True =\> 0}=1) | cooldown | 8 | seconds | Decoded |   |
| Celestial Potency (Base; Second Ability Selected Selector{\[State\] Hero\_Merlin\\Ability Primary/Primary Primary\\State Ability Primary Primary =\> 1; \[State\] Hero\_Merlin\\Ability Primary/Primary Secondary\\State Ability Primary Secondary =\> 2; \[State\] Hero\_Merlin\\Ability Primary/Primary Defense\\State Ability Primary Defense =\> 3; \[State\] Hero\_Merlin\\Ability Secondary/Secondary Primary\\State Ability Secondary Primary =\> 1; \[State\] Hero\_Merlin\\Ability Secondary/Secondary Secondary\\State Ability Secondary Secondary =\> 2; \[State\] Hero\_Merlin\\Ability Secondary/Secondary Defense\\State Ability Secondary Defense =\> 3; \[State\] Hero\_Merlin\\Ability Defense/Defense Primary\\State Ability Defense Primary =\> 1; \[State\] Hero\_Merlin\\Ability Defense/Defense Secondary\\State Ability Defense Secondary =\> 2; \[State\] Hero\_Merlin\\Ability Defense/Defense Defense\\State Ability Defense Defense =\> 3; \[State\] Hero\_Merlin\\Ability Ultimate 2/Ultimate 2 Primary\\State Ability Ultimate 2 Primary =\> 1; \[State\] Hero\_Merlin\\Ability Ultimate 2/Ultimate 2 Secondary\\State Ability Ultimate 2 Secondary =\> 2; \[State\] Hero\_Merlin\\Ability Ultimate 2/Ultimate 2 Defense\\State Ability Ultimate 2 Defense =\> 3; True =\> 0}=2) | cooldown | 8 | seconds | Decoded |   |
| Celestial Potency (Base; Second Ability Selected Selector{\[State\] Hero\_Merlin\\Ability Primary/Primary Primary\\State Ability Primary Primary =\> 1; \[State\] Hero\_Merlin\\Ability Primary/Primary Secondary\\State Ability Primary Secondary =\> 2; \[State\] Hero\_Merlin\\Ability Primary/Primary Defense\\State Ability Primary Defense =\> 3; \[State\] Hero\_Merlin\\Ability Secondary/Secondary Primary\\State Ability Secondary Primary =\> 1; \[State\] Hero\_Merlin\\Ability Secondary/Secondary Secondary\\State Ability Secondary Secondary =\> 2; \[State\] Hero\_Merlin\\Ability Secondary/Secondary Defense\\State Ability Secondary Defense =\> 3; \[State\] Hero\_Merlin\\Ability Defense/Defense Primary\\State Ability Defense Primary =\> 1; \[State\] Hero\_Merlin\\Ability Defense/Defense Secondary\\State Ability Defense Secondary =\> 2; \[State\] Hero\_Merlin\\Ability Defense/Defense Defense\\State Ability Defense Defense =\> 3; \[State\] Hero\_Merlin\\Ability Ultimate 2/Ultimate 2 Primary\\State Ability Ultimate 2 Primary =\> 1; \[State\] Hero\_Merlin\\Ability Ultimate 2/Ultimate 2 Secondary\\State Ability Ultimate 2 Secondary =\> 2; \[State\] Hero\_Merlin\\Ability Ultimate 2/Ultimate 2 Defense\\State Ability Ultimate 2 Defense =\> 3; True =\> 0}=3) | cooldown | 8 | seconds | Decoded |   |
| Celestial Potency | charges | 1 | charges | Decoded (baseline) |   |
| Celestial Potency | active duration | *not decoded* | seconds | Not decoded |   |
| Celestial Potency | resource cost | *not decoded* | resource | Not decoded |   |
| Celestial Potency | intangible duration | *not decoded* | seconds | Not decoded |   |

### Attack

| Name | Stat | Value | Unit | Status | In-game check |
|---|---|---|---|---|---|
| Magic Strikes | full combo damage | *not decoded* | damage | Not decoded | Second decoding pass: 56 |
| Magic Strikes | hit count | *not decoded* | hits | Not decoded |   |
| Magic Strikes | hit damage sequence | *not decoded* | damage | Not decoded |   |
| Magic Strikes | attack timing | *not decoded* | seconds | Not decoded |   |

### Power / Prep

| Name | Stat | Value | Unit | Status | In-game check |
|---|---|---|---|---|---|
| Nature Spells | prepared spells | Giant Brambles / Starfall / Stone Shield |   | Fixed text |   |
| Nature Spells (Base; Second Ability Selected Selector{\[State\] Hero\_Merlin\\Ability Primary/Primary Primary\\State Ability Primary Primary =\> 1; \[State\] Hero\_Merlin\\Ability Primary/Primary Secondary\\State Ability Primary Secondary =\> 2; \[State\] Hero\_Merlin\\Ability Primary/Primary Defense\\State Ability Primary Defense =\> 3; \[State\] Hero\_Merlin\\Ability Secondary/Secondary Primary\\State Ability Secondary Primary =\> 1; \[State\] Hero\_Merlin\\Ability Secondary/Secondary Secondary\\State Ability Secondary Secondary =\> 2; \[State\] Hero\_Merlin\\Ability Secondary/Secondary Defense\\State Ability Secondary Defense =\> 3; \[State\] Hero\_Merlin\\Ability Defense/Defense Primary\\State Ability Defense Primary =\> 1; \[State\] Hero\_Merlin\\Ability Defense/Defense Secondary\\State Ability Defense Secondary =\> 2; \[State\] Hero\_Merlin\\Ability Defense/Defense Defense\\State Ability Defense Defense =\> 3; \[State\] Hero\_Merlin\\Ability Ultimate 2/Ultimate 2 Primary\\State Ability Ultimate 2 Primary =\> 1; \[State\] Hero\_Merlin\\Ability Ultimate 2/Ultimate 2 Secondary\\State Ability Ultimate 2 Secondary =\> 2; \[State\] Hero\_Merlin\\Ability Ultimate 2/Ultimate 2 Defense\\State Ability Ultimate 2 Defense =\> 3; True =\> 0}=0) | cooldown | 0 | seconds | Decoded |   |
| Nature Spells (Base; Second Ability Selected Selector{\[State\] Hero\_Merlin\\Ability Primary/Primary Primary\\State Ability Primary Primary =\> 1; \[State\] Hero\_Merlin\\Ability Primary/Primary Secondary\\State Ability Primary Secondary =\> 2; \[State\] Hero\_Merlin\\Ability Primary/Primary Defense\\State Ability Primary Defense =\> 3; \[State\] Hero\_Merlin\\Ability Secondary/Secondary Primary\\State Ability Secondary Primary =\> 1; \[State\] Hero\_Merlin\\Ability Secondary/Secondary Secondary\\State Ability Secondary Secondary =\> 2; \[State\] Hero\_Merlin\\Ability Secondary/Secondary Defense\\State Ability Secondary Defense =\> 3; \[State\] Hero\_Merlin\\Ability Defense/Defense Primary\\State Ability Defense Primary =\> 1; \[State\] Hero\_Merlin\\Ability Defense/Defense Secondary\\State Ability Defense Secondary =\> 2; \[State\] Hero\_Merlin\\Ability Defense/Defense Defense\\State Ability Defense Defense =\> 3; \[State\] Hero\_Merlin\\Ability Ultimate 2/Ultimate 2 Primary\\State Ability Ultimate 2 Primary =\> 1; \[State\] Hero\_Merlin\\Ability Ultimate 2/Ultimate 2 Secondary\\State Ability Ultimate 2 Secondary =\> 2; \[State\] Hero\_Merlin\\Ability Ultimate 2/Ultimate 2 Defense\\State Ability Ultimate 2 Defense =\> 3; True =\> 0}=1) | cooldown | 8 | seconds | Decoded |   |
| Nature Spells (Base; Second Ability Selected Selector{\[State\] Hero\_Merlin\\Ability Primary/Primary Primary\\State Ability Primary Primary =\> 1; \[State\] Hero\_Merlin\\Ability Primary/Primary Secondary\\State Ability Primary Secondary =\> 2; \[State\] Hero\_Merlin\\Ability Primary/Primary Defense\\State Ability Primary Defense =\> 3; \[State\] Hero\_Merlin\\Ability Secondary/Secondary Primary\\State Ability Secondary Primary =\> 1; \[State\] Hero\_Merlin\\Ability Secondary/Secondary Secondary\\State Ability Secondary Secondary =\> 2; \[State\] Hero\_Merlin\\Ability Secondary/Secondary Defense\\State Ability Secondary Defense =\> 3; \[State\] Hero\_Merlin\\Ability Defense/Defense Primary\\State Ability Defense Primary =\> 1; \[State\] Hero\_Merlin\\Ability Defense/Defense Secondary\\State Ability Defense Secondary =\> 2; \[State\] Hero\_Merlin\\Ability Defense/Defense Defense\\State Ability Defense Defense =\> 3; \[State\] Hero\_Merlin\\Ability Ultimate 2/Ultimate 2 Primary\\State Ability Ultimate 2 Primary =\> 1; \[State\] Hero\_Merlin\\Ability Ultimate 2/Ultimate 2 Secondary\\State Ability Ultimate 2 Secondary =\> 2; \[State\] Hero\_Merlin\\Ability Ultimate 2/Ultimate 2 Defense\\State Ability Ultimate 2 Defense =\> 3; True =\> 0}=2) | cooldown | 8 | seconds | Decoded |   |
| Nature Spells (Base; Second Ability Selected Selector{\[State\] Hero\_Merlin\\Ability Primary/Primary Primary\\State Ability Primary Primary =\> 1; \[State\] Hero\_Merlin\\Ability Primary/Primary Secondary\\State Ability Primary Secondary =\> 2; \[State\] Hero\_Merlin\\Ability Primary/Primary Defense\\State Ability Primary Defense =\> 3; \[State\] Hero\_Merlin\\Ability Secondary/Secondary Primary\\State Ability Secondary Primary =\> 1; \[State\] Hero\_Merlin\\Ability Secondary/Secondary Secondary\\State Ability Secondary Secondary =\> 2; \[State\] Hero\_Merlin\\Ability Secondary/Secondary Defense\\State Ability Secondary Defense =\> 3; \[State\] Hero\_Merlin\\Ability Defense/Defense Primary\\State Ability Defense Primary =\> 1; \[State\] Hero\_Merlin\\Ability Defense/Defense Secondary\\State Ability Defense Secondary =\> 2; \[State\] Hero\_Merlin\\Ability Defense/Defense Defense\\State Ability Defense Defense =\> 3; \[State\] Hero\_Merlin\\Ability Ultimate 2/Ultimate 2 Primary\\State Ability Ultimate 2 Primary =\> 1; \[State\] Hero\_Merlin\\Ability Ultimate 2/Ultimate 2 Secondary\\State Ability Ultimate 2 Secondary =\> 2; \[State\] Hero\_Merlin\\Ability Ultimate 2/Ultimate 2 Defense\\State Ability Ultimate 2 Defense =\> 3; True =\> 0}=3) | cooldown | 8 | seconds | Decoded |   |
| Nature Spells | charges | 1 | charges | Decoded (baseline) |   |
| Nature Spells | active duration | *not decoded* | seconds | Not decoded |   |
| Nature Spells | resource cost | *not decoded* | resource | Not decoded |   |

### Power / Nature

| Name | Stat | Value | Unit | Status | In-game check |
|---|---|---|---|---|---|
| Giant Brambles | damage | *not decoded* | damage | Not decoded | Second decoding pass: 50 |
| Giant Brambles | active duration | *not decoded* | seconds | Not decoded |   |
| Giant Brambles | resource cost | *not decoded* | resource | Not decoded |   |
| Giant Brambles | cooldown | 0.5 | seconds | Decoded |   |
| Giant Brambles | charges | 1 | charges | Decoded |   |

### Special / Nature

| Name | Stat | Value | Unit | Status | In-game check |
|---|---|---|---|---|---|
| Starfall (Base; Potency Counter.0x1163b1e9=0) | targets by potency | 3 | targets | Decoded |   |
| Starfall (Base; Potency Counter.0x1163b1e9=1) | targets by potency | 4 | targets | Decoded |   |
| Starfall (Base; Potency Counter.0x1163b1e9=2) | targets by potency | 5 | targets | Decoded |   |
| Starfall (Base; Potency Counter.0x1163b1e9=3) | targets by potency | 6 | targets | Decoded |   |
| Starfall (Base; Potency Counter.0x1163b1e9=0) | damage per star by potency | 70 | damage | Decoded (baseline) |   |
| Starfall (Base; Potency Counter.0x1163b1e9=1) | damage per star by potency | 105 | damage | Decoded (baseline) |   |
| Starfall (Base; Potency Counter.0x1163b1e9=2) | damage per star by potency | 126 | damage | Decoded (baseline) |   |
| Starfall (Base; Potency Counter.0x1163b1e9=3) | damage per star by potency | 140 | damage | Decoded (baseline) |   |
| Starfall | active duration | *not decoded* | seconds | Not decoded |   |
| Starfall | resource cost | *not decoded* | resource | Not decoded |   |
| Starfall | cooldown | 0.5 | seconds | Decoded |   |
| Starfall | charges | 1 | charges | Decoded |   |

### Defense / Nature

| Name | Stat | Value | Unit | Status | In-game check |
|---|---|---|---|---|---|
| Stone Shield | explosion delay | *not decoded* | seconds | Not decoded |   |
| Stone Shield | explosion damage | *not decoded* | damage | Not decoded | Second decoding pass: 30 |
| Stone Shield | active duration | *not decoded* | seconds | Not decoded |   |
| Stone Shield | resource cost | *not decoded* | resource | Not decoded |   |
| Stone Shield | damage per second | *not decoded* | damage per second | Not decoded | Second decoding pass: 10 |
| Stone Shield | cooldown | 0.5 | seconds | Decoded |   |
| Stone Shield | charges | 1 | charges | Decoded |   |

### Special / Prep

| Name | Stat | Value | Unit | Status | In-game check |
|---|---|---|---|---|---|
| Arcane Spells | cooldown | 30 | seconds | Decoded |   |
| Arcane Spells | charges | 1 | charges | Decoded (baseline) |   |
| Arcane Spells | active duration | *not decoded* | seconds | Not decoded |   |
| Arcane Spells | resource cost | *not decoded* | resource | Not decoded |   |

### Power / Arcane

| Name | Stat | Value | Unit | Status | In-game check |
|---|---|---|---|---|---|
| Fork of Lightning | max channel duration | 2 | seconds | Decoded |   |
| Fork of Lightning | damage per second | *not decoded* | damage per second | Not decoded | Second decoding pass: 55 |
| Fork of Lightning | resource cost | *not decoded* | resource | Not decoded |   |
| Fork of Lightning | cooldown | 0.5 | seconds | Decoded |   |
| Fork of Lightning | charges | 1 | charges | Decoded |   |
| Fork of Lightning | active duration | 2 | seconds | Decoded |   |

### Special / Arcane

| Name | Stat | Value | Unit | Status | In-game check |
|---|---|---|---|---|---|
| Fireball (Base; Potency Counter.0x1163b1e9=0) | base damage | 36 | damage | Decoded (baseline) |   |
| Fireball (Base; Potency Counter.0x1163b1e9=1) | base damage | 57.6 | damage | Decoded (baseline) |   |
| Fireball (Base; Potency Counter.0x1163b1e9=2) | base damage | 77.14 | damage | Decoded (baseline) |   |
| Fireball (Base; Potency Counter.0x1163b1e9=3) | base damage | 96 | damage | Decoded (baseline) |   |
| Fireball (Base; Potency Counter.0x1163b1e9=0) | maximum distance damage increase | 100 | percent | Decoded |   |
| Fireball (Base; Potency Counter.0x1163b1e9=1) | maximum distance damage increase | 150 | percent | Decoded |   |
| Fireball (Base; Potency Counter.0x1163b1e9=2) | maximum distance damage increase | 180 | percent | Decoded |   |
| Fireball (Base; Potency Counter.0x1163b1e9=3) | maximum distance damage increase | 200 | percent | Decoded |   |
| Fireball | active duration | *not decoded* | seconds | Not decoded |   |
| Fireball | resource cost | *not decoded* | resource | Not decoded |   |
| Fireball | distance damage formula | *not decoded* |   | Not decoded |   |
| Fireball | automatic explosion delay | *not decoded* | seconds | Not decoded |   |
| Fireball | cooldown | 0.5 | seconds | Decoded |   |
| Fireball | charges | 1 | charges | Decoded |   |

### Defense / Arcane

| Name | Stat | Value | Unit | Status | In-game check |
|---|---|---|---|---|---|
| Frost Orb (Base; Potency Counter.0x1163b1e9=0) | lifetime | 6 | seconds | Decoded |   |
| Frost Orb (Base; Potency Counter.0x1163b1e9=1) | lifetime | 8 | seconds | Decoded |   |
| Frost Orb (Base; Potency Counter.0x1163b1e9=2) | lifetime | 10 | seconds | Decoded |   |
| Frost Orb (Base; Potency Counter.0x1163b1e9=3) | lifetime | 12 | seconds | Decoded |   |
| Frost Orb | damage per tick | *not decoded* | damage | Not decoded | Second decoding pass: 30 |
| Frost Orb | tick interval | 2 | seconds | Decoded |   |
| Frost Orb | active duration | *not decoded* | seconds | Not decoded |   |
| Frost Orb | resource cost | *not decoded* | resource | Not decoded |   |
| Frost Orb | cooldown | 0.5 | seconds | Decoded |   |
| Frost Orb | charges | 1 | charges | Decoded |   |

### Defense / Prep

| Name | Stat | Value | Unit | Status | In-game check |
|---|---|---|---|---|---|
| Sacred Spells | prepared spells | Blessing / Light Nova / Blink |   | Fixed text |   |
| Sacred Spells (Base; Second Ability Selected Selector{\[State\] Hero\_Merlin\\Ability Primary/Primary Primary\\State Ability Primary Primary =\> 1; \[State\] Hero\_Merlin\\Ability Primary/Primary Secondary\\State Ability Primary Secondary =\> 2; \[State\] Hero\_Merlin\\Ability Primary/Primary Defense\\State Ability Primary Defense =\> 3; \[State\] Hero\_Merlin\\Ability Secondary/Secondary Primary\\State Ability Secondary Primary =\> 1; \[State\] Hero\_Merlin\\Ability Secondary/Secondary Secondary\\State Ability Secondary Secondary =\> 2; \[State\] Hero\_Merlin\\Ability Secondary/Secondary Defense\\State Ability Secondary Defense =\> 3; \[State\] Hero\_Merlin\\Ability Defense/Defense Primary\\State Ability Defense Primary =\> 1; \[State\] Hero\_Merlin\\Ability Defense/Defense Secondary\\State Ability Defense Secondary =\> 2; \[State\] Hero\_Merlin\\Ability Defense/Defense Defense\\State Ability Defense Defense =\> 3; \[State\] Hero\_Merlin\\Ability Ultimate 2/Ultimate 2 Primary\\State Ability Ultimate 2 Primary =\> 1; \[State\] Hero\_Merlin\\Ability Ultimate 2/Ultimate 2 Secondary\\State Ability Ultimate 2 Secondary =\> 2; \[State\] Hero\_Merlin\\Ability Ultimate 2/Ultimate 2 Defense\\State Ability Ultimate 2 Defense =\> 3; True =\> 0}=0) | cooldown | 0 | seconds | Decoded |   |
| Sacred Spells (Base; Second Ability Selected Selector{\[State\] Hero\_Merlin\\Ability Primary/Primary Primary\\State Ability Primary Primary =\> 1; \[State\] Hero\_Merlin\\Ability Primary/Primary Secondary\\State Ability Primary Secondary =\> 2; \[State\] Hero\_Merlin\\Ability Primary/Primary Defense\\State Ability Primary Defense =\> 3; \[State\] Hero\_Merlin\\Ability Secondary/Secondary Primary\\State Ability Secondary Primary =\> 1; \[State\] Hero\_Merlin\\Ability Secondary/Secondary Secondary\\State Ability Secondary Secondary =\> 2; \[State\] Hero\_Merlin\\Ability Secondary/Secondary Defense\\State Ability Secondary Defense =\> 3; \[State\] Hero\_Merlin\\Ability Defense/Defense Primary\\State Ability Defense Primary =\> 1; \[State\] Hero\_Merlin\\Ability Defense/Defense Secondary\\State Ability Defense Secondary =\> 2; \[State\] Hero\_Merlin\\Ability Defense/Defense Defense\\State Ability Defense Defense =\> 3; \[State\] Hero\_Merlin\\Ability Ultimate 2/Ultimate 2 Primary\\State Ability Ultimate 2 Primary =\> 1; \[State\] Hero\_Merlin\\Ability Ultimate 2/Ultimate 2 Secondary\\State Ability Ultimate 2 Secondary =\> 2; \[State\] Hero\_Merlin\\Ability Ultimate 2/Ultimate 2 Defense\\State Ability Ultimate 2 Defense =\> 3; True =\> 0}=1) | cooldown | 8 | seconds | Decoded |   |
| Sacred Spells (Base; Second Ability Selected Selector{\[State\] Hero\_Merlin\\Ability Primary/Primary Primary\\State Ability Primary Primary =\> 1; \[State\] Hero\_Merlin\\Ability Primary/Primary Secondary\\State Ability Primary Secondary =\> 2; \[State\] Hero\_Merlin\\Ability Primary/Primary Defense\\State Ability Primary Defense =\> 3; \[State\] Hero\_Merlin\\Ability Secondary/Secondary Primary\\State Ability Secondary Primary =\> 1; \[State\] Hero\_Merlin\\Ability Secondary/Secondary Secondary\\State Ability Secondary Secondary =\> 2; \[State\] Hero\_Merlin\\Ability Secondary/Secondary Defense\\State Ability Secondary Defense =\> 3; \[State\] Hero\_Merlin\\Ability Defense/Defense Primary\\State Ability Defense Primary =\> 1; \[State\] Hero\_Merlin\\Ability Defense/Defense Secondary\\State Ability Defense Secondary =\> 2; \[State\] Hero\_Merlin\\Ability Defense/Defense Defense\\State Ability Defense Defense =\> 3; \[State\] Hero\_Merlin\\Ability Ultimate 2/Ultimate 2 Primary\\State Ability Ultimate 2 Primary =\> 1; \[State\] Hero\_Merlin\\Ability Ultimate 2/Ultimate 2 Secondary\\State Ability Ultimate 2 Secondary =\> 2; \[State\] Hero\_Merlin\\Ability Ultimate 2/Ultimate 2 Defense\\State Ability Ultimate 2 Defense =\> 3; True =\> 0}=2) | cooldown | 8 | seconds | Decoded |   |
| Sacred Spells (Base; Second Ability Selected Selector{\[State\] Hero\_Merlin\\Ability Primary/Primary Primary\\State Ability Primary Primary =\> 1; \[State\] Hero\_Merlin\\Ability Primary/Primary Secondary\\State Ability Primary Secondary =\> 2; \[State\] Hero\_Merlin\\Ability Primary/Primary Defense\\State Ability Primary Defense =\> 3; \[State\] Hero\_Merlin\\Ability Secondary/Secondary Primary\\State Ability Secondary Primary =\> 1; \[State\] Hero\_Merlin\\Ability Secondary/Secondary Secondary\\State Ability Secondary Secondary =\> 2; \[State\] Hero\_Merlin\\Ability Secondary/Secondary Defense\\State Ability Secondary Defense =\> 3; \[State\] Hero\_Merlin\\Ability Defense/Defense Primary\\State Ability Defense Primary =\> 1; \[State\] Hero\_Merlin\\Ability Defense/Defense Secondary\\State Ability Defense Secondary =\> 2; \[State\] Hero\_Merlin\\Ability Defense/Defense Defense\\State Ability Defense Defense =\> 3; \[State\] Hero\_Merlin\\Ability Ultimate 2/Ultimate 2 Primary\\State Ability Ultimate 2 Primary =\> 1; \[State\] Hero\_Merlin\\Ability Ultimate 2/Ultimate 2 Secondary\\State Ability Ultimate 2 Secondary =\> 2; \[State\] Hero\_Merlin\\Ability Ultimate 2/Ultimate 2 Defense\\State Ability Ultimate 2 Defense =\> 3; True =\> 0}=3) | cooldown | 8 | seconds | Decoded |   |
| Sacred Spells | charges | 1 | charges | Decoded (baseline) |   |
| Sacred Spells | active duration | *not decoded* | seconds | Not decoded |   |
| Sacred Spells | resource cost | *not decoded* | resource | Not decoded |   |

### Power / Sacred

| Name | Stat | Value | Unit | Status | In-game check |
|---|---|---|---|---|---|
| Blessing | regeneration amount | *not decoded* | regeneration | Not decoded | Second decoding pass: 2 |
| Blessing | active duration | *not decoded* | seconds | Not decoded |   |
| Blessing | resource cost | *not decoded* | resource | Not decoded |   |
| Blessing | regeneration duration | *not decoded* | seconds | Not decoded |   |
| Blessing | regeneration tick rule | *not decoded* |   | Not decoded |   |
| Blessing | cooldown | 0.5 | seconds | Decoded |   |
| Blessing | charges | 1 | charges | Decoded |   |

### Special / Sacred

| Name | Stat | Value | Unit | Status | In-game check |
|---|---|---|---|---|---|
| Light Nova (Base; Potency Counter.0x1163b1e9=0) | stagger points by potency | 50 | stagger | Decoded |   |
| Light Nova (Base; Potency Counter.0x1163b1e9=1) | stagger points by potency | 75 | stagger | Decoded |   |
| Light Nova (Base; Potency Counter.0x1163b1e9=2) | stagger points by potency | 90 | stagger | Decoded |   |
| Light Nova (Base; Potency Counter.0x1163b1e9=3) | stagger points by potency | 100 | stagger | Decoded |   |
| Light Nova (Base; Potency Counter.0x1163b1e9=0) | shield amount | 9 | shield | Decoded (baseline) |   |
| Light Nova (Base; Potency Counter.0x1163b1e9=1) | shield amount | 12 | shield | Decoded (baseline) |   |
| Light Nova (Base; Potency Counter.0x1163b1e9=2) | shield amount | 15 | shield | Decoded (baseline) |   |
| Light Nova (Base; Potency Counter.0x1163b1e9=3) | shield amount | 18 | shield | Decoded (baseline) |   |
| Light Nova | active duration | *not decoded* | seconds | Not decoded |   |
| Light Nova | resource cost | *not decoded* | resource | Not decoded |   |
| Light Nova | stun duration | *not decoded* | seconds | Not decoded |   |
| Light Nova | cooldown | 0.5 | seconds | Decoded |   |
| Light Nova | charges | 1 | charges | Decoded |   |
| Light Nova | shield duration | 6 | seconds | Decoded |   |

### Defense / Sacred

| Name | Stat | Value | Unit | Status | In-game check |
|---|---|---|---|---|---|
| Blink | intangible duration | *not decoded* | seconds | Not decoded |   |
| Blink | active duration | *not decoded* | seconds | Not decoded |   |
| Blink | resource cost | *not decoded* | resource | Not decoded |   |
| Blink | cooldown | 0.5 | seconds | Decoded |   |
| Blink | charges | 1 | charges | Decoded |   |

### Ultimate 1

| Name | Stat | Value | Unit | Status | In-game check |
|---|---|---|---|---|---|
| Standing Stone | cooldown | 60 | seconds | Decoded |   |
| Standing Stone | charges | 1 | charges | Decoded (baseline) |   |
| Standing Stone | explosion damage | 300 | damage | Decoded (baseline) |   |
| Standing Stone | active duration | *not decoded* | seconds | Not decoded |   |
| Standing Stone | resource cost | *not decoded* | resource | Not decoded |   |
| Standing Stone | starting health | *not decoded* | health | Not decoded |   |
| Standing Stone | health loss rate | *not decoded* | health per second | Not decoded |   |
| Standing Stone | lifetime formula | *not decoded* |   | Not decoded |   |

### Ultimate 2 / Prep

| Name | Stat | Value | Unit | Status | In-game check |
|---|---|---|---|---|---|
| Forbidden Spells (Base; Second Ability Selected Selector{\[State\] Hero\_Merlin\\Ability Primary/Primary Primary\\State Ability Primary Primary =\> 1; \[State\] Hero\_Merlin\\Ability Primary/Primary Secondary\\State Ability Primary Secondary =\> 2; \[State\] Hero\_Merlin\\Ability Primary/Primary Defense\\State Ability Primary Defense =\> 3; \[State\] Hero\_Merlin\\Ability Secondary/Secondary Primary\\State Ability Secondary Primary =\> 1; \[State\] Hero\_Merlin\\Ability Secondary/Secondary Secondary\\State Ability Secondary Secondary =\> 2; \[State\] Hero\_Merlin\\Ability Secondary/Secondary Defense\\State Ability Secondary Defense =\> 3; \[State\] Hero\_Merlin\\Ability Defense/Defense Primary\\State Ability Defense Primary =\> 1; \[State\] Hero\_Merlin\\Ability Defense/Defense Secondary\\State Ability Defense Secondary =\> 2; \[State\] Hero\_Merlin\\Ability Defense/Defense Defense\\State Ability Defense Defense =\> 3; \[State\] Hero\_Merlin\\Ability Ultimate 2/Ultimate 2 Primary\\State Ability Ultimate 2 Primary =\> 1; \[State\] Hero\_Merlin\\Ability Ultimate 2/Ultimate 2 Secondary\\State Ability Ultimate 2 Secondary =\> 2; \[State\] Hero\_Merlin\\Ability Ultimate 2/Ultimate 2 Defense\\State Ability Ultimate 2 Defense =\> 3; True =\> 0}=0) | cooldown | 0 | seconds | Decoded |   |
| Forbidden Spells (Base; Second Ability Selected Selector{\[State\] Hero\_Merlin\\Ability Primary/Primary Primary\\State Ability Primary Primary =\> 1; \[State\] Hero\_Merlin\\Ability Primary/Primary Secondary\\State Ability Primary Secondary =\> 2; \[State\] Hero\_Merlin\\Ability Primary/Primary Defense\\State Ability Primary Defense =\> 3; \[State\] Hero\_Merlin\\Ability Secondary/Secondary Primary\\State Ability Secondary Primary =\> 1; \[State\] Hero\_Merlin\\Ability Secondary/Secondary Secondary\\State Ability Secondary Secondary =\> 2; \[State\] Hero\_Merlin\\Ability Secondary/Secondary Defense\\State Ability Secondary Defense =\> 3; \[State\] Hero\_Merlin\\Ability Defense/Defense Primary\\State Ability Defense Primary =\> 1; \[State\] Hero\_Merlin\\Ability Defense/Defense Secondary\\State Ability Defense Secondary =\> 2; \[State\] Hero\_Merlin\\Ability Defense/Defense Defense\\State Ability Defense Defense =\> 3; \[State\] Hero\_Merlin\\Ability Ultimate 2/Ultimate 2 Primary\\State Ability Ultimate 2 Primary =\> 1; \[State\] Hero\_Merlin\\Ability Ultimate 2/Ultimate 2 Secondary\\State Ability Ultimate 2 Secondary =\> 2; \[State\] Hero\_Merlin\\Ability Ultimate 2/Ultimate 2 Defense\\State Ability Ultimate 2 Defense =\> 3; True =\> 0}=1) | cooldown | 90 | seconds | Decoded |   |
| Forbidden Spells (Base; Second Ability Selected Selector{\[State\] Hero\_Merlin\\Ability Primary/Primary Primary\\State Ability Primary Primary =\> 1; \[State\] Hero\_Merlin\\Ability Primary/Primary Secondary\\State Ability Primary Secondary =\> 2; \[State\] Hero\_Merlin\\Ability Primary/Primary Defense\\State Ability Primary Defense =\> 3; \[State\] Hero\_Merlin\\Ability Secondary/Secondary Primary\\State Ability Secondary Primary =\> 1; \[State\] Hero\_Merlin\\Ability Secondary/Secondary Secondary\\State Ability Secondary Secondary =\> 2; \[State\] Hero\_Merlin\\Ability Secondary/Secondary Defense\\State Ability Secondary Defense =\> 3; \[State\] Hero\_Merlin\\Ability Defense/Defense Primary\\State Ability Defense Primary =\> 1; \[State\] Hero\_Merlin\\Ability Defense/Defense Secondary\\State Ability Defense Secondary =\> 2; \[State\] Hero\_Merlin\\Ability Defense/Defense Defense\\State Ability Defense Defense =\> 3; \[State\] Hero\_Merlin\\Ability Ultimate 2/Ultimate 2 Primary\\State Ability Ultimate 2 Primary =\> 1; \[State\] Hero\_Merlin\\Ability Ultimate 2/Ultimate 2 Secondary\\State Ability Ultimate 2 Secondary =\> 2; \[State\] Hero\_Merlin\\Ability Ultimate 2/Ultimate 2 Defense\\State Ability Ultimate 2 Defense =\> 3; True =\> 0}=2) | cooldown | 90 | seconds | Decoded |   |
| Forbidden Spells (Base; Second Ability Selected Selector{\[State\] Hero\_Merlin\\Ability Primary/Primary Primary\\State Ability Primary Primary =\> 1; \[State\] Hero\_Merlin\\Ability Primary/Primary Secondary\\State Ability Primary Secondary =\> 2; \[State\] Hero\_Merlin\\Ability Primary/Primary Defense\\State Ability Primary Defense =\> 3; \[State\] Hero\_Merlin\\Ability Secondary/Secondary Primary\\State Ability Secondary Primary =\> 1; \[State\] Hero\_Merlin\\Ability Secondary/Secondary Secondary\\State Ability Secondary Secondary =\> 2; \[State\] Hero\_Merlin\\Ability Secondary/Secondary Defense\\State Ability Secondary Defense =\> 3; \[State\] Hero\_Merlin\\Ability Defense/Defense Primary\\State Ability Defense Primary =\> 1; \[State\] Hero\_Merlin\\Ability Defense/Defense Secondary\\State Ability Defense Secondary =\> 2; \[State\] Hero\_Merlin\\Ability Defense/Defense Defense\\State Ability Defense Defense =\> 3; \[State\] Hero\_Merlin\\Ability Ultimate 2/Ultimate 2 Primary\\State Ability Ultimate 2 Primary =\> 1; \[State\] Hero\_Merlin\\Ability Ultimate 2/Ultimate 2 Secondary\\State Ability Ultimate 2 Secondary =\> 2; \[State\] Hero\_Merlin\\Ability Ultimate 2/Ultimate 2 Defense\\State Ability Ultimate 2 Defense =\> 3; True =\> 0}=3) | cooldown | 90 | seconds | Decoded |   |
| Forbidden Spells | charges | 1 | charges | Decoded (baseline) |   |
| Forbidden Spells | active duration | *not decoded* | seconds | Not decoded |   |
| Forbidden Spells | resource cost | *not decoded* | resource | Not decoded |   |

### Power / Forbidden

| Name | Stat | Value | Unit | Status | In-game check |
|---|---|---|---|---|---|
| Cataclysm | meteorite damage | 500 | damage | Decoded (baseline) |   |
| Cataclysm | active duration | *not decoded* | seconds | Not decoded |   |
| Cataclysm | resource cost | *not decoded* | resource | Not decoded |   |
| Cataclysm | targeting window before impact | *not decoded* | seconds | Not decoded |   |
| Cataclysm | cooldown | 0.5 | seconds | Decoded |   |
| Cataclysm | charges | 1 | charges | Decoded |   |

### Special / Forbidden

| Name | Stat | Value | Unit | Status | In-game check |
|---|---|---|---|---|---|
| Unholy Strikes | empowered attacks count | *not decoded* | attacks | Not decoded | Second decoding pass: 6 |
| Unholy Strikes | projectile damage | 60 | damage | Decoded (baseline) |   |
| Unholy Strikes | active duration | *not decoded* | seconds | Not decoded |   |
| Unholy Strikes | resource cost | *not decoded* | resource | Not decoded |   |
| Unholy Strikes | cooldown | 0.5 | seconds | Decoded |   |
| Unholy Strikes | charges | 1 | charges | Decoded |   |

### Defense / Forbidden

| Name | Stat | Value | Unit | Status | In-game check |
|---|---|---|---|---|---|
| Blood Ritual | health sacrifice | 25 | percent | Decoded |   |
| Blood Ritual | ally heal | 200 | percent | Decoded |   |
| Blood Ritual | enemy damage multiplier | 10 | multiplier | Decoded |   |
| Blood Ritual | active duration | *not decoded* | seconds | Not decoded |   |
| Blood Ritual | resource cost | *not decoded* | resource | Not decoded |   |
| Blood Ritual | cooldown | 0.5 | seconds | Decoded |   |
| Blood Ritual | charges | 1 | charges | Decoded |   |

## Talents

Values separated by / are for Common / Rare / Epic / Legendary.

| Talent | Unlocks at rank | Effect |
|---|---|---|
| Arcane Shield | 1 | Casting an Arcane Spell (SPECIAL) surrounds Merlin with protection that blocks any attack for 1.2 / 1.5 / 1.8 / 2 seconds |
| Arcanic Rune | 2 | Hitting at least one enemy with an Arcane Spell (SPECIAL) conjures a rune of POTENCY<br>Arcane Spells (SPECIAL) deal +20 / 25 / 30 / 35% damage |
| Astrology | 1 | Gain +3 Star(s) of Fate<br>Future Talents have a +15 / 25 / 35 / 45% chance of being Rare or above |
| Brambles Whirlwind | 1 | When casting the Giant Brambles Spell, Merlin makes the brambles spin around him, dealing +32 / 40 / 48 / 56% damage all around |
| Celestial Wrath | 8 | TRAIT triggers a lightning strike on up to 4 / 5 / 6 / 7 nearby enemies<br>Lightning strikes deal 80 damage each and are stronger if fewer enemies are hit |
| Corrupted Arts | 9 | Forbidden Spells (ULTIMATE) deal +12 / 15 / 18 / 21% damage per Cursed Magical Object owned |
| Dark Swiftness | 6 | DASH can be held for up to 0.5 second(s) to deal 60 / 75 / 90 / 105 damage to enemies passed through |
| Elemental Affinity | 5 | All of Merlin's Abilities have +16 / 20 / 24 / 28% Crit Chance on enemies affected by IGNITE or CHILLED status (both can stack) |
| Energy Stone | 1 | For every 10% health lost, Standing Stone emits a blast of energy toward a nearby enemy, dealing 30 / 37.5 / 45 / 52.5 damage |
| Eternal Dream | 2 | Each time Merlin casts his nine different Spells, he gains 30 / 40 / 50 / 60 Dream Shards<br>Does not work within a Safe Zone or during Chapter Boss fights |
| Fire Barrage | 1 | The Fireball Spell also sends 2 fire missiles (+2 per Rune of POTENCY spent) to nearby enemies, dealing 16 / 20 / 24 / 28 damage each |
| Freezing Stones | 4 | The Stone Shield Spell applies CHILLED to enemies hit, and its final explosion deals +40 / 50 / 60 / 70% damage |
| Frost Arcane | 7 | Whenever Frost Orb is touched by Merlin's ATTACK, it emits a blast dealing 20 / 25 / 30 / 35 damage all around |
| Grace of Heaven | 1 | Casting a Sacred Spell (DEFENSE) reduces TRAIT cooldown by 2 / 2.5 / 3 / 3.5 seconds |
| Holy Fire | 4 | The Light Nova Spell deals 28 / 35 / 42 / 49 damage (+100% per rune of POTENCY spent) to enemies hit and applies IGNITE |
| Life Seed | 8 | When in combat, DASH creates a life seed that sprouts shortly after to restore 4 / 5 / 6 / 7 health points to the most heavily injured nearby Hero |
| Lightning Storm | 3 | Every 4 times the Fork of Lightning Spell hits an enemy, a lightning strike will hit a nearby enemy, dealing 12 / 15 / 18 / 21 damage |
| Megalithic Site | 9 | Merlin extracts 3 standing stones from the ground around him, with each one dealing 80 / 100 / 120 / 140% damage when destroyed |
| Natural Harmony | 1 | Hitting at least one enemy with a Nature Spell (POWER) restores 8 / 10 / 12 / 14 health to all nearby Heroes |
| Retaliation | 7 | The Blessing Spell also applies 10 SHIELD for 6 seconds to the Hero affected<br>When this expires or is destroyed, it deals 80 / 100 / 120 / 140 area damage |
| Runic Might | 1 | Quest (x20): In combat, casting a Spell that consumes 3 runes of POTENCY earns +0.5 DMG<br>Complete: Repeating this action makes the Spell cast gain 20 / 25 / 30 / 35% Crit Chance |
| Sacred Ground | 1 | After casting the Blink Spell, a sacred area will appear on the ground for 5 seconds<br>All Heroes inside the area will gain +0.4 / 0.5 / 0.6 / 0.7 DMG |
| Sacred Strike | 1 | After casting a Sacred Spell (DEFENSE), Merlin's next ATTACK will be a finisher that conjures a rune of POTENCY if it hits an enemy and deals 320 / 400 / 480 / 560% damage |
| Shooting Stars | 3 | The Starfall Spell applies VULNERABLE to enemies hit for 4 / 5 / 6 / 7 seconds |
| Trinity | 5 | Quest (x3): Collect Excalibur, Holy Grail or Father Time's Hourglass to gain +2 Stars of Fate<br>Complete: Gain +1 TRAIT charge and all critical damage will increase by +40 / 50 / 60 / 70% |
| Wild Magic | 1 | After casting a Nature Spell (POWER), the next 3 ATTACKS also project thorns, dealing 200 / 250 / 300 / 350% damage as BLEED |

## Outfits

| Outfit | How to unlock | Description |
|---|---|---|
| Signature Outfit | Completed the 'Runic Might' Talent Quest | Unlocked by completing the 'Runic Might' Talent Quest |
| Traveler Outfit | Reached Chapter 3 | Unlocked by reaching Chapter 3 |
| Master Outfit | Completed the game in Darkness Difficulty | Unlocked by completing the game  in Darkness Difficulty |
| Hidden Outfit | Morgan's Blessing | Hidden Requirements |
| Ravens Outfit | Merlin Hero DLC acquired | Available in the Merlin Hero DLC |
| Nightmares Outfit | Merlin Hero DLC acquired | Available in the Merlin Hero DLC |
| Royal Counselor Outfit | Merlin Hero DLC acquired | Available in the Merlin Hero DLC |


**How to read the text**

- **Bold** words are highlighted in the game.
- `{0}`, `{1}` and so on are numbers or names the game fills in while you play.

Source: [`Hero_Merlin_Common.LangEN.tsv`](../../data/Hero_Merlin_Common.LangEN.tsv), [`Hero_Merlin_Abilities.tsv`](../../data/Hero_Merlin_Abilities.tsv), [`Hero_Merlin_Talents.tsv`](../../data/Hero_Merlin_Talents.tsv), [`Hero_Merlin_Skins.LangEN.tsv`](../../data/Hero_Merlin_Skins.LangEN.tsv).
Game version: Game build 1.06 (Steam build ID 25174305); the displayed version string is unverified. See VERSION.json.

*This page is generated from the TSV files in [data/](../../data/) by `tools/build_browse.py`. Do not edit it by hand; fix the data and re-run the script.*
