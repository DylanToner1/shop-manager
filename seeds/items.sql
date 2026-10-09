TRUNCATE TABLE items CASCADE;
ALTER SEQUENCE items_id_seq RESTART WITH 1;

INSERT INTO items (name, price, stock_count) VALUES ('item1', 3.99, 0);
INSERT INTO items (name, price, stock_count) VALUES ('item2', 6.99, 6);
INSERT INTO items (name, price, stock_count) VALUES ('item3', 1.99, 124);
INSERT INTO items (name, price, stock_count) VALUES ('item4', 36.99, 32);
INSERT INTO items (name, price, stock_count) VALUES ('item5', 4.99, 640);
INSERT INTO items (name, price, stock_count) VALUES ('item6', 8.99, 4);