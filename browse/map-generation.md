# Map generation

[All tables](README.md)

Resource roles, weights, quotas, caps, tier bands and probability models used when maps are built. See [MAP_GENERATION.md](../MAP_GENERATION.md) for what each column means and what the data cannot show.

## Map Generation References

| Resource path pattern | Class name | Role | Status |
|---|---|---|---|
| Definitions/Tiles/\<Map\>!\<tile\>.tiledef.ot.DtTileDefinition.gen | oCDtTileDefinition | one placeable tile: its flags, footprint, tier band, and pick weight | documented-configuration |
| Definitions/Maps/\<Map\>\_LiveOps\_Update5.mapdef.ot.DtMapDefinition.gen | oCDtMapDefinition | the pool: which tiledefs this chapter may draw from at all | documented-configuration |
| Ot/\<Map\>/Map\_\<Map\>\_LiveOps\_Update5\_TileGeneration.level.ot.GameStream.gen | oCDtEntityCpntTileSpawnerSettings and children | the slots, the per-kind quotas, and the per-flag caps | documented-configuration |

## Map Generation Weights

| Map id | Selection family | Variant | Row kind | Relative weight | Status | Notes |
|---|---|---|---|---|---|---|
| Dark\_Hills | regular-stash | Combat | documented-variant | 0.5 | documented-configuration | Stored relative weight; proportional draw is inferred, not verified generator code. Values are not normalized during conversion. |
| Dark\_Hills | regular-stash | Cursed | documented-variant | 0.4 | documented-configuration | Stored relative weight; proportional draw is inferred, not verified generator code. Values are not normalized during conversion. |
| Dark\_Hills | regular-stash | Gold room | documented-variant | 0.1 | documented-configuration | Stored relative weight; proportional draw is inferred, not verified generator code. Values are not normalized during conversion. |
| Avalon | regular-stash | Combat | documented-variant | 0.5 | documented-configuration | Stored relative weight; proportional draw is inferred, not verified generator code. Values are not normalized during conversion. |
| Avalon | regular-stash | Cursed | documented-variant | 0.4 | documented-configuration | Stored relative weight; proportional draw is inferred, not verified generator code. Values are not normalized during conversion. |
| Avalon | regular-stash | Gold room | documented-variant | 0.1 | documented-configuration | Stored relative weight; proportional draw is inferred, not verified generator code. Values are not normalized during conversion. |
| Storm\_Island | regular-stash | Combat | documented-variant | 0.5 | documented-configuration | Stored relative weight; proportional draw is inferred, not verified generator code. Values are not normalized during conversion. |
| Storm\_Island | regular-stash | Cursed | documented-variant | 0.4 | documented-configuration | Stored relative weight; proportional draw is inferred, not verified generator code. Values are not normalized during conversion. |
| Storm\_Island | regular-stash | Gold room | documented-variant | 0.1 | documented-configuration | Stored relative weight; proportional draw is inferred, not verified generator code. Values are not normalized during conversion. |
| Dark\_Hills | Special | Mirror room | documented-variant | 0.2 | documented-configuration | Stored relative weight; proportional draw is inferred, not verified generator code. Values are not normalized during conversion. |
| Avalon | Special | Mirror room | documented-variant | 0.2 | documented-configuration | Stored relative weight; proportional draw is inferred, not verified generator code. Values are not normalized during conversion. |
| Storm\_Island | Special | Mirror room | documented-variant | 0.2 | documented-configuration | Stored relative weight; proportional draw is inferred, not verified generator code. Values are not normalized during conversion. |
| Dark\_Hills | houses | Straw house | documented-variant | 0.33 | documented-configuration | Stored relative weight; proportional draw is inferred, not verified generator code. Values are not normalized during conversion. |
| Dark\_Hills | houses | Wood house | documented-variant | 0.33 | documented-configuration | Stored relative weight; proportional draw is inferred, not verified generator code. Values are not normalized during conversion. |
| Dark\_Hills | houses | Stone house | documented-variant | 0.33 | documented-configuration | Stored relative weight; proportional draw is inferred, not verified generator code. Values are not normalized during conversion. |
| Avalon | Mordred underground entrance | Fix | documented-variant | 0.5 | documented-configuration | Stored relative weight; proportional draw is inferred, not verified generator code. Values are not normalized during conversion. |
| Avalon | Mordred underground entrance | Interval | documented-variant | 0.5 | documented-configuration | Stored relative weight; proportional draw is inferred, not verified generator code. Values are not normalized during conversion. |
| Storm\_Island | Sinbad / Roc quest caves | Sinbad cyclops cave | documented-variant | 0.5 | documented-configuration | Stored relative weight; proportional draw is inferred, not verified generator code. Values are not normalized during conversion. |
| Storm\_Island | Sinbad / Roc quest caves | Roc quest cave | documented-variant | 0.5 | documented-configuration | Stored relative weight; proportional draw is inferred, not verified generator code. Values are not normalized during conversion. |
| Dark\_Hills | default rule | other tiles in the documented pool | default-rule | 1.0 | documented-configuration | Default rule from the note, not an enumerated census of individual tiles. |
| Avalon | default rule | other tiles in the documented pool | default-rule | 1.0 | documented-configuration | Default rule from the note, not an enumerated census of individual tiles. |
| Storm\_Island | default rule | other tiles in the documented pool | default-rule | 1.0 | documented-configuration | Default rule from the note, not an enumerated census of individual tiles. |

