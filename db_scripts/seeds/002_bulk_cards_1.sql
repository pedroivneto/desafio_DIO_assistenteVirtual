INSERT INTO tbl_cards (hp, name, info, attack, damage, weak, resist, retreat,
cardNumberInCollection, collection_id, type_id, stage_id)
VALUES 
-- 1 Pikachu
(40, 'Pikachu', 'Mouse Pokémon', 'Thunder Jolt', '30', 'Fighting', 'Steel', '1',
58, 1, 4, 1),
-- 2 Charizard
(120, 'Charizard', 'Flame Pokémon', 'Fire Spin', '100', 'Water', 'None', '3',
4, 1, 2, 3),
-- 3 Blastoise
(100, 'Blastoise', 'Shellfish Pokémon', 'Hydro Pump', '40+', 'Electric', 'None', '3',
2, 1, 3, 3),
-- 4 Bulbasaur
(40, 'Bulbasaur', 'Seed Pokémon', 'Leech Seed', '20', 'Fire', 'Water', '1',
44, 1, 1, 1),
-- 5 Ivysaur
(60, 'Ivysaur', 'Seed Pokémon', 'Vine Whip', '30', 'Fire', 'Water', '2',
30, 1, 1, 2),
-- 6 Venusaur
(100, 'Venusaur', 'Seed Pokémon', 'Solarbeam', '60', 'Fire', 'Water', '2',
15, 1, 1, 3),
-- 7 Charmander
(50, 'Charmander', 'Lizard Pokémon', 'Ember', '30', 'Water', 'None', '1',
46, 1, 2, 1),
-- 8 Charmeleon
(80, 'Charmeleon', 'Flame Pokémon', 'Flamethrower', '50', 'Water', 'None', '2',
24, 1, 2, 2),
-- 9 Squirtle
(40, 'Squirtle', 'Tiny Turtle Pokémon', 'Bubble', '20', 'Electric', 'None', '1',
63, 1, 3, 1),
-- 10 Wartortle
(70, 'Wartortle', 'Turtle Pokémon', 'Withdraw', '30', 'Electric', 'None', '1',
42, 1, 3, 2),
-- 11 Caterpie
(40, 'Caterpie', 'Worm Pokémon', 'String Shot', '10', 'Fire', 'None', '1',
45, 1, 1, 1),
-- 12 Metapod
(60, 'Metapod', 'Cocoon Pokémon', 'Stiffen', '—', 'Fire', 'None', '2',
54, 1, 1, 2),
-- 13 Butterfree
(70, 'Butterfree', 'Butterfly Pokémon', 'Whirlwind', '20', 'Fire', 'Fighting', '1',
33, 1, 1, 3),
-- 14 Gastly
(30, 'Gastly', 'Gas Pokémon', 'Lick', '10', 'Psychic', 'None', '1',
50, 1, 5, 1),
-- 15 Haunter
(60, 'Haunter', 'Gas Pokémon', 'Hypnosis', '—', 'Psychic', 'None', '1',
29, 1, 5, 2),
-- 16 Gengar
(80, 'Gengar', 'Shadow Pokémon', 'Nightmare', '20', 'Psychic', 'None', '1',
5, 1, 5, 3),
-- 17 Machop
(50, 'Machop', 'Superpower Pokémon', 'Low Kick', '20', 'Psychic', 'None', '1',
66, 1, 6, 1),
-- 18 Machoke
(80, 'Machoke', 'Superpower Pokémon', 'Karate Chop', '50', 'Psychic', 'None', '2',
34, 1, 6, 2),
-- 19 Machamp
(100, 'Machamp', 'Superpower Pokémon', 'Seismic Toss', '60', 'Psychic', 'None', '3',
8, 1, 6, 3),
-- 20 Mewtwo
(130, 'Mewtwo', 'Genetic Pokémon', 'Psychic', '40+', 'Psychic', 'None', '3',
10, 1, 5, 1);