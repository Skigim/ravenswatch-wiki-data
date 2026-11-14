# Selected tables

The repository holds 96 selected TSV files: 46 decoded text and index exports, 13 numerical talent tables, 18 numerical value tables, 3 enemy reference tables, 3 combat-configuration tables, 7 map-generation tables, 1 dialogue table, 1 voice-audio table, 2 game-modifier tables and 2 achievement and outfit tables. It also holds one corrections record. SHA-256 hashes identify exact file bytes. Declared row counts come from each file header.

The `2026-10-12-1.06` snapshot re-extracts every table from game build 1.06, except `In_Game_Observations.tsv` and `Fill_Pass_Values.tsv`. Those two hold evidence gathered on 1.05 and are unchanged. The snapshot adds five tables for Kintarō. [CHANGES-1.06.md](CHANGES-1.06.md) lists every row that changed. [VERSION.json](VERSION.json) records the source version of each table.

The `2026-10-20-memoir-corrections` snapshot corrects 17 spelling errors in eight hero memoir tables. Nothing was re-extracted. Every other table is unchanged.

The `2026-10-20-dialogue` snapshot adds one dialogue table decoded from the same 1.06 extraction. Every other table is unchanged.

The `2026-11-10-voice-audio` snapshot adds one voice-audio table read from the same 1.06 install. Every other table is unchanged.

The `2026-11-10-voice-banks` snapshot extends that table to the hero banks and `Maps.bank` and adds a `bank` column. Every other table is unchanged.

The `2026-11-12-starting-talents` snapshot adds `starting_talent` and `starting_talent_source` columns to the 13 numerical talent tables, read from the same 1.06 build. The other changes in those tables are a sentence added to the `notes` cell of each starting talent, the `# snapshot_id` header line and a new `# note` header line. Every other table is unchanged.

The `2026-11-13-contributor-claims` snapshot checks contributor claims against the 1.06 files, adds four tables (game modifiers, challenges, achievements and hero outfit unlocks) and adds or sharpens rows in `Mechanics_Values.tsv`, `Magical_Objects_Values.tsv` and `Map_Stash_Models.tsv`. Every other table is unchanged. [CLAIMS.md](CLAIMS.md) records the evidence.

## Text and index exports

These are verbatim decoded exports, except the eight memoir tables marked "spelling corrected". 30 of the 43 published in earlier snapshots came out of the 1.06 build byte for byte unchanged. 13 changed, and the three `Hero_Kintaro_*` text tables are new.

