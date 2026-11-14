# Contributor claim checks, November 2026

This page records the evidence behind the `2026-11-13-contributor-claims` snapshot. Each section covers one claim from wiki page revisions edited between October 29 and November 12, 2026, checked against the cooked game files of the 1.06 extraction tree and `Ravenswatch.exe` of the same install: Steam (PC) `1.06.00.04.27511`, Steam build ID `25174305`, executable SHA-256 `b9c3642884a8f3a463782f36c9a3a62bc14c88105315220c733fe6c2229ba904`. Nothing here was checked in game.

Verdicts: confirmed, contradicted, partly true, not found. A configured literal is not a runtime formula; a value whose scope or condition is unproven is "partly true". Each fact is marked observed (a literal read from a resource, or an immediate in code) or inferred (reasoned from names or decompiled code). "Not found" names its search boundary. Offsets are byte offsets in the named resource; function addresses are in `Ravenswatch.exe`. Row references are `file line`, counting header lines, in this snapshot.

Value ids are 32-bit hashes registered in `FUN_1401d2a90` (status values) and `FUN_1401d0030` (stat values). Float constants: `DAT_140fc8be0` = 1.0, `DAT_140fc8ddc` = 10.0, `DAT_140fc8b74` = 0.5.

## Stats and status effects

### S1 Vulnerable: partly true
- Value: `GlobalValues/Common_Settings/Vulnerable_Value` = 0.25 (observed).
- Rule: the incoming-damage handler `FUN_1403bce50` (0x1403bce50) computes damage * max(0, 1.0 + Vulnerable + IncreaseDamageTaken + Marked) * ((x + F) - x * F), with F = max(0, 1 - Resistant). Ids: Vulnerable 0x16ede062, IncreaseDamageTaken 0x15efab05, Marked 0x1a40367d, Resistant 0x16ede05e. The same sum is in `FUN_1403d5e70`. The additive grouping is inferred from the pseudocode. The base term is a field read (`param_3+0x13`), not a literal 1.0: inferred. No hero or enemy branch was seen, so +25% is not enemy-only (inferred).
- Heroes: `Hero_Common` has "Debuff Hero Is Vulnerable" with a "Hero Is Vulnerable Armour Modifier" and listener (offsets 0x30fde, 0x98210). `Hero_Is_Vulnerable_Value` = -100.0 (id 0xba4bf279; its only code reference is the registration at 0x1401d369d). How -100 armour becomes damage was not found (see S5). `Character_Common` carries a shared Vulnerable listener (0x3ffaa), so heroes probably also take +25% (inferred).
- Rows: Mechanics_Values.tsv 57, 69 (and the existing 0.25 row).

### S2 Weakened: confirmed (value and consumer); scope inferred
- `Weak_Value` = 0.25 (observed). `FUN_1403be100` (0x1403be100): multiplier = max(0, 1.0 + Strength(0x16ede056) + stat 0x19c9c243 - Weak(0x16ede068)), stored at attacker+0xe8. Weak subtracts 0.25 from damage dealt; Strength adds on the same term. The Weak id is inferred from the consumer, because the name string is not adjacent. The handler is the base-character one, not hero-only (inferred).
- Rows: Mechanics_Values.tsv 58, 70.

### S3 Critical Damage: base not found; overflow coefficient found
- `FUN_1403bfe10` (0x1403bfe10): crit damage = a float at +0x100 of the app-settings singleton (`DAT_1414706b0`, built in `FUN_14021dd50`) plus stat 0x15c82d13. No resource holding that float was located, so +50% is neither confirmed nor contradicted. Boundary: `FUN_1403bfe10`, `FUN_1403bfc30`, `FUN_1403c3220`, `FUN_14021dd50`, `FUN_1401f9b50`.
- Overflow: `FUN_1403c3220` (0x1403c3220) displays Crit Damage Final = max(0, critChance - 1.0) + critDamage, a 1:1 coefficient (observed constant `DAT_140fc8be0`). That damage code uses the same sum is inferred.
- Rows: Mechanics_Values.tsv 53 (unresolved, note sharpened), 54.

