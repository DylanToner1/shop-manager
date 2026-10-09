CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    item_id INT NOT NULL,
    customer_id INT NOT NULL,
    placed_on TIMESTAMP NOT NULL,

    CONSTRAINT fk_item foreign key(item_id) REFERENCES items(id) ON DELETE CASCADE,
    CONSTRAINT fk_customer foreign key(customer_id) REFERENCES customers(id) ON DELETE CASCADE
);