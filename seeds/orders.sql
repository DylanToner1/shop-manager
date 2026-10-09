TRUNCATE TABLE orders CASCADE;
ALTER SEQUENCE orders_id_seq RESTART WITH 1;

INSERT INTO orders (item_id, customer_id, placed_on) VALUES (1, 1, '2026-10-09 15:30:00Z');
INSERT INTO orders (item_id, customer_id, placed_on) VALUES (5, 2, '2026-10-09 15:35:00Z');
INSERT INTO orders (item_id, customer_id, placed_on) VALUES (3, 3, '2026-10-09 15:40:00Z');