### S4 Damage stat: not found
- No DMG stat id is registered in the stat table (only Attack power and Deal extra damage). The {0}% is filled from Hero Controller and Character Controller properties read by `Hero_Common` "AP Display Ratio Operation" and the lookups `FUN_14039f3e0` and `FUN_1403bcbc0`. The +1% per point coefficient is not a literal found there. Possible lead: stat 0x19c9c243 in the S2 sum.
- Row: none.

### S5 Armor: formula not found
- The armour display reads Hero Controller property 0x1b8ddfa2 (controller+0x1c98). The armour-to-reduction code was not located; Armour registers with id 0. Observed floor-at-0 clamps: damage dealt (S2), incoming damage (S1), crit overflow (S3). "Armor is the only stat that can go negative" is unverified. The text key Menu_DmgTooltip_Desc_Negative exists, so negative DMG is displayed by design (text only).
- Rows: Mechanics_Values.tsv 51, 52 (unresolved, notes sharpened).

### S6 Chilled: partly true
- Defaults 0.4 and 5 s (observed, GlobalValues). The Chilled debuff is defined in `Character_Common`. `Hero_Snow_Queen` overrides: "Chilled Effect Value" picker fallback 0.5 (0x90618) and "Better Frost Chilled Effect Increase Value Selector" = +0.2 for Frost Queen (0x82ad7). Runtime gating was not evaluated. Snow Queen tooltip arguments stay unresolved. Merlin has "Skill Power Defense Chilled Value Selector" (0xc4b83), not decoded. Romeo, Pied Piper, Melusine and Sun Wukong have no Chilled value component by name. Enemy appliers and heroes as victims were not searched.
- Row: Mechanics_Values.tsv 61.

### S7 Trapped: partly true
- `Character_Common` "Debuff Rooted" carries Root -1- Treant and Root -2- Spider flags, a Root Entity Spawner and a ROOT_END sender (names only). `Wolves_Model` has "Attack Bite FX Trapped Tester" and "Played Flag"; the spider model has "Attack Web". Treant roots and the wolf bite relate to Trapped by name; the spider web is also related. Victims are heroes (inferred).
- Row: none.

### S8 Stealth: partly true
- "Concealed" is the registered status value 0x16ede05c, named in `Hero_Common`, Carmilla, Melusine and Scarlet. Global Enemy_Detection_Min and Max_Height_Default exist (a detection height band; values not interpreted). The break rule and the co-op rule were not found. No wind or speed-line FX name was found in `Hero_Common` or `Character_Common`.
- Row: none.

### S9 Move Speed and Sun Wukong Dash: partly true
- The base Dash uses its own displacement ("Primary Ability Dash Move Speed Operation"), not the Move Speed Ratio stat (0x044dadde). The Dash talent Sprint gives +10/12/14/16% Move Speed (Hero_SunWukong_Talents.tsv line 27; selector "Skill Dash Sprint Move Speed Increase Selector"). The wiki's "Dash" source is therefore the Sprint talent (inferred).
- Row: none.

## Difficulty, modifiers and feathers

