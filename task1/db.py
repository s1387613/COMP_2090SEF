from pathlib import Path
import sqlite3

class DBHelper:
    def __init__(self, db_name='log.db', db_schema='schema.sql'):
        self.query = {
            'add_catagory'   : 'INSERT INTO catagories (name) VALUES (?)',
            'add_method'     : 'INSERT INTO methods (name) VALUES (?)',
            'get_catagory_id': 'SELECT id FROM catagories WHERE (name) = (?)',
            'get_method_id'  : 'SELECT id FROM methods WHERE (name) = (?)',
            'add_transaction': 'INSERT INTO transactions (amount, catagory_id, method_id, description) VALUES (?, ?, ?, ?)',
            'get_balance'    : 'SELECT SUM(amount) FROM transactions'
        }
        self.db_name = db_name
        self.db_schema = db_schema
        self.connection = None

    def __enter__(self):
        if not Path(self.db_name).exists():
            self.connection = sqlite3.connect(self.db_name)
            cursor = self.connection.cursor()
            with open(self.db_schema, 'r') as f:
                cursor.executescript(f.read())
                f.close()
        else:
            self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.connection:
            self.connection.commit()
            self.connection.close()

    def __get_catagory_and_method_id(self, catagory_name, transaction_method):
        self.cursor.execute(self.query['add_catagory'], (catagory_name,))
        catagory_id = self.cursor.execute(self.query['get_catagory_id'], (catagory_name,)).fetchone()[0]
        self.cursor.execute(self.query['add_method'], (transaction_method,))
        method_id = self.cursor.execute(self.query['get_method_id'], (transaction_method,)).fetchone()[0]
        return catagory_id, method_id

    def add_transaction(self, amount, catagory_name, transaction_method, description=''):
        catagory_id, method_id = self.__get_catagory_and_method_id(catagory_name, transaction_method)
        self.cursor.execute(self.query['add_transaction'], (amount, catagory_id, method_id, description))
        self.connection.commit()

    def get_balance(self):
        self.cursor.execute(self.query['get_balance'])
        return self.cursor.fetchone()[0] or 0.0

if __name__ == '__main__':
    with DBHelper() as db:
        db.add_transaction(-45.0, 'food', 'cash', description='test1')
        db.add_transaction(-12.0, 'transport', 'alipay', description='test2')
        # datetime.strptime(text, '%Y-%m-%d %H:%M:%S')
        print(db.cursor.execute('SELECT date FROM transactions').fetchone()[0])
        print(f'Current balance: {db.get_balance():2f}')