## Map Generation Quotas

| Map id | Kind | Configured count | Footprints | Spacing lower metres | Spacing upper metres | Spacing status | Status |
|---|---|---|---|---|---|---|---|
| Dark\_Hills | Thieves\_Entrance | 1 | 40x40 | 0 | 0 | exact | documented-configuration |
| Avalon | Thieves\_Entrance | 1 | 40x40 | 0 | 0 | exact | documented-configuration |
| Storm\_Island | Thieves\_Entrance | 1 | 40x40 | 0 | 0 | exact | documented-configuration |
| Dark\_Hills | Special | 5 | 40x40 | 90 | 90 | exact | documented-configuration |
| Avalon | Special | 5 | 40x40 | 100 | 100 | exact | documented-configuration |
| Storm\_Island | Special | 5 | 40x40 | 100 | 100 | exact | documented-configuration |
| Dark\_Hills | Camp | 5 | 40x40;64x64 | 60 | 100 | aggregate-range; exact per-map minimum unspecified | documented-configuration |
| Avalon | Camp | 5 | 40x40;64x64 | 60 | 100 | aggregate-range; exact per-map minimum unspecified | documented-configuration |
| Storm\_Island | Camp | 5 | 40x40;64x64 | 60 | 100 | aggregate-range; exact per-map minimum unspecified | documented-configuration |
| Dark\_Hills | Teleporter | 17 | 6x6 | 45 | 55 | aggregate-range; exact per-map minimum unspecified | documented-configuration |
| Avalon | Teleporter | 10 | 6x6 | 45 | 55 | aggregate-range; exact per-map minimum unspecified | documented-configuration |
| Storm\_Island | Teleporter | 18 | 6x6 | 45 | 55 | aggregate-range; exact per-map minimum unspecified | documented-configuration |
| Dark\_Hills | Fountain | 7 | 6x6 | 90 | 100 | aggregate-range; exact per-map minimum unspecified | documented-configuration |
| Avalon | Fountain | 7 | 6x6;9x9 | 90 | 100 | aggregate-range; exact per-map minimum unspecified | documented-configuration |
| Storm\_Island | Fountain | 7 | 6x6 | 90 | 100 | aggregate-range; exact per-map minimum unspecified | documented-configuration |
| Dark\_Hills | Wandering\_Camp | 6 | 6x6 | 70 | 120 | aggregate-range; exact per-map minimum unspecified | documented-configuration |
| Avalon | Wandering\_Camp | 7 | 6x6 | 70 | 120 | aggregate-range; exact per-map minimum unspecified | documented-configuration |
| Storm\_Island | Wandering\_Camp | 8 | 6x6 | 70 | 120 | aggregate-range; exact per-map minimum unspecified | documented-configuration |
| Dark\_Hills | Corpse\_Master | 1 | 6x6 | 0 | 80 | aggregate-range; exact per-map minimum unspecified | documented-configuration |
| Avalon | Corpse\_Master | 1 | 6x6 | 0 | 80 | aggregate-range; exact per-map minimum unspecified | documented-configuration |
| Storm\_Island | Corpse\_Master | 1 | 6x6 | 0 | 80 | aggregate-range; exact per-map minimum unspecified | documented-configuration |
| Dark\_Hills | Crystal | 50 | 3x3;6x6 | 40 | 50 | aggregate-range; exact per-map minimum unspecified | documented-configuration |
| Avalon | Crystal | 40 | 3x3;6x6 | 40 | 50 | aggregate-range; exact per-map minimum unspecified | documented-configuration |
| Storm\_Island | Crystal | 40 | 3x3;6x6 | 40 | 50 | aggregate-range; exact per-map minimum unspecified | documented-configuration |
| Dark\_Hills | Start | 1 | 40x40 | 0 | 0 | exact | documented-configuration |
| Dark\_Hills | Map\_Boss | 1 | 64x64 | 0 | 0 | exact | documented-configuration |
| Dark\_Hills | Altar\_Of\_Heroes | 1 | 40x40 | 0 | 0 | exact | documented-configuration |
| Dark\_Hills | Key\_Keeper | 1 | 40x40 | 0 | 0 | exact | documented-configuration |
| Avalon | Start | 1 | 40x40 | 0 | 0 | exact | documented-configuration |
| Avalon | Map\_Boss | 1 | 64x64 | 0 | 0 | exact | documented-configuration |
| Avalon | Altar\_Of\_Heroes | 1 | 40x40 | 0 | 0 | exact | documented-configuration |
| Avalon | Key\_Keeper | 1 | 40x40 | 0 | 0 | exact | documented-configuration |
| Storm\_Island | Start | 1 | 40x40 | 0 | 0 | exact | documented-configuration |
| Storm\_Island | Map\_Boss | 1 | 64x64 | 0 | 0 | exact | documented-configuration |
| Storm\_Island | Altar\_Of\_Heroes | 1 | 40x40 | 0 | 0 | exact | documented-configuration |
| Storm\_Island | Key\_Keeper | 1 | 40x40 | 0 | 0 | exact | documented-configuration |
| Dark\_Hills | Ruin | 0 | 6x6 |   |   | not-specified | documented-configuration |
| Dark\_Hills | Key | 0 | 6x6 |   |   | not-specified | documented-configuration |
| Avalon | Ruin | 0 | 6x6 |   |   | not-specified | documented-configuration |
| Avalon | Key | 0 | 6x6 |   |   | not-specified | documented-configuration |
| Storm\_Island | Ruin | 0 | 6x6 |   |   | not-specified | documented-configuration |
| Storm\_Island | Key | 0 | 6x6 |   |   | not-specified | documented-configuration |
| Avalon | Stairs\_Entrance\_SW | 2 | 20x20 | 0 | 0 | exact | documented-configuration |
| Avalon | Stairs\_Entrance\_S | 2 | 20x20 | 0 | 0 | exact | documented-configuration |
| Avalon | Stairs\_Entrance\_SE | 3 | 20x20 | 0 | 0 | exact | documented-configuration |