### D1 Difficulty page: mostly not found
- Starting Raven Feathers 6/4/3/2 and XP -10/-20/-30%: not found. The UI has a "Difficulty Xp Modifier" label and String Format (`Play_Book_Page` 0x8f84) but no numbers. `GameModes`, `EnemyCampDifficulties` (six camp tiers, not the four named difficulties), `Play_Book_Page`, `Hero_Common` and `Altar_Of_Heroes_Model` hold no count. Probably code or runtime.
- Difficulty names and blurbs: confirmed. Common.LangEN.tsv keys Difficulty_Normal/Hard/VeryHard/Nightmare (indexes 240-251) match the page for Adventure, Twilight, Darkness and Nightmare.
- Unlock order, win conditions, Epilogue requirement: not found. Code strings "Unlock difficulty" (`FUN_1401ce9f0`) and `Modal_Difficulty_Unlocked` exist; the conditions are not decoded.
- "Dark red skin" for Corrupted enemies: not found (visual).
- Master Outfit in Darkness: partly true. Common.LangEN.tsv index 364 reads "Unlocked when victorious in Darkness difficulty or above"; the link to the Master outfits is not shown. The Hero_Skin_Unlocks.tsv rows with unlock type "progression condition" read "Completed the game in Darkness Difficulty" (observed text).
- Rows: none.

### D2 Modifiers and challenges: confirmed; the page lacks none
- The page lists 22 modifiers (11 positive, 11 negative), not 20, and the game ships 22 definitions, so none is missing. Names and score percentages match Game_Modifiers.tsv. Wording differences: Solid Heroes "100% Max Health" vs "+100%"; Hyperactive "a extra" vs "1 extra". Positive and negative follow the sign of the score (inferred).
- The five challenge presets match Challenges.tsv, including totals +15, 0, 0, +15, +20 (additive combination inferred). Three more challenge titles exist in text with no definition file: Blessed and Cursed, One for All, The Crucible.
- Master of Challenges: the condition `CompleteChallengesInDarknessDifficulty` stores 2 and 5 (observed); 5 challenges and 2 as the Darkness index are readings (inferred).
- OCAID: all five named modifiers exist; the community-challenge framing is not game data.
- Tables: Game_Modifiers.tsv (22 rows), Challenges.tsv (5 rows).

### D3 Raven Feathers and the Altar of Heroes: partly true
- Co-op sharing and whose count is used: not found (needs runtime or code).
- One Altar of Heroes per chapter: the generation recipe sets an Altar_Of_Heroes quota of 1 on each map (observed).
- Altar reward: `Altar_Of_Heroes_Model` "XP Reward Value Selector" default 500 (int 0x1f4, offset 0x158a8) feeds a Dt Resource Gain named XP Reward (type inferred from names). No Dream Shard reward value was found, so "+100 Dream Shards per player" is not supported. The price: "Price Value Selector" and "Price operation" exist but no numeric price is in the model or the per-map altar entities.
- Feather per payment: "Feather Gain Value" = 1 (offset 0x15043); events ALTAR_FEATHER_GAIN and REVIVE_TOKEN_GAIN. The achievement BuyFeathersFromAltarOfHeroesInASingleRun has threshold 3 on ALTAR_FEATHER_GAIN (see A1).
- Dreamcatcher is `Magical_Objects/Common/Reduce_All_DS_Price`; its Price Reduction literal is 0.1 (float cdcccc3d at 0xf31). The altar model has a "Reduce All DS price Modifier Listener", so altar prices follow it (inferred).
- Angry Birds: the NoFeathers modifier reads "Heroes start with no Raven Feather, and none can be recovered", score +15% (observed text). The mechanics come from the description only.
- Rows: Mechanics_Values.tsv 98, 99, 100; notes on 93-95.

## Magical Objects and enemies

### O1 Excalibur: partly true
- Counting: Excalibur's "Legendary Skill Count Get Value" reads `Hero_Common` "Skill Legendary Count Value" (group Rarity Counters, property id 0x188c1379, offset 0xe0ce8), which `FUN_14039f260` maps to hero-controller+0x11f8. `FUN_1403b21f0` (0x1403b21f0) fills four counters: for each of 10 skill slots (controller+0x1008, stride 0x20) it reads the skill rarity index (uint at skill+0x68, counted only below 4) and increments counter[index]. Counter[3] feeds +0x11f8, so the count is occupied talent slots with rarity index 3; that index 3 is Legendary is inferred from the counter order and name.
- Damage Value literal 10 (Excalibur entity offset 0x11f8, int) = +10 DMG per counted Legendary Talent; the operation multiplies by the count (inferred).
- Maximum talents: the slot array holds 10 entries (`FUN_1403a00e0`, `FUN_1403b2100`, `FUN_1403b24c0`). The page says 9 (+90). The bound 10 does not confirm 9; what caps talents at 9 was not found.
- Row: Magical_Objects_Values.tsv 317.

