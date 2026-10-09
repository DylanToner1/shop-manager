As a shop manager
So I can know which items I have in stock
I want to keep a list of my shop items with their name and unit price.

As a shop manager
So I can know which items I have in stock
I want to know which quantity (a number) I have for each item.

As a shop manager
So I can manage items
I want to be able to create a new item.

As a shop manager
So I can know which orders were made
I want to keep a list of orders with their customer name.

As a shop manager
So I can know which orders were made
I want to assign each order to their corresponding item.

As a shop manager
So I can know which orders were made
I want to know on which date an order was placed. 

As a shop manager
So I can manage orders
I want to be able to create a new order.


```sql

CREATE TABLE items (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    price DECIMAL(10, 2) NOT NULL, -- store as fixed point to avoid floating point errors
    stock_count INT NOT NULL DEFAULT 0
)

CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    item_id INT NOT NULL,
    customer_id INT NOT NULL,
    placed_on TIMESTAMP NOT NULL,

    CONSTRAINT fk_item foreign key(item_id) REFERENCES items(id) ON DELETE CASCADE,
    CONSTRAINT fk_customer foreign key(customer_id) REFERENCES customers(id) ON DELETE CASCADE
)

CREATE TABLE customers (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE -- everyone has their own email, no 2 people should have the same
)

```