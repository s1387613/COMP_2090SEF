from abc import ABC, abstractmethod
from datetime import datetime
from enum import Enum
# import json

class user_account:
    def __init__(self, username, user_id):
        self.__username = username
        self.__user_id = user_id

    def get_username(self):
        return self.__username

    def get_user_id(self):
        return self.__user_id

class transaction(ABC):
    @staticmethod
    def get_current_date():
        return datetime.now().date()

    @staticmethod
    def write_transaction_history(history_type,
                                  time,
                                  account,
                                  transaction_method,
                                  amount,
                                  currency,
                                  expense_type,
                                  transferor):

        # TODO: write the transaction history to a json file
        if history_type == self.transaction_type.EXPENSE:
            pass
        elif history_type == self.transaction_type.DEPOSIT:
            pass
        else:
            print('incorrect transaction type')
            return

    @abstractmethod
    def print_current_log():
        pass

    class transaction_type(Enum):
        EXPENSE = 1
        DEPOSIT = 2

    class expense_type(Enum):
        FOOD = 1
        TRANSPORT = 2
        RENT = 3
        BILLS = 4
        INVESTMENT = 5
        OTHERS = 6

    class transaction_method(Enum):
        WIRE = 1
        CASH = 2
        ALIPAY = 3
        APPLE_PAY = 4
        CREDIT_CARD = 5
        OTHERS = 6

    class currency(Enum):
        HKD = 1
        USD = 2

class expense(transaction):
    def __init__(self,
                 account: user_account,
                 transaction_method: transaction.transaction_method,
                 amount: float,
                 currency: transaction.currency,
                 expense_type: transaction.expense_type):

        self.time = super().get_current_date()
        self.__account = account
        self.transaction_method = transaction_method
        self.amount = amount
        self.currency = currency
        self.expense_type = expense_type

    def print_current_log(self):
        print(f'[{self.time}] | {self.__account.get_username()}: -{self.amount}{self.currency.name} | ({self.expense_type.name}, {self.transaction_method.name})')
        return

class deposit(transaction):
    def __init__(self,
                 account: user_account,
                 transaction_method: transaction.transaction_method,
                 amount: float,
                 currency: transaction.currency,
                 transferor: user_account):

        self.time = super().get_current_date()
        self.__account = account
        self.transaction_method = transaction_method
        self.amount = amount
        self.currency = currency
        self.__transferor = transferor

    def print_current_log(self):
        print(f'[{self.time}] | {self.__account.get_username()} -> {self.__transferor.get_username()}: {self.amount}{self.currency.name} | ({self.transaction_method.name})')
        return

if __name__ == '__main__':
    user1 = user_account('Alice', 1)
    user2 = user_account('Bob', 2)

    e = expense(user1,
                transaction.transaction_method.APPLE_PAY,
                100,
                transaction.currency.HKD,
                transaction.expense_type.FOOD)
    e.print_current_log()

    d = deposit(user1,
                transaction.transaction_method.CASH,
                1000,
                transaction.currency.USD,
                user2)
    d.print_current_log()