## Map Generation Caps

| Map id | Flag | Cap scope | Tier | Configured maximum | Status | Notes |
|---|---|---|---|---|---|---|
| Dark\_Hills | Thieves\_Entrance | aggregate-flag |   | 1 | documented-configuration | Independent ceiling, not a guaranteed spawn count. |
| Dark\_Hills | Mirror\_Entrance | aggregate-flag |   | 1 | documented-configuration | Independent ceiling, not a guaranteed spawn count. |
| Dark\_Hills | Gold\_Entrance | aggregate-flag |   | 1 | documented-configuration | Independent ceiling, not a guaranteed spawn count. |
| Dark\_Hills | Combat\_Entrance | aggregate-flag |   | 1 | documented-configuration | Independent ceiling, not a guaranteed spawn count. |
| Dark\_Hills | Cursed\_Entrance | aggregate-flag |   | 1 | documented-configuration | Independent ceiling, not a guaranteed spawn count. |
| Dark\_Hills | Wishing\_Well | aggregate-flag |   | 1 | documented-configuration | Independent ceiling, not a guaranteed spawn count. |
| Dark\_Hills | Leprechaun\_Cauldron | aggregate-flag |   | 1 | documented-configuration | Independent ceiling, not a guaranteed spawn count. |
| Dark\_Hills | Grimoire\_Of\_Monsters | aggregate-flag |   | 2 | documented-configuration | Independent ceiling, not a guaranteed spawn count. |
| Dark\_Hills | Crystal\_Field | aggregate-flag |   | 1 | documented-configuration | Independent ceiling, not a guaranteed spawn count. |
| Dark\_Hills | Refugee | aggregate-flag |   | 1 | documented-configuration | Independent ceiling, not a guaranteed spawn count. |
| Dark\_Hills | Tumor | aggregate-flag |   | 1 | documented-configuration | Independent ceiling, not a guaranteed spawn count. |
| Dark\_Hills | Boss | aggregate-flag |   | 2 | documented-configuration | Independent ceiling, not a guaranteed spawn count. |
| Dark\_Hills | Blood\_Fountain | aggregate-flag |   | 2 | documented-configuration | Independent ceiling, not a guaranteed spawn count. |
| Dark\_Hills | Grimoire\_Of\_Monsters | each-tier | 1 | 1 | documented-configuration | Independent ceiling, not a guaranteed spawn count. |
| Dark\_Hills | Grimoire\_Of\_Monsters | each-tier | 2 | 1 | documented-configuration | Independent ceiling, not a guaranteed spawn count. |
| Dark\_Hills | Grimoire\_Of\_Monsters | each-tier | 3 | 1 | documented-configuration | Independent ceiling, not a guaranteed spawn count. |
| Dark\_Hills | Boss | each-boss-tile |   | 1 | documented-configuration | Independent ceiling, not a guaranteed spawn count. |
| Avalon | Thieves\_Entrance | aggregate-flag |   | 1 | documented-configuration | Independent ceiling, not a guaranteed spawn count. |
| Avalon | Mirror\_Entrance | aggregate-flag |   | 1 | documented-configuration | Independent ceiling, not a guaranteed spawn count. |
| Avalon | Gold\_Entrance | aggregate-flag |   | 1 | documented-configuration | Independent ceiling, not a guaranteed spawn count. |
| Avalon | Combat\_Entrance | aggregate-flag |   | 1 | documented-configuration | Independent ceiling, not a guaranteed spawn count. |
| Avalon | Cursed\_Entrance | aggregate-flag |   | 1 | documented-configuration | Independent ceiling, not a guaranteed spawn count. |
| Avalon | Wishing\_Well | aggregate-flag |   | 1 | documented-configuration | Independent ceiling, not a guaranteed spawn count. |
| Avalon | Leprechaun\_Cauldron | aggregate-flag |   | 1 | documented-configuration | Independent ceiling, not a guaranteed spawn count. |
| Avalon | Grimoire\_Of\_Monsters | aggregate-flag |   | 2 | documented-configuration | Independent ceiling, not a guaranteed spawn count. |
| Avalon | Crystal\_Field | aggregate-flag |   | 1 | documented-configuration | Independent ceiling, not a guaranteed spawn count. |
| Avalon | Refugee | aggregate-flag |   | 1 | documented-configuration | Independent ceiling, not a guaranteed spawn count. |
| Avalon | Tumor | aggregate-flag |   | 1 | documented-configuration | Independent ceiling, not a guaranteed spawn count. |
| Avalon | Boss | aggregate-flag |   | 2 | documented-configuration | Independent ceiling, not a guaranteed spawn count. |
| Avalon | Blood\_Fountain | aggregate-flag |   | 2 | documented-configuration | Independent ceiling, not a guaranteed spawn count. |
| Avalon | Grimoire\_Of\_Monsters | each-tier | 1 | 1 | documented-configuration | Independent ceiling, not a guaranteed spawn count. |
| Avalon | Grimoire\_Of\_Monsters | each-tier | 2 | 1 | documented-configuration | Independent ceiling, not a guaranteed spawn count. |
| Avalon | Grimoire\_Of\_Monsters | each-tier | 3 | 1 | documented-configuration | Independent ceiling, not a guaranteed spawn count. |
| Avalon | Boss | each-boss-tile |   | 1 | documented-configuration | Independent ceiling, not a guaranteed spawn count. |
| Storm\_Island | Thieves\_Entrance | aggregate-flag |   | 1 | documented-configuration | Independent ceiling, not a guaranteed spawn count. |
| Storm\_Island | Mirror\_Entrance | aggregate-flag |   | 1 | documented-configuration | Independent ceiling, not a guaranteed spawn count. |
| Storm\_Island | Gold\_Entrance | aggregate-flag |   | 1 | documented-configuration | Independent ceiling, not a guaranteed spawn count. |
| Storm\_Island | Combat\_Entrance | aggregate-flag |   | 1 | documented-configuration | Independent ceiling, not a guaranteed spawn count. |
| Storm\_Island | Cursed\_Entrance | aggregate-flag |   | 1 | documented-configuration | Independent ceiling, not a guaranteed spawn count. |
| Storm\_Island | Wishing\_Well | aggregate-flag |   | 1 | documented-configuration | Independent ceiling, not a guaranteed spawn count. |
| Storm\_Island | Leprechaun\_Cauldron | aggregate-flag |   | 1 | documented-configuration | Independent ceiling, not a guaranteed spawn count. |
| Storm\_Island | Grimoire\_Of\_Monsters | aggregate-flag |   | 2 | documented-configuration | Independent ceiling, not a guaranteed spawn count. |
| Storm\_Island | Crystal\_Field | aggregate-flag |   | 1 | documented-configuration | Independent ceiling, not a guaranteed spawn count. |
| Storm\_Island | Refugee | aggregate-flag |   | 1 | documented-configuration | Independent ceiling, not a guaranteed spawn count. |
| Storm\_Island | Tumor | aggregate-flag |   | 1 | documented-configuration | Independent ceiling, not a guaranteed spawn count. |
| Storm\_Island | Boss | aggregate-flag |   | 2 | documented-configuration | Independent ceiling, not a guaranteed spawn count. |
| Storm\_Island | Blood\_Fountain | aggregate-flag |   | 2 | documented-configuration | Independent ceiling, not a guaranteed spawn count. |
| Storm\_Island | Grimoire\_Of\_Monsters | each-tier | 1 | 1 | documented-configuration | Independent ceiling, not a guaranteed spawn count. |
| Storm\_Island | Grimoire\_Of\_Monsters | each-tier | 2 | 1 | documented-configuration | Independent ceiling, not a guaranteed spawn count. |
| Storm\_Island | Grimoire\_Of\_Monsters | each-tier | 3 | 1 | documented-configuration | Independent ceiling, not a guaranteed spawn count. |
| Storm\_Island | Boss | each-boss-tile |   | 1 | documented-configuration | Independent ceiling, not a guaranteed spawn count. |
| Dark\_Hills | Treants | aggregate-flag |   | 3 | documented-configuration | Independent ceiling, not a guaranteed spawn count. |

