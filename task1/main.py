from datetime import datetime

class transaction:
    @staticmethod
    def get_current_date():
        return datetime.now().date()

class expense(transaction):
    def __init__(self, account, expense_type, amount, time):
        self.__account = account
        self.expense_type = expense_type
        self.amount = amount
        self.time = time

class deposit(transaction):
    def __init__(self, account, transferor, transfer_method, currency):
        self.__account = account
        self.__transferor = transferor
        self.transfer_method = transfer_method
        self.currency = currency

if __name__ == '__main__':
    e = expense('acc', 'food', '$100', 'today')
    d = deposit('acc', 'me', 'wire', 'HKD')
    print(e.get_current_date())