| File | Declared rows | Source identifier | SHA-256 |
|---|---:|---|---|
| [Common.LangEN.tsv](data/Common.LangEN.tsv) | 535 | `Common~GAM.xls` | `5c821888751faff0710c8d98e5f00d1dbebe2888786f81899c06a1fdd9d0f980` |
| [Enemy_Common.LangEN.tsv](data/Enemy_Common.LangEN.tsv) | 18 | `Enemy_Common~GAM.xls` | `2fa656a21181b93555aa6193d374b69630c9e410db98a6319652936dbf3be733` |
| [Hero_Aladdin_Common.LangEN.tsv](data/Hero_Aladdin_Common.LangEN.tsv) | 86 | `Hero_Aladdin_Common~GAM.xls` | `46e7694abd34e6a1a78e54bc47251c107e62517dd370cfb138c6e39e07273ba9` |
| [Hero_Aladdin_Memoirs.LangEN.tsv](data/Hero_Aladdin_Memoirs.LangEN.tsv) | 15 | `Hero_Aladdin_Memoirs~GAM.xls` (spelling corrected) | `d9b6292e0c12f28dab67a0cb7bbcee5dbaeca7706f503fcb402be65171c1ac0c` |
| [Hero_Aladdin_Skins.LangEN.tsv](data/Hero_Aladdin_Skins.LangEN.tsv) | 24 | `Hero_Aladdin_Skins~GAM.xls` | `62bc9c731052d465e395b03debd885962513171e4ff77e3c15f0c3d5aba1fb36` |
| [Hero_Beowulf_Common.LangEN.tsv](data/Hero_Beowulf_Common.LangEN.tsv) | 81 | `Hero_Beowulf_Common~GAM.xls` | `179131e4672e970a471a711aefcb6e4bd489365981e1f8ed9e075f8a0330cebd` |
| [Hero_Beowulf_Memoirs.LangEN.tsv](data/Hero_Beowulf_Memoirs.LangEN.tsv) | 15 | `Hero_Beowulf_Memoirs~GAM.xls` | `367f0525d796e1eaff9d2983fd1bbe6e937c592787d494b2bb31c86141851afa` |
| [Hero_Beowulf_Skins.LangEN.tsv](data/Hero_Beowulf_Skins.LangEN.tsv) | 24 | `Hero_Beowulf_Skins~GAM.xls` | `9093534cf162df3d6536d4b469dda0bd290c7b772d6ff45349b108f3b1f83de0` |
| [Hero_Carmilla_Common.LangEN.tsv](data/Hero_Carmilla_Common.LangEN.tsv) | 80 | `Hero_Carmilla_Common~GAM.xls` | `6d82739fd93a36b4b13e379c8e9ed6350154ee38461c4d6abe74a4569f24773b` |
| [Hero_Carmilla_Memoirs.LangEN.tsv](data/Hero_Carmilla_Memoirs.LangEN.tsv) | 15 | `Hero_Carmilla_Memoirs~GAM.xls` (spelling corrected) | `61938ca9df3b57787c6dd2e382b31ad7525c00c01b93131a5ebcd6e06b97809c` |
| [Hero_Carmilla_Skins.LangEN.tsv](data/Hero_Carmilla_Skins.LangEN.tsv) | 21 | `Hero_Carmilla_Skins~GAM.xls` | `e5fbfe5d0699bdbbdaa3ac2b99e8d2cf8b9d7fdcb4ec61b9c2f0e60ecd29ffc9` |
| [Hero_Geppetto_Common.LangEN.tsv](data/Hero_Geppetto_Common.LangEN.tsv) | 85 | `Hero_Geppetto_Common~GAM.xls` | `1e272b9c01aa6b37b2ca08d805d80f2b9fcc3fef2ca03b2ee8ac6c10e437d599` |
| [Hero_Geppetto_Memoirs.LangEN.tsv](data/Hero_Geppetto_Memoirs.LangEN.tsv) | 15 | `Hero_Geppetto_Memoirs~GAM.xls` (spelling corrected) | `5fa4467340db47137238f36cab1b421fa3783a1201f3e01a5a3908e12ec31340` |
| [Hero_Geppetto_Skins.LangEN.tsv](data/Hero_Geppetto_Skins.LangEN.tsv) | 24 | `Hero_Geppetto_Skins~GAM.xls` | `adb44842b3ef708c455f27ac1bf816479f90cf9d6341343bb7f3318b899a1353` |
| [Hero_Juliet_Common.LangEN.tsv](data/Hero_Juliet_Common.LangEN.tsv) | 76 | `Hero_Juliet_Common~GAM.xls` | `8ad8038d9b41748d771b2f1fe154a386750e801734eeffb27ab3bf7b062a60d5` |
| [Hero_Juliet_Memoirs.LangEN.tsv](data/Hero_Juliet_Memoirs.LangEN.tsv) | 15 | `Hero_Juliet_Memoirs~GAM.xls` (spelling corrected) | `6e1d00f3aac1ef1275ba836ff557750afcf82b38f0121b7017fb23f0127ffc82` |
| [Hero_Juliet_Skins.LangEN.tsv](data/Hero_Juliet_Skins.LangEN.tsv) | 20 | `Hero_Juliet_Skins~GAM.xls` | `01f3722d4d23051a2b3dc4e0a1829f49df25b03a332036dc319abb0f5a64af25` |
| [Hero_Kintaro_Common.LangEN.tsv](data/Hero_Kintaro_Common.LangEN.tsv) | 83 | `Hero_Kintaro_Common~GAM.xls` | `ed29a93fcf31ed6185d73407fa95b96027be3252d2f8959c743cb08ffc9f51d1` |
| [Hero_Kintaro_Memoirs.LangEN.tsv](data/Hero_Kintaro_Memoirs.LangEN.tsv) | 22 | `Hero_Kintaro_Memoirs~GAM.xls` (spelling corrected) | `62c470599ddd5a5ea4184b42d7c764a87457ff7cf9854c0af89aca400a591720` |
| [Hero_Kintaro_Skins.LangEN.tsv](data/Hero_Kintaro_Skins.LangEN.tsv) | 21 | `Hero_Kintaro_Skins~GAM.xls` | `37af62c088672b1c5f0b8042fc150601b479f1a6f259ddcb2b6e97a55e9375b4` |
| [Hero_Melusine_Common.LangEN.tsv](data/Hero_Melusine_Common.LangEN.tsv) | 79 | `Hero_Melusine_Common~GAM.xls` | `635dddb89bc732c0f1b7478483b806e81a20aeb16164b64243881b50185a4dd4` |
| [Hero_Melusine_Memoirs.LangEN.tsv](data/Hero_Melusine_Memoirs.LangEN.tsv) | 15 | `Hero_Melusine_Memoirs~GAM.xls` | `2c1b3db5cb3c8dd924b1d7aef0403b2d7bf2db83a569f3a19753b938e4aa98ff` |
| [Hero_Melusine_Skins.LangEN.tsv](data/Hero_Melusine_Skins.LangEN.tsv) | 21 | `Hero_Melusine_Skins~GAM.xls` | `c86e5156a3e339ca07b4db8ca0e57e3e4277247db657f4c0c90b05481f7f8b3a` |
| [Hero_Merlin_Common.LangEN.tsv](data/Hero_Merlin_Common.LangEN.tsv) | 103 | `Hero_Merlin_Common~GAM.xls` | `0f1329dc7a8d7681b1b30af8187f38b7342ee87c1ff11e8db823fb3966c298d5` |
| [Hero_Merlin_Memoirs.LangEN.tsv](data/Hero_Merlin_Memoirs.LangEN.tsv) | 22 | `Hero_Merlin_Memoirs~GAM.xls` (spelling corrected) | `8c5aaac9afa7fc586e3c0a9eec4682e91ba6dc73c29ad8f27f3497c130a2e3e3` |
| [Hero_Merlin_Skins.LangEN.tsv](data/Hero_Merlin_Skins.LangEN.tsv) | 21 | `Hero_Merlin_Skins~GAM.xls` | `a9986dc79f7d03b92b71e1d9f83d0787926bf07bccefe5edf8a39919284fc971` |
| [Hero_Piper_Common.LangEN.tsv](data/Hero_Piper_Common.LangEN.tsv) | 83 | `Hero_Piper_Common~GAM.xls` | `2fdefe094a3723e8b0eeb5692930222f796a37399218b670c36556029220a0ee` |
| [Hero_Piper_Memoirs.LangEN.tsv](data/Hero_Piper_Memoirs.LangEN.tsv) | 15 | `Hero_Piper_Memoirs~GAM.xls` (spelling corrected) | `6d6af07af491e725f8de24ca05db4ac8e5e48eda6615463b89a278f04036464b` |
| [Hero_Piper_Skins.LangEN.tsv](data/Hero_Piper_Skins.LangEN.tsv) | 27 | `Hero_Piper_Skins~GAM.xls` | `ccc5210108b0b67a40f5bef240fd3898481eaf80d32c025e4ed10295e51f1d79` |
| [Hero_RED_Common.LangEN.tsv](data/Hero_RED_Common.LangEN.tsv) | 103 | `Hero_RED_Common~GAM.xls` | `15d1686fbd9dc9e11abc542693f63fcbaeaab2e3338c22671135a7377cfb3286` |
| [Hero_RED_Memoirs.LangEN.tsv](data/Hero_RED_Memoirs.LangEN.tsv) | 15 | `Hero_RED_Memoirs~GAM.xls` | `2e687c97e7624c5eda8f5333d37284f47dfcb8dfcde0ae8a80f04ae03842d706` |
| [Hero_RED_Skins.LangEN.tsv](data/Hero_RED_Skins.LangEN.tsv) | 24 | `Hero_RED_Skins~GAM.xls` | `a95da39d3fbe07ba6a77243eb9cca5cf91e29abf341943c3d0f7ac83ee2a59d0` |
| [Hero_Romeo_Common.LangEN.tsv](data/Hero_Romeo_Common.LangEN.tsv) | 75 | `Hero_Romeo_Common~GAM.xls` | `70ed35b44eef487c4b052c02ed7c3bc1f9dce5d9338b41f071f244c5fc21124d` |
| [Hero_Romeo_Memoirs.LangEN.tsv](data/Hero_Romeo_Memoirs.LangEN.tsv) | 15 | `Hero_Romeo_Memoirs~GAM.xls` (spelling corrected) | `63fe1fbec7e56478eba6ccfdf25d30a09b80c03845b3e736e833f2a84e5f0636` |
| [Hero_Romeo_Skins.LangEN.tsv](data/Hero_Romeo_Skins.LangEN.tsv) | 20 | `Hero_Romeo_Skins~GAM.xls` | `f30b0b2def0d7cd0ea7c34759e4ad3eaa4727ca8b075eb44cce4544f50e5d7a8` |
| [Hero_Snow_Queen_Common.LangEN.tsv](data/Hero_Snow_Queen_Common.LangEN.tsv) | 82 | `Hero_Snow_Queen_Common~GAM.xls` | `3a47fbd08948ecf733471ea27fc6240740c46b6258f005fe67735f9e641fdad1` |
| [Hero_Snow_Queen_Memoirs.LangEN.tsv](data/Hero_Snow_Queen_Memoirs.LangEN.tsv) | 15 | `Hero_Snow_Queen_Memoirs~GAM.xls` | `28aba846681eac9c60be2b21b60114aef40aa5fee222eca09392e475cba5762c` |
| [Hero_Snow_Queen_Skins.LangEN.tsv](data/Hero_Snow_Queen_Skins.LangEN.tsv) | 27 | `Hero_Snow_Queen_Skins~GAM.xls` | `ceaacf8fc2d39156304e2852fa92d5aa6efea7fe0c5ccd7fe0b00934b273823b` |
| [Hero_SunWukong_Common.LangEN.tsv](data/Hero_SunWukong_Common.LangEN.tsv) | 74 | `Hero_SunWukong_Common~GAM.xls` | `a25d4792c94325b4f6f5deab460c94d81ec1f28d73fa61e3cc3c149a29453875` |
| [Hero_SunWukong_Memoirs.LangEN.tsv](data/Hero_SunWukong_Memoirs.LangEN.tsv) | 15 | `Hero_SunWukong_Memoirs~GAM.xls` | `793292dabf76818f586b341275fc65c074947fb15ac5396f8c0e6ecc9fcaaea3` |
| [Hero_SunWukong_Skins.LangEN.tsv](data/Hero_SunWukong_Skins.LangEN.tsv) | 24 | `Hero_SunWukong_Skins~GAM.xls` | `d35daca52df7540d2d71376b75b85cd805a1e80314251cd0959a5ec8f5a981a5` |
| [Magical_Objects.LangEN.tsv](data/Magical_Objects.LangEN.tsv) | 334 | `Magical_Objects~GAM.xls` | `6b55434f642d7d608c681968d26fb9c149c8ca6d198c6c46fe9db72a1564bb82` |
| [Magical_Objects_Index.tsv](data/Magical_Objects_Index.tsv) | 58 | `EntitySettings/Objects/Magical_Objects!<Rarity>!<Name>` | `eaeaf0ac45e8c0a2cf618f898987c6e04c0dc7d9872a06547ba5dce25f6c8d21` |
| [Magical_Objects_Sources.tsv](data/Magical_Objects_Sources.tsv) | 48 | `EntitySettings/<Folder>/<Entity> that set Loot\<Rarity> Drop Chance values` | `90b96437c3ac3d6c6502b0bedf0313b8a94a1f0bed9ea32a31542390ceadb46d` |
| [Melodies.LangEN.tsv](data/Melodies.LangEN.tsv) | 25 | `Melodies~GAM.xls` | `e977ea1557aa498834a7ad20ab16ecdfb6deee6b5817efb763f31b07f2e1b5ca` |
| [Melodies_Index.tsv](data/Melodies_Index.tsv) | 12 | `EntitySettings/Objects/Melodies!<Name>` | `a2d89ce5cfe3ca02c9ca15b4f4c9ea5e2be0de8fbd18f9a280d481b1ebce6205` |

