# Enemy combat settings

[All tables](README.md)

Stored combat constants, picker roles and difficulty damage factors. There is no confirmed final-damage formula. See [COMBAT.md](../COMBAT.md) for what each column means and what the data cannot show.

## Enemy Combat Values

| Subject id | Subject kind | Field | Stored value | Unit | Condition | Inheritance | Status | Notes |
|---|---|---|---|---|---|---|---|---|
| Boss\_Tentacle\_Master | enemy-or-entity | Raw Max Health | 250 |   | stored named constant; active runtime result unvalidated | local-override | documented-configuration |   |
| Boss\_Tentacle\_Master | enemy-or-entity | Fast Slam Damage Multiplier | 1.5 |   | stored named constant; active runtime result unvalidated | local-override | documented-configuration |   |
| Boss\_Tentacle\_Master | enemy-or-entity | Ring Damage Multiplier | 0.8 |   | stored named constant; active runtime result unvalidated | local-override | documented-configuration | Used through a conditional selector; exact branch evaluation unvalidated. |
| Boss\_Tentacle\_Master | enemy-or-entity | Final Ring Damage Multiplier | 0.8 |   | stored named constant; active runtime result unvalidated | local-override | documented-configuration | Used through a conditional selector; exact branch evaluation unvalidated. |
| Boss\_Tentacle\_Master | enemy-or-entity | Attack Shot Damage Multiplier | 5 |   | stored named constant; active runtime result unvalidated | local-override | documented-configuration | Literal field name; assignment to Rain hit damage is unestablished. |
| Boss\_Tentacle\_Master | enemy-or-entity | Default Resistance | 0 |   | stored named constant; active runtime result unvalidated | local-override | documented-configuration |   |
| Boss\_Tentacle\_Master | enemy-or-entity | Stagger Max Points | 200 |   | stored named constant; active runtime result unvalidated | local-override | documented-configuration |   |
| Boss\_Tentacle\_Master | enemy-or-entity | Staggered Duration | 12 |   | stored named constant; active runtime result unvalidated | local-override | documented-configuration |   |
| Boss\_Tentacle\_Master | enemy-or-entity | Attack Shockwave Attack Radius | 7.3 |   | stored named constant; active runtime result unvalidated | local-override | documented-configuration |   |
| Boss\_Tentacle\_Master | enemy-or-entity | Attack Shockwave Attack Lighting Count | 16 |   | stored named constant; active runtime result unvalidated | local-override | documented-configuration |   |
| Boss\_Tentacle\_Master | enemy-or-entity | Attack Spread Projectiles Amount Per Wave | 16 |   | stored named constant; active runtime result unvalidated | local-override | documented-configuration |   |
| Projectile\_Tentacle\_Nightmare\_Thorn | enemy-or-entity | Damage Multiplier Default | 0.3 |   | stored named constant; active runtime result unvalidated | projectile-setting | documented-configuration | Projectile default. Boss thorn variant references this entity and has no local damage override. |
| Projectile\_TentacleNightmare\_Lightning\_Bolt | enemy-or-entity | Damage Multiplier Default | 0.8 |   | stored named constant; active runtime result unvalidated | projectile-setting | documented-configuration |   |
| Attack\_Tentacle\_Nightmare\_Rain\_Missile | enemy-or-entity | Warning Time | 1.5 |   | stored named constant; active runtime result unvalidated | projectile-setting | documented-configuration |   |
| Standard\_Wolf\_Timber | enemy-or-entity | Raw Max Health | 100 |   | stored raw health; effective HP unvalidated | inherited-model | documented-configuration | W, inherited model value |
| Elite\_Coral\_Crab | enemy-or-entity | Raw Max Health | 90 |   | stored raw health; effective HP unvalidated | local-override | documented-configuration | C, local override |
| Boss\_Marsh\_Ghoul | enemy-or-entity | Raw Max Health | 200 |   | stored raw health; effective HP unvalidated | local-override | documented-configuration | G, local override |
| Character\_Common | shared-entity | Raw Damage | 10 |   | shared stored baseline | shared-character-setting | documented-configuration |   |
| Character\_Common | shared-entity | Raw Max Health | 100 |   | shared stored baseline | shared-character-setting | documented-configuration |   |
| Wolves\_Model | enemy-or-entity | Attack Bite Damage Multiplier Value | 0.4 |   | named multiplier referenced by bite component; final hit unvalidated | model-setting | documented-configuration |   |
| Crabs\_Model | enemy-or-entity | Raw Max Health | 70 |   | parent value overridden by Elite\_Coral\_Crab | parent-model | documented-configuration | Union offset not supplied by the note. |
| Festering\_Ghoul | enemy-or-entity | Raw Max Health | 100 |   | parent value overridden by Boss\_Marsh\_Ghoul | parent-entity | documented-configuration | Union offset not supplied by the note. |
| GlobalValues | global-default | NGP Enemy Damage Modifier | 0 |   | cooked default only; selected-difficulty runtime input unknown | global-default | documented-configuration | Exact file and offset not supplied; NGP-to-difficulty mapping is unestablished. |
| GlobalValues | global-default | NGP Master Nightmares Damage Modifier | 0 |   | cooked default only; selected-difficulty runtime input unknown | global-default | documented-configuration | Exact file and offset not supplied; NGP-to-difficulty mapping is unestablished. |

