# The Pied Piper

[All tables](../README.md)

[Abilities](#abilities) · [Ability values](#ability-values) · [Talents](#talents) · [Outfits](#outfits) · [Memoir](../memoirs/The_Pied_Piper.md)

Once the greatest musician of his generation until cursed by Nightmares, Franz the Pied Piper's songs have become distorted melodies of mass destruction, only pleasant to the ears of the rats that gather round him. When overwhelmed, the critters can be called to the rescue, unleashing a swarm of gnashing teeth.

## Abilities

| Slot | Name | Description |
|---|---|---|
| Trait | Infestation | • Rats spawn from the ground at regular intervals and follow the Hero (up to **`{0}`** rats)<br>• Activate to order all rats to attack enemies. They attack up to **`{1}`** times for **`{2}`** damage each and die afterwards |
| Attack | Flute | • Hold to play the flute, sending notes that deal **`{0}`** damage each<br>• Does not prevent movement but reduces Move Speed |
| Power | Solo | • Play a solo on the flute, sending **`{0}`** waves of **`{1}`** notes, each one dealing **`{2}`** damage<br>• Does not prevent movement but reduces Move Speed |
| Special | Fortissimo | • Create a zone of power that makes all enemies inside **VULNERABLE** |
| Defense | Acoustic Blast | • `{0}` briefly becomes **INTANGIBLE** then creates an accoustic blast, stunning and pushing back all enemies around |
| Ultimate 1 | Unchained Melody | • Play notes continuously and rapidly, automatically targeting the closest enemy and dealing up to **`{0}`** damage per second<br>• During this ability, the Hero runs forward but the direction can be controlled |
| Ultimate 2 | Plague of Rats | • Channel a melody to control a swarm of rats that rushes forward and deals up to **`{0}`** damage per second over a large area |

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
| Infestation | max rats | 20 | rats | Decoded | Matches the game |
| Infestation | attacks per rat | 3 | attacks | Decoded | Matches the game |
| Infestation | damage per attack | 5 | damage | Decoded (baseline) | Matches the game |
| Infestation | cooldown | 0 | seconds | Decoded | Matches the game |
| Infestation | charges | 1 | charges | Decoded (baseline) |   |
| Infestation | active duration | *not decoded* | seconds | Not decoded |   |
| Infestation | resource cost | *not decoded* | resource | Not decoded |   |
| Infestation | rat spawn interval | 9 | seconds | Decoded |   |

### Attack

| Name | Stat | Value | Unit | Status | In-game check |
|---|---|---|---|---|---|
| Flute | damage per note | *not decoded* | damage | Not decoded | Game shows 6 |
| Flute (night) (Night) | damage per note | *not decoded* | damage | Not decoded | Game shows 4 |
| Flute | hit count | *not decoded* | hits | Not decoded |   |
| Flute | hit damage sequence | *not decoded* | damage | Not decoded |   |
| Flute | attack timing | *not decoded* | seconds | Not decoded |   |
| Flute (night) (Night) | hit count | *not decoded* | hits | Not decoded |   |
| Flute (night) (Night) | hit damage sequence | *not decoded* | damage | Not decoded |   |
| Flute (night) (Night) | attack timing | *not decoded* | seconds | Not decoded |   |
| Flute | note frequency | *not decoded* | per second | Not decoded |   |
| Flute | movement speed reduction | *not decoded* | percent | Not decoded |   |
| Flute (night) (Night) | note frequency | *not decoded* | per second | Not decoded |   |
| Flute (night) (Night) | movement speed reduction | *not decoded* | percent | Not decoded |   |
| Flute | note interval | 0.15 | seconds | Decoded |   |

### Power

| Name | Stat | Value | Unit | Status | In-game check |
|---|---|---|---|---|---|
| Solo | cooldown | 4 | seconds | Decoded | Matches the game |
| Solo | charges | 1 | charges | Decoded (baseline) |   |
| Solo | wave count | *not decoded* | waves | Not decoded | Game shows 3 |
| Solo | notes per wave | 3 |   | Decoded (baseline) | Matches the game |
| Solo | damage per note | *not decoded* | damage | Not decoded | Game shows 12 |
| Solo (night) (Night) | damage per note | *not decoded* | damage | Not decoded | Game shows 8 |
| Solo | active duration | *not decoded* | seconds | Not decoded |   |
| Solo | resource cost | *not decoded* | resource | Not decoded |   |
| Solo (night) (Night) | cooldown | 4 | seconds | Decoded |   |
| Solo (night) (Night) | charges | 1 | charges | Decoded (baseline) |   |
| Solo (night) (Night) | active duration | *not decoded* | seconds | Not decoded |   |
| Solo (night) (Night) | resource cost | *not decoded* | resource | Not decoded |   |
| Solo | movement speed reduction | *not decoded* | percent | Not decoded |   |
| Solo (night) (Night) | wave count | *not decoded* | waves | Not decoded | Game shows 3 |
| Solo (night) (Night) | notes per wave | *not decoded* |   | Not decoded | Game shows 3 |
| Solo (night) (Night) | movement speed reduction | *not decoded* | percent | Not decoded |   |
| Solo | wave interval | 0.05 | seconds | Decoded |   |

### Special

| Name | Stat | Value | Unit | Status | In-game check |
|---|---|---|---|---|---|
| Fortissimo | cooldown | 16 | seconds | Decoded (baseline) | Matches the game |
| Fortissimo | charges | 1 | charges | Decoded (baseline) |   |
| Fortissimo | duration | 6 | seconds | Decoded (baseline) |   |
| Fortissimo | active duration | *not decoded* | seconds | Not decoded |   |
| Fortissimo | resource cost | *not decoded* | resource | Not decoded |   |

### Defense

| Name | Stat | Value | Unit | Status | In-game check |
|---|---|---|---|---|---|
| Acoustic Blast | cooldown | 8 | seconds | Decoded | Matches the game |
| Acoustic Blast | charges | 1 | charges | Decoded (baseline) |   |
| Acoustic Blast | stun duration | *not decoded* | seconds | Not decoded |   |
| Acoustic Blast | active duration | *not decoded* | seconds | Not decoded |   |
| Acoustic Blast | resource cost | *not decoded* | resource | Not decoded |   |
| Acoustic Blast | intangible duration | *not decoded* | seconds | Not decoded |   |

### Ultimate 1

| Name | Stat | Value | Unit | Status | In-game check |
|---|---|---|---|---|---|
| Unchained Melody | cooldown | *not decoded* | seconds | Not decoded | Game shows 90 |
| Unchained Melody | charges | 1 | charges | Decoded (baseline) |   |
| Unchained Melody | damage per second | *not decoded* | damage per second | Not decoded | Game shows 120 |
| Unchained Melody | resource cost | *not decoded* | resource | Not decoded |   |
| Unchained Melody | active duration | 7 | seconds | Decoded |   |

### Ultimate 2

| Name | Stat | Value | Unit | Status | In-game check |
|---|---|---|---|---|---|
| Plague of Rats | cooldown | *not decoded* | seconds | Not decoded | Game shows 60 |
| Plague of Rats | charges | 1 | charges | Decoded (baseline) |   |
| Plague of Rats | damage per second | *not decoded* | damage per second | Not decoded | Game shows 100 |
| Plague of Rats | resource cost | *not decoded* | resource | Not decoded |   |
| Plague of Rats | active duration | 4 | seconds | Decoded |   |

## Talents

Values separated by / are for Common / Rare / Epic / Legendary.

**Unlocks at rank** is the hero rank, not the level reached in a run.

### Starting talents

The talents offered at level 1 of a run. A starting talent not yet unlocked at your hero rank can still fill an empty card. The Lack of Inspiration modifier lowers the offer to 3 cards. See [TALENTS.md](../../TALENTS.md).

| Talent | Unlocks at rank | Effect |
|---|---|---|
| Horde | 1 | Rats spawn in groups of 3 (instead of 2)<br>Increase maximum controllable rats by 6 / 8 / 10 / 12 |
| Sound Barrier | 1 | Quest (x20): Gain +1.5 ARMOR whenever DEFENSE hits at least 2 enemies<br>Complete: Doing so again grants 15 / 18 / 21 / 24 SHIELD to all nearby Heroes for 6 seconds |
| Freezing Trap | 2 | Enemies within SPECIAL's area of effect are CHILLED and take +10 / 15 / 20 / 25% damage |
| Virtuoso | 5 | Move Speed when using ATTACK or POWER is increased by 30%<br>Gain +10 / 15 / 20 / 25% ATTACK Speed |

### Ultimates

The talent tables do not include the base ultimates or their unlock ranks; this text is from the hero's text table.

| Ultimate | Description |
|---|---|
| Unchained Melody | • Continuously play notes that target the closest enemy<br>• Movement is FORCED but the direction can be controlled |
| Plague of Rats | • Channel a melody to control a swarm of rats that rushes forward and deals damage over a large area |

### Ultimate upgrades

| Talent | Upgrades | Unlocks at rank | Effect |
|---|---|---|---|
| Jig | Unchained Melody | 1 | DASH sends 4 / 5 / 6 / 7 ULTIMATE notes to nearby enemies |
| Rain of Notes | Unchained Melody | 9 | During ULTIMATE, 12 / 15 / 18 / 21 notes per second fall from the sky in the surroundings, each dealing 10 area damage |
| Vermin Massacre | Plague of Rats | 6 | When ULTIMATE is channeled to completion, the swarm of rats explodes, dealing 200 / 250 / 300 / 350 area damage |
| Rat King | Plague of Rats | 9 | Each rat summoned has a 10 / 15 / 20 / 25% chance to be a Rat King, capable of attacking twice as much and dealing +150% damage |

### Other talents

| Talent | Unlocks at rank | Effect |
|---|---|---|
| Explosive Blast | 1 | DEFENSE deals 45 / 56.2 / 67.5 / 78.75 damage |
| Explosive Rats | 1 | Rats explode when they die and deal 6 / 7.5 / 9 / 10.5 damage all around |
| Extra Measure | 1 | After hitting an enemy with DEFENSE, the next POWER within 3 seconds lasts longer (+2 / 3 / 4 / 5 waves of notes) |
| Giant Rats | 1 | Rats' attacks WEAKEN enemies and deal +20 / 25 / 30 / 35% damage |
| Grand Finale | 1 | When SPECIAL's effect expires, the area of effect explodes and deals 60 / 75 / 90 / 105 damage |
| Quintuplets | 1 | POWER plays 5 notes each wave (instead of 3) but each note deals -20 / -15 / -10 / -5% damage |
| Sforzando | 1 | SPECIAL triggers an implosive DEFENSE (pulling enemies inwards) with its range increased by 20 / 25 / 30 / 35% |
| Sniper | 1 | Notes from ATTACK and POWER have a longer range and deal +20 / 25 / 30 / 35% damage if they hit after halfway |
| Perfect Harmony | 2 | DEFENSE restores 4 / 5 / 6 / 7 Health to all nearby Heroes for each enemy hit (up to 4) |
| Acoustic Pulses | 3 | SPECIAL deals 8 / 10 / 12 / 14 damage every second |
| Low Notes | 3 | ATTACK sends bigger notes that deal +60 / 75 / 90 / 105% damage in an area of effect but at a 40% reduced frequency |
| Spinning Solo | 4 | POWER triggered after DASH makes Hero move quicker and has +40 / 50 / 60 / 70% Crit Chance |
| Stimulant Vibes | 4 | Rats attacking within SPECIAL's zone deal +20% damage and have a 50 / 63 / 75 / 88% chance to summon a new rat upon death |
| Music of the Spheres | 5 | DASH leaves a bubbled clef that explodes when hit, sending 4 / 5 / 6 / 7 POWER music notes to enemies around |
| Chorus | 7 | Every 1 / 0.8 / 0.65 / 0.55 second(s), the SPECIAL area of effect fires 5 ATTACK notes, targeting the closest enemies |
| Invasive Blast | 7 | Hitting at least one enemy with DEFENSE spawns up to 4 / 5 / 6 / 7 rats, which immediately attack nearby enemies |
| Ghost Notes | 8 | For every 10 / 8 / 7 / 6 notes played, a ghost note is sent towards the nearest enemy, dealing 20 area damage |
| Leeching Charm | 8 | For every 20 attacks that rats made on enemies, restore 4 / 5 / 6 / 7 health to all nearby heroes |

## Outfits

| Outfit | How to unlock | Description |
|---|---|---|
| Signature Outfit | Completed 'Sound Barrier' Talent Quest | Unlocked by completing 'Sound Barrier' Talent Quest |
| Traveler Outfit | Reached Chapter 3 | Unlocked by reaching Chapter 3 |
| Master Outfit | Completed the game in Darkness Difficulty | Unlocked by completing the game  in Darkness Difficulty |
| Hidden Outfit | Rats Lover | Hidden Requirements |
| Ravens Outfit | Ravens Skin Pack Acquired | Available in the Ravens Skin Pack |
| Nightmares Outfit | Nightmares Skin Pack Acquired | Available in the Nightmares Skin Pack |
| Fairytales Outfit | Fairytales Skin Pack Acquired | Available in the Fairytales Skin Pack |
| Unleashed Outfit | Unleashed Skin Pack acquired | Available from the Unleashed Skin Pack |
| Mercenaries Outfit | Mercenaries Skin Pack Acquired | Available in the Mercenaries Skin Pack |


**How to read the text**

- **Bold** words are highlighted in the game.
- `{0}`, `{1}` and so on are numbers or names the game fills in while you play.

Source: [`Hero_Piper_Common.LangEN.tsv`](../../data/Hero_Piper_Common.LangEN.tsv), [`Hero_Piper_Abilities.tsv`](../../data/Hero_Piper_Abilities.tsv), [`Hero_Piper_Talents.tsv`](../../data/Hero_Piper_Talents.tsv), [`Hero_Piper_Skins.LangEN.tsv`](../../data/Hero_Piper_Skins.LangEN.tsv).
Game version: Game build 1.06 (Steam build ID 25174305); the displayed version string is unverified. See VERSION.json.

*This page is generated from the TSV files in [data/](../../data/) by `tools/build_browse.py`. Do not edit it by hand; fix the data and re-run the script.*