## Corrections record

This file lists every spelling correction made to the memoir tables, by text key, with the wrong and right strings. After a new game export, reapply a row only where its wrong string is still present.

| File | Declared rows | Source identifier | SHA-256 |
|---|---:|---|---|
| [Hero_Memoirs_Corrections.tsv](data/Hero_Memoirs_Corrections.tsv) | 17 | Spelling corrections to `Hero_*_Memoirs.LangEN.tsv` (2026-10-20) | `7751eb39388ba403cf5ec565bf7bdbef08c324882dcd0d525da0617977f0076c` |

## Numerical talent tables

These tables publish 26 talents for each of the 13 heroes, with unlock ranks and tooltip traces. Rows whose effect text is unchanged since 1.05 keep their October 5 compendium check. Changed and new rows are datamined only. [TALENTS.md](TALENTS.md) describes the method.

| File | Declared rows | Source identifier | SHA-256 |
|---|---:|---|---|
| [Hero_RED_Talents.tsv](data/Hero_RED_Talents.tsv) | 26 | Re-extracted from build 1.06 (2026-10-12); unchanged rows keep the 2026-10-05 compendium check | `9beb0d5a6bd6339762df13cacb11d62da1fd6f9d39b71f1940483a253bf16ed5` |
| [Hero_Snow_Queen_Talents.tsv](data/Hero_Snow_Queen_Talents.tsv) | 26 | Re-extracted from build 1.06 (2026-10-12); unchanged rows keep the 2026-10-05 compendium check | `1d4ad08bfacc41c85d7ab50059bb415cb3fa0da98d39f0cab42c33f64c53cdf0` |
| [Hero_Beowulf_Talents.tsv](data/Hero_Beowulf_Talents.tsv) | 26 | Re-extracted from build 1.06 (2026-10-12); unchanged rows keep the 2026-10-05 compendium check | `5ba78075a8158f09347849d6f873be9c5fff8760fc12be15bd500ff6b14dd5bb` |
| [Hero_Piper_Talents.tsv](data/Hero_Piper_Talents.tsv) | 26 | Re-extracted from build 1.06 (2026-10-12); unchanged rows keep the 2026-10-05 compendium check | `ed34b5eab63fab2b426ec75fd3aaabbed5add94434bddbd873303577b7bb5f2e` |
| [Hero_Aladdin_Talents.tsv](data/Hero_Aladdin_Talents.tsv) | 26 | Re-extracted from build 1.06 (2026-10-12); unchanged rows keep the 2026-10-05 compendium check | `a78e787e14812939732044b743a5764b2c6a8c712d172f78beb3cb543b3f71d6` |
| [Hero_Melusine_Talents.tsv](data/Hero_Melusine_Talents.tsv) | 26 | Re-extracted from build 1.06 (2026-10-12); unchanged rows keep the 2026-10-05 compendium check | `138aa5d7c2c008343b5ba8261f17b8c0cad25d5e74e16c868bbf01be7c13d5eb` |
| [Hero_Geppetto_Talents.tsv](data/Hero_Geppetto_Talents.tsv) | 26 | Re-extracted from build 1.06 (2026-10-12); unchanged rows keep the 2026-10-05 compendium check | `85bbe86e365dc0eab11fd95a8efc77a9adad5c602c338cabbac2ee7d4d31ba37` |
| [Hero_SunWukong_Talents.tsv](data/Hero_SunWukong_Talents.tsv) | 26 | Re-extracted from build 1.06 (2026-10-12); unchanged rows keep the 2026-10-05 compendium check | `622fafb99cff7eb2ccfb961c96a5f6e7d5d0db9614b1a375a9efc63e1912d249` |
| [Hero_Carmilla_Talents.tsv](data/Hero_Carmilla_Talents.tsv) | 26 | Re-extracted from build 1.06 (2026-10-12); unchanged rows keep the 2026-10-05 compendium check | `f5741a626ef1a0bc3c64e0229a27a14fc85633de031393b9a64b6f4866446fce` |
| [Hero_Romeo_Talents.tsv](data/Hero_Romeo_Talents.tsv) | 26 | Re-extracted from build 1.06 (2026-10-12); unchanged rows keep the 2026-10-05 compendium check | `8b9395c56d7f8cc0b8ed485cef62138c756d2521b60eecb7b3faf2632657565d` |
| [Hero_Juliet_Talents.tsv](data/Hero_Juliet_Talents.tsv) | 26 | Re-extracted from build 1.06 (2026-10-12); unchanged rows keep the 2026-10-05 compendium check | `efa448a3a05644ea3ace4cb51d5727061a116253d46fc09786dc03969e135c8b` |
| [Hero_Merlin_Talents.tsv](data/Hero_Merlin_Talents.tsv) | 26 | Re-extracted from build 1.06 (2026-10-12); unchanged rows keep the 2026-10-05 compendium check | `b1feda8a3a32173af0962f05d5f468744674a98f6d90fd815aa81439a52d068b` |
| [Hero_Kintaro_Talents.tsv](data/Hero_Kintaro_Talents.tsv) | 26 | Extracted from build 1.06 (2026-10-12); datamined only | `f453234be0d027b1914e266ec6ac4ba6e7916d6007552bf15088d73b87a8dae6` |