## Map Tile Tier Bands

| Map id | Tile selector | Tier | Band low | Band high | Status | Notes |
|---|---|---|---|---|---|---|
| Dark\_Hills | tier-suffixed tiles | 1 | 0 | 0.33 | documented-configuration | Preserves documented endpoints; boundary tie-breaking and final selection are not inferred here. |
| Dark\_Hills | tier-suffixed tiles | 2 | 0.33 | 0.67 | documented-configuration | Preserves documented endpoints; boundary tie-breaking and final selection are not inferred here. |
| Dark\_Hills | tier-suffixed tiles | 3 | 0.67 | 1 | documented-configuration | Preserves documented endpoints; boundary tie-breaking and final selection are not inferred here. |
| Dark\_Hills | blockers |   | 0 | 1 | documented-configuration | Preserves documented endpoints; boundary tie-breaking and final selection are not inferred here. |
| Dark\_Hills | regular stash entrances |   | 0.33 | 1 | documented-configuration | Preserves documented endpoints; boundary tie-breaking and final selection are not inferred here. |
| Dark\_Hills | Refugee camp |   | 0.33 | 1 | documented-configuration | Preserves documented endpoints; boundary tie-breaking and final selection are not inferred here. |
| Dark\_Hills | Mirror entrance |   | 0.33 | 1 | documented-configuration | Preserves documented endpoints; boundary tie-breaking and final selection are not inferred here. |
| Avalon | tier-suffixed tiles | 1 | 0 | 0.33 | documented-configuration | Preserves documented endpoints; boundary tie-breaking and final selection are not inferred here. |
| Avalon | tier-suffixed tiles | 2 | 0.33 | 0.67 | documented-configuration | Preserves documented endpoints; boundary tie-breaking and final selection are not inferred here. |
| Avalon | tier-suffixed tiles | 3 | 0.67 | 1 | documented-configuration | Preserves documented endpoints; boundary tie-breaking and final selection are not inferred here. |
| Avalon | blockers |   | 0 | 1 | documented-configuration | Preserves documented endpoints; boundary tie-breaking and final selection are not inferred here. |
| Avalon | regular stash entrances |   | 0.33 | 1 | documented-configuration | Preserves documented endpoints; boundary tie-breaking and final selection are not inferred here. |
| Avalon | Refugee camp |   | 0 | 1 | documented-configuration | Preserves documented endpoints; boundary tie-breaking and final selection are not inferred here. |
| Avalon | Mirror entrance |   | 0 | 1 | documented-configuration | Preserves documented endpoints; boundary tie-breaking and final selection are not inferred here. |
| Storm\_Island | tier-suffixed tiles | 1 | 0 | 0.33 | documented-configuration | Preserves documented endpoints; boundary tie-breaking and final selection are not inferred here. |
| Storm\_Island | tier-suffixed tiles | 2 | 0.33 | 0.67 | documented-configuration | Preserves documented endpoints; boundary tie-breaking and final selection are not inferred here. |
| Storm\_Island | tier-suffixed tiles | 3 | 0.67 | 1 | documented-configuration | Preserves documented endpoints; boundary tie-breaking and final selection are not inferred here. |
| Storm\_Island | blockers |   | 0 | 1 | documented-configuration | Preserves documented endpoints; boundary tie-breaking and final selection are not inferred here. |
| Storm\_Island | regular stash entrances |   | 0.33 | 1 | documented-configuration | Preserves documented endpoints; boundary tie-breaking and final selection are not inferred here. |
| Storm\_Island | Refugee camp |   | 0 | 1 | documented-configuration | Preserves documented endpoints; boundary tie-breaking and final selection are not inferred here. |
| Storm\_Island | Mirror entrance |   | 0 | 1 | documented-configuration | Preserves documented endpoints; boundary tie-breaking and final selection are not inferred here. |