## Enemy Combat Picker Values

| Subject id | Component | Stored literal | Semantic status | Notes |
|---|---|---|---|---|
| Boss\_Tentacle\_Master | Fast Slam | 3 | embedded-fallback | Offset is the damage component; picker fallback does not replace its referenced named 1.5 constant. |
| Wolves\_Model | Attack Bite Damage | 1 | embedded-fallback | Offset is the component. Multiplier-picker fallback; the referenced named multiplier is 0.4. |
| Wolves\_Model | Attack Bite Damage | 8 | embedded-fallback | Offset is the component. First-picker fallback; the picker references the shared Character Controller. |
| Tentacle\_Nightmares\_Model | Shockwave | 2 | inferred-multiplier-role | Analogous picker position; no independent member-name or runtime verification. |
| Tentacle\_Nightmares\_Model | Swipe | 3 | inferred-multiplier-role | Analogous picker position; no independent member-name or runtime verification. |
| Crabs\_Model | Attack Claw Damage | 0.8 | inferred-multiplier-role | Role follows an analogous picker position; final damage is not established. |
| Attack\_Tentacle\_Nightmare\_Rain\_Missile | damage component first picker | 10 | unresolved-runtime-role | First-picker literal only; location offset not supplied; not validated Rain damage. |
| Boss\_Tentacle\_Master | Attraction multiplier selector | 1 | conditional-selector-operand | Selector contains an enraged-state reference and a named 0.8 reference; branch mapping and runtime evaluation unvalidated. |
| Boss\_Tentacle\_Master | Attraction multiplier selector | 1 | conditional-selector-operand | Selector contains an enraged-state reference and a named 0.8 reference; branch mapping and runtime evaluation unvalidated. |

## Enemy Chapter Damage Factors

| Difficulty index | Difficulty display name | Chapter | Configured damage factor | Global name | Status | Notes |
|---|---|---|---|---|---|---|
| 0 |   | 1 | 0.8 | Game Difficulty | documented-configuration | Authored switch-selector value. Difficulty display names unverified; runtime consumption unproven. |
| 0 |   | 2 | 1.7 | Game Difficulty | documented-configuration | Authored switch-selector value. Difficulty display names unverified; runtime consumption unproven. |
| 0 |   | 3 | 2.7 | Game Difficulty | documented-configuration | Authored switch-selector value. Difficulty display names unverified; runtime consumption unproven. |
| 0 |   | 4 | 2.8 | Game Difficulty | documented-configuration | Authored switch-selector value. Difficulty display names unverified; runtime consumption unproven. |
| 1 |   | 1 | 0.9 | Game Difficulty | documented-configuration | Authored switch-selector value. Difficulty display names unverified; runtime consumption unproven. |
| 1 |   | 2 | 1.9 | Game Difficulty | documented-configuration | Authored switch-selector value. Difficulty display names unverified; runtime consumption unproven. |
| 1 |   | 3 | 3.0 | Game Difficulty | documented-configuration | Authored switch-selector value. Difficulty display names unverified; runtime consumption unproven. |
| 1 |   | 4 | 3.1 | Game Difficulty | documented-configuration | Authored switch-selector value. Difficulty display names unverified; runtime consumption unproven. |
| 2 |   | 1 | 1.0 | Game Difficulty | documented-configuration | Authored switch-selector value. Difficulty display names unverified; runtime consumption unproven. |
| 2 |   | 2 | 2.0 | Game Difficulty | documented-configuration | Authored switch-selector value. Difficulty display names unverified; runtime consumption unproven. |
| 2 |   | 3 | 3.2 | Game Difficulty | documented-configuration | Authored switch-selector value. Difficulty display names unverified; runtime consumption unproven. |
| 2 |   | 4 | 3.3 | Game Difficulty | documented-configuration | Authored switch-selector value. Difficulty display names unverified; runtime consumption unproven. |
| 3 |   | 1 | 1.0 | Game Difficulty | documented-configuration | Authored switch-selector value. Difficulty display names unverified; runtime consumption unproven. |
| 3 |   | 2 | 2.1 | Game Difficulty | documented-configuration | Authored switch-selector value. Difficulty display names unverified; runtime consumption unproven. |
| 3 |   | 3 | 3.4 | Game Difficulty | documented-configuration | Authored switch-selector value. Difficulty display names unverified; runtime consumption unproven. |
| 3 |   | 4 | 3.5 | Game Difficulty | documented-configuration | Authored switch-selector value. Difficulty display names unverified; runtime consumption unproven. |

Source: [`Enemy_Combat_Values.tsv`](../data/Enemy_Combat_Values.tsv), [`Enemy_Combat_Picker_Values.tsv`](../data/Enemy_Combat_Picker_Values.tsv), [`Enemy_Chapter_Damage_Factors.tsv`](../data/Enemy_Chapter_Damage_Factors.tsv).
*This page is generated from the TSV files in [data/](../data/) by `tools/build_browse.py`. Do not edit it by hand; fix the data and re-run the script.*