### O2 Trinity: partly true
- Starting talent: confirmed (Hero_Merlin_Talents.tsv line 33, tier 0; no edit).
- `Hero_Merlin` has three separate flags "State Skill Trait Quest Gain Charge Has Excalibur / Has Holy Grail / Has Father Time's Hourglass", each with a listener and a "Last MO Tester", and a counter whose target "Quest Count Value" has literal fallback 3 (offsets 0xff4f, 0x1013f), events SKILL_TRAIT_QUEST_COUNTER_INC/DEC/SET and a "Charge Complete" state. Per-object flags suggest three distinct objects, not any three; increment gating was not traced (inferred).
- Row: none.

### E1 Phoenix egg: not found (name, XP); kill rule partly
- `Phoenix_Egg.enemydef` has no name key and `Enemy_Common.LangEN.tsv` has no Egg or Phoenix key; "Phoenix egg" stays a descriptive label.
- XP: Phoenix_Egg, Roc_Egg and Rocling entities carry no XP value by name. `Roc_Egg_Model` has "Alerted XP None Value Spawner" and `Roc_Birds_Model` "Attack Summon Birds XP None Spawner Value" (names only). Equal XP: not found.
- In the Belly: the tooltip says "Eat the closest non-boss enemy, instantly killing it" (Hero_RED_Abilities.tsv line 66). No Is Boss value appears in Phoenix_Egg strings, so eggs are plausibly non-boss; targeting was not checked.
- Row: none.

### E2 Enemy page claims: mostly not found
- Abu Al Jann stagger bar: `Boss_Jinn` has "Is Stagger Resistant", "Possession Pause Stagger Timer", "Stagger Recovery Speed Selector" and "Leaving Possession Teleport" (names only); not confirmed.
- Jinn teleporting, day and night behaviour of wolves, spiders and snakes, Alpha wolf up to three Giant Leaps (a "Attack Giant Leap Condition" exists, no repeat count), Sinbad stamina loss: not found.
- Row: none.

## Map, chests, stash and locations

Rows added to the Map_* tables keep those tables' "unverified" source-version override; each says in its own columns that it was read from the 1.06 tree.

### M1 Stingy Jack: partly true
- Rule: Stingy_Jack_Reward_<Map>_T# entries (spawning `Stingy_Jack_Model` on a chest mesh) are listed in `Definitions/Rewards/Camp_Rewards_<Map>_Update5` beside the Basic and Locked chest entries of the same tier. Avalon and Storm Island list T1-T3; Dark Hills lists T2 and T3 only (observed; Avalon entries at 0x50f, 0x640, 0x771). `Reward_GenerateAndDistribute` (0x1401e3340) assigns reward entries to reward-spawner slots by tile-tier band and flags, using the game RNG (inferred). "Any regular chest" is plausible but not shown for every tier or chapter. The per-chest chance was not decoded. Map references that list him as absent are contradicted: the reward lists contain him in all three chapters.
- Row: Mechanics_Values.tsv 143.

