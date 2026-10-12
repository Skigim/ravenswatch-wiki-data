# Changes in build 1.06

This report compares the `2026-10-06-values` snapshot, taken from version 1.05, with the `2026-10-12-1.06` snapshot. Build 1.06 shipped on October 12, 2026, with the Kintarō DLC. The tables were extracted from the Steam install the same day (Steam build ID 25174305). The version string the game displays was not recorded, so the attribution in [VERSION.json](VERSION.json) is `unverified`.

The report has four parts:

- A summary of what changed.
- Answers to the specific checks requested for this refresh.
- A comparison with the 1.06 patch notes.
- Kintarō facts and art paths.

Every changed row, file by file, follows in [Per-file changes](#per-file-changes).

## Summary

**Text and index exports.** All 43 published exports were re-extracted. 30 are byte for byte unchanged. 13 changed:

- `Common`: 7 rows added, and the 5 news and DLC rows were rewritten for 1.06.
- 10 hero `Common` tables: new and replacement talent text, mostly as new `_Update6` keys beside the old ones. Old keys stay in the tables.
- `Hero_Carmilla_Memoirs` and `Hero_Merlin_Memoirs`: text edits, and 7 new rows for Merlin.

Three Kintarō text tables are new.

**Talent tables.** All 12 hero tables were rebuilt, and Kintarō's is new.

- Five talents were replaced:
  - Scarlet: Reload and Short Wick → Deadly Combo and Focus. Short Wick's effect moved into Distant Explosions.
  - Beowulf: Secondary Tremor → Maelstrom.
  - Aladdin: Cyclonic Appearance and Dancing Blades → Jinn Charge and Spectral Blades.
- Of the 312 existing rows, 267 keep their 1.05 effect text and compendium check. 56 effects were re-rendered from the 1.06 data. 15 were written by hand where the data needed interpretation; the row notes say why.
- Merlin's talents are unchanged. Only byte offsets and argument graph indices moved.

**Value tables.** All 15 decoded value tables were rebuilt, and Kintarō's ability table is new. Row order is the same as in 1.05. The October 6 check columns are carried over. 10 checks are marked `stale: checked on 1.05; decoded value changed in 1.06`, where the decoded value or its formula changed:

| Table | Row | Field | 1.05 | 1.06 |
|---|---|---|---|---|
| The Snow Queen | Ice Shards | `damage` | 65 | 80 |
| The Snow Queen | Ice Shards | `bonus_damage_vs_chilled` | 50% | 50%. The formula gains an override branch |
| Scarlet | Gusting Roar | `cooldown` | Maximum 60 | Maximum 75, with a new minimum cooldown tied to Focus |
| Romeo | Black Roses | `cooldown` | Maximum 75 | Maximum 60 |
| Beowulf | Shockwave | `damage` | Base value unchanged | A new branch for Double Shock |
| Vajra | — | `damage_per_dash` | — | Gains a runtime binding (the YANG modifier fix) |
| The Goose Girl Melody | — | `wind_trigger_interval` | 15 | 10 |
| The Goose Girl Melody | — | `area_damage` | 150 | DMG × 10 (100 at the baseline) |
| The Little Tailor Melody | — | `consumables_per_qualifying_level` | 3 | 1 |
| The Little Tailor Melody | — | `exclusive_level_threshold` | 10 | 6 |

Aladdin's Enchanted Blades rows now point at `Ability_Special_Update6_Desc` (row 85), which replaces `Ability_Special_Desc` in 1.06. `In_Game_Observations.tsv` and `Fill_Pass_Values.tsv` hold 1.05 evidence and are unchanged.

## Requested checks

1. **Love Thread** (Romeo). The tooltip value is 265 / 330 / 395 / 460 damage per second (1.05: 200 / 250 / 300 / 350). The patch notes give 44 / 55 / 65 / 76, up from 33 / 41 / 50 / 58. Those figures are the data values divided by 6, which suggests they are per tick, not per second.
2. **Pack Leader** (Scarlet). Human: 5 / 6.25 / 7.5 / 8.7 health per second (1.05: 3 / 4 / 5 / 6). Werewolf: 15 / 18.75 / 22.5 / 26.2 to 28 / 35 / 42 / 49 SHIELD (1.05: 12.5 / 13.75 / 15 / 16.3 to 25 / 27.5 / 30 / 32.5). The patch notes round these figures.
3. **Panache** (Romeo). Each token gave +0.05 DMG in 1.05. In 1.06 it increases ATTACK damage by 20%. The ATTACK SPEED bonus of 4 / 5 / 6 / 7% is unchanged.
4. **Kick** (Romeo). It was 400 / 500 / 600 / 700% damage. It is a flat 48.4 / 60.5 / 72.6 / 84.7 damage: 10 × 1.1 × 4.4 / 5.5 / 6.6 / 7.7. The patch notes give 44 (400%) → 48 (436%). In the data, the Common multiplier is 4.4 on a base of 11 (10 × 1.1): 440%, or 48.4 damage. The notes' 436% is 48 ÷ 11.
5. **Stimulant Vibes** (The Pied Piper). The damage bonus is a flat +20% at every rarity (1.05: 20 / 25 / 30 / 35%). The new respawn chance is 50 / 63 / 75 / 88%.
6. **Wedding Gifts** (Juliet), all ranks. Common objects 25 / 30 / 35 / 40%, rare 12 / 15 / 17 / 19%, epic 6 / 7 / 8 / 9%. In 1.05: 20 / 25 / 30 / 35%, 10 / 12.5 / 15 / 17.5% and 5 / 6 / 7 / 8%.
7. **Ice Skating minimum cooldown** (The Snow Queen). `Ability Defense Min Cooldown` goes from 0 in 1.05 to 4 in 1.06, set in `Hero_Snow_Queen_Update6`. The Defensive controller cooldown stays 6. The patch notes say the minimum went from 2 to 5. The October 6 reading on 1.05 was 8 seconds. The data can't settle which figure the game shows; it needs a reading in 1.06.
8. **The Little Tailor wording.** The Melody's text is unchanged: "Grants #{0}@ consumables each time the group of Heroes reaches a level above {1}". The game text says "consumables", not "power ups". The values change from 3 to 1 per qualifying level and the threshold from 10 to 6.
9. **Life Tap** (Carmilla). With its values filled in and markup removed, the 1.06 tooltip reads: "In Winged Form, activating TRAIT again consumes health equivalent to 15% of max health to recover up to 40 / 50 / 60 / 70 BLOOD points. This ability cannot be used when below health cost and has a 10-second cooldown." The talent table renders it from the text key `Skill_Trait_Life_Tap_Desc` and the Life Tap health cost, BLOOD gain and cooldown components. The ability controller's own cooldown field goes from 30 to 0, so the 10-second cooldown comes from the Life Tap cooldown component.

## Comparison with the patch notes

### In the patch notes and confirmed by the data

Devourer, Murderous Intent, Evisceration, Pack Leader, Distant Explosions, Sound Barrier, Explosive Blast, Stimulant Vibes, Shield Charge, Sudden Growth, Battle Cry, Bladestorm, Frost Queen, Ice Spray, Ice Beam, Ice Cores, Aerial Catch, Master Puppet, the Unstable Cores delay, Way of Awakening, Thirst for Immortality, Focused Strikes, Seductive Provocation, Life Tap, Bat Master, Panache, Secret Weapon, Ice Rose, Volcanic Shots, Lucky Shot, and Guns and Roses.

Seductive Provocation now taunts 4 enemies for 6 / 7.5 / 9 / 10.5 seconds, at most every 6 seconds.

Two non-talent changes also match the notes:

- Meca-Puppet maximum health 200 → 180, in `Hero_Geppetto_MecaPuppet_Update6`.
- Stingy Jack: maximum health 275 → 300, and maximum stagger points 200 → 225 (`Stingy_Jack_Model`).

### In the patch notes but not found in the data, or different

- **Ice Skating.** See check 7. The data has a minimum of 4, not 5.
- **Carmilla's Blood Lash.** The patch notes give BLOOD gains going from 2 / 2 / 6 to 6 / 6 / 12. The data has Blood Gain Default 2 → 6, Finisher 4 → 12 and Add Zone Attack 4 → 8. The two lists can't be matched one to one.
- **Rat King** (The Pied Piper). The patch notes say explosive Rat damage +100%. The data has the bonus damage going from +100% to +150%.
- **Kick.** See check 4: the notes say 436%; the data gives 440%.
- **Love Thread.** See check 1: the notes' figures are per tick.
- **Hunter's Souvenir** (Scarlet). The notes say the ultimate no longer ends automatically. The data still has 2 charges. One controller flag changes from true to false, which fits the note, but that flag isn't decoded.
- **Shimmering Scales** (Melusine). The build-up time halves from 10 to 5 seconds. Spread evenly, that's +8 / 12 / 16 / 20 ARMOR per second, as in the notes. The per-second value passes through an engine-fed operand, so it isn't resolved from the data.
- **Kintarō's outfits.** The notes call one outfit "Explorer"; the game text calls it the Traveler Outfit. The notes list "Royal Counselor" among his premium outfits; that is a Merlin outfit. Kintarō's premium outfits are Ravens, Nightmares and Sakura.
- **Kintarō's first ultimate talent.** The notes spell it "Giant Carp Supplex". The game text is "Giant Carp Suplex"; the ultimate itself is "Giant Carp".

### In the data but not in the patch notes

- Rampart (Beowulf): the quest ARMOR goes from +1 to +1.5.
- Unstable Cores (Geppetto): damage 80 / 90 / 100 / 110 → 70 / 87.5 / 105 / 122.5.
- Flashy Ending (Juliet): maximum damage 540 / 607.5 / 675 / 742.5 → 540 / 675 / 810 / 945.
- Carmilla's second ultimate: stagger 32 / 32 / 8 → 24 / 24 / 12.
- Geppetto's finisher radius: 3.5 → 4.0.
- Scarlet's Werewolf first ultimate (Gusting Roar): maximum cooldown 60 → 75, and a new minimum cooldown selector tied to Focus (75 with Focus, otherwise 10).
- Beowulf's Wyrm: maximum size 1.4–2.0 → 2.0–2.6. This fits the notes' "larger zone".
- Aladdin's Power Wish: minimum range ratio 1.0 → 0.7. This fits Jinn's Might.
- Melusine's Defense: hold speed 4 → 5.
- Carmilla's Dash Taunt: animation speed 1.0 → 1.25.
- Life Tap: the ability controller's cooldown 30 → 0. See check 9.
- Juliet gains a Raw Max Health of 90 in `Hero_Juliet_Update6`.
- Every damage settings component (136 of them) gains one trailing field, `0.0`. This is a layout change, not a value change.

## Kintarō

**Name.** The display name is Kintarō. Files use the internal identifier `Kintaro`. His bear companion is Kuma.

**Trait.** Animal Bond. It doesn't split into Passive and Active descriptions like other heroes' traits. Instead it has a Mounted description and a Dismounted description, and the Dismounted one has keyboard and controller variants. INTERNAL DAMAGE is a highlighted game term (`#INTERNAL DAMAGE@`). On foot, Kintarō takes 30% of the damage Kuma sustains as internal damage. Riding Kuma heals it over time.

**Abilities.** Each slot has a Mounted and a Dismounted form:

| Slot | Mounted | Dismounted |
|---|---|---|
| Attack | Claw Swipes | Axe |
| Power | Charge | Whirl and Pound |
| Special | Leap | Double Leap |
| Defense | Roar | Roar and Shout |

The ultimates are Giant Carp and Rikishi. Giant Carp deals 150 area damage, then a 350 slam, with a 90-second cooldown. Rikishi's damage and cooldown aren't resolved from the data. [Hero_Kintaro_Abilities.tsv](data/Hero_Kintaro_Abilities.tsv) has 34 rows: 14 `decoded`, 15 `decoded-baseline` and 5 `unresolved`. None was checked in the game.

**Talents.** 26 talents: 11 at rank 1, two each at ranks 2 through 5, one at rank 6, and two each at ranks 7 through 9. All rows are datamined only. Two values aren't resolved from the data: Targeted Bite's damage, which is read at runtime from Kuma's entity, and Skewer's maximum, which multiplies a selector that has no rarity values.

**Memoirs.** Seven pages, each with a title, a description and an intro poem, under the memoir title "The Boy, the Bear, and the Brightest Flower".

**Outfits.**

| Outfit | How to get it | Icon |
|---|---|---|
| Default | — | `Icon_Skin_Kintaro_01` |
| Signature | Complete the Raijin Axe talent quest | `02Panda` |
| Traveler | Reach Chapter 3 | `03Jungle` |
| Master | Complete the game in Darkness difficulty | `04Polar` |
| Hidden | Hidden requirement; the unlock text is "Floral dream" | `05Kabuki` |
| Ravens | Kintarō DLC | `06Raven` |
| Nightmares | Kintarō DLC | `07Nightmare` |
| Sakura | Kintarō DLC (internal key `Unleashed`) | `08Unleashed` |

**Unlock requirement.** The game text for the premium outfits is "Available in the Kintarō DLC". The hero itself comes with the DLC.

## Art paths

No art is in this repository. These are paths in the decoded 1.06 tree, relative to `Ui/`. Each file ends in `.png.Texture.dxt`.

**Portraits and hero select:**

- `Heroes/Kintaro!Portrait_Kintaro_01`
- `BookMenu/Heroes!UI_HeroPortrait_Kintaro_Active`, `_Locked`, `_Standart` and `_Unavailable`
- `Common/NewHeroPic!NewHero_Kintaro`
- `Heroes/Kintaro!HUD_Banner_Kintaro`
- `BookMenu/UI_Ability_Icon_Kintaro`

**Trait and ability icons:** `Heroes/Kintaro!Ability_Kintaro_<Form>_<Slot>`, where `<Form>` is `Mounted` or `Dismounted` and `<Slot>` is `Trait`, `Attack`, `Power`, `Special` or `Defensive`. The Dismounted trait also has `Dismounted_Trait_Alt`. The ultimates are `Ability_Kintaro_Ultimate_1` and `Ability_Kintaro_Ultimate_2`. Each icon has a `_Disabled` variant.

**Kintarō talent icons:**

| Talent | Path |
|---|---|
| Berserk | `Heroes/Kintaro!Skill Passive Damage Per Internal Damage` |
| Bold Strike | `Heroes/Kintaro!Skill Defense Attack Block` |
| Boomerang Axe | `Heroes/Kintaro!Skill Power Throws Axe` |
| Brutal Taming | `Heroes/Kintaro!Skill Ultimate 1 Slam` |
| Crushing Combo | `Heroes/Kintaro!Skill Special Buff After Power` |
| Deafening Cry | `Heroes/Kintaro!Skill Defense Deals Damage` |
| Dohyo | `Heroes/Kintaro!Skill Ultimate 2 Heal` |
| Energy Discharge | `Heroes/Kintaro!Skill Passive Ability Attack` |
| Forest Spirits | `Heroes/Kintaro!Skill Defense Summon Spirit` |
| Frenzy | `Heroes/Kintaro!Skill Attack Chain Speed` |
| Hardened Skin | `Heroes/Kintaro!Skill Passive Armor` |
| Hearty Aura | `Heroes/Kintaro!Skill Passive Move Speed` |
| Leaping Dash | `Heroes/Kintaro!Skill Special Dash After Power` |
| Mend Pet | `Heroes/Kintaro!Skill Trait Heal` |
| Nekodamashi | `Heroes/Kintaro!Skill Ultimate 2 Clap` |
| Power Charge | `Heroes/Kintaro!Skill Power Hold` |
| Raijin Axe | `Heroes/Kintaro!Skill Attack Quest Lightning` |
| Rain of Fish | `Heroes/Kintaro!Skill Ultimate 1 Projectile` |
| Rush Strikes | `Heroes/Kintaro!Skill Dash Attack` |
| Shattered Earth | `Heroes/Kintaro!Skill Special Delayed AOE` |
| Skewer | `Heroes/Kintaro!Skill Power Chain Damage` |
| Stampede | `Heroes/Kintaro!Skill Power Bear Charge` |
| Strong-Willed | `Heroes/Kintaro!Skill Passive Internal Damage` |
| Targeted Bite | `Heroes/Kintaro!Skill Attack Bite` |
| Unchained Beast | `Heroes/Kintaro!Skill Passive Bear Combo` |
| Woodcutter's Swipe | `Heroes/Kintaro!Skill Attack Special Swipe` |

**Replacement talent icons:**

| Talent | Path |
|---|---|
| Deadly Combo | `Heroes/Red!Skill Power End AOE` |
| Focus | `Heroes/Red!Skill Ultimate 1 Piercing Shot Tornado` |
| Maelstrom | `Heroes/Beowulf!Skill_Special_Finisher_More_Damage` |
| Jinn Charge | `Heroes/Aladdin!Skill Dash After Power` |
| Spectral Blades | `Heroes/Aladdin!Skill Special Retrieved AOE` |

The same tree also has Kintarō's Codex illustrations, footer and corner pictures, outfit icons, credits art, a minimap icon and the Berserk gauge mask.

## Per-file changes

Text tables are compared by key, talent tables by talent name, and value tables by row position. Internal operand and binding indices renumber in every rebuilt file, so formulas and notes are compared with those indices normalized. Byte offsets, roster order, argument graphs and reference chains change in almost every row. They're counted per file, not listed. `(blank)` marks an empty cell.

### Common.LangEN.tsv

Rows: 528 → 535. Added 7, removed 0, text changed 5, index moved 3.

| Change | Index | Key | Old | New |
|---|---|---|---|---|
| added | 525 | `Options_PrivacyPolicyCateg` | | CONFIDENTIALITY POLICY |
| added | 529 | `Options_VoiceChatModeDisabledByGameChat` | | Voice chat disabled by GameChat |
| added | 530 | `Options_DisplayPing` | | Display latency |
| added | 531 | `Book_Page_Max_player` | | Party maximum size |
| added | 532 | `Status_Intangible` | | Intangible |
| added | 533 | `Status_Invincible` | | Invincible |
| added | 534 | `Status_Blocking` | | Blocking |
| changed | 459 → 459 | `Social_Page_DLC_Title` | DLC - Mercenaries Skin Pack | New DLC – Kintarō |
| changed | 460 → 460 | `Social_Page_DLC_Desc` | Wear new Mercenaries Outfits – for The Pied Piper, Snow Queen, Aladdin, Geppetto, and Sun Wukong. | Kintarō joins the Ravenswatch! Fight alongside your Bear, or join forces by riding on its back! |
| changed | 461 → 461 | `Social_Page_PatchNote_Title` | New Update - Songs of Thieves | New Update - Free Content |
| changed | 462 → 462 | `Social_Page_PatchNote_Desc` | Thieves are coming to the land of Reverie in Ravenswatch's latest free update! Find out more about the new content in the full patch notes. | Learn more about reworked Heroes' Talents, balancing changes and quality of life improvements in the full patch notes. |
| changed | 466 → 466 | `Book_Page_News_Redirect_Desc` | IT'S AN AMBUSH!\n\nThis new free update to Ravenswatch is shaking up the world of Reverie with the arrival of the Thieves and their formidable stashes. What could they be hiding in their treasure rooms filled with deadly traps? Complete the various Melodies to become even stronger, but watch out for any sticky fingers after your Dream Shards!\n\nMultiplayer pause has also been added, along with a new Mercenaries Skin Pack.\n\nLearn more about the new content in the official trailer and the full patch note.\n\n• The Passtech Games Team | KINTARŌ JOINS THE RAVENSWATCH!\n\nPlay as the Golden boy Kintarō, a legendary hero straight from Japanese folklore! Mount Kuma, the Bear, for a fierce and brutal battle against the Nightmares! Or fight side by side with your loyal companion and your incredible strength!\n\nThis paid Hero DLC includes a new character with a unique playstyle and premium Outfits for Ravenswatch's battlefield. \n\nA free update is also now available for all players, which includes a Heroes Talents overhaul and more! Find out about the new hero and the recent changes in the full patch notes.\n\n• The Passtech Games Team |

Index moves: `Menu_Pause_Remaining` 525 → 526, `Menu_Pause_Delay_Time_Left` 526 → 527, `Book_Page_Melodies` 527 → 528.

### Hero_Aladdin_Common.LangEN.tsv

Rows: 81 → 86. Added 5, removed 0, text changed 0, index moved 0.

| Change | Index | Key | Old | New |
|---|---|---|---|---|
| added | 81 | `Skill_Dash_After_Power_Name` | | Jinn Charge |
| added | 82 | `Skill_Dash_After_Power_Desc` | | • #DASH@ used after #POWER@ summons the Jinn to charge through enemies and deal &{1}~ damage  |
| added | 83 | `Skill_Special_Retrieved_AOE_Name` | | Spectral Blades |
| added | 84 | `Skill_Special_Retrieved_AOE_Desc` | | • Retrieving #SPECIAL@'s blades before they return to {0} triggers a flurry of attacks that can deal up to &{1}~ area damage |
| added | 85 | `Ability_Special_Update6_Desc` | | • Throw scimitars: They move forward, stop to spin, then return to {0}, dealing up to &{1}~ damage\n• Scimitars gain #ENCHANTMENT@ points for each enemy hit\n• Blades can be recalled sooner by triggering #SPECIAL@ again |

### Hero_Beowulf_Common.LangEN.tsv

Rows: 76 → 81. Added 5, removed 0, text changed 0, index moved 0.

| Change | Index | Key | Old | New |
|---|---|---|---|---|
| added | 76 | `Skill_Special_Loop_Name_Update6` | | Bladestorm |
| added | 77 | `Skill_Special_Loop_Desc_Update6` | | • #SPECIAL@ spins &{0}~ more time(s) for #{1}%@ damage each\n• {2} remains #INTANGIBLE@ throughout additional spins |
| added | 78 | `Skill_Special_Finisher More Damage_Name` | | Maelstrom |
| added | 79 | `Skill_Special_Finisher More Damage_Desc` | | • #SPECIAL@'s final hit deals &+{0}%~ damage for each different enemy already hit (up to #+{1}%@) |
| added | 80 | `Skill_Trait_Battlecry_Update6_Desc` | | • #TRAIT@ increases Move Speed by #{2}%@ and grants &{0}~ #SHIELD@ to all Heroes in the area for #{1}@ seconds |

### Hero_Carmilla_Common.LangEN.tsv

Rows: 80 → 80. Added 0, removed 0, text changed 2, index moved 0.

| Change | Index | Key | Old | New |
|---|---|---|---|---|
| changed | 26 → 26 | `Skill_Dash_Taunt_Desc` | • Using #DASH@ without specifying a move direction makes {0} seduce up to &{1}~ non-boss enemies in front of her, applying #WEAKENED@ and #VULNERABLE@ to them for #{2}@ seconds | • Using #DASH@ without specifying a move direction makes {0} seduce up to #{1}@ non-boss enemies in front of her, applying #WEAKENED@ and #VULNERABLE@ to them for &{2}~ seconds (every #{3}@ seconds max) |
| changed | 28 → 28 | `Skill_Dash_Blood_Desc` | • Each enemy passed through by #DASH@ earns &{0}~ $BLOOD* | • Each enemy passed through while using #DASH@ earns &{0}~ $BLOOD* |

### Hero_Carmilla_Memoirs.LangEN.tsv

Rows: 15 → 15. Added 0, removed 0, text changed 1, index moved 0.

| Change | Index | Key | Old | New |
|---|---|---|---|---|
| changed | 12 → 12 | `Carmilla_Memoir6_Desc` | My precious Laura,\n\nOur friends of the Watch left me alone to mourn your betrayal, though I know they shared my pain. I was inconsolable for weeks, wishing I had the disposition to take my own life. An easier darker path began to tease my mind. I could simply join you and the witch, abandonning my human nature, to become a horror alongside the woman I loved.\n\nAnd so I began to send you letters, asking for you to come and meet me when the moon was at its fullest and the sun its farthest from the dusk and dawn. You joined me in all your splendor, with eyes aglow and hunger in your bosom. We kissed.\n\nI like to think that I saw a last glimmer of your human soul as I drove the wooden stake deep into your heart. The tears in my eyes were playing tricks on my vision. A thousand moments of joy and happiness passed before me as your light went out.\n\nI buried you in your family vault alongside the tombs of those who had raised you. I wept upon your grave, filled with the pain one can only know when one has truly loved. Wherever you had gone, I would soon join you. I set off to kill the Witch.\n\nYour eternal love, Carmilla | My precious Laura,\n\nOur friends of the Watch left me alone to mourn your betrayal, though I know they shared my pain. I was inconsolable for weeks, wishing I had the disposition to take my own life. An easier darker path began to tease my mind. I could simply join you and the witch, abandoning my human nature, to become a horror alongside the woman I loved.\n\nAnd so I began to send you letters, asking for you to come and meet me when the moon was at its fullest and the sun its farthest from the dusk and dawn. You joined me in all your splendor, with eyes aglow and hunger in your bosom. We kissed.\n\nI like to think that I saw a last glimmer of your human soul as I drove the wooden stake deep into your heart. The tears in my eyes were playing tricks on my vision. A thousand moments of joy and happiness passed before me as your light went out.\n\nI buried you in your family vault alongside the tombs of those who had raised you. I wept upon your grave, filled with the pain one can only know when one has truly loved. Wherever you had gone, I would soon join you. I set off to kill the Witch.\n\nYour eternal love, Carmilla |

### Hero_Juliet_Common.LangEN.tsv

Rows: 75 → 76. Added 1, removed 0, text changed 0, index moved 0.

| Change | Index | Key | Old | New |
|---|---|---|---|---|
| added | 75 | `Skill_Attack_Update6_Burst_Desc` | | • #ATTACK@ triggered right after #DASH@ shoots &{0}~ times in a row, consuming #{1}@ \AMMO§ |

### Hero_Kintaro_Common.LangEN.tsv

New table, 83 rows.

### Hero_Kintaro_Memoirs.LangEN.tsv

New table, 22 rows.

### Hero_Kintaro_Skins.LangEN.tsv

New table, 21 rows.

### Hero_Melusine_Common.LangEN.tsv

Rows: 79 → 79. Added 0, removed 0, text changed 1, index moved 0.

| Change | Index | Key | Old | New |
|---|---|---|---|---|
| changed | 60 → 60 | `Skill_Defense_Hold_Desc` | • Hold #DEFENSE@ to move quickly underwater. All enemies passed become #VULNERABLE@ for &{0}~ seconds | • #DEFENSE@ can be held to move more quickly underwater\n• All enemies passed become #VULNERABLE@ for &{0}~ seconds |

### Hero_Merlin_Memoirs.LangEN.tsv

Rows: 15 → 22. Added 7, removed 0, text changed 7, index moved 0.

| Change | Index | Key | Old | New |
|---|---|---|---|---|
| added | 15 | `Merlin_Memoir1_Intro` | | "Ambitious maiden longs for power held by a mage.\nShe beds his body, steals his heart, and locks him in a cage." |
| added | 16 | `Merlin_Memoir2_Intro` | | "When Fallen King doth dream sans crown nor head to don its light.\nReverie shall form a flock of ravens cursed to fight." |
| added | 17 | `Merlin_Memoir3_Intro` | | "Immortal mage shall kneel before the ancient sage of dreams\nAnd learn that light and laughter harbor shadows and their screams." |
| added | 18 | `Merlin_Memoir4_Intro` | | "And all the soothsayer's carefree thoughts in prophecy transpire.\nCompanions desperate for a seer make little of his ire." |
| added | 19 | `Merlin_Memoir5_Intro` | | "A demon spawn of human mother drinks the witch's brew.\nWhile Raven warriors ponder omens destined yet untrue." |
| added | 20 | `Merlin_Memoir6_Intro` | | "The prophet mage decrees a future no man can debate.\nThe hero warrior writes new lines oblivious of fate." |
| added | 21 | `Merlin_Memoir7_Intro` | | "The love of Merlin shall return when prophecies abate.\nOnly then can Vivian determine her own fate." |
| changed | 2 → 2 | `Merlin_Memoir1_Desc` | "Ambitious maiden longs for power held by a mage.\nShe beds his body, steals his heart, and locks him in a cage."\n\nI know these words were written by my hand, \nsome centuries past before thee, Vivian, \ndid trap me in a tomb of amber stone.\nI know within them hides a glimpse of morrows\none day proven true. My prophecies\nare legend. Oracle and sage, the mystic \nmage, Merlin's verse the voice of Delphi.\n\nI know as well for I foresaw its coming,\nhow you trapped me in a jail cell staved \nwith tree-root bars. Thou'st needed sunshine free \nof mentor's shadow. Hence I let thee cage\nme, mind and body, 'til thee found thy footing,\nfree to walk amongst the trees alone.\nAlas, I do not know, nor can I fathom\nwhy thee let me leave my prison cave\nbereft of future sight. I read my words\nonce written with full grasp of deeds\nunfolding under moons to come, yet am\na fool before their meaning now. I ask,\ndear Vivian, what are thy plans for me?\n\nThine mentor past and lover still, a trusting \nfriend unto the Otherworld beyond. | I know these words were written by my hand, \nsome centuries past before thee, Vivian, \ndid trap me in a tomb of amber stone.\nI know within them hides a glimpse of morrows\none day proven true. My prophecies\nare legend. Oracle and sage, the mystic \nmage, Merlin's verse the voice of Delphi.\n\nI know as well for I foresaw its coming\nhow you trapped me in a jail cell staved \nwith tree-root bars. Thou'st needed sunshine free \nof mentor's shadow. Hence I let thee cage\nme, mind and body, 'til thee found thy footing\nfree to walk amongst the trees alone.\nAlas, I do not know, nor can I fathom\nwhy thee let me leave my prison cave\nbereft of future sight. I read my words\nonce written with full grasp of deeds\nunfolding under moons to come, yet am\na fool before their meaning now. I ask,\ndear Vivian, what are thy plans for me?\n\nThine mentor past and lover still, a trusting \nfriend unto the Otherworld beyond. |
| changed | 4 → 4 | `Merlin_Memoir2_Desc` | "When Fallen King doth dream sans crown nor head to don its light.\nReverie shall form a flock of ravens cursed to fight."\n\nThis verse I wrote four centuries past and had\nforgotten every word. 'Til Morgan Fey \nunrolled the scroll and asked me what would follow.\nFor Arthur's bones now lack his skull and Mordred's \nghost has turned into a crown thief, stalking \ntombstone hollows. Damned I'd be, were I\nto know, my forsooth inklings dried and withered.\nThe Fey Queen Morgan would not hear my plight. \nShe'd known me enigmatic, every word \na riddle, every phrase a coaxing spell.\nWe too had once been lovers for a century,\nmaybe two. Once learning all I'd had \nto teach, she sprouted wings, away she flew.\nAnd now, though I had carefully explained\nhow Vivian had locked me up and freed \nme, leaving mind and soul intact, without \nmy power to oracle, nor recall futures seen.\n\nFey Morgan would not hear of it. She thinks\nme old and vain. "While Reverie is dying,\nMerlin laughs and has his game, 'til demon \nmischief's course is run and all our joys \nunsung." Dear Vivian, return to me, I cannot\nhelp without my power of prophecy. | This verse I wrote four centuries past and had\nforgotten every word. 'Til Morgan Fey \nunrolled the scroll and asked me what would follow.\nFor Arthur's bones now lack his skull and Mordred's \nghost has turned into a crown thief, stalking \ntombstone hollows. Damned I'd be, were I\nto know, my forsooth inklings dried and withered.\nThe Fey Queen Morgan would not hear my plight. \nShe'd known me enigmatic, every word \na riddle, every phrase a coaxing spell.\nWe too had once been lovers for a century,\nmaybe, two. Once learning all I'd had \nto teach, she sprouted wings, away she flew.\nAnd now though I had carefully explained\nhow Vivian had locked me up and freed \nme leaving mind and soul intact, without \nmy power to oracle, nor recall futures seen.\n\nFey Morgan would not hear of it. She thinks\nme old and vain. "While Reverie is dying\nMerlin laughs and has his game, 'til demon \nmischief's course is run and all our joys \nunsung." Dear Vivian return to me, I cannot\nhelp without my power of prophecy. |
| changed | 6 → 6 | `Merlin_Memoir3_Desc` | \n"Immortal mage shall kneel before the ancient sage of dreams\nAnd learn that light and laughter harbor shadows and their screams."\n\nMy prophecies when read without my soothing \nsight, give pause to ponder whether weed \nand mead were not at work when put to quill.\nAlas, the Sandman, Lord of Sleep, I came \nto meet in seeking answers to my blindness.\n"Merlin, mage, you've wandered far astray.\nThe only remedy for those who wish \nto see the world that is to be, is planted\ndeep within your fabled family tree."\nAnd then he proffered me a hero's quest.\n"Embrace the Raven's Watch, old friend, as wizard,\nsage and leader. Free our lands of witch's \nminions and your vision shall return."\n\nAnd so, my Vivian, off I go to fight\nagainst these foreign demons, well aware \nthat my own father born of hellish blood\nmight run amongst their ilk and fiendish kind.\nIf this quest should lead to where you keep\nmy powers locked, I do no longer know.\nThis journey is a first for me to witness\nonly that which stands before me in\nthe now. And so, to serendipity, \nI vow to take this path, where'er it leads.\nYour erstwhile wizard sage of Raven's Watch | My prophecie when read without my soothing \nsight, give pause to ponder whether weed \nand mead were not at work when put to quill.\nAlas the Sandman, Lord of Sleep, I came \nto meet in seeking answers to my blindness.\n"Merlin mage, you've wandered far astray.\nThe only remedy for those who wish \nto see the world that is to be, is planted\ndeep within your fabled family tree."\nAnd then he proffered me a hero's quest.\n"Embrace the Raven's Watch old friend as wizard,\nsage and leader. Free our lands of witch's \nminions and your vision shall return."\n\nAnd so my Vivian off I go to fight\nagaint these foreign demons, well aware \nthat my own father born of hellish blood\nmight run amongst their ilk and fiendish kind.\nIf this quest should lead to where you keep\nmy powers locked, I do no longer know.\nThis journey is a first for me to witness\nonly that which stands before me in\nthe now. And so to serendipity \nI vow to take this path where'er it leads.\nYour erstwhile wizard sage of Raven's Watch |
| changed | 8 → 8 | `Merlin_Memoir4_Desc` | \n"And all the soothsayer's carefree thoughts in prophecy transpire.\nCompanions desperate for a seer make little of his ire."\n\nAgain 'tis I who wrote that cryptic verse\nsome centuries ago. And only now \nis meaning met. Cassandra comes to mind.\nIn Troy, no hero, friend or foe, would heed \nthe warning in her words of future doom.\nIn Reverie, my curse is surely worse.\nFor every word I utter, whether jest\nor greetings lightly made, is turned\nto omen or portentous proof of something\nhorrid yet to come. Though I protest,\nand I confess my farsight in me's lacking,\nthe warriors of the watch are drawn to fear\nmy reputation as a sorcerer and seer.\n\nFor in this hour where witches roam and Nightmares\nwrite anew our fabled tales. I say \n"hello", and off they go, headlong into \nbattle. I say "goodnight, what starry night",\nand sleepless hours await them, hatching plans.\nI find myself running hither to the fray,\na-casting spells to save the day my careless \nwords had set so rapidly afoot.\nAnd so, my Vivian, I beg for mercy,\nnot for me but those who need truesight. | Again 'tis I who wrote that cryptic verse\nsome centuries ago. And only now \nis meaning met. Cassandra comes to mind.\nIn Troy no hero, friend or foe, would heed \nthe warning in her words of future doom.\nIn Reverie my curse is surely worse.\nFor every word I utter, whether jest\nor greetings lightly made is turned\nto omen or portentous proof of something\nhorrid yet to come. Though I protest\nand I confess my farsight in me's lacking,\nthe warriors of the watch are drawn to fear\nmy reputation as a sorceror and seer.\n\nFor in this hour where witches roam and Nightmares\nwrite anew our fabled tales. I say \n"hello" and off they go headlong into \nbattle. I say "goodnight, what starry night"\nand sleepless hours await them hatching plans.\nI find myself running hither to the fray\na-casting spells to save the day my careless \nwords had set so rapidly afoot.\nAnd so my Vivian, I beg for mercy\nnot for me but those who need truesight. |
| changed | 10 → 10 | `Merlin_Memoir5_Desc` | \n"A demon spawn of human mother drinks the witch's brew.\nWhile Raven warriors ponder omens destined yet untrue."\n\nI dreamt a dream last night, a songe sent by\nmy devil father speaking with his guile.\nHe helped me see quite woefully that you\nwere not the sorceress who'd opened up \nmy cage, nor laid the curse to steal the powers\ngifted by my spawner. A wailful witch \nnamed Baba Yaga was she alone to blame. \n"Woe on her, her doom is nigh," according\nto my father. Omen spoken, words \nin demon tongue, a prophecy from hell.\n\nBlast this witch of icy climes from o'er \nthe Volga vales. I take the fight to Baba!\nHer nightmare minions hail from nowhere known\non earth, nor hell, nor Otherworldly realm.\nMy fellow Raven keepers are too human \nto avail. In fact, I've grown too fond of them \nto let them risk their lives in battle with this \ncauldron-wielding witch from sleepless hell.\nSince every word I speak to them, they turn\nto prophecy, I've told them I must fight\nthis fight alone, "'Tis written in the stars."\nAnd so, my love, farewell to thee, should Baba\nYaga triumph, task to lock this witch \naway and save what's left of Reverie. | I dreamt a dream last night, a songe sent by\nmy devil father speaking with his guile.\nHe helped me see quite woefully that you\nwere not the sorceress who'd opened up \nmy cage, nor laid the curse to steal the powers\ngifted by my spawner. A wailful witch \nnamed Baba Yaga was she alone to blame. \n"Woe on her, her doom is nigh," according\nto my father. Omen spoken, words \nin demon tongue, a prophecy from hell.\n\nBlast this witch of icy climes from o'er \nthe Volga vales. I take the fight to Baba!\nHer nightmare minions hail from nowhere known\non earth, nor hell, nor Otherworldly realm.\nMy fellow Raven keepers are too human \nto avail. In fact I've grown too fond of them \nto let them risk their lives in battle with this \ncauldron wielding witch from sleepless hell.\nSince every word I speak to them they turn\nto prophecy, I've told them I must fight\nthis fight alone, "'Tis written in the stars."\nAnd so my love farewell to thee, should Baba\nYaga triumph, task to lock this witch \naway and save what's left of Reverie. |
| changed | 12 → 12 | `Merlin_Memoir6_Desc` | "The prophet mage decrees a future no man can debate.\nThe hero warrior writes new lines oblivious of fate."\n\nSweet Vivian, I have returned a victor\no'er the witch. Our Baba Yaga fought\nwith savage fury, equal to my spells.\nI would have died had not the Watch\nappeared in greater numbers than her minions\ncould repel. She finally fell to druid \nmagic, mixed with snow-queen ice and dragon\nfire, a piper's song, a mermaid's chant,\nand wolfen warrior's thrashings. Flax-haired maiden \nboy in tow, with Romeo and lovely \nJuliet. Geppetto backed Carmilla as\nAladdin with Wukong closed out our ranks.\n\nMy prophecy of single battle, I \nagainst the witch, they'd thrown aside and leapt\nto fray, their superstitions swept aside. \n'Twas then I saw what makes a man or woman\nbrave. To face one's death, a certainty,\ndefying even fate for greater good.\nIf prophecy has any worth, it cannot\nbe in champion's song. For future sight, \nit sheds no light, but steals the hero's heart.\nI must ponder this predicament\nuntil I've learned the lesson meant for me. | Sweet Vivian I have returned a victor\no'er the witch. Our Baba Yaga fought\nwith savage fury, equal to my spells.\nI would have died had not the Watch\nappeared in greater numbers than her minions\ncould repel. She finally fell to druid \nmagic, mixed with snow-queen ice, and dragon\nfire, a piper's song, a mermaid's chant,\nand wolfen warrior's thrashings. Flax-haired maiden \nboy in tow, with Romeo and lovely \nJuliet. Gepetto backed Carmilla as\nAladdin with Wukong closed out our ranks.\n\nMy prophecy of single battle, I \nagainst the witch, they'd thrown aside and leapt\nto fray, their superstitions swept aside. \n'twas then I saw what makes a man or woman\nbrave. To face one's death, a certainty,\ndefying even fate for greater good.\nIf prophecy has any worth it cannot\nbe in champion's song. For future sight \nit sheds no light, but steals the hero's heart.\nI must ponder this predicament\nuntil I've learned the lesson meant for me. |
| changed | 14 → 14 | `Merlin_Memoir7_Desc` | \n"The love of Merlin shall return when prophecies abate.\nOnly then can Vivian determine her own fate."\n\nAt last, I now can see just why you locked\nyour mentor fast in stone. Our fleshly commerce\nset aside, our harps, our singing through the night.\nThere were no future choices made beyond \nthe verse your lover voiced in parchment and \non stone. How ever could you learn from follies\nof your own device, if by and by \nthe words I'd woven traced your every step.\n\nI pen this final missive, dear, written \nwithout malice. Hopeful how your heart\nwill read it, for my future sight has went\nand gone. I've come to love these days of question: \nmornings bear a sentiment of hope, 'til night\ncomes all too quickly, sleep a promise of\nanother day. Finally I have cast \naside my demon gifts, more truly now \na human son I've finally become.\nWould you, my Vivian, return to love \na man without a vision for the future? \nNothing more have I to give, all powers \nyou have mastered, all my secrets you've \nrevealed. There's nothing left in me but love \nfor thee, my harp and legendary wit. | At last I now can see just why you locked\nyour mentor fast in stone. Our fleshly commerce\nset aside, our harps, our singing through the night.\nThere were no future choices made beyond \nthe verse your lover voiced in parchment and \non stone. How ever could you learn from follies\nof your own device, if bye and bye \nthe words I'd woven traced your every step.\n\nI pen this final missive, dear, written \nwithout malice. Hopeful how your heart\nwill read it, for my future sight has went\nand gone. I've come to love these days of question: \nmornings bear a sentiment of hope, 'til night\ncomes all too quickly, sleep a promise of\nanother day. Finally I have cast \naside my demon gifts, more truly now \na human son I've finally become.\nWould you, my Vivian, return to love \na man without a vision for the future? \nNothing more have I to give, all powers \nyou have mastered, all my secrets you've \nrevealed. There's nothing left in me but love \nfor thee, my harp and legendary wit. |

### Hero_Piper_Common.LangEN.tsv

Rows: 82 → 83. Added 1, removed 0, text changed 0, index moved 0.

| Change | Index | Key | Old | New |
|---|---|---|---|---|
| added | 82 | `Skill_Trait_Pets_Within_Special_Update6_Desc` | | • Rats attacking within #SPECIAL@'s zone deal #+{0}%@ damage and have a &{1}%~ chance to summon a new rat upon death |

### Hero_RED_Common.LangEN.tsv

Rows: 96 → 103. Added 7, removed 0, text changed 0, index moved 0.

| Change | Index | Key | Old | New |
|---|---|---|---|---|
| added | 96 | `Skill_Power_Wolf_Quest_Desc_Update6` | | • #Repeatable Quest@: Each kill with #Werewolf POWER@ earns &+{0}~ #DMG@{1} |
| added | 97 | `Skill_Power_End_AOE_Name` | | Deadly Combo |
| added | 98 | `Skill_Power_End_AOE_Desc` | | • #POWER@ ends with an area attack dealing &{0}%~ damage |
| added | 99 | `Skill_Ultimate_Piercing_Shot_Tornado_Name` | | Focus |
| added | 100 | `Skill_Ultimate_Piercing_Shot_Tornado_Desc` | | • #Human@: The shotgun fires piercing bullets with greater range, dealing &{0}~ damage\n• #Werewolf@: The gust summons a tornado that remains on the ground, dealing &{1}~ damage per second |
| added | 101 | `Skill_Special_Can_Hold_Update6_Name` | | Distant Explosions |
| added | 102 | `Skill_Special_Can_Hold_Update6_Desc` | | • #SPECIAL@ now targets a farther location and deals &+{0}%~ damage \n• #Human@: #SPECIAL@ no longer affects {1} and bomb explodes as soon as it hits the ground |

### Hero_Romeo_Common.LangEN.tsv

Rows: 73 → 75. Added 2, removed 0, text changed 0, index moved 0.

| Change | Index | Key | Old | New |
|---|---|---|---|---|
| added | 73 | `Skill_Attack_Panache_Update6_Desc` | | • Hitting an enemy with any additional #ATTACK@ move, such as #DASH@ attack or #DEFENSE@'s #Ripost@, grants one #Panache token@ (up to #{0}@) \n• Each #Panache token@ increases #ATTACK@ damage by #{3}%@ and grants &+{1}%~ #ATTACK SPEED@, all #Panache tokens@ are lost when {2} is hit |
| added | 74 | `Skill_Attack_Kick_Update6_Desc` | | • Adds a kick to #ATTACK@ combo, dealing &{0}~ damage and pushing light enemies back |

### Hero_Snow_Queen_Common.LangEN.tsv

Rows: 80 → 82. Added 2, removed 0, text changed 0, index moved 0.

| Change | Index | Key | Old | New |
|---|---|---|---|---|
| added | 80 | `Skill_Passive_Better_Frost_Update_6_Desc` | | • Frost generated by your abilities remains on the ground for &{0}~ seconds\n• Enemies #CHILLED@ by {2} suffer #{1}@ damage per second |
| added | 81 | `Skill_Special_Icicles_Update6_Desc` | | • Each enemy hit by #POWER@ summons #2@ cores of ice (up to #{0}@)\n• The #SPECIAL@ consumes each core to fire an #ATTACK@ dealing &{1}%~ damage |

### Hero_SunWukong_Common.LangEN.tsv

Rows: 73 → 74. Added 1, removed 0, text changed 0, index moved 0.

| Change | Index | Key | Old | New |
|---|---|---|---|---|
| added | 73 | `Skill_Passive_Objects_Quest_Update6_Desc` | | • #Quest (x{0}):@ Obtaining a Magical Object with an Epic quality or better grants #+{1} DMG@\n• #Complete:@ Grants &+{2}~ #VITALITY@, but now $only Hero or Magical Object heals* are effective |

### Hero_Aladdin_Talents.tsv

Rows: 26 → 26. Added 2, removed 2.

| Talent | Change | Old | New |
|---|---|---|---|
| Cyclonic Appearance | removed | When triggering POWER, Jinn hits all nearby enemies and deals 50 / 60 / 70 / 80% of POWER's damage | |
| Dancing Blades | removed | Spin duration of SPECIAL's blades is increased by 75 / 100 / 125 / 150%\nBlades can be recalled sooner by triggering SPECIAL again | |
| Jinn Charge | added (rank 1) | | DASH used after POWER summons the Jinn to charge through enemies and deal 25 / 31.25 / 37.5 / 43.7 damage |
| Spectral Blades | added (rank 1) | | Retrieving SPECIAL's blades before they return to Aladdin triggers a flurry of attacks that can deal up to 44 / 55 / 66 / 77 area damage |
| Aerial Catch | `effect_en` | Quest (x15): After they hit an enemy, retrieving SPECIAL blades during DEFENSE grants +1 ARMOR\nComplete: Doing it again grants 12 / 15 / 18 / 21 SHIELD to all nearby Heroes for 6 seconds | Quest (x15): After they hit an enemy, retrieving SPECIAL blades during DEFENSE grants +2 ARMOR\nComplete: Doing it again grants 12 / 15 / 18 / 21 SHIELD to all nearby Heroes for 6 seconds |

Trace-only changes (offsets, roster order, argument graphs): 62 cells.

### Hero_Beowulf_Talents.tsv

Rows: 26 → 26. Added 1, removed 1.

| Talent | Change | Old | New |
|---|---|---|---|
| Secondary Tremor | removed | SPECIAL sends out a Shockwave, dealing 120 / 150 / 180 / 210% of POWER damage | |
| Maelstrom | added (rank 7) | | SPECIAL's final hit deals +24 / 30 / 36 / 42% damage for each different enemy already hit (up to +120 / 150 / 180 / 210%) |
| Battle Cry | `desc_key` | Skill_Trait_Battlecry_Desc | Skill_Trait_Battlecry_Update6_Desc |
| Battle Cry | `effect_en` | Activating TRAIT clears POWER cooldown for all Heroes in the area and gives them a 12 / 15 / 18 / 21 SHIELD for 6 seconds | TRAIT increases Move Speed by 15% and grants 12 / 15 / 18 / 21 SHIELD to all Heroes in the area for 6 seconds |
| Bladestorm | `desc_key` | Skill_Special_Loop_Desc | Skill_Special_Loop_Desc_Update6 |
| Bladestorm | `effect_en` | Special performs 2 / 3 / 4 / 5 additional spins for 100% damage each | Special performs 2 / 3 / 4 / 5 additional spins for 100% damage each\nBeowulf remains INTANGIBLE throughout additional spins |
| Rampart | `effect_en` | Quest (x20): blocking at least one attack during Defense grants +1 Armor\nComplete: Wyrm Defense heals 50 / 60 / 70 / 80% more in a larger radius | Quest (x20): blocking at least one attack during Defense grants +1.5 Armor\nComplete: Wyrm Defense heals 50 / 60 / 70 / 80% more in a larger radius |
| Shield Charge | `effect_en` | DEFENSE makes Beowulf dash forward and deal +100 / 125 / 150 / 175% damage along the path | DEFENSE makes Beowulf dash forward and deal +150 / 187.5 / 225 / 262.5% damage along the path |
| Sudden Growth | `effect_en` | During ULTIMATE, the Wyrm grows and breathes fire in a wider zone, dealing +20 / 25 / 30 / 35% damage | During ULTIMATE, the Wyrm grows and breathes fire in a wider zone, dealing +40 / 50 / 60 / 70% damage |

Trace-only changes (offsets, roster order, argument graphs): 60 cells.

### Hero_Carmilla_Talents.tsv

Rows: 26 → 26. Added 0, removed 0.

| Talent | Change | Old | New |
|---|---|---|---|
| Bat Master | `effect_en` | When not in combat, DEFENSE grants STEALTH and can be held without consuming BLOOD\nDEFENSE deals +40 / 50 / 60 / 70% damage\nSTEALTH make Carmilla undetectable by enemies | When not in combat, DEFENSE grants STEALTH and can be held without consuming BLOOD\nDEFENSE deals +20 / 25 / 30 / 35% damage\nSTEALTH make Carmilla undetectable by enemies |
| Life Tap | `effect_en` | In Winged Form, activating TRAIT again consumes 20% of maximum health to recover up to 30 / 40 / 50 / 60 BLOOD points.\nCannot be used below the health cost; has a 5-second cooldown. | In Winged Form, activating TRAIT again consumes 15% of maximum health to recover up to 40 / 50 / 60 / 70 BLOOD points.\nCannot be used below the health cost; has a 10-second cooldown. |
| Life Tap | `notes` | (blank) | The tooltip text matches two string-format components that bind the same three values; the values come from the Life Tap health cost, BLOOD gain and cooldown components. |
| Puncture | `effect_en` | Each enemy passed through by DASH earns 8 / 10 / 12 / 14 BLOOD | Each enemy passed through while using DASH earns 8 / 10 / 12 / 14 BLOOD |
| Seductive Provocation | `effect_en` | Using DASH without specifying a move direction makes Carmilla seduce up to 2 / 3 / 4 / 5 non-boss enemies in front of her, applying WEAKENED and VULNERABLE to them for 6 seconds | Using DASH without specifying a move direction makes Carmilla seduce up to 4 non-boss enemies in front of her, applying WEAKENED and VULNERABLE to them for 6 / 7.5 / 9 / 10.5 seconds (every 6 seconds max) |

Trace-only changes (offsets, roster order, argument graphs): 50 cells.

### Hero_Geppetto_Talents.tsv

Rows: 26 → 26. Added 0, removed 0.

| Talent | Change | Old | New |
|---|---|---|---|
| Master Puppet | `effect_en` | When the Meca-Puppet is built, it consumes any DUMMY built around to gain 20 / 25 / 30 / 35% max. health and deal 10 / 12 / 14 / 16% more damage per DUMMY consumed | When the Meca-Puppet is built, it consumes any DUMMY built around to gain 32 / 40 / 48 / 56% max. health and deal 16 / 20 / 24 / 28% more damage per DUMMY consumed |
| Unstable Cores | `effect_en` | 5 seconds after their creation, DUMMIES become unstable\nIf an unstable DUMMY is hit with POWER - or if it is destroyed or dismantled - this will cause it to explode, dealing 80 / 90 / 100 / 110 area damage | 3 seconds after their creation, DUMMIES become unstable\nIf an unstable DUMMY is hit with POWER - or if it is destroyed or dismantled - this will cause it to explode, dealing 70 / 87.5 / 105 / 122.5 area damage |

Trace-only changes (offsets, roster order, argument graphs): 52 cells.

### Hero_Juliet_Talents.tsv

Rows: 26 → 26. Added 0, removed 0.

| Talent | Change | Old | New |
|---|---|---|---|
| Flashy Ending | `effect_en` | Dancing gauge can be filled up according to the synchronization of Romeo and Juliet's movements during ULTIMATE\nTrigger an explosion at the end of the dance dealing from 270 / 337.5 / 405 / 472.5 to 540 / 607.5 / 675 / 742.5 area damage (based on dancing gauge level) | Dancing gauge can be filled up according to the synchronization of Romeo and Juliet's movements during ULTIMATE\nTrigger an explosion at the end of the dance dealing from 270 / 337.5 / 405 / 472.5 to 540 / 675 / 810 / 945 area damage (based on dancing gauge level) |
| Guns & Roses | `effect_en` | Quest (x10): Hitting an enemy by exploding Romeo's Rose with a PERFECT SHOT grants +1 DMG\nComplete: Rose explosions triggered with a PERFECT SHOT gain +50% range and deals +20 / 25 / 30 / 35% damage | Quest (x10): Hitting an enemy by exploding Romeo's Rose with a PERFECT SHOT grants +1 DMG\nComplete: Rose explosions triggered with a PERFECT SHOT gain +50% range and deals +28 / 35 / 42 / 49% damage |
| Lucky Shot | `effect_en` | ATTACKS have a 6 / 8 / 10 / 12% chance to turn into a POWER shot | ATTACKS have a 4 / 5 / 6 / 7% chance to turn into a POWER shot |
| Volcanic Shots | `desc_key` | Skill_Attack_Burst_Desc | Skill_Attack_Update6_Burst_Desc |
| Volcanic Shots | `effect_en` | ATTACK triggered right after DASH shoots 3 / 4 / 5 / 6 times in a row, consuming only one AMMO | ATTACK triggered right after DASH shoots 3 / 4 / 5 / 6 times in a row, consuming 3 AMMO |
| Wedding Gifts | `effect_en` | Whenever they obtain a Magical Object, Juliet and Romeo have a 20 / 25 / 30 / 35%/10 / 12.5 / 15 / 17.5%/5 / 6 / 7 / 8% chance to gift the other the same common, rare or epic Magical Object | Whenever they obtain a Magical Object, Juliet and Romeo have a 25 / 30 / 35 / 40%/12 / 15 / 17 / 19%/6 / 7 / 8 / 9% chance to gift the other the same common, rare or epic Magical Object |

Trace-only changes (offsets, roster order, argument graphs): 46 cells.

### Hero_Kintaro_Talents.tsv

Rows: 0 → 26. Added 26, removed 0.

| Talent | Change | Old | New |
|---|---|---|---|
| Berserk | added (rank 3) | | Gain +0.08 / 0.1 / 0.12 / 0.14 DMG for every 10% of maximum health set as INTERNAL DAMAGE |
| Bold Strike | added (rank 5) | | Canceling DEFENSE with an ATTACK triggers a finisher that blocks enemy attacks and deals 200 / 250 / 300 / 350% damage |
| Boomerang Axe | added (rank 3) | | When triggering POWER, Kintarō throws his axe, which bounces up to 2 times between nearby enemies, dealing 20 / 25 / 30 / 35% damage to each target hit |
| Brutal Taming | added (rank 9) | | During ULTIMATE, Kintarō grabs the carp by the tail and slams it violently against the ground three times, with each strike dealing 60 / 75 / 90 / 105% area damage |
| Crushing Combo | added (rank 7) | | SPECIAL triggered shortly after POWER gains +25% range and deals +40 / 50 / 60 / 70% damage |
| Deafening Cry | added (rank 1) | | While using DEFENSE, Kuma deals up to 60 / 75 / 90 / 105 damage in an area in front of him\nIf Kintarō is on foot, he applies VULNERABLE to enemies in front of him for 4 / 5 / 6 / 7 seconds |
| Dohyo | added (rank 9) | | Before channeling his ULTIMATE, Kintarō tosses salt into the air to create an arena around him\nAll Heroes within the arena recover health equal to 12 / 15 / 18 / 21% of their maximum health every second |
| Energy Discharge | added (rank 7) | | While Kintarō is on foot, using POWER, SPECIAL or DEFENSE triggers an energy discharge between Kintarō and Kuma, dealing 40 / 50 / 60 / 70 damage to enemies passed through |
| Forest Spirits | added (rank 8) | | Whenever Kintarō blocks an attack, a Forest Spirit appears around him (up to 6)\nFor each successful ATTACK, a Forest Spirit is released, dealing 20 / 25 / 30 / 35 damage, and then disappears |
| Frenzy | added (rank 1) | | Each ATTACK that hits an enemy grants Kintarō and Kuma +3 / 5 / 7 / 9% ATTACK SPEED (up to +25%)\nThese bonuses are lost after going 3 seconds without hitting an enemy with an ATTACK |
| Hardened Skin | added (rank 4) | | Gain +30 / 45 / 60 / 75 ARMOR\nWhile Kintarō is on foot, Kuma benefits from 25% of Kintarō's ARMOR |
| Hearty Aura | added (rank 1) | | While Kintarō is riding Kuma, he and all nearby Heroes gain +16 / 20 / 24 / 28% MOVE SPEED |
| Leaping Dash | added (rank 8) | | Using DASH just after POWER makes Kintarō leap forward and triggers a SPECIAL effect in the area around where he lands, dealing 40 / 50 / 60 / 70% SPECIAL damage |
| Mend Pet | added (rank 1) | | Whenever Kintarō mounts Kuma, he recovers 8 / 10 / 12 / 14 health\nThis Talent has a 10 second cooldown |
| Nekodamashi | added (rank 6) | | Before channeling his ULTIMATE, Kintarō claps his hands to deal 100 / 125 / 150 / 175 damage and 100 stagger points to enemies in front of him |
| Power Charge | added (rank 1) | | POWER can be held to store up to 3 levels of charge before it is released\nEach charge level increases its Crit Chance by 12 / 15 / 18 / 21% |
| Raijin Axe | added (rank 5) | | Quest (x10): Spending 100 Dream Shards grants +0.01 Crit Chance\nComplete: ATTACK finisher sends 3 lightning strikes to nearby enemies, with each strike dealing 12 / 15 / 18 / 21 damage |
| Rain of Fish | added (rank 1) | | ULTIMATE slam launches 12 / 15 / 18 / 21 fishes in the air that then fall to the ground, with each one dealing 20 area damage |
| Rush Strikes | added (rank 1) | | ATTACK triggered right after DASH quickly strikes twice, with each strike dealing 200 / 250 / 300 / 350% ATTACK damage |
| Shattered Earth | added (rank 1) | | SPECIAL leaves a fractured area that explodes after a short time, dealing 40 / 50 / 60 / 70% area damage |
| Skewer | added (rank 1) | | POWER deals +40 / 50 / 60 / 70% damage for each different enemy hit, up to a maximum |
| Stampede | added (rank 1) | | When Kintarō is on foot, moving Kuma causes him to charge in the indicated direction, dealing 80 / 100 / 120 / 140% POWER damage to enemies hit\nThis talent has a cooldown of 5 seconds |
| Strong-Willed | added (rank 1) | | When Kintarō is on foot, he takes 20 / 25 / 30 / 35% of the damage he suffers as INTERNAL DAMAGE |
| Targeted Bite | added (rank 2) | | Kuma's ATTACKS have a 50% chance to turn into a bite, hitting a single target |
| Unchained Beast | added (rank 2) | | While Kintarō is on foot, Kuma can chain attacks the same way he does while Kintarō is riding him, dealing +100 / 125 / 150 / 175% damage in total |
| Woodcutter's Swipe | added (rank 4) | | Kintarō's ATTACK, triggered shortly after a SPECIAL, performs a sweep of his axe that deals 90 / 112.5 / 135 / 157.5 area damage |

### Hero_Melusine_Talents.tsv

Rows: 26 → 26. Added 0, removed 0.

| Talent | Change | Old | New |
|---|---|---|---|
| Shimmering Scales | `effect_en` | In SING STANCE, Melusine gains temporary +4 / 6 / 8 / 10 ARMOR every second, up to a maximum of 40 / 60 / 80 / 100 | In SING STANCE, Melusine gains temporary ARMOR every second, up to a maximum of 40 / 60 / 80 / 100 |
| Shimmering Scales | `notes` | (blank) | ARMOR per second isn't resolved from the data. 1.06 halves the build-up time from 10 to 5 seconds; spread evenly, that is +8 / 12 / 16 / 20 per second, as in the patch notes (1.05: +4 / 6 / 8 / 10). The tooltip's own value multiplies and divides by 2 around an engine-fed operand, so it can't be evaluated statically. |
| Underwater Predation | `effect_en` | Hold DEFENSE to move quickly underwater. All enemies passed become VULNERABLE for 4 / 5 / 6 / 7 seconds | DEFENSE can be held to move more quickly underwater\nAll enemies passed become VULNERABLE for 4 / 5 / 6 / 7 seconds |

Trace-only changes (offsets, roster order, argument graphs): 52 cells.

### Hero_Merlin_Talents.tsv

Rows: 26 → 26. Added 0, removed 0.

Trace-only changes (offsets, roster order, argument graphs): 52 cells.

### Hero_Piper_Talents.tsv

Rows: 26 → 26. Added 0, removed 0.

| Talent | Change | Old | New |
|---|---|---|---|
| Explosive Blast | `effect_en` | DEFENSE deals 40 / 50 / 60 / 70 damage | DEFENSE deals 45 / 56.2 / 67.5 / 78.75 damage |
| Rat King | `effect_en` | Each rat summoned has a 10 / 15 / 20 / 25% chance to be a Rat King, capable of attacking twice as much and dealing +100% damage | Each rat summoned has a 10 / 15 / 20 / 25% chance to be a Rat King, capable of attacking twice as much and dealing +150% damage |
| Sound Barrier | `effect_en` | Quest (x20): Gain +1 ARMOR whenever DEFENSE hits at least 2 enemies\nComplete: Doing so again grants 12 / 15 / 18 / 21 SHIELD to all nearby Heroes for 6 seconds | Quest (x20): Gain +1.5 ARMOR whenever DEFENSE hits at least 2 enemies\nComplete: Doing so again grants 15 / 18 / 21 / 24 SHIELD to all nearby Heroes for 6 seconds |
| Stimulant Vibes | `desc_key` | Skill_Trait_Pets_Within_Special_Desc | Skill_Trait_Pets_Within_Special_Update6_Desc |
| Stimulant Vibes | `effect_en` | Rats attacking within SPECIAL's zone cannot die, and deal +20 / 25 / 30 / 35% damage | Rats attacking within SPECIAL's zone deal +20% damage and have a 50 / 63 / 75 / 88% chance to summon a new rat upon death |

Trace-only changes (offsets, roster order, argument graphs): 53 cells.

### Hero_RED_Talents.tsv

Rows: 26 → 26. Added 2, removed 2.

| Talent | Change | Old | New |
|---|---|---|---|
| Reload | removed | Every 16 / 14 / 12 / 10 times POWER, SPECIAL or DEFENSE is used, clear ULTIMATE cooldown | |
| Short Wick | removed | Human: SPECIAL no longer affects Scarlet and bomb explodes as soon as it hits the ground\nSPECIAL recharges 20 / 25 / 30 / 35% faster in both forms | |
| Deadly Combo | added (rank 1) | | POWER ends with an area attack dealing 40 / 50 / 60 / 70% damage |
| Focus | added (rank 9) | | Human: The shotgun fires piercing bullets with greater range, dealing 350 / 437.5 / 525 / 612.5 damage\nWerewolf: The gust summons a tornado that remains on the ground, dealing 70 / 87.5 / 105 / 122 damage per second |
| Devourer | `desc_key` | Skill_Power_Wolf_Quest_Desc | Skill_Power_Wolf_Quest_Desc_Update6 |
| Devourer | `effect_en` | Quest (x20): Each kill with Werewolf POWER earns +0.5 DMG\nComplete: POWER has a 40 / 60 / 80 / 100% chance to have no cooldown if it kills an enemy (for both forms) | Repeatable Quest: Each kill with Werewolf POWER earns +0.4 / 0.5 / 0.6 / 0.7 DMG |
| Distant Explosions | `desc_key` | Skill_Special_Can_Hold_Desc | Skill_Special_Can_Hold_Update6_Desc |
| Distant Explosions | `effect_en` | SPECIAL now targets a farther location and deals +40 / 50 / 60 / 70% damage | SPECIAL now targets a farther location and deals +40 / 50 / 60 / 70% damage\nHuman: SPECIAL no longer affects Scarlet and bomb explodes as soon as it hits the ground |
| Evisceration | `effect_en` | Each Combo Point spent by POWER applies 8 / 10 / 12 / 14% damage dealt in the form of BLEED | Each Combo Point spent by POWER applies 16 / 20 / 24 / 28% damage dealt in the form of BLEED |
| Murderous Intent | `effect_en` | DEFENSE instantly bestows 2 Combo Points and lasts 20 / 25 / 30 / 35% longer | DEFENSE instantly bestows 3 Combo Points and lasts 20 / 25 / 30 / 35% longer |
| Pack Leader | `effect_en` | Human: Ash cloud restores 3 / 4 / 5 / 6 hit points per second to all Heroes within\nWerewolf: Eating an enemy applies a 12.5 / 13.75 / 15 / 16.3 to 25 / 27.5 / 30 / 32.5 SHIELD to all heroes around (depending on its size) | Human: Ash cloud restores 5 / 6.25 / 7.5 / 8.7 hit points per second to all Heroes within\nWerewolf: Eating an enemy applies a 15 / 18.75 / 22.5 / 26.2 to 28 / 35 / 42 / 49 SHIELD to all heroes around (depending on its size) |

Trace-only changes (offsets, roster order, argument graphs): 64 cells.

### Hero_Romeo_Talents.tsv

Rows: 26 → 26. Added 0, removed 0.

| Talent | Change | Old | New |
|---|---|---|---|
| Ice Rose | `effect_en` | POWER now throws ice Roses, applying CHILLED to hit enemies\nPOWER deals +40 / 50 / 60 / 70% damage | POWER now throws ice Roses, applying CHILLED to hit enemies\nPOWER deals +32 / 40 / 48 / 56% damage |
| Kick | `desc_key` | Skill_Attack_Kick_Desc | Skill_Attack_Kick_Update6_Desc |
| Kick | `effect_en` | Adds a kick to ATTACK combo, dealing 400 / 500 / 600 / 700% damage and pushing light enemies back | Adds a kick to ATTACK combo, dealing 48.4 / 60.5 / 72.6 / 84.7 damage and pushing light enemies back |
| Love Thread | `effect_en` | Using TRAIT casts a beam towards Juliet for 6 second(s), dealing 200 / 250 / 300 / 350 damage per second to crossed enemies | Using TRAIT casts a beam towards Juliet for 6 second(s), dealing 265 / 330 / 395 / 460 damage per second to crossed enemies |
| Panache | `desc_key` | Skill_Attack_Panache_Desc | Skill_Attack_Panache_Update6_Desc |
| Panache | `effect_en` | Hitting an enemy with any additional ATTACK move, such as DASH attack or DEFENSE's Ripost, grants one Panache token (up to 3) \nEach Panache token grants +0.05 DMG and +4 / 5 / 6 / 7% ATTACK SPEED, all Panache tokens are lost when Romeo is hit | Hitting an enemy with any additional ATTACK move, such as DASH attack or DEFENSE's Ripost, grants one Panache token (up to 3)\nEach Panache token increases ATTACK damage by 20% and grants +4 / 5 / 6 / 7% ATTACK SPEED, all Panache tokens are lost when Romeo is hit |
| Secret Weapon | `effect_en` | Quest(x20): Blocking at least once during DEFENSE grants +0.5 DMG\nComplete: Ripost ATTACK after DEFENSE deals +32 / 40 / 48 / 56% damage per successful block (up to 3 times) | Quest(x20): Blocking at least once during DEFENSE grants +0.5 DMG\nComplete: Ripost ATTACK after DEFENSE deals +40 / 50 / 60 / 70% damage per successful block (up to 4 times) |

Trace-only changes (offsets, roster order, argument graphs): 49 cells.

### Hero_Snow_Queen_Talents.tsv

Rows: 26 → 26. Added 0, removed 0.

| Talent | Change | Old | New |
|---|---|---|---|
| Frost Queen | `desc_key` | Skill_Passive_Better_Frost_Desc | Skill_Passive_Better_Frost_Update_6_Desc |
| Frost Queen | `effect_en` | Frost generated by your abilities remains on the ground for 2 / 3 / 4 / 5 seconds\nCHILLED effects slow enemies by an additional 20% | Frost generated by your abilities remains on the ground for 2 / 3 / 4 / 5 seconds\nEnemies CHILLED by The Snow Queen suffer 5 damage per second |
| Ice Beam | `effect_en` | ULTIMATE now channels an ice beam, dealing 160 / 200 / 240 / 280% damage and inflicting CHILLED to first enemy hit | ULTIMATE now channels an ice beam, dealing 180 / 225 / 270 / 315% damage and inflicting CHILLED to first enemy hit |
| Ice Cores | `desc_key` | Skill_Special_Icicles_Desc | Skill_Special_Icicles_Update6_Desc |
| Ice Cores | `effect_en` | Each enemy hit by POWER summons a core of ice (up to 6)\nThe SPECIAL consumes each core to fire an ATTACK dealing 80 / 100 / 120 / 140% damage | Each enemy hit by POWER summons 2 cores of ice (up to 6)\nThe SPECIAL consumes each core to fire an ATTACK dealing 80 / 100 / 120 / 140% damage |
| Ice Spray | `effect_en` | SPECIAL sprays two bursts of ice shards in opposite directions, dealing +20 / 25 / 30 / 35% damage to CHILLED enemies. | SPECIAL sprays two bursts of ice shards in opposite directions, dealing +32 / 40 / 48 / 56% damage to CHILLED enemies. |

Trace-only changes (offsets, roster order, argument graphs): 54 cells.

### Hero_SunWukong_Talents.tsv

Rows: 26 → 26. Added 0, removed 0.

| Talent | Change | Old | New |
|---|---|---|---|
| Focused Strikes | `effect_en` | POWER can be held down to deliver the next strike to the same target and deals +12 / 16 / 20 / 24% damage | POWER can be held down to deliver the next strike to the same target and deals +8 / 10 / 12 / 14% damage |
| Thirst for Immortality | `desc_key` | Skill_Passive_Objects_Quest_Desc | Skill_Passive_Objects_Quest_Update6_Desc |
| Thirst for Immortality | `effect_en` | Quest (x7): Obtaining a Magical Object with a Rare quality or better grants +2 DMG\nComplete: Grants +1 / 1.25 / 1.5 / 1.75 VITALITY but now only Hero or Magical Object heals are effective | Quest (x7): Obtaining a Magical Object with an Epic quality or better grants +2 DMG\nComplete: Grants +1 / 1.25 / 1.5 / 1.75 VITALITY, but now only Hero or Magical Object heals are effective |
| Way of Awakening | `effect_en` | After 8 successful DEFENSE actions, the next TRAIT activates AWAKENED STANCE for 12 / 15 / 18 / 21 seconds\nAWAKENED STANCE grants both YIN and YANG effects, without taking any additional damage | After 7 successful DEFENSE actions, the next TRAIT activates AWAKENED STANCE for 12 / 15 / 18 / 21 seconds\nAWAKENED STANCE grants both YIN and YANG effects, without taking any additional damage |

Trace-only changes (offsets, roster order, argument graphs): 53 cells.

### Hero_Aladdin_Abilities.tsv

Rows: 57 → 57.

| Row | Name / form / field | Column | Old | New |
|---|---|---|---|---|
| 16 | Enchanted Blades / Base / `cooldown` | `text_key` | Ability_Special_Desc | Ability_Special_Update6_Desc |
| 16 | Enchanted Blades / Base / `cooldown` | `source_row_index` | 8 | 85 |
| 17 | Enchanted Blades / Base / `charges` | `text_key` | Ability_Special_Desc | Ability_Special_Update6_Desc |
| 17 | Enchanted Blades / Base / `charges` | `source_row_index` | 8 | 85 |
| 18 | Enchanted Blades / Base / `max_total_damage` | `text_key` | Ability_Special_Desc | Ability_Special_Update6_Desc |
| 18 | Enchanted Blades / Base / `max_total_damage` | `source_row_index` | 8 | 85 |
| 18 | Enchanted Blades / Base / `max_total_damage` | `source_path` | EntitySettings\Heroes\Hero_Aladdin!Hero_Aladdin.entity.ot.EntitySettingsResource.gen; EntitySettings\Character_Common\Character_Common.entity.ot.EntitySettingsResource.gen; EntitySettings\Heroes\Hero_Common!Hero_Common.entity.ot.EntitySettingsResource.gen | EntitySettings\Heroes\Hero_Aladdin!Hero_Aladdin_Update6.entity.ot.EntitySettingsResource.gen; EntitySettings\Heroes\Hero_Aladdin!Hero_Aladdin.entity.ot.EntitySettingsResource.gen; EntitySettings\Character_Common\Character_Common.entity.ot.EntitySettingsResource.gen; EntitySettings\Heroes\Hero_Common!Hero_Common.entity.ot.EntitySettingsResource.gen |
| 19 | Enchanted Blades / Base / `enchantment_cap` | `text_key` | Ability_Special_Desc | Ability_Special_Update6_Desc |
| 19 | Enchanted Blades / Base / `enchantment_cap` | `source_row_index` | 8 | 85 |
| 32 | Enchanted Blades / Base / `tooltip_binding_coverage` | `text_key` | Ability_Special_Desc | Ability_Special_Update6_Desc |
| 32 | Enchanted Blades / Base / `tooltip_binding_coverage` | `source_row_index` | 8 | 85 |
| 46 | Enchanted Blades / Base / `active_duration` | `text_key` | Ability_Special_Desc | Ability_Special_Update6_Desc |
| 46 | Enchanted Blades / Base / `active_duration` | `source_row_index` | 8 | 85 |
| 47 | Enchanted Blades / Base / `resource_cost` | `text_key` | Ability_Special_Desc | Ability_Special_Update6_Desc |
| 47 | Enchanted Blades / Base / `resource_cost` | `source_row_index` | 8 | 85 |
| 53 | Enchanted Blades / Base / `enchantment_per_hit` | `text_key` | Ability_Special_Desc | Ability_Special_Update6_Desc |
| 53 | Enchanted Blades / Base / `enchantment_per_hit` | `source_row_index` | 8 | 85 |

Trace-only changes (reference chains and byte offsets): 30 cells.

### Hero_Beowulf_Abilities.tsv

Rows: 53 → 53.

| Row | Name / form / field | Column | Old | New |
|---|---|---|---|---|
| 9 | Shockwave / Base / `damage` | `formula` | (Level Damage Selector{[State] Character_Common\Bhv Preview\Behaviour Preview => DMG; True => DMG} * (5.0 * runtime_operand[N] * Skill Special Sends Power Extra Damage Multiplier Operand{[State] Hero_Beowulf\Skill Special Sends Power\Event Skill Special Sends Power Active => Skill Special Sends Power Extra Damage Multiplier Selector{[Dt Skill Controller] Hero_Beowulf\Skills\Skill Controller Special Sends Power => 2.0999999046325684; [Dt Skill Controller] Hero_Beowulf\Skills\Skill Controller Special Sends Power => 1.7999999523162842; [Dt Skill Controller] Hero_Beowulf\Skills\Skill Controller Special Sends Power => 1.5; True => 1.2000000476837158}; True => 1.0}) * (1.0 + AP + NO_TALENT_OBJECT_MODIFIER(Primary Ability AP Modifier Listener))) | (Level Damage Selector{[State] Character_Common\Bhv Preview\Behaviour Preview => DMG; True => DMG} * (5.0 * runtime_operand[N] * Skill Special Sends Power Extra Damage Multiplier Operand{[State] Hero_Beowulf_Update6\Skill Special Sends Power\Event Skill Special Sends Power Active => Skill Special Sends Power Extra Damage Multiplier Selector{[Dt Skill Controller] Hero_Beowulf\Skills\Skill Controller Special Sends Power => 2.0999999046325684; [Dt Skill Controller] Hero_Beowulf\Skills\Skill Controller Special Sends Power => 1.7999999523162842; [Dt Skill Controller] Hero_Beowulf\Skills\Skill Controller Special Sends Power => 1.5; True => 1.2000000476837158}; [State] Hero_Beowulf_Update6\Skill Special Sends Power\Event Skill Special Sends Power Active Double => Skill Special Sends Power Extra Damage Multiplier Selector{[Dt Skill Controller] Hero_Beowulf\Skills\Skill Controller Special Sends Power => 2.0999999046325684; [Dt Skill Controller] Hero_Beowulf\Skills\Skill Controller Special Sends Power => 1.7999999523162842; [Dt Skill Controller] Hero_Beowulf\Skills\Skill Controller Special Sends Power => 1.5; True => 1.2000000476837158}; True => 1.0}) * (1.0 + AP + NO_TALENT_OBJECT_MODIFIER(Primary Ability AP Modifier Listener))) |
| 9 | Shockwave / Base / `damage` | `notes` | Formatter/configuration decoding only; engine-fed operands and runtime branches preserved.  Blocked: Runtime selector predicate [State] Character_Common\Bhv Preview\Behaviour Preview.0xfd2833c is not established by serialized flag initialization; Property access needs engine semantics; no fallback substitution (Behaviour Preview.0xfd2833c); Engine-fed operation operand binding; serialized fallback must not replace live operand (operand binding 1381); Property access needs engine semantics; no fallback substitution (Event Skill Special Sends Power Active.0xfd2832a); Runtime selector predicate [Dt Skill Controller] Hero_Beowulf\Skills\Skill Controller Special Sends Power.0x15fc6bf9 is not established by serialized flag initialization; Runtime selector predicate [Dt Skill Controller] Hero_Beowulf\Skills\Skill Controller Special Sends Power.0x15fc6bf1 is not established by serialized flag initialization; Runtime selector predicate [Dt Skill Controller] Hero_Beowulf\Skills\Skill Controller Special Sends Power.0x15fc6bf7 is not established by serialized flag initialization; Property access needs engine semantics; no fallback substitution (Skill Controller Special Sends Power.0x15fc6bf9); Property access needs engine semantics; no fallback substitution (Skill Controller Special Sends Power.0x15fc6bf1); Property access needs engine semantics; no fallback substitution (Skill Controller Special Sends Power.0x15fc6bf7) | Formatter/configuration decoding only; engine-fed operands and runtime branches preserved.  Blocked: Runtime selector predicate [State] Character_Common\Bhv Preview\Behaviour Preview.0xfd2833c is not established by serialized flag initialization; Property access needs engine semantics; no fallback substitution (Behaviour Preview.0xfd2833c); Engine-fed operation operand binding; serialized fallback must not replace live operand (operand binding 1381); Property access needs engine semantics; no fallback substitution (Event Skill Special Sends Power Active.0xfd2832a); Runtime selector predicate [Dt Skill Controller] Hero_Beowulf\Skills\Skill Controller Special Sends Power.0x15fc6bf9 is not established by serialized flag initialization; Runtime selector predicate [Dt Skill Controller] Hero_Beowulf\Skills\Skill Controller Special Sends Power.0x15fc6bf1 is not established by serialized flag initialization; Runtime selector predicate [Dt Skill Controller] Hero_Beowulf\Skills\Skill Controller Special Sends Power.0x15fc6bf7 is not established by serialized flag initialization; Property access needs engine semantics; no fallback substitution (Skill Controller Special Sends Power.0x15fc6bf9); Property access needs engine semantics; no fallback substitution (Skill Controller Special Sends Power.0x15fc6bf1); Property access needs engine semantics; no fallback substitution (Skill Controller Special Sends Power.0x15fc6bf7); Property access needs engine semantics; no fallback substitution (Event Skill Special Sends Power Active Double.0xfd2832a) |
| 9 | Shockwave / Base / `damage` | `source_path` | EntitySettings\Heroes\Hero_Beowulf!Hero_Beowulf.entity.ot.EntitySettingsResource.gen; EntitySettings\Character_Common\Character_Common.entity.ot.EntitySettingsResource.gen; EntitySettings\Heroes\Hero_Common!Hero_Common.entity.ot.EntitySettingsResource.gen | EntitySettings\Heroes\Hero_Beowulf!Hero_Beowulf.entity.ot.EntitySettingsResource.gen; EntitySettings\Character_Common\Character_Common.entity.ot.EntitySettingsResource.gen; EntitySettings\Heroes\Hero_Beowulf!Hero_Beowulf_Update6.entity.ot.EntitySettingsResource.gen; EntitySettings\Heroes\Hero_Common!Hero_Common.entity.ot.EntitySettingsResource.gen |
| 9 | Shockwave / Base / `damage` | `maintainer_check` | read in game: no decoded value | stale: checked on 1.05; decoded value changed in 1.06 |

Trace-only changes (reference chains and byte offsets): 28 cells.

### Hero_Carmilla_Abilities.tsv

Rows: 76 → 76.

| Row | Name / form / field | Column | Old | New |
|---|---|---|---|---|
| 0 | Dash / Base / `cooldown` | `source_path` | EntitySettings\Heroes\Hero_Common!Hero_Common.entity.ot.EntitySettingsResource.gen | EntitySettings\Heroes\Hero_Carmilla!Hero_Carmilla_Update6.entity.ot.EntitySettingsResource.gen; EntitySettings\Heroes\Hero_Common!Hero_Common.entity.ot.EntitySettingsResource.gen |
| 1 | Dash / Base / `charges` | `source_path` | EntitySettings\Heroes\Hero_Common!Hero_Common.entity.ot.EntitySettingsResource.gen | EntitySettings\Heroes\Hero_Carmilla!Hero_Carmilla_Update6.entity.ot.EntitySettingsResource.gen; EntitySettings\Heroes\Hero_Common!Hero_Common.entity.ot.EntitySettingsResource.gen |

Trace-only changes (reference chains and byte offsets): 43 cells.

### Hero_Geppetto_Abilities.tsv

Rows: 58 → 58.

Trace-only changes (reference chains and byte offsets): 31 cells.

### Hero_Juliet_Abilities.tsv

Rows: 70 → 70.

Trace-only changes (reference chains and byte offsets): 33 cells.

### Hero_Kintaro_Abilities.tsv

New table, 34 rows.

### Hero_Melusine_Abilities.tsv

Rows: 51 → 51.

Trace-only changes (reference chains and byte offsets): 23 cells.

### Hero_Merlin_Abilities.tsv

Rows: 172 → 172.

Trace-only changes (reference chains and byte offsets): 99 cells.

### Hero_Piper_Abilities.tsv

Rows: 73 → 73.

Trace-only changes (reference chains and byte offsets): 33 cells.

### Hero_RED_Abilities.tsv

Rows: 89 → 89.

| Row | Name / form / field | Column | Old | New |
|---|---|---|---|---|
| 19 | Hunter's Souvenir / Human / `cooldown` | `source_path` | EntitySettings\Heroes\Hero_Red!Hero_Red.entity.ot.EntitySettingsResource.gen | EntitySettings\Heroes\Hero_Red!Hero_Red_Update6.entity.ot.EntitySettingsResource.gen |
| 20 | Hunter's Souvenir / Human / `charges` | `source_path` | EntitySettings\Heroes\Hero_Red!Hero_Red.entity.ot.EntitySettingsResource.gen | EntitySettings\Heroes\Hero_Red!Hero_Red_Update6.entity.ot.EntitySettingsResource.gen; EntitySettings\Heroes\Hero_Red!Hero_Red.entity.ot.EntitySettingsResource.gen |
| 39 | Gusting Roar / Werewolf / `cooldown` | `formula` | (10.0 0x17b29bf0 60.0 0x17b29bf0 unresolved(Wolf Ultimate Power 1 Active Timer)) | (Min Cooldown Value Selector {[State] Hero_Red_Update6\Skill Ultimate 1 Piercing Shot Tornado\Skill Ultimate 1 Piercing Shot Tornado => 75.0; False => 10.0} 0x17b29bf0 75.0 0x17b29bf0 unresolved(Wolf Ultimate Power 1 Active Timer)) |
| 39 | Gusting Roar / Werewolf / `cooldown` | `notes` | Formatter/configuration decoding only; engine-fed operands and runtime branches preserved.  Blocked: Property access needs engine semantics; no fallback substitution (Wolf Ultimate Power 1 Active Timer.0xfd2825a) | Formatter/configuration decoding only; engine-fed operands and runtime branches preserved.  Blocked: Property access needs engine semantics; no fallback substitution (Skill Ultimate 1 Piercing Shot Tornado.0xfd2832a); Property access needs engine semantics; no fallback substitution (Wolf Ultimate Power 1 Active Timer.0xfd2825a) |
| 39 | Gusting Roar / Werewolf / `cooldown` | `source_path` | EntitySettings\Heroes\Hero_Red!Hero_Red.entity.ot.EntitySettingsResource.gen | EntitySettings\Heroes\Hero_Red!Hero_Red.entity.ot.EntitySettingsResource.gen; EntitySettings\Heroes\Hero_Red!Hero_Red_Update6.entity.ot.EntitySettingsResource.gen |
| 39 | Gusting Roar / Werewolf / `cooldown` | `maintainer_check` | read in game: no decoded value | stale: checked on 1.05; decoded value changed in 1.06 |

Trace-only changes (reference chains and byte offsets): 44 cells.

### Hero_Romeo_Abilities.tsv

Rows: 58 → 58.

| Row | Name / form / field | Column | Old | New |
|---|---|---|---|---|
| 25 | Black Roses / Base / `cooldown` | `formula` | (10.0 0x17b29bf0 75.0 0x17b29bf0 unresolved(Ultimate Power 2 Active Timer)) | (10.0 0x17b29bf0 60.0 0x17b29bf0 unresolved(Ultimate Power 2 Active Timer)) |
| 25 | Black Roses / Base / `cooldown` | `source_path` | EntitySettings\Heroes\Hero_Romeo!Hero_Romeo.entity.ot.EntitySettingsResource.gen | EntitySettings\Heroes\Hero_Romeo!Hero_Romeo.entity.ot.EntitySettingsResource.gen; EntitySettings\Heroes\Hero_Romeo!Hero_Romeo_Update6.entity.ot.EntitySettingsResource.gen |
| 25 | Black Roses / Base / `cooldown` | `maintainer_check` | accepted without reading | stale: checked on 1.05; decoded value changed in 1.06 |

Trace-only changes (reference chains and byte offsets): 33 cells.

### Hero_Snow_Queen_Abilities.tsv

Rows: 57 → 57.

| Row | Name / form / field | Column | Old | New |
|---|---|---|---|---|
| 15 | Ice Shards / Base / `damage` | `value` | 65 | 80 |
| 15 | Ice Shards / Base / `damage` | `formula` | (Level Damage Selector{[State] Character_Common\Bhv Preview\Behaviour Preview => DMG; True => DMG} * 1.2999999523162842 * (5 + Skill Special Extra Waves Amount Operand{[State] Hero_Snow_Queen\Skill Special Extra Waves\Skill Special Extra Waves => Skill Special Extra Waves Amount Selector{[Dt Skill Controller] Hero_Snow_Queen\Skills\Skill Controller Special Extra Waves => 5; [Dt Skill Controller] Hero_Snow_Queen\Skills\Skill Controller Special Extra Waves => 4; [Dt Skill Controller] Hero_Snow_Queen\Skills\Skill Controller Special Extra Waves => 3; True => 2}; True => 0}) * (1.0 + AP + NO_TALENT_OBJECT_MODIFIER(Secondary Ability AP Modifier Listener))) | (Level Damage Selector{[State] Character_Common\Bhv Preview\Behaviour Preview => DMG; True => DMG} * 1.600000023841858 * (5 + Skill Special Extra Waves Amount Operand{[State] Hero_Snow_Queen\Skill Special Extra Waves\Skill Special Extra Waves => Skill Special Extra Waves Amount Selector{[Dt Skill Controller] Hero_Snow_Queen\Skills\Skill Controller Special Extra Waves => 5; [Dt Skill Controller] Hero_Snow_Queen\Skills\Skill Controller Special Extra Waves => 4; [Dt Skill Controller] Hero_Snow_Queen\Skills\Skill Controller Special Extra Waves => 3; True => 2}; True => 0}) * (1.0 + AP + NO_TALENT_OBJECT_MODIFIER(Secondary Ability AP Modifier Listener))) |
| 15 | Ice Shards / Base / `damage` | `source_path` | EntitySettings\Heroes\Hero_Snow_Queen!Hero_Snow_Queen.entity.ot.EntitySettingsResource.gen; EntitySettings\Character_Common\Character_Common.entity.ot.EntitySettingsResource.gen; EntitySettings\Heroes\Hero_Common!Hero_Common.entity.ot.EntitySettingsResource.gen | EntitySettings\Heroes\Hero_Snow_Queen!Hero_Snow_Queen.entity.ot.EntitySettingsResource.gen; EntitySettings\Character_Common\Character_Common.entity.ot.EntitySettingsResource.gen; EntitySettings\Heroes\Hero_Snow_Queen!Hero_Snow_Queen_Update6.entity.ot.EntitySettingsResource.gen; EntitySettings\Heroes\Hero_Common!Hero_Common.entity.ot.EntitySettingsResource.gen |
| 15 | Ice Shards / Base / `damage` | `maintainer_check` | read in game: match | stale: checked on 1.05; decoded value changed in 1.06 |
| 16 | Ice Shards / Base / `bonus_damage_vs_chilled` | `formula` | 100 * ((0.5 + Skill Special Double Bonus Damage To Chilled Operand{[State] Hero_Snow_Queen\Skill Special Double\Skill Special Double => Skill Special Double Bonus Damage To Chilled Value Selector{[Dt Skill Controller] Hero_Snow_Queen\Skills\Skill Controller Special Double => 0.3499999940395355; [Dt Skill Controller] Hero_Snow_Queen\Skills\Skill Controller Special Double => 0.30000001192092896; [Dt Skill Controller] Hero_Snow_Queen\Skills\Skill Controller Special Double => 0.25; True => 0.20000000298023224}; True => 0.0} + Skill Passive Damage To Chilled Extra Damage Operand{[State] Hero_Snow_Queen\Skill Passive Damage To Chilled\Skill Passive Damage To Chilled => Skill Passive Damage To Chilled Extra Damage Selector{[Dt Skill Controller] Hero_Snow_Queen\Skills\Skill Controller Passive Damage To Chilled => 0.3499999940395355; [Dt Skill Controller] Hero_Snow_Queen\Skills\Skill Controller Passive Damage To Chilled => 0.30000001192092896; [Dt Skill Controller] Hero_Snow_Queen\Skills\Skill Controller Passive Damage To Chilled => 0.25; True => 0.20000000298023224}; True => 0.0})) | 100 * ((0.5 + Skill Special Double Bonus Damage To Chilled Operand{[State] Hero_Snow_Queen\Skill Special Double\Skill Special Double => Skill Special Double Bonus Damage To Chilled Value Selector{[Dt Skill Controller] Hero_Snow_Queen\Skills\Skill Controller Special Double => 0.5600000023841858; [Dt Skill Controller] Hero_Snow_Queen\Skills\Skill Controller Special Double => 0.47999998927116394; [Dt Skill Controller] Hero_Snow_Queen\Skills\Skill Controller Special Double => 0.4000000059604645; True => 0.3199999928474426}; True => 0.0} + Skill Passive Damage To Chilled Extra Damage Operand{[State] Hero_Snow_Queen\Skill Passive Damage To Chilled\Skill Passive Damage To Chilled => Skill Passive Damage To Chilled Extra Damage Selector{[Dt Skill Controller] Hero_Snow_Queen\Skills\Skill Controller Passive Damage To Chilled => 0.3499999940395355; [Dt Skill Controller] Hero_Snow_Queen\Skills\Skill Controller Passive Damage To Chilled => 0.30000001192092896; [Dt Skill Controller] Hero_Snow_Queen\Skills\Skill Controller Passive Damage To Chilled => 0.25; True => 0.20000000298023224}; True => 0.0})) |
| 16 | Ice Shards / Base / `bonus_damage_vs_chilled` | `source_path` | EntitySettings\Heroes\Hero_Snow_Queen!Hero_Snow_Queen.entity.ot.EntitySettingsResource.gen | EntitySettings\Heroes\Hero_Snow_Queen!Hero_Snow_Queen.entity.ot.EntitySettingsResource.gen; EntitySettings\Heroes\Hero_Snow_Queen!Hero_Snow_Queen_Update6.entity.ot.EntitySettingsResource.gen |
| 16 | Ice Shards / Base / `bonus_damage_vs_chilled` | `maintainer_check` | read in game: match | stale: checked on 1.05; decoded value changed in 1.06 |
| 23 | Frost Ray / Base / `damage_per_second` | `source_path` | EntitySettings\Heroes\Hero_Snow_Queen!Hero_Snow_Queen.entity.ot.EntitySettingsResource.gen; EntitySettings\Character_Common\Character_Common.entity.ot.EntitySettingsResource.gen | EntitySettings\Heroes\Hero_Snow_Queen!Hero_Snow_Queen.entity.ot.EntitySettingsResource.gen; EntitySettings\Heroes\Hero_Snow_Queen!Hero_Snow_Queen_Update6.entity.ot.EntitySettingsResource.gen; EntitySettings\Character_Common\Character_Common.entity.ot.EntitySettingsResource.gen |

Trace-only changes (reference chains and byte offsets): 28 cells.

### Hero_SunWukong_Abilities.tsv

Rows: 57 → 57.

| Row | Name / form / field | Column | Old | New |
|---|---|---|---|---|
| 27 | Transfiguration / Base / `cooldown` | `source_path` | EntitySettings\Heroes\Hero_SunWukong!Hero_SunWukong.entity.ot.EntitySettingsResource.gen | EntitySettings\Heroes\Hero_SunWukong!Hero_SunWukong_Update6.entity.ot.EntitySettingsResource.gen |
| 28 | Transfiguration / Base / `charges` | `source_path` | EntitySettings\Heroes\Hero_SunWukong!Hero_SunWukong.entity.ot.EntitySettingsResource.gen; EntitySettings\Heroes\Hero_Common!Hero_Common.entity.ot.EntitySettingsResource.gen | EntitySettings\Heroes\Hero_SunWukong!Hero_SunWukong_Update6.entity.ot.EntitySettingsResource.gen; EntitySettings\Heroes\Hero_Common!Hero_Common.entity.ot.EntitySettingsResource.gen |

Trace-only changes (reference chains and byte offsets): 31 cells.

### Magical_Objects_Values.tsv

Rows: 315 → 315.

| Row | Name / form / field | Column | Old | New |
|---|---|---|---|---|
| 41 | Vajra / main effect / `damage_per_dash` | `formula` | multiply(40.0, RuntimeBinding[N], selector default: 1) | selector default: multiply(40.0, RuntimeBinding[N], selector default: 1, RuntimeBinding[N]) |
| 41 | Vajra / main effect / `damage_per_dash` | `maintainer_check` | accepted without reading | stale: checked on 1.05; decoded value changed in 1.06 |

Trace-only changes (reference chains and byte offsets): 34 cells.

### Mechanics_Values.tsv

Rows: 240 → 240.

### Melodies_Values.tsv

Rows: 21 → 21.

| Row | Name / form / field | Column | Old | New |
|---|---|---|---|---|
| 0 | The Goose Girl Melody / Base / `wind_trigger_interval` | `value` | 15.0 | 10.0 |
| 0 | The Goose Girl Melody / Base / `wind_trigger_interval` | `formula` | 15.0 | 10.0 |
| 0 | The Goose Girl Melody / Base / `wind_trigger_interval` | `maintainer_check` | accepted without reading | stale: checked on 1.05; decoded value changed in 1.06 |
| 1 | The Goose Girl Melody / Base / `area_damage` | `formula` | multiply(150.0, RuntimeBinding[N]) | multiply(selector default: 10.0, 10.0, RuntimeBinding[N]) |
| 1 | The Goose Girl Melody / Base / `area_damage` | `maintainer_check` | accepted without reading | stale: checked on 1.05; decoded value changed in 1.06 |
| 8 | The Little Tailor Melody / Base / `consumables_per_qualifying_level` | `value` | 3 | 1 |
| 8 | The Little Tailor Melody / Base / `consumables_per_qualifying_level` | `formula` | 3 | 1 |
| 8 | The Little Tailor Melody / Base / `consumables_per_qualifying_level` | `maintainer_check` | accepted without reading | stale: checked on 1.05; decoded value changed in 1.06 |
| 9 | The Little Tailor Melody / Base / `exclusive_level_threshold` | `value` | 10 | 6 |
| 9 | The Little Tailor Melody / Base / `exclusive_level_threshold` | `formula` | 10 | 6 |
| 9 | The Little Tailor Melody / Base / `exclusive_level_threshold` | `maintainer_check` | accepted without reading | stale: checked on 1.05; decoded value changed in 1.06 |

Trace-only changes (reference chains and byte offsets): 12 cells.

