# Shared mechanics

[All tables](README.md)

Settings shared by all heroes: reward sources, difficulties, drops, status effects, prices, resources, stats and timers.

**How to read the values**

- **Decoded** values come straight from the game files.
- **Decoded (baseline)** values assume a level 1 hero with damage 10, healing 10, no talents and no Magical Objects.
- **Not decoded** means nobody has found the number yet. It does not mean zero.
- **In-game check** shows what the maintainer read in the game's Compendium, when that was checked.

### Drops / Chests

| Name | Stat | Value | Unit | Status | In-game check |
|---|---|---|---|---|---|
| Storm Island Basic Chest T1 (Decoded concrete T1 owner; inherited T1 values where stated) | common drop chance | 70 | percent | Decoded (baseline) |   |
| Storm Island Basic Chest T1 (Decoded concrete T1 owner; inherited T1 values where stated) | rare drop chance | 30 | percent | Decoded (baseline) |   |
| Storm Island Basic Chest T1 (Decoded concrete T1 owner; inherited T1 values where stated) | epic drop chance | 0 | percent | Decoded (baseline) |   |
| Storm Island Basic Chest T1 (Core) | active spawn and display tier | *not decoded* |   | Not decoded |   |
| Storm Island Basic Chest T2 (Decoded concrete T2 owner; inherited T1 values where stated) | common drop chance | 30 | percent | Decoded (baseline) |   |
| Storm Island Basic Chest T2 (Decoded concrete T2 owner; inherited T1 values where stated) | rare drop chance | 50 | percent | Decoded (baseline) |   |
| Storm Island Basic Chest T2 (Decoded concrete T2 owner; inherited T1 values where stated) | epic drop chance | 20 | percent | Decoded (baseline) |   |
| Storm Island Basic Chest T2 (Core) | active spawn and display tier | *not decoded* |   | Not decoded |   |
| Storm Island Basic Chest T3 (Decoded concrete T3 owner; inherited T1 values where stated) | common drop chance | 10 | percent | Decoded (baseline) |   |
| Storm Island Basic Chest T3 (Decoded concrete T3 owner; inherited T1 values where stated) | rare drop chance | 25 | percent | Decoded (baseline) |   |
| Storm Island Basic Chest T3 (Decoded concrete T3 owner; inherited T1 values where stated) | epic drop chance | 65 | percent | Decoded (baseline) |   |
| Storm Island Basic Chest T3 (Core) | active spawn and display tier | *not decoded* |   | Not decoded |   |

### Drops / Spawners

| Name | Stat | Value | Unit | Status | In-game check |
|---|---|---|---|---|---|
| Hourglass Drop Bag Spawner (Spawner parameter default; custom chances apply only when Custom Drop Chance Condition selects that branch) | configured drop count | 5 | drops | Decoded (baseline) |   |
| Hourglass Drop Bag Spawner (Spawner parameter default; custom chances apply only when Custom Drop Chance Condition selects that branch) | custom common drop chance | 70 | percent | Decoded (baseline) |   |
| Hourglass Drop Bag Spawner (Spawner parameter default; custom chances apply only when Custom Drop Chance Condition selects that branch) | custom rare drop chance | 20 | percent | Decoded (baseline) |   |
| Hourglass Drop Bag Spawner (Spawner parameter default; custom chances apply only when Custom Drop Chance Condition selects that branch) | custom epic drop chance | 9 | percent | Decoded (baseline) |   |
| Hourglass Drop Bag Spawner (Spawner parameter default; custom chances apply only when Custom Drop Chance Condition selects that branch) | custom each legendary cursed drop chance | 0.5 | percent | Decoded (baseline) |   |
| Hourglass Drop Bag Spawner (Core) | effective odds by spawn position | *not decoded* |   | Not decoded |   |
| Wishing Well Bag (Is Common Condition is true; otherwise zero) | conditional common drop chance selector | 100 | percent | Decoded (baseline) |   |
| Wishing Well Bag (Is Legendary Or Cursed Condition is true; otherwise zero) | conditional cursed drop chance selector | 50 | percent | Decoded (baseline) |   |
| Wishing Well Bag (Is Epic Condition is true; otherwise zero) | conditional epic drop chance selector | 100 | percent | Decoded (baseline) |   |
| Wishing Well Bag (Is Legendary Or Cursed Condition is true; otherwise zero) | conditional legendary drop chance selector | 50 | percent | Decoded (baseline) |   |
| Wishing Well Bag (Is Power Up Condition is true; otherwise zero) | conditional power up drop chance selector | 100 | percent | Decoded (baseline) |   |
| Wishing Well Bag (Is Rare Condition is true; otherwise zero) | conditional rare drop chance selector | 100 | percent | Decoded (baseline) |   |
| Wishing Well Bag (Core) | effective rarity odds | *not decoded* |   | Not decoded |   |
| Single MO Bag (Is Common Condition is true; otherwise zero) | conditional common drop chance selector | 100 | percent | Decoded (baseline) |   |
| Single MO Bag (Is Cursed Condition is true; otherwise zero) | conditional cursed drop chance selector | 100 | percent | Decoded (baseline) |   |
| Single MO Bag (Is Epic Condition is true; otherwise zero) | conditional epic drop chance selector | 100 | percent | Decoded (baseline) |   |
| Single MO Bag (\[Cpnt Value Tester\] Single\_MO\_Drop\_Bag\\Is Legendary Condition is true; otherwise zero) | conditional legendary drop chance selector | 100 | percent | Decoded (baseline) |   |
| Single MO Bag (Is PowerUp Condition is true; otherwise zero) | conditional powerup drop chance selector | 100 | percent | Decoded (baseline) |   |
| Single MO Bag (Is Rare Condition is true; otherwise zero) | conditional rare drop chance selector | 100 | percent | Decoded (baseline) |   |
| Single MO Bag (Core) | effective rarity odds | *not decoded* |   | Not decoded |   |
| Geppetto Flash of Genius (Geppetto passive create-objects controller/event/spawner references this bag) | common drop chance | 40 | percent | Decoded (baseline) |   |
| Geppetto Flash of Genius (Geppetto passive create-objects controller/event/spawner references this bag) | rare drop chance | 30 | percent | Decoded (baseline) |   |
| Geppetto Flash of Genius (Geppetto passive create-objects controller/event/spawner references this bag) | epic drop chance | 20 | percent | Decoded (baseline) |   |
| Geppetto Flash of Genius (Geppetto passive create-objects controller/event/spawner references this bag) | legendary drop chance | 5 | percent | Decoded (baseline) |   |
| Geppetto Flash of Genius (Geppetto passive create-objects controller/event/spawner references this bag) | cursed drop chance | 5 | percent | Decoded (baseline) |   |

