PRAGMA foreign_keys = ON;

CREATE TABLE categories (
    category_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL UNIQUE
);

CREATE TABLE payment_methods (
    payment_method_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL UNIQUE
);

CREATE TABLE expenses (
    expense_id INTEGER PRIMARY KEY,
    expense_date TEXT NOT NULL,
    category_id INTEGER NOT NULL,
    description TEXT NOT NULL CHECK (TRIM(description) <> ''),
    amount REAL NOT NULL CHECK (amount > 0),
    payment_method_id INTEGER NOT NULL,

    FOREIGN KEY (category_id) REFERENCES categories(category_id),
    FOREIGN KEY (payment_method_id) REFERENCES payment_methods(payment_method_id)
);

INSERT OR IGNORE INTO categories (name) VALUES
    ('Food'),
    ('Entertainment'),
    ('Groceries'),
    ('Transportation'),
    ('Other');

INSERT OR IGNORE INTO payment_methods (name) VALUES
    ('Credit Card'),
    ('Debit Card'),
    ('Cash'),
    ('Other');

CREATE INDEX IF NOT EXISTS idx_expenses_date
    ON expenses(expense_date);

CREATE INDEX IF NOT EXISTS idx_expenses_category
    ON expenses(category_id);

CREATE INDEX IF NOT EXISTS idx_expenses_payment_method
    ON expenses(payment_method_id);

CREATE INDEX IF NOT EXISTS idx_expenses_amount
    ON expenses(amount);