### M2 Chest: partly true
- Locked chest copies: `Chest_Model` "Copies Count Value Selector" is keyed on "Chest Starts Locked Value"; its bytes equal the Reroll Price selector (locked 2, default 1) apart from name and class ids (offsets 0xad32 and 0xc35f), so locked gives 2 copies (inferred).
- Two interactions: the chest spawns `Objects/Key_Lock/Key_Lock` through a "Lock Entity Spawner" (own interaction, "Chest Has Been Unlocked Flag", LOCK_UNLOCKED listener) besides its own Dt Interaction (offsets 0x6596, 0xa51e); behaviour inferred.
- Locked minimap icon names: `MiniMap/Icons/High/Minimap_IconHigh_Locked_Chest.png` (small: `Map_Icons_Common_Locked_Chest.png`), text key MinimapMarker_LockedChest (observed names; the look is not checked).
- Closing the reward window: Loot has an "Event Back" state and the chest returns to State Closed (0x372c); whether the reward stays unclaimed needs runtime.
- Row: none (reroll cost 2 is Mechanics_Values.tsv, existing rows).

### M3 Thieves' Stash: partly true
- Notes per room (orange 3, red 4): not found. Underground rooms use `Underground_Ruin_*` with "Note Gain Amount Value", Is T1/T2/T3 testers and activity names harpe_<kind>_easy/medium/hard; the per-tier literal was not isolated (Underground_Ruin_Model 0x3033).
- Traps: confirmed. Dark Hills combat room: Thieves_Trap_Poison. Storm Island: Thieves_Trap_Cannon, with Thieves_Trap_Poison also referenced. Avalon: Thieves_Trap_Avalon_Fire_Zones_Manager plus Thieve_Crystal_Ground_Trap and Thieve_Crystal_Wall_Trap. Damage and stagger not read.
- Magic Mirror sizes: confirmed. `Thieves_Magic_Mirror` "Nb Choice Selector": Is T1 = 2, Is T2 = 3, Is T3 = 4 (offset 0x1c985; values near 0x1ca7c, 0x1cb5c, 0x1cc3c). The tier-to-colour mapping is not in the file.
- Green stash guaranteed a Mirror: not supported. The Mirror entrance is a Special-pool tile (weight 0.2, Mirror_Entrance cap 1) drawn among 5 Special slots, separate from the single Thieves_Entrance slot. Its tier band is 0.333-1 on Dark Hills and 0-1 on Avalon and Storm Island (observed). Placement code (`TileSpawn_PlaceTiles`) was not read.
- At least one stash per chapter: the Thieves_Entrance quota is 1 on all three maps (configured count, not proof of fill).
- Combat, Cursed and Gold never green: the three entrance tiles have band 0.33-1 on all maps, so never tier 1 (observed); green = tier 1 is inferred.
- Curse mechanics: not found (needs runtime). The Cursed room uses Underground_Ruin_Cursed with harpe_curse_* activity names.
- Existing weights 0.5/0.4/0.1, Mirror 0.2 and Special 5 are unchanged on 1.06.
- Rows: Map_Stash_Models.tsv 12, 13, 14.

### M4 Locations: not found (colours); Cyclop claim not supported
- Spawn-zone colours: not found. Only asset names exist: `Map_Icons_3Pigs_House_Straw/Wood/Stone.png` (Straw 40x40, band 0.1-0.667; Wood 40x40, band 0.333-1; Stone 64x64, band 0.1-1; weight 0.33 each), `Ingredients/Bean.png` for Jack tiles, `Map_Icons_Npc_Quest.png` for Sinbad and Mordred tiles.
- Chapter 3 quest torch colours: not found. Avalon has Citadel_Torch_Wall objects only; no quest-torch asset by file name.
- Cyclop "any Point of Interest zone not overlapping Roc Peak": not supported as worded. The Cyclop entrance is 40x40, band 0.3333-1, weight 0.5, flags Story and Cyclop_Cave_Entrance; the Roc entrance is 64x64, weight 0.5. They use different footprint groups; no overlap rule was found.
- Row: none.

## Achievements and outfits

