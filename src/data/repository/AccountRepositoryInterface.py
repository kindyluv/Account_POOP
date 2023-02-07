from abc import ABC, abstractmethod


class AccountRepositoryInterface(ABC):
    @abstractmethod
    def create_new_account(self, first_name, last_name, mobile_number, age, gender, realship, lga, state, email):
        pass

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount, pin):
        pass

    @abstractmethod
    def transfer(self, amount, account_name, account_number, bank_name, pin):
        pass

    @abstractmethod
    def check_balance(self, account_number, pin):
        pass
