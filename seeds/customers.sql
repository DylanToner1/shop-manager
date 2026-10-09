TRUNCATE TABLE customers CASCADE;
ALTER SEQUENCE customers_id_seq RESTART WITH 1;

INSERT INTO customers (name, email) VALUES ('customer1', 'customer1@example.com');
INSERT INTO customers (name, email) VALUES ('customer2', 'customer2@example.com');
INSERT INTO customers (name, email) VALUES ('customer3', 'customer3@example.com');