## Numerical value tables

These tables hold decoded ability, Magical Object, Melody and mechanics values beside the October 6 check. A check whose decoded value changed in 1.06 is marked stale. [VALUES.md](VALUES.md) describes the columns, the statuses and the check.

| File | Declared rows | Source identifier | SHA-256 |
|---|---:|---|---|
| [Hero_RED_Abilities.tsv](data/Hero_RED_Abilities.tsv) | 89 | Re-extracted from build 1.06 (2026-10-12) with the 2026-10-06 check carried over | `4587a3f33fa3b5cb71d3d8f3d2664c5fc1ee379cf3ec34e8a54180f737daed53` |
| [Hero_Snow_Queen_Abilities.tsv](data/Hero_Snow_Queen_Abilities.tsv) | 57 | Re-extracted from build 1.06 (2026-10-12) with the 2026-10-06 check carried over | `60d85081371a4355547910c7d2592bb9a451e3e0ece1583635fc6006c0c7f89d` |
| [Hero_Beowulf_Abilities.tsv](data/Hero_Beowulf_Abilities.tsv) | 53 | Re-extracted from build 1.06 (2026-10-12) with the 2026-10-06 check carried over | `82693809643bd6170e153388fa67978ec6493a16c5f7e8989216b1e849e232a2` |
| [Hero_Piper_Abilities.tsv](data/Hero_Piper_Abilities.tsv) | 73 | Re-extracted from build 1.06 (2026-10-12) with the 2026-10-06 check carried over | `688f7c2439b080011715569ff3255e790bb2672894024e030dac7b2144fe2749` |
| [Hero_Aladdin_Abilities.tsv](data/Hero_Aladdin_Abilities.tsv) | 57 | Re-extracted from build 1.06 (2026-10-12) with the 2026-10-06 check carried over | `c3ed01b498de917d4889d7933cb16e87893e17d6a89c7140872d70db9e84e33a` |
| [Hero_Melusine_Abilities.tsv](data/Hero_Melusine_Abilities.tsv) | 51 | Re-extracted from build 1.06 (2026-10-12) with the 2026-10-06 check carried over | `40d70b4fad3771665ddba7aeb19389d8b6831bbabaa62ee9387f4a3de2a55d11` |
| [Hero_Geppetto_Abilities.tsv](data/Hero_Geppetto_Abilities.tsv) | 58 | Re-extracted from build 1.06 (2026-10-12) with the 2026-10-06 check carried over | `9659a50a8a9ea9760b133600c4b365f8ca941c06c0df730db843452170e2a7b3` |
| [Hero_SunWukong_Abilities.tsv](data/Hero_SunWukong_Abilities.tsv) | 57 | Re-extracted from build 1.06 (2026-10-12) with the 2026-10-06 check carried over | `f26b61e30e5e11e304102fd1e31e18311c7232928ade3d112573c9111f82a0d0` |
| [Hero_Carmilla_Abilities.tsv](data/Hero_Carmilla_Abilities.tsv) | 76 | Re-extracted from build 1.06 (2026-10-12) with the 2026-10-06 check carried over | `8c4829a1ed4f6d1128df5c826c1d9482f02290aa89a7e924e014093c84d380be` |
| [Hero_Romeo_Abilities.tsv](data/Hero_Romeo_Abilities.tsv) | 58 | Re-extracted from build 1.06 (2026-10-12) with the 2026-10-06 check carried over | `2e4ce7561380d56d405c04d699b94f5bebc3ff24d37050cc633610033534987d` |
| [Hero_Juliet_Abilities.tsv](data/Hero_Juliet_Abilities.tsv) | 70 | Re-extracted from build 1.06 (2026-10-12) with the 2026-10-06 check carried over | `97fd70168ecdcc76479d0bafa864c77048f84e571bd1a72c423f470cdc50c837` |
| [Hero_Merlin_Abilities.tsv](data/Hero_Merlin_Abilities.tsv) | 172 | Re-extracted from build 1.06 (2026-10-12) with the 2026-10-06 check carried over | `8889cd28e1847c34e565571cb8ae6c2ba3b7608f0306956a84ab21ffaebf6e5c` |
| [Hero_Kintaro_Abilities.tsv](data/Hero_Kintaro_Abilities.tsv) | 34 | Extracted from build 1.06 (2026-10-12); not checked in game | `116513b4d905d334cc368aebf59079d9c516ca4fb8b33c7b08cf1d04eca9fe9f` |
| [Magical_Objects_Values.tsv](data/Magical_Objects_Values.tsv) | 315 | Re-extracted from build 1.06 (2026-10-12) with the 2026-10-06 check carried over | `d625b24a5a8e5f388e3a2967a5969075155bf9ee9acc4e4d15f49d7998427b96` |
| [Melodies_Values.tsv](data/Melodies_Values.tsv) | 21 | Re-extracted from build 1.06 (2026-10-12) with the 2026-10-06 check carried over | `d4d77bee1227a56b1ca41bfbbe2aef9560d95065d63038f56af7287175b1a75d` |
| [Mechanics_Values.tsv](data/Mechanics_Values.tsv) | 247 | Re-extracted from build 1.06 (2026-10-12) with the 2026-10-06 check carried over | `8ff55c18ed3f8e8a9a0d8283ddc9962dc7b509792bcae2361d677a43b3143fb1` |
| [In_Game_Observations.tsv](data/In_Game_Observations.tsv) | 94 | Maintainer readings in the in-game Compendium on 1.05 (2026-10-06) | `d1d58bba05a0d935c50c18dd13f6d2639cab65b3589d349f3e60e1e3c952f08c` |
| [Fill_Pass_Values.tsv](data/Fill_Pass_Values.tsv) | 65 | Second decoding pass over values missing from the 1.05 corrected table (2026-10-06) | `8161ee55777b3989a2377b9f34c9845bd548d90a8ae66f8dc2bd73029907293b` |