### Stats

| Name | Stat | Value | Unit | Status | In-game check |
|---|---|---|---|---|---|
| Raw Damage (Decoded owner default) | baseline damage | 10 | damage | Decoded (baseline) |   |
| Raw Healing (Decoded owner default) | baseline healing | 10 | healing | Decoded (baseline) |   |
| Raw Max Health (Decoded owner default) | baseline max health | 100 | health | Decoded (baseline) |   |
| Critical Strike Chance (Decoded owner default) | base crit chance | 5 | percent | Decoded (baseline) |   |
| Vitality (Core) | max health scaling per point | *not decoded* |   | Not decoded |   |
| Damage (DMG) (Core) | stat to damage formula | *not decoded* |   | Not decoded |   |
| Armor (Core) | positive armor formula | *not decoded* |   | Not decoded |   |
| Armor (Core) | negative armor formula | *not decoded* |   | Not decoded |   |
| Critical Damage (Core) | base crit multiplier | *not decoded* |   | Not decoded |   |
| Critical Strike Overflow (Core) | overflow conversion coefficient | *not decoded* |   | Not decoded |   |
| Critical Strike Overflow (Core) | overflow rule | Crit chance above100% transforms into critical damage |   | Fixed text |   |

### Status Effects

| Name | Stat | Value | Unit | Status | In-game check |
|---|---|---|---|---|---|
| Vulnerable (Global configured default; application overrides may differ) | configured damage taken modifier | 0.25 | fraction | Decoded (baseline) |   |
| Chilled (Global configured default; application overrides may differ) | configured movement modifier | 0.4 | fraction | Decoded (baseline) |   |
| Chilled (Global configured default; application overrides may differ) | default duration | 5 | seconds | Decoded (baseline) |   |
| Strength (Global configured default; application overrides may differ) | configured damage dealt modifier | 0.25 | fraction | Decoded (baseline) |   |
| Bleed (Global configured default; application overrides may differ) | default duration | 5 | seconds | Decoded (baseline) |   |
| Ignite (Global configured default; application overrides may differ) | default duration | 5.5 | seconds | Decoded (baseline) |   |
| Regeneration (Global configured default; application overrides may differ) | configured healing modifier | 0.04 | fraction | Decoded (baseline) |   |
| Regeneration (Global configured default; application overrides may differ) | default duration | 5 | seconds | Decoded (baseline) |   |
| Ignite (Decoded owner default) | default raw tick damage coefficient | 0.5 | coefficient | Decoded (baseline) |   |
| Ignite (Core) | entity default duration | *not decoded* | seconds | Not decoded |   |
| Vulnerable (Core) | damage taken scope | *not decoded* |   | Not decoded |   |
| Chilled (Core) | movement slow formula | *not decoded* |   | Not decoded |   |
| Chilled (Core) | ability override rule | *not decoded* |   | Not decoded |   |
| Strength (Core) | damage dealt scope | *not decoded* |   | Not decoded |   |
| Critical Health (Core) | health threshold | *not decoded* |   | Not decoded |   |
| Critical Health (Core) | threshold comparison | *not decoded* |   | Not decoded |   |
| Ignite (Core) | tick interval | *not decoded* |   | Not decoded |   |
| Ignite (Core) | damage formula | *not decoded* |   | Not decoded |   |
| Bleed (Core) | tick interval | *not decoded* |   | Not decoded |   |
| Bleed (Core) | damage formula | *not decoded* |   | Not decoded |   |
| Regeneration (Core) | tick interval | *not decoded* |   | Not decoded |   |
| Regeneration (Core) | healing formula | *not decoded* |   | Not decoded |   |
| Life on Hit (Core) | healing formula | *not decoded* |   | Not decoded |   |
| Lifesteal (Core) | healing formula | *not decoded* |   | Not decoded |   |

