CREATE TABLE tbl_collections (
    id INT AUTO_INCREMENT PRIMARY KEY,
    collectionSetName VARCHAR(100) NOT NULL,
    release_date DATE NOT NULL,
    totalCardsInCollection SMALLINT UNSIGNED NOT NULL
);

CREATE TABLE tbl_types (
    id INT AUTO_INCREMENT PRIMARY KEY,
    typeName VARCHAR(30) NOT NULL
);

CREATE TABLE tbl_stages (
    id INT AUTO_INCREMENT PRIMARY KEY,
    stageName VARCHAR(20) NOT NULL
);

CREATE TABLE tbl_cards (
    id INT AUTO_INCREMENT PRIMARY KEY,
    hp SMALLINT UNSIGNED,
    name VARCHAR(80) NOT NULL,
    info VARCHAR(255),
    attack VARCHAR(100),
    damage VARCHAR(10),
    weak VARCHAR(30),
    resist VARCHAR(30),
    retreat VARCHAR(30),
    cardNumberInCollection SMALLINT UNSIGNED NOT NULL,
    collection_id INT NOT NULL,
    type_id INT NOT NULL,
    stage_id INT NOT NULL,
    FOREIGN KEY (collection_id) REFERENCES tbl_collections(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY (type_id) REFERENCES tbl_types(id)
        ON DELETE RESTRICT
        ON UPDATE CASCADE,
    FOREIGN KEY (stage_id) REFERENCES tbl_stages(id)
        ON DELETE RESTRICT
        ON UPDATE CASCADE
);