## Enemy reference selection

These three tables were added in `2026-10-16-enemies` from existing Markdown
notes, not newly decoded or checked in game. The earlier 77 tables above
were not changed by that addition. Source game version and extraction date remain
unknown; VERSION.json contains explicit table overrides. See ENEMIES.md.

| File | Declared rows | Source identifier | SHA-256 |
|---|---:|---|---|
| [Enemy_Definitions.tsv](data/Enemy_Definitions.tsv) | 81 | Existing enemy Markdown note, source commit `77b9e0416a01146a08d232ca465dd1b4b4756aa8` | `048d9fc7fd4de0e43736db234cfabbb1895b4cc28c6d14aa1e22d9f5e78bace0` |
| [Enemy_Tribe_Map_References.tsv](data/Enemy_Tribe_Map_References.tsv) | 75 | Existing enemy Markdown note, source commit `77b9e0416a01146a08d232ca465dd1b4b4756aa8` | `805062a3712239d95580b3b59814cd390ee6a0e04b942b3d12805fd175f9ae60` |
| [Enemy_Definition_Flags.tsv](data/Enemy_Definition_Flags.tsv) | 6 | Existing enemy Markdown note, source commit `77b9e0416a01146a08d232ca465dd1b4b4756aa8` | `bbbf661494672f006a7060f1824e32fece71e15f04944c90fc49f132035cc8bb` |

