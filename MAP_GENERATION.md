# Map generation reference

These seven tables transcribe the existing chapter-map generation note.
They describe the documented Dark Hills, Avalon and Storm Island recipes.
The recorded LiveOps_Update5 resource names do not establish a public game
version. They are not a fresh extraction or a cross-run occurrence census.

| Table | Rows | Contents |
|---|---:|---|
| [Map_Generation_References.tsv](data/Map_Generation_References.tsv) | 3 | Which resources supply tiles, pools, and recipes |
| [Map_Generation_Weights.tsv](data/Map_Generation_Weights.tsv) | 22 | Non-default variant weights and an explicit default rule per map |
| [Map_Generation_Quotas.tsv](data/Map_Generation_Quotas.tsv) | 45 | Per-kind counts, footprints, and documented spacing |
| [Map_Generation_Caps.tsv](data/Map_Generation_Caps.tsv) | 52 | Independent aggregate, tier, and per-boss-tile ceilings |
| [Map_Tile_Tier_Bands.tsv](data/Map_Tile_Tier_Bands.tsv) | 21 | Documented tier-band and map-specific placement ranges |
| [Map_Stash_Models.tsv](data/Map_Stash_Models.tsv) | 4 | Three conditional regular-stash shares and the approximate Mirror model |
| [Map_Generation_Observations.tsv](data/Map_Generation_Observations.tsv) | 4 | Dark Hills slot counts and the single reported run census |

## Configuration, models, and observations

`documented-configuration` means a setting reported by the source note.
`inferred` marks a probability model, and `reported-observation` marks the
existing single-run observation. Conversion itself performs no new game
measurement. These statuses must remain separate when writing an article.

A tile definition supplies flags, footprint, tier band and weight; the map
definition supplies the eligible pool; the generation recipe supplies kinds,
quotas, caps, slots and scenario restrictions. Configured counts are not a
guarantee that every requested placement succeeds. A per-slot scenario may
close a slot to a kind; it does not remove a tile definition from the pool.

## Counts, footprints and spacing

The source gives counts in Dark Hills / Avalon / Storm Island order. That
order is expanded into explicit map IDs: Teleporter counts are 17 / 10 / 18,
and Wandering_Camp counts are 6 / 7 / 8. All three have five Special slots.
Map_Boss uses 64x64; Avalon's fountains may also use 9x9; the three stair
kinds are recorded for Avalon only.

The note summarizes some spacing as a range across maps. For example, Camp
spacing is 60–100 metres. Those rows retain `aggregate-range; exact per-map
minimum unspecified` rather than inventing an exact minimum for each map.
`source_spacing` preserves the original expression. Ruin and Key have a
configured count of 0, but their unspecified spacing stays blank, not zero.

Caps are independent ceilings. Grimoire_Of_Monsters has an aggregate cap of
2 and a per-tier cap of 1. Boss has an aggregate cap of 2 and a cap of 1 for
each boss tile. These are separate scopes, not values to add together.
Thieves_Entrance and Mirror_Entrance have independent caps of 1.

Tier-band endpoints remain exactly as documented. Their boundary
tie-breaking is not inferred. Regular stash entrances have band [0.33, 1].
The Refugee camp and Mirror entrance use [0.33, 1] on Dark Hills and [0, 1]
on the other two maps. The broad non-default weight families are preserved,
including the printed 0.33 house weights; they are not silently normalized.

## Stash model limits

Regular Combat / Cursed / Gold stash entrance weights are 0.5 / 0.4 / 0.1.
The 50% / 40% / 10% shares depend on proportional weighted selection.
The placement driver's implementation was not read in the source work.
These shares therefore remain inferred conditional results, not measured
frequencies. The Mirror is a Special-pool candidate with weight 0.2; this
does not itself mean a 20% occurrence probability.

The source's roughly-one-in-five Mirror estimate assumes five weighted
draws without replacement against about seven eligible weight-1 competitors.
Its row is `inferred` and `approximate=true`, and does not claim a universal
or independently measured per-map rate. The single Dark Hills run filled
19 slots and placed five Special tiles, but does not establish a Mirror rate.
Its observation date was not recorded, so that field stays blank.

## Provenance

Every row records the original note, line, canonical Git-byte SHA-256 and
source revision. Resource patterns are game-relative identifiers. The
game version and extraction date were not established in the note and
remain null in VERSION.json, overriding the old 1.06 default. The original
private Markdown stays as evidence; binary format specifications, tools,
viewer implementation notes and app source remain outside this selection.

Source note: `datamining/tile_generation.md` at `0ae8f70b327a3b37b615babd9bd50f1281ac7acc`.
Canonical source SHA-256: `d1c3dfe5f4e39ab0680281ed8e461ec3d28df0920430e00a2559a50e6c9064f9`.