### Resources

| Name | Stat | Value | Unit | Status | In-game check |
|---|---|---|---|---|---|
| Death's Door (Decoded owner default) | starting duration | 30 | seconds | Decoded (baseline) |   |
| Death's Door (Decoded owner default) | duration reduction per ally revive | 5 | seconds | Decoded (baseline) |   |
| Dream Shards (Core) | starting count | *not decoded* |   | Not decoded |   |
| Dream Shards (Core) | paid activity cost scaling | *not decoded* |   | Not decoded |   |
| Stars of Fate (Core) | starting count | *not decoded* |   | Not decoded |   |
| Stars of Fate (Core) | talent reroll cost | *not decoded* |   | Not decoded |   |
| Stars of Fate (Core) | talent choice count | *not decoded* |   | Not decoded |   |
| Stars of Fate (Core) | object choice count | *not decoded* |   | Not decoded |   |
| Stars of Fate (Core) | reroll modifiers | *not decoded* |   | Not decoded |   |
| Raven Feather (Core) | starting count | *not decoded* |   | Not decoded |   |
| Raven Feather (Core) | shared or per player count | *not decoded* |   | Not decoded |   |
| Raven Feather (Core) | consumption per recovery | *not decoded* |   | Not decoded |   |
| Raven Feather (Core) | revive channel duration | *not decoded* |   | Not decoded |   |
| Raven Feather (Core) | revived health ratio | *not decoded* |   | Not decoded |   |
| Nightmare Key (Core) | starting count | *not decoded* |   | Not decoded |   |
| Nightmare Key (Core) | keys per lock | *not decoded* |   | Not decoded |   |
| Stars of Fate (Chest Starts Locked Value true) | chest reroll cost | 2 | stars of fate | Decoded (baseline) |   |
| Stars of Fate (Default branch otherwise) | chest reroll cost | 1 | stars of fate | Decoded (baseline) |   |

### Sources / Prices

| Name | Stat | Value | Unit | Status | In-game check |
|---|---|---|---|---|---|
| Wishing Well (Decoded owner default) | configured max reward count | 3 | objects | Decoded (baseline) |   |
| Wishing Well (Reward Tier selects T1; Dropped Objects Counter == 0) | base purchase price | 50 | dream shards | Decoded (baseline) |   |
| Wishing Well (Reward Tier selects T1; Dropped Objects Counter == 1) | base purchase price | 100 | dream shards | Decoded (baseline) |   |
| Wishing Well (Reward Tier selects T1; Dropped Objects Counter == 2) | base purchase price | 150 | dream shards | Decoded (baseline) |   |
| Wishing Well (Reward Tier selects T2; Dropped Objects Counter == 0) | base purchase price | 100 | dream shards | Decoded (baseline) |   |
| Wishing Well (Reward Tier selects T2; Dropped Objects Counter == 1) | base purchase price | 150 | dream shards | Decoded (baseline) |   |
| Wishing Well (Reward Tier selects T2; Dropped Objects Counter == 2) | base purchase price | 250 | dream shards | Decoded (baseline) |   |
| Wishing Well (Reward Tier selects T3; Dropped Objects Counter == 0) | base purchase price | 150 | dream shards | Decoded (baseline) |   |
| Wishing Well (Reward Tier selects T3; Dropped Objects Counter == 1) | base purchase price | 250 | dream shards | Decoded (baseline) |   |
| Wishing Well (Reward Tier selects T3; Dropped Objects Counter == 2) | base purchase price | 350 | dream shards | Decoded (baseline) |   |
| Wishing Well (Core) | final price formula | *not decoded* |   | Not decoded |   |
| Sandman (Core) | price or reward rule | *not decoded* |   | Not decoded |   |
| Sandman (Core) | rarity selection rule | *not decoded* |   | Not decoded |   |
| Sandman (Core) | region difficulty modifiers | *not decoded* |   | Not decoded |   |
| Shops (Core) | price or reward rule | *not decoded* |   | Not decoded |   |
| Shops (Core) | rarity selection rule | *not decoded* |   | Not decoded |   |
| Shops (Core) | region difficulty modifiers | *not decoded* |   | Not decoded |   |
| Camp rewards (Core) | price or reward rule | *not decoded* |   | Not decoded |   |
| Camp rewards (Core) | rarity selection rule | *not decoded* |   | Not decoded |   |
| Camp rewards (Core) | region difficulty modifiers | *not decoded* |   | Not decoded |   |

