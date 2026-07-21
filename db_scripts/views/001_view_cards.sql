CREATE VIEW vw_cards_detalhados AS
SELECT 
    c.id,
    c.hp,
    c.name,
    c.info,
    c.attack,
    c.damage,
    c.weak,
    c.resist,
    c.retreat,
    c.cardNumberInCollection,
    col.collectionSetName AS collection_name,
    col.release_date AS collection_release_date,
    col.totalCardsInCollection AS total_cards_in_collection,
    t.typeName AS type_name,
    s.stageName AS stage_name
FROM tbl_cards c
INNER JOIN tbl_collections col ON c.collection_id = col.id
INNER JOIN tbl_types t ON c.type_id = t.id
INNER JOIN tbl_stages s ON c.stage_id = s.id;