### A1 Achievements: partly true
- The game ships 48 achievement definitions; the page lists 49 rows. Platform ids 1-33 appear on 33 definitions (the Xbox "33", observed). The page row "Just a Little Nightmare: Get all Trophies" has no definition (PlayStation only, not in game data), so "34 trophies" cannot be settled.
- 47 page rows map one to one to definitions by event or name. "The Thirst for Power: Use 6 Sacrificial Idols" has no definition of that name; the unmatched definition is UseBloodFountainsInASingleRun (threshold 6). Idol = Blood Fountain is inferred (same count, no other candidate).
- Thresholds that match the page (observed in the definitions): healing fountains 6, refugees 6, quests 3, grimoires 4, equipped Magical Objects 20, Legendary talents 9, keys 5, mini-bosses 3 (the page says "optional bosses"), altar feathers 3, tumors 3, blood fountains 6, mirror duplications 4, hidden outfits 3, hourglass Magical Objects 9, Darkness challenges 5, hero skill badges 9.
- Not stored in the definitions: Leprechaun 400 shards (event COLLECTED_LEPRECHAUN_CAULDRON_TREASURE, count 1), the revive-3 condition (REVIVE_THREE_HEROES inferred), wish 3 Magical Objects (WISHING_WELL_COMPLETED), DLC requirements, and cauldron and mirror tier notes.
- No achievement name or description text ships in the game files, so the page's spelling ("equiped") and the wording "Magical Mirror" cannot be checked against achievement text. The game's own name for the object and the room is "Magic Mirror" (Common.LangEN.tsv indexes 512 and 516; Magical_Objects.LangEN.tsv index 167).
- Table: Achievements.tsv (48 rows).

### H1 Hidden outfits: partly true
- Entity thresholds read from the hero entities (observed): Juliet PERFECT_SHOT_HIT_STREAK_COMPLETE, "Perfect Shot Hit Streak Target" = int 12 (offsets 0x72342, 0x723d3), matches the page. Geppetto MANY_PUPPETS_CONTROLLED, "Many Puppets Alive Value" = int 6 (0x63e36), tester at 0x156fd, matches. Snow Queen ENEMIES_SHATTERED_AT_ONCE, "Enemies Shattered At Once Target Value" = int 20 (0x90871), tester at 0x26c94, matches; the "Chilled" qualifier is not checked. Carmilla TRAIT_ACTIVE_LONG_ENOUGH, "Trait Hold Timer Value" = 60.0 (0xa0411) driving "Trait Active Long Enough Timer" (0xe6b7), so a 60 s timer is confirmed; the "Winged Form" label is inferred.
- Not found: Melusine HEALED_AND_SHIELDED_ENOUGH has a tester (0x1d707) and sender (0x777ef) with no threshold literal, so 10,000 is not stored in the entity (searched names containing Heal, Shield, Total, Counter, Store and Enough).
- Condition only, no number in the entity: Romeo (boss defeated without being hit), Scarlet (a transformation event), Merlin (Trinity quest completed, Morgan), Kintaro (no matching component name; the event is sent elsewhere).
- Counts stored in the definitions (observed): Aladdin 3 wishes in a chapter, Beowulf 200 ignited-enemy explosions, Piper 7 (RAT_LEGENDARY_TALENT), Sun Wukong 3 (MASTER_NIGHTMARE_DEFEATED_WHILE_TRANSFORMED); other heroes store count flag 0. Every hero has a Default outfit.
- Romance outfit: Hero_Romeo_Skins.LangEN.tsv indexes 12-14 and the Juliet equivalents hold "Romance Outfit" text, but neither `Romeo_Update6` nor `Juliet_Update6` `.herodef` contains a Romance skin entry. Each lists 8 skins. The text exists, but no skin is defined (observed).
- Snow Queen: the game ids are `Snow_Queen` (`Snow_Queen_Update6.herodef`, `Hero_Snow_Queen` entity); the page infobox uses `ID=Snow Queen`.
- Table: Hero_Skin_Unlocks.tsv (113 rows, with entity_threshold and entity_threshold_source columns; four rows filled).