## Enemy combat configuration

Added in `2026-10-16-gameplay-notes` from existing Markdown evidence only. No fresh game
extraction or live verification was performed. Game-version overrides are
unverified; previous tables keep their attribution. See [COMBAT.md](COMBAT.md).

| File | Declared rows | Source identifier | SHA-256 |
|---|---:|---|---|
| [Enemy_Combat_Values.tsv](data/Enemy_Combat_Values.tsv) | 24 | `datamining/docs/enemy_combat_fields.md` at `0ae8f70b327a3b37b615babd9bd50f1281ac7acc` | `051dc647c5e38727bc209f0d9f6d7d69a8bd32330105c4adae37035a2075e455` |
| [Enemy_Combat_Picker_Values.tsv](data/Enemy_Combat_Picker_Values.tsv) | 9 | `datamining/docs/enemy_combat_fields.md` at `0ae8f70b327a3b37b615babd9bd50f1281ac7acc` | `32ca684a696825808022dbd110d12d10ba9c9d8e9f8580ba9117e70dca53d571` |
| [Enemy_Chapter_Damage_Factors.tsv](data/Enemy_Chapter_Damage_Factors.tsv) | 16 | `datamining/docs/enemy_combat_fields.md` at `0ae8f70b327a3b37b615babd9bd50f1281ac7acc` | `95d96e2b9e1a5b85f98e5c59353424f5ad6c0241c8b3b8aecf5b138f5a4feb54` |

