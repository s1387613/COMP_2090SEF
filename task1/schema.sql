DROP TABLE IF EXISTS methods;
DROP TABLE IF EXISTS catagories;
DROP TABLE IF EXISTS transactions;

CREATE TABLE methods (
    id INTEGER PRIMARY KEY,
    name TEXT CHECK(name IN ('wire', 'cash', 'alipay', 'apple_pay', 'credit_card', 'others'))
);

CREATE TABLE catagories (
    id INTEGER PRIMARY KEY,
    name TEXT CHECK(name IN ('food', 'transport', 'rent', 'bills', 'tax', 'investment', 'others', 'non_expense'))
);

CREATE TABLE transactions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    amount REAL NOT NULL,
    date TEXT DEFAULT CURRENT_TIMESTAMP,
    catagory_id INTEGER REFERENCES catagories(id),
    method_id INTEGER REFERENCES methods(id),
    description TEXT
);
