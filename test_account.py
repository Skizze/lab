import pytest
from account import *

class Test:
    def setup_method(self):
        self.a1 = Account('John')

    def teardown_method(self):
        del self.a1

    def test_init(self):
        assert self.a1.get_name() == 'John'
        assert self.a1.get_balance() == 0.0

    def test_deposit(self):
        assert self.a1.deposit(-1.5) is False
        assert self.a1.get_balance() == 0.0

        assert self.a1.deposit(0) is False
        assert self.a1.get_balance() == 0.0

        assert self.a1.deposit(15.5) is True
        assert self.a1.get_balance() == 15.5

    def test_withdraw(self):
        self.a1.deposit(15.5)
        assert self.a1.withdraw(-15.5) is False
        assert self.a1.get_balance() == 15.5

        assert self.a1.withdraw(0) is False
        assert self.a1.get_balance() == 15.5

        assert self.a1.withdraw(21.47) is False
        assert self.a1.get_balance() == 15.5

        assert self.a1.withdraw(12) is True
        assert self.a1.get_balance() == 3.5