## Map generation

Added in `2026-10-16-gameplay-notes` from existing Markdown evidence only. No fresh game
extraction or live verification was performed. Game-version overrides are
unverified; previous tables keep their attribution. See [MAP_GENERATION.md](MAP_GENERATION.md).

| File | Declared rows | Source identifier | SHA-256 |
|---|---:|---|---|
| [Map_Generation_References.tsv](data/Map_Generation_References.tsv) | 3 | `datamining/tile_generation.md` at `0ae8f70b327a3b37b615babd9bd50f1281ac7acc` | `a0af67f074b43ea44660eb47fdd27ab3f025151098b4f564147833e20a3362de` |
| [Map_Generation_Weights.tsv](data/Map_Generation_Weights.tsv) | 22 | `datamining/tile_generation.md` at `0ae8f70b327a3b37b615babd9bd50f1281ac7acc` | `72084223425b8da56d0fb7173c3b5e5d0f580c3bf77c687311412c436a263cc3` |
| [Map_Generation_Quotas.tsv](data/Map_Generation_Quotas.tsv) | 45 | `datamining/tile_generation.md` at `0ae8f70b327a3b37b615babd9bd50f1281ac7acc` | `7e7dafa25f6c747240eb97658644b88ec5984ab7309e8edf299d210d3d12e693` |
| [Map_Generation_Caps.tsv](data/Map_Generation_Caps.tsv) | 52 | `datamining/tile_generation.md` at `0ae8f70b327a3b37b615babd9bd50f1281ac7acc` | `5455c322557b7948d2a5aef55c46cd93d23aa740d12f3e6738e5083acdb2ee95` |
| [Map_Tile_Tier_Bands.tsv](data/Map_Tile_Tier_Bands.tsv) | 21 | `datamining/tile_generation.md` at `0ae8f70b327a3b37b615babd9bd50f1281ac7acc` | `38e1cb9ec745c1c630d1c98431e689b0d68159d750ed581755589cb030155190` |
| [Map_Stash_Models.tsv](data/Map_Stash_Models.tsv) | 7 | `datamining/tile_generation.md` at `0ae8f70b327a3b37b615babd9bd50f1281ac7acc` | `2721cf68507bd2a81dde7b0a1664eb0ed6f71452f501577c2a4655a6b5b232be` |
| [Map_Generation_Observations.tsv](data/Map_Generation_Observations.tsv) | 4 | `datamining/tile_generation.md` at `0ae8f70b327a3b37b615babd9bd50f1281ac7acc` | `7805fa5e50201585a9f3cce9bcc5652bb20e956fe4b9a06dbd0bd11015af7a6a` |