## Map Stash Models

| Room | Probability percent | Approximate | Map scope | Condition | Model | Status | Notes |
|---|---|---|---|---|---|---|---|
| Combat | 50 | false | all three documented chapter maps | regular Thieves\_Entrance slot under proportional weighted selection | relative weights 0.5 / 0.4 / 0.1 | inferred | Conditional model result, not an empirical observed rate. |
| Cursed | 40 | false | all three documented chapter maps | regular Thieves\_Entrance slot under proportional weighted selection | relative weights 0.5 / 0.4 / 0.1 | inferred | Conditional model result, not an empirical observed rate. |
| Gold (Dagda's Harp) | 10 | false | all three documented chapter maps | regular Thieves\_Entrance slot under proportional weighted selection | relative weights 0.5 / 0.4 / 0.1 | inferred | Conditional model result, not an empirical observed rate. |
| Magic Mirror | 20 | true | conditional example; per-map empirical rate unestablished | five weighted draws without replacement against about seven eligible weight-1 competitors | Mirror weight 0.2; the eligible pool and draw model determine the result | inferred | Rough estimate recorded in the note, not a measured rate or a universal probability. |
| Magic Mirror choices (T1 tier) |   | false | all three maps; read from the 1.06 tree (Steam build 25174305) | Thieves\_Magic\_Mirror Nb Choice Selector, tester Is T1 Difficulty Condition | Magical Objects offered = 2 | decoded | Int literal read from the 1.06 tree. The mapping of tier T1/T2/T3 to green/orange/red is not stated in the file. |
| Magic Mirror choices (T2 tier) |   | false | all three maps; read from the 1.06 tree (Steam build 25174305) | Thieves\_Magic\_Mirror Nb Choice Selector, tester Is T2 Difficulty Condition | Magical Objects offered = 3 | decoded | Int literal read from the 1.06 tree. The mapping of tier T1/T2/T3 to green/orange/red is not stated in the file. |
| Magic Mirror choices (T3 tier) |   | false | all three maps; read from the 1.06 tree (Steam build 25174305) | Thieves\_Magic\_Mirror Nb Choice Selector, tester Is T3 Difficulty Condition | Magical Objects offered = 4 | decoded | Int literal read from the 1.06 tree. The mapping of tier T1/T2/T3 to green/orange/red is not stated in the file. |

## Map Generation Observations

| Map id | Metric | Reported count | Status | Sample scope | Observation date | Notes |
|---|---|---|---|---|---|---|
| Dark\_Hills | 40x40 slots | 14 | documented-configuration | one documented Dark Hills recipe/run; not a cross-run census |   | No new run was observed during conversion. |
| Dark\_Hills | 64x64 slots | 5 | documented-configuration | one documented Dark Hills recipe/run; not a cross-run census |   | No new run was observed during conversion. |
| Dark\_Hills | filled slots | 19 | reported-observation | one documented Dark Hills recipe/run; not a cross-run census |   | No new run was observed during conversion. |
| Dark\_Hills | placed Special tiles | 5 | reported-observation | one documented Dark Hills recipe/run; not a cross-run census |   | No new run was observed during conversion. |

Source: [`Map_Generation_References.tsv`](../data/Map_Generation_References.tsv), [`Map_Generation_Weights.tsv`](../data/Map_Generation_Weights.tsv), [`Map_Generation_Quotas.tsv`](../data/Map_Generation_Quotas.tsv), [`Map_Generation_Caps.tsv`](../data/Map_Generation_Caps.tsv), [`Map_Tile_Tier_Bands.tsv`](../data/Map_Tile_Tier_Bands.tsv), [`Map_Stash_Models.tsv`](../data/Map_Stash_Models.tsv), [`Map_Generation_Observations.tsv`](../data/Map_Generation_Observations.tsv).
*This page is generated from the TSV files in [data/](../data/) by `tools/build_browse.py`. Do not edit it by hand; fix the data and re-run the script.*
