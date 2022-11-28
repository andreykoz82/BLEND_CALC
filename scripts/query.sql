-- data table
CREATE TABLE IF NOT EXISTS data (
	id integer PRIMARY KEY,
	date timestamp NOT NULL,
	order_num text,
	item text,
    item_type text,
    lot_num text,
    quantity float,
    indicator text,
    indicator_quantity float
);

-- data table
CREATE TABLE IF NOT EXISTS results (
	id integer PRIMARY KEY,
	date DATETIME DEFAULT CURRENT_TIMESTAMP,
	order_num text,
    results float
);

DROP TABLE results;
DELETE from data;

SELECT * FROM results;
SELECT * FROM data;