## Dialogue

Added in `2026-10-20-dialogue`. Decoded from the 1.06 extraction of 2026-10-12: the dialogue text tables, with speakers from the bark players and triggers from the bark setups in the entity settings, or the situation the key names where no trigger was decoded. Not checked in game. See [DIALOGUE.md](DIALOGUE.md).

| File | Declared rows | Source identifier | SHA-256 |
|---|---:|---|---|
| [Dialogue_Lines.tsv](data/Dialogue_Lines.tsv) | 5847 | `Hero_<Hero>_Barks~GAM.xls` (13), `NPC_Sandman`, `NPC_Sinbad`, `NPC_Morgan`, `NPC_BabaYaga`, `Map_Dark_Hills_Dialogs`, `Refugees` (spoken rows); EntitySettings bark setups and bark players | `073af62f8b2eae4eb2bb65dbf37c4facdd0fae01269c4e25fc82010067a56422` |

## Voice audio

Added in `2026-11-10-voice-audio`; extended to the hero banks and `Maps.bank` in `2026-11-10-voice-banks`. Clip names, positions and lengths read on 2026-11-10 from the audio banks of the 1.06 install (Steam build ID `25174305`), paired with the keys of the dialogue and memoir tables. Not checked by listening. See [VOICE.md](VOICE.md).

| File | Declared rows | Source identifier | SHA-256 |
|---|---:|---|---|
| [Voice_Lines_Audio.tsv](data/Voice_Lines_Audio.tsv) | 6004 | `Audio/Voice_EN.bank`, `Audio/Hero_<Hero>.bank` (12), `Audio/Maps.bank`; `data/Dialogue_Lines.tsv`; `data/Hero_<Hero>_Memoirs.LangEN.tsv` (13) | `d70c547b7d76a84f77dcc1d45424c15200991c83569f08a53a6c4fe514fcf197` |

## Game modifiers, challenges, achievements and outfits

Added in `2026-11-13-contributor-claims`. Read from the Definitions of the 1.06 extraction tree (Steam build ID `25174305`) and the text tables, and not checked in game. Achievements ship no name or description text, so those columns are empty. See [CLAIMS.md](CLAIMS.md).

| File | Declared rows | Source identifier | SHA-256 |
|---|---:|---|---|
| [Game_Modifiers.tsv](data/Game_Modifiers.tsv) | 22 | `ChallengesAndGameModifiers~GAM.xls`; `Definitions/GameModifiers/*.gamemodifierdef` | `145256fabc23c393feaf914e40360880a0ce420ac4f72a396076242002a9432c` |
| [Challenges.tsv](data/Challenges.tsv) | 5 | `ChallengesAndGameModifiers~GAM.xls`; `Definitions/Challenges/*.challengedef` | `5931acd2a6d81bb06602f280eb88b49d9667b1079d7b0548c328de78ed364060` |
| [Achievements.tsv](data/Achievements.tsv) | 48 | `Definitions/Achievements/*.Achievementdef` | `a430a47702153a379883514a2285183fea84a30e73a28513b22f4eba0891e2e2` |
| [Hero_Skin_Unlocks.tsv](data/Hero_Skin_Unlocks.tsv) | 113 | `Definitions/Heroes/*.herodef` (SkinProfileDataSettings); `Hero_<Hero>_Skins.LangEN.tsv`; `Common.LangEN.tsv`; hero entity named values | `6f13a8adaaff601683f1d7e0e13715fe390ed7011bfadb9b14bb827cc16fb17a` |
