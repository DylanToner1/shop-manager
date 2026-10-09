CREATE TABLE items (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    price DECIMAL(10, 2) NOT NULL, -- store as fixed point to avoid floating point errors
    stock_count INT NOT NULL DEFAULT 0
);