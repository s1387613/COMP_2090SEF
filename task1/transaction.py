from abc import ABC, abstractmethod
from datetime import datetime
from enum import StrEnum, unique, auto
from db import DBHelper

@unique
class ExpenseType(StrEnum):
    # auto() is not used to ensure proper
    # interaction with sqlite
    FOOD        = 'food'
    TRANSPORT   = 'transport'
    RENT        = 'rent'
    BILLS       = 'bills'
    INVESTMENT  = 'investment'
    OTHERS      = 'others'
    NON_EXPENSE = 'non_expense'

@unique
class TransactionMethod(StrEnum):
    WIRE        = 'wire'
    CASH        = 'cash'
    ALIPAY      = 'alipay'
    APPLE_PAY   = 'apple_pay'
    CREDIT_CARD = 'credit_card'
    OTHERS      = 'others'

class Transaction(ABC):
    @staticmethod
    def get_current_date():
        return datetime.now().date()

    def write_transaction_history(self):
        with DBHelper() as db:
            db.add_transaction(self.amount, self.expense_type, self.transaction_method, description=self.description)

class Expense(Transaction):
    def __init__(self,
                 transaction_method: TransactionMethod,
                 amount: float,
                 expense_type: ExpenseType,
                 description=''):

        if amount > 0:
            raise ValueError('transaction.py: expense amount should be negative value')

        self.time = super().get_current_date()
        self.transaction_method = transaction_method
        self.amount = amount
        self.expense_type = expense_type
        self.description = description

class Deposit(Transaction):
    def __init__(self,
                 transaction_method: TransactionMethod,
                 amount: float,
                 description=''):

        if amount < 0:
            raise ValueError('transaction.py: deposit amount should be positive value')

        self.time = super().get_current_date()
        self.transaction_method = transaction_method
        self.amount = amount
        self.expense_type = ExpenseType.NON_EXPENSE
        self.description = description

if __name__ == '__main__':
    Expense(TransactionMethod.APPLE_PAY, -100, ExpenseType.FOOD).write_transaction_history()
    Deposit(TransactionMethod.CASH, 1000).write_transaction_history()

    try:
        Expense(TransactionMethod.CASH, 100, ExpenseType.FOOD)
    except ValueError:
        print('Error caught')

    with DBHelper() as db:
        exp_type = db.cursor.execute(db.query['get_catagory_id'], ('food',)).fetchone()[0]
        print(db.cursor.execute('SELECT * FROM transactions WHERE (catagory_id) = (?)', (exp_type,)).fetchall())