### Sources / Rewards

| Name | Stat | Value | Unit | Status | In-game check |
|---|---|---|---|---|---|
| Avalon/Objects\_Tree\_Quest!Morgan\_Tree\_Quest\_Reward\_Spawner (Prior canonical explicit entity setting; active reward mapping unresolved) | common entity set chance | 0 | percent | Earlier table |   |
| Avalon/Objects\_Tree\_Quest!Morgan\_Tree\_Quest\_Reward\_Spawner (Prior canonical explicit entity setting; active reward mapping unresolved) | rare entity set chance | 0 | percent | Earlier table |   |
| Avalon/Objects\_Tree\_Quest!Morgan\_Tree\_Quest\_Reward\_Spawner (Prior canonical explicit entity setting; active reward mapping unresolved) | epic entity set chance | 0 | percent | Earlier table |   |
| Avalon/Objects\_Tree\_Quest!Morgan\_Tree\_Quest\_Reward\_Spawner (Prior canonical explicit entity setting; active reward mapping unresolved) | legendary entity set chance | 100 | percent | Earlier table |   |
| Avalon/Objects\_Tree\_Quest!Morgan\_Tree\_Quest\_Reward\_Spawner (Prior canonical explicit entity setting; active reward mapping unresolved) | cursed entity set chance | 0 | percent | Earlier table |   |
| Avalon/Objects\_Tree\_Quest!Morgan\_Tree\_Quest\_Reward\_Spawner (Core) | active reward mapping and display name | *not decoded* |   | Not decoded |   |
| DarkHills/Houses\_3Pigs!Pig\_House\_Reward\_Spawner (Prior canonical explicit entity setting; active reward mapping unresolved) | common entity set chance | 0 | percent | Earlier table |   |
| DarkHills/Houses\_3Pigs!Pig\_House\_Reward\_Spawner (Prior canonical explicit entity setting; active reward mapping unresolved) | rare entity set chance | 0 | percent | Earlier table |   |
| DarkHills/Houses\_3Pigs!Pig\_House\_Reward\_Spawner (Prior canonical explicit entity setting; active reward mapping unresolved) | epic entity set chance | 0 | percent | Earlier table |   |
| DarkHills/Houses\_3Pigs!Pig\_House\_Reward\_Spawner (Prior canonical explicit entity setting; active reward mapping unresolved) | legendary entity set chance | 100 | percent | Earlier table |   |
| DarkHills/Houses\_3Pigs!Pig\_House\_Reward\_Spawner (Prior canonical explicit entity setting; active reward mapping unresolved) | cursed entity set chance | 0 | percent | Earlier table |   |
| DarkHills/Houses\_3Pigs!Pig\_House\_Reward\_Spawner (Core) | active reward mapping and display name | *not decoded* |   | Not decoded |   |
| DarkHills/Jack!Jack\_Reward\_Spawner (Prior canonical explicit entity setting; active reward mapping unresolved) | common entity set chance | 0 | percent | Earlier table |   |
| DarkHills/Jack!Jack\_Reward\_Spawner (Prior canonical explicit entity setting; active reward mapping unresolved) | rare entity set chance | 0 | percent | Earlier table |   |
| DarkHills/Jack!Jack\_Reward\_Spawner (Prior canonical explicit entity setting; active reward mapping unresolved) | epic entity set chance | 0 | percent | Earlier table |   |
| DarkHills/Jack!Jack\_Reward\_Spawner (Prior canonical explicit entity setting; active reward mapping unresolved) | legendary entity set chance | 100 | percent | Earlier table |   |
| DarkHills/Jack!Jack\_Reward\_Spawner (Prior canonical explicit entity setting; active reward mapping unresolved) | cursed entity set chance | 0 | percent | Earlier table |   |
| DarkHills/Jack!Jack\_Reward\_Spawner (Core) | active reward mapping and display name | *not decoded* |   | Not decoded |   |
| DarkHills/Objects\_DarkHills!Boss\_Shrine\_White\_Lady\_Reward (Prior canonical explicit entity setting; active reward mapping unresolved) | common entity set chance | 0 | percent | Earlier table |   |
| DarkHills/Objects\_DarkHills!Boss\_Shrine\_White\_Lady\_Reward (Prior canonical explicit entity setting; active reward mapping unresolved) | rare entity set chance | 0 | percent | Earlier table |   |
| DarkHills/Objects\_DarkHills!Boss\_Shrine\_White\_Lady\_Reward (Prior canonical explicit entity setting; active reward mapping unresolved) | epic entity set chance | 0 | percent | Earlier table |   |
| DarkHills/Objects\_DarkHills!Boss\_Shrine\_White\_Lady\_Reward (Prior canonical explicit entity setting; active reward mapping unresolved) | legendary entity set chance | 0 | percent | Earlier table |   |
| DarkHills/Objects\_DarkHills!Boss\_Shrine\_White\_Lady\_Reward (Prior canonical explicit entity setting; active reward mapping unresolved) | cursed entity set chance | 100 | percent | Earlier table |   |
| DarkHills/Objects\_DarkHills!Boss\_Shrine\_White\_Lady\_Reward (Core) | active reward mapping and display name | *not decoded* |   | Not decoded |   |
| Enemies/Stingy\_Jack!Stingy\_Jack\_Reward\_Avalon\_T1 (Prior canonical explicit entity setting; active reward mapping unresolved) | common entity set chance | 60 | percent | Earlier table |   |
| Enemies/Stingy\_Jack!Stingy\_Jack\_Reward\_Avalon\_T1 (Prior canonical explicit entity setting; active reward mapping unresolved) | rare entity set chance | 40 | percent | Earlier table |   |
| Enemies/Stingy\_Jack!Stingy\_Jack\_Reward\_Avalon\_T1 (Prior canonical explicit entity setting; active reward mapping unresolved) | epic entity set chance | 0 | percent | Earlier table |   |
| Enemies/Stingy\_Jack!Stingy\_Jack\_Reward\_Avalon\_T1 (Core) | active reward mapping and display name | *not decoded* |   | Not decoded |   |
| Enemies/Stingy\_Jack!Stingy\_Jack\_Reward\_Avalon\_T2 (Prior canonical explicit entity setting; active reward mapping unresolved) | common entity set chance | 20 | percent | Earlier table |   |
| Enemies/Stingy\_Jack!Stingy\_Jack\_Reward\_Avalon\_T2 (Prior canonical explicit entity setting; active reward mapping unresolved) | rare entity set chance | 50 | percent | Earlier table |   |
| Enemies/Stingy\_Jack!Stingy\_Jack\_Reward\_Avalon\_T2 (Prior canonical explicit entity setting; active reward mapping unresolved) | epic entity set chance | 30 | percent | Earlier table |   |
| Enemies/Stingy\_Jack!Stingy\_Jack\_Reward\_Avalon\_T2 (Core) | active reward mapping and display name | *not decoded* |   | Not decoded |   |
| Enemies/Stingy\_Jack!Stingy\_Jack\_Reward\_Avalon\_T3 (Prior canonical explicit entity setting; active reward mapping unresolved) | common entity set chance | 0 | percent | Earlier table |   |
| Enemies/Stingy\_Jack!Stingy\_Jack\_Reward\_Avalon\_T3 (Prior canonical explicit entity setting; active reward mapping unresolved) | rare entity set chance | 20 | percent | Earlier table |   |
| Enemies/Stingy\_Jack!Stingy\_Jack\_Reward\_Avalon\_T3 (Prior canonical explicit entity setting; active reward mapping unresolved) | epic entity set chance | 80 | percent | Earlier table |   |
| Enemies/Stingy\_Jack!Stingy\_Jack\_Reward\_Avalon\_T3 (Core) | active reward mapping and display name | *not decoded* |   | Not decoded |   |
| Enemies/Stingy\_Jack!Stingy\_Jack\_Reward\_Dark\_Hills\_T2 (Prior canonical explicit entity setting; active reward mapping unresolved) | common entity set chance | 40 | percent | Earlier table |   |
| Enemies/Stingy\_Jack!Stingy\_Jack\_Reward\_Dark\_Hills\_T2 (Prior canonical explicit entity setting; active reward mapping unresolved) | rare entity set chance | 50 | percent | Earlier table |   |
| Enemies/Stingy\_Jack!Stingy\_Jack\_Reward\_Dark\_Hills\_T2 (Prior canonical explicit entity setting; active reward mapping unresolved) | epic entity set chance | 10 | percent | Earlier table |   |
| Enemies/Stingy\_Jack!Stingy\_Jack\_Reward\_Dark\_Hills\_T2 (Core) | active reward mapping and display name | *not decoded* |   | Not decoded |   |
| Enemies/Stingy\_Jack!Stingy\_Jack\_Reward\_Dark\_Hills\_T3 (Prior canonical explicit entity setting; active reward mapping unresolved) | common entity set chance | 20 | percent | Earlier table |   |
| Enemies/Stingy\_Jack!Stingy\_Jack\_Reward\_Dark\_Hills\_T3 (Prior canonical explicit entity setting; active reward mapping unresolved) | rare entity set chance | 30 | percent | Earlier table |   |
| Enemies/Stingy\_Jack!Stingy\_Jack\_Reward\_Dark\_Hills\_T3 (Prior canonical explicit entity setting; active reward mapping unresolved) | epic entity set chance | 50 | percent | Earlier table |   |
| Enemies/Stingy\_Jack!Stingy\_Jack\_Reward\_Dark\_Hills\_T3 (Core) | active reward mapping and display name | *not decoded* |   | Not decoded |   |
| Enemies/Stingy\_Jack!Stingy\_Jack\_Reward\_Storm\_Island\_T1 (Prior canonical explicit entity setting; active reward mapping unresolved) | common entity set chance | 70 | percent | Earlier table |   |
| Enemies/Stingy\_Jack!Stingy\_Jack\_Reward\_Storm\_Island\_T1 (Prior canonical explicit entity setting; active reward mapping unresolved) | rare entity set chance | 30 | percent | Earlier table |   |
| Enemies/Stingy\_Jack!Stingy\_Jack\_Reward\_Storm\_Island\_T1 (Prior canonical explicit entity setting; active reward mapping unresolved) | epic entity set chance | 0 | percent | Earlier table |   |
| Enemies/Stingy\_Jack!Stingy\_Jack\_Reward\_Storm\_Island\_T1 (Core) | active reward mapping and display name | *not decoded* |   | Not decoded |   |
| Enemies/Stingy\_Jack!Stingy\_Jack\_Reward\_Storm\_Island\_T2 (Prior canonical explicit entity setting; active reward mapping unresolved) | common entity set chance | 30 | percent | Earlier table |   |
| Enemies/Stingy\_Jack!Stingy\_Jack\_Reward\_Storm\_Island\_T2 (Prior canonical explicit entity setting; active reward mapping unresolved) | rare entity set chance | 50 | percent | Earlier table |   |
| Enemies/Stingy\_Jack!Stingy\_Jack\_Reward\_Storm\_Island\_T2 (Prior canonical explicit entity setting; active reward mapping unresolved) | epic entity set chance | 20 | percent | Earlier table |   |
| Enemies/Stingy\_Jack!Stingy\_Jack\_Reward\_Storm\_Island\_T2 (Core) | active reward mapping and display name | *not decoded* |   | Not decoded |   |
| Enemies/Stingy\_Jack!Stingy\_Jack\_Reward\_Storm\_Island\_T3 (Prior canonical explicit entity setting; active reward mapping unresolved) | common entity set chance | 10 | percent | Earlier table |   |
| Enemies/Stingy\_Jack!Stingy\_Jack\_Reward\_Storm\_Island\_T3 (Prior canonical explicit entity setting; active reward mapping unresolved) | rare entity set chance | 25 | percent | Earlier table |   |
| Enemies/Stingy\_Jack!Stingy\_Jack\_Reward\_Storm\_Island\_T3 (Prior canonical explicit entity setting; active reward mapping unresolved) | epic entity set chance | 65 | percent | Earlier table |   |
| Enemies/Stingy\_Jack!Stingy\_Jack\_Reward\_Storm\_Island\_T3 (Core) | active reward mapping and display name | *not decoded* |   | Not decoded |   |
| Objects\_Common/Rare\_Chest (Prior canonical explicit entity setting; active reward mapping unresolved) | common entity set chance | 0 | percent | Earlier table |   |
| Objects\_Common/Rare\_Chest (Prior canonical explicit entity setting; active reward mapping unresolved) | rare entity set chance | 0 | percent | Earlier table |   |
| Objects\_Common/Rare\_Chest (Prior canonical explicit entity setting; active reward mapping unresolved) | epic entity set chance | 0 | percent | Earlier table |   |
| Objects\_Common/Rare\_Chest (Prior canonical explicit entity setting; active reward mapping unresolved) | legendary entity set chance | 50 | percent | Earlier table |   |
| Objects\_Common/Rare\_Chest (Prior canonical explicit entity setting; active reward mapping unresolved) | cursed entity set chance | 50 | percent | Earlier table |   |
| Objects\_Common/Rare\_Chest (Core) | active reward mapping and display name | *not decoded* |   | Not decoded |   |
| Storm\_Island/Objects\_Storm\_Island!Boss\_Shrine\_Jinn\_Reward (Prior canonical explicit entity setting; active reward mapping unresolved) | common entity set chance | 0 | percent | Earlier table |   |
| Storm\_Island/Objects\_Storm\_Island!Boss\_Shrine\_Jinn\_Reward (Prior canonical explicit entity setting; active reward mapping unresolved) | rare entity set chance | 0 | percent | Earlier table |   |
| Storm\_Island/Objects\_Storm\_Island!Boss\_Shrine\_Jinn\_Reward (Prior canonical explicit entity setting; active reward mapping unresolved) | epic entity set chance | 0 | percent | Earlier table |   |
| Storm\_Island/Objects\_Storm\_Island!Boss\_Shrine\_Jinn\_Reward (Prior canonical explicit entity setting; active reward mapping unresolved) | legendary entity set chance | 0 | percent | Earlier table |   |
| Storm\_Island/Objects\_Storm\_Island!Boss\_Shrine\_Jinn\_Reward (Prior canonical explicit entity setting; active reward mapping unresolved) | cursed entity set chance | 100 | percent | Earlier table |   |
| Storm\_Island/Objects\_Storm\_Island!Boss\_Shrine\_Jinn\_Reward (Core) | active reward mapping and display name | *not decoded* |   | Not decoded |   |
| Storm\_Island/Quest\_Sinbad!Quest\_Cyclop!Sinbad\_Cyclop\_Quest\_Reward\_Spawner (Prior canonical explicit entity setting; active reward mapping unresolved) | common entity set chance | 0 | percent | Earlier table |   |
| Storm\_Island/Quest\_Sinbad!Quest\_Cyclop!Sinbad\_Cyclop\_Quest\_Reward\_Spawner (Prior canonical explicit entity setting; active reward mapping unresolved) | rare entity set chance | 0 | percent | Earlier table |   |
| Storm\_Island/Quest\_Sinbad!Quest\_Cyclop!Sinbad\_Cyclop\_Quest\_Reward\_Spawner (Prior canonical explicit entity setting; active reward mapping unresolved) | epic entity set chance | 0 | percent | Earlier table |   |
| Storm\_Island/Quest\_Sinbad!Quest\_Cyclop!Sinbad\_Cyclop\_Quest\_Reward\_Spawner (Prior canonical explicit entity setting; active reward mapping unresolved) | legendary entity set chance | 100 | percent | Earlier table |   |
| Storm\_Island/Quest\_Sinbad!Quest\_Cyclop!Sinbad\_Cyclop\_Quest\_Reward\_Spawner (Prior canonical explicit entity setting; active reward mapping unresolved) | cursed entity set chance | 0 | percent | Earlier table |   |
| Storm\_Island/Quest\_Sinbad!Quest\_Cyclop!Sinbad\_Cyclop\_Quest\_Reward\_Spawner (Core) | active reward mapping and display name | *not decoded* |   | Not decoded |   |
| Storm\_Island/Quest\_Sinbad!Quest\_Roc!Roc\_Quest\_Reward\_Spawner (Prior canonical explicit entity setting; active reward mapping unresolved) | common entity set chance | 0 | percent | Earlier table |   |
| Storm\_Island/Quest\_Sinbad!Quest\_Roc!Roc\_Quest\_Reward\_Spawner (Prior canonical explicit entity setting; active reward mapping unresolved) | rare entity set chance | 0 | percent | Earlier table |   |
| Storm\_Island/Quest\_Sinbad!Quest\_Roc!Roc\_Quest\_Reward\_Spawner (Prior canonical explicit entity setting; active reward mapping unresolved) | epic entity set chance | 0 | percent | Earlier table |   |
| Storm\_Island/Quest\_Sinbad!Quest\_Roc!Roc\_Quest\_Reward\_Spawner (Prior canonical explicit entity setting; active reward mapping unresolved) | legendary entity set chance | 100 | percent | Earlier table |   |
| Storm\_Island/Quest\_Sinbad!Quest\_Roc!Roc\_Quest\_Reward\_Spawner (Prior canonical explicit entity setting; active reward mapping unresolved) | cursed entity set chance | 0 | percent | Earlier table |   |
| Storm\_Island/Quest\_Sinbad!Quest\_Roc!Roc\_Quest\_Reward\_Spawner (Core) | active reward mapping and display name | *not decoded* |   | Not decoded |   |

