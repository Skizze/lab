class Account:
    def __init__(self, name:str) -> None:
        """
        Create an account object
        :param name: account name
        """
        self.__account_name = name
        self.__account_balance = 0.0

    def deposit(self, amount:float) -> bool:
        """
        Attempt to add funds to account
        :param amount: amount to add
        :return: bool of if process succeeded
        """
        if amount <= 0.0:
            return False
        self.__account_balance += amount
        return True

    def withdraw(self, amount:float) -> bool:
        """
        Attempt to subtract funds from account
        :param amount: amount to subtract
        :return: bool of if process succeeded
        """
        if amount <= 0.0:
            return False
        elif amount > self.__account_balance:
            return False
        self.__account_balance -= amount
        return True

    def get_balance(self) -> float:
        """
        Getter for current balance
        :return: account balance
        """
        return self.__account_balance

    def get_name(self) -> str:
        """
        Getter for account name
        :return: account name
        """
        return self.__account_name
