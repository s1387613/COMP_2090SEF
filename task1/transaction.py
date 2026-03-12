from abc import ABC, abstractmethod
from datetime import datetime
from enum import StrEnum, unique, auto

class UserAccount:
    def __init__(self, username, user_id):
        self.__username = username
        self.__user_id = user_id

    def get_username(self):
        return self.__username

    def get_user_id(self):
        return self.__user_id

@unique
class TransactionType(StrEnum):
    EXPENSE = auto()
    DEPOSIT = auto()

@unique
class ExpenseType(StrEnum):
    # auto() is not used to ensure proper
    # interaction with sqlite
    FOOD = 'food'
    TRANSPORT = 'transport'
    RENT = 'rent'
    BILLS = 'bills'
    INVESTMENT = 'investment'
    OTHERS = 'others'

@unique
class TransactionMethod(StrEnum):
    WIRE = auto()
    CASH = auto()
    ALIPAY = auto()
    APPLE_PAY = auto()
    CREDIT_CARD = auto()
    OTHERS = auto()

@unique
class CurrencyType(StrEnum):
    HKD = auto()
    USD = auto()

class Transaction(ABC):
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

class Expense(Transaction):
    def __init__(self,
                 account: UserAccount,
                 transaction_method: TransactionMethod,
                 amount: float,
                 currency: CurrencyType,
                 expense_type: ExpenseType):

        self.time = super().get_current_date()
        self.__account = account
        self.transaction_method = transaction_method
        self.amount = amount
        self.currency = currency
        self.expense_type = expense_type

    def print_current_log(self):
        print(f'[{self.time}] | {self.__account.get_username()}: -{self.amount}{self.currency} | ({self.expense_type}, {self.transaction_method})')
        return

class Deposit(Transaction):
    def __init__(self,
                 account: UserAccount,
                 transaction_method: TransactionMethod,
                 amount: float,
                 currency: CurrencyType,
                 transferor: UserAccount):

        self.time = super().get_current_date()
        self.__account = account
        self.transaction_method = transaction_method
        self.amount = amount
        self.currency = currency
        self.__transferor = transferor

    def print_current_log(self):
        print(f'[{self.time}] | {self.__account.get_username()} -> {self.__transferor.get_username()}: {self.amount}{self.currency} | ({self.transaction_method})')
        return

if __name__ == '__main__':
    user1 = UserAccount('Alice', 1)
    user2 = UserAccount('Bob', 2)

    e = Expense(user1, TransactionMethod.APPLE_PAY, 100, CurrencyType.HKD, ExpenseType.FOOD)
    e.print_current_log()

    d = Deposit(user1, TransactionMethod.CASH, 1000, CurrencyType.USD, user2)
    d.print_current_log()