### Difficulties

| Name | Stat | Value | Unit | Status | In-game check |
|---|---|---|---|---|---|
| Adventure (Adventure) | game rule description | Game rules set by default |   | Fixed text |   |
| Adventure (Adventure) | enemy health modifier | *not decoded* |   | Not decoded |   |
| Adventure (Adventure) | enemy damage modifier | *not decoded* |   | Not decoded |   |
| Adventure (Adventure) | enemy stagger resistance modifier | *not decoded* |   | Not decoded |   |
| Adventure (Adventure) | master nightmare health modifier | *not decoded* |   | Not decoded |   |
| Adventure (Adventure) | master nightmare damage modifier | *not decoded* |   | Not decoded |   |
| Adventure (Adventure) | master nightmare stagger resistance modifier | *not decoded* |   | Not decoded |   |
| Adventure (Adventure) | healing orb modifier | *not decoded* |   | Not decoded |   |
| Adventure (Adventure) | corrupted spawn rule probability | *not decoded* |   | Not decoded |   |
| Adventure (Adventure) | high rank spawn rule probability | *not decoded* |   | Not decoded |   |
| Adventure (Adventure) | inherited modifier rules | *not decoded* |   | Not decoded |   |
| Twilight (Twilight) | game rule description | Corrupted enemies can appear<br>Master Nightmares are stronger |   | Fixed text |   |
| Twilight (Twilight) | enemy health modifier | *not decoded* |   | Not decoded |   |
| Twilight (Twilight) | enemy damage modifier | *not decoded* |   | Not decoded |   |
| Twilight (Twilight) | enemy stagger resistance modifier | *not decoded* |   | Not decoded |   |
| Twilight (Twilight) | master nightmare health modifier | *not decoded* |   | Not decoded |   |
| Twilight (Twilight) | master nightmare damage modifier | *not decoded* |   | Not decoded |   |
| Twilight (Twilight) | master nightmare stagger resistance modifier | *not decoded* |   | Not decoded |   |
| Twilight (Twilight) | healing orb modifier | *not decoded* |   | Not decoded |   |
| Twilight (Twilight) | corrupted spawn rule probability | *not decoded* |   | Not decoded |   |
| Twilight (Twilight) | high rank spawn rule probability | *not decoded* |   | Not decoded |   |
| Twilight (Twilight) | inherited modifier rules | *not decoded* |   | Not decoded |   |
| Darkness (Darkness) | game rule description | Healing orbs heal less<br>Master Nightmares are even stronger! |   | Fixed text |   |
| Darkness (Darkness) | enemy health modifier | *not decoded* |   | Not decoded |   |
| Darkness (Darkness) | enemy damage modifier | *not decoded* |   | Not decoded |   |
| Darkness (Darkness) | enemy stagger resistance modifier | *not decoded* |   | Not decoded |   |
| Darkness (Darkness) | master nightmare health modifier | *not decoded* |   | Not decoded |   |
| Darkness (Darkness) | master nightmare damage modifier | *not decoded* |   | Not decoded |   |
| Darkness (Darkness) | master nightmare stagger resistance modifier | *not decoded* |   | Not decoded |   |
| Darkness (Darkness) | healing orb modifier | *not decoded* |   | Not decoded |   |
| Darkness (Darkness) | corrupted spawn rule probability | *not decoded* |   | Not decoded |   |
| Darkness (Darkness) | high rank spawn rule probability | *not decoded* |   | Not decoded |   |
| Darkness (Darkness) | inherited modifier rules | *not decoded* |   | Not decoded |   |
| Nightmare (Nightmare) | game rule description | More high-rank enemies<br>All enemies are stronger! |   | Fixed text |   |
| Nightmare (Nightmare) | enemy health modifier | *not decoded* |   | Not decoded |   |
| Nightmare (Nightmare) | enemy damage modifier | *not decoded* |   | Not decoded |   |
| Nightmare (Nightmare) | enemy stagger resistance modifier | *not decoded* |   | Not decoded |   |
| Nightmare (Nightmare) | master nightmare health modifier | *not decoded* |   | Not decoded |   |
| Nightmare (Nightmare) | master nightmare damage modifier | *not decoded* |   | Not decoded |   |
| Nightmare (Nightmare) | master nightmare stagger resistance modifier | *not decoded* |   | Not decoded |   |
| Nightmare (Nightmare) | healing orb modifier | *not decoded* |   | Not decoded |   |
| Nightmare (Nightmare) | corrupted spawn rule probability | *not decoded* |   | Not decoded |   |
| Nightmare (Nightmare) | high rank spawn rule probability | *not decoded* |   | Not decoded |   |
| Nightmare (Nightmare) | inherited modifier rules | *not decoded* |   | Not decoded |   |

### Timers

| Name | Stat | Value | Unit | Status | In-game check |
|---|---|---|---|---|---|
| Chapter Duration (Core) | total chapter time | *not decoded* |   | Not decoded |   |
| Chapter Duration (Core) | awakening to showdown interval | *not decoded* |   | Not decoded |   |
| Chapter Duration (Core) | Otohime timer formula | *not decoded* |   | Not decoded |   |
| Day/Night Cycle (Core) | phase duration | *not decoded* |   | Not decoded |   |
| Day/Night Cycle (Core) | initial phase | *not decoded* |   | Not decoded |   |
| Day/Night Cycle (Core) | transition schedule | *not decoded* |   | Not decoded |   |

Source: [`Mechanics_Values.tsv`](../data/Mechanics_Values.tsv).
*This page is generated from the TSV files in [data/](../data/) by `tools/build_browse.py`. Do not edit it by hand; fix the data and re-run the script.*
