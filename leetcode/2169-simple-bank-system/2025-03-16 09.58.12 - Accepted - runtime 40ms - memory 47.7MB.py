class Bank:

    def __init__(self, balance: List[int]):
        self.balance = balance

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        n = len(self.balance)
        if account1<1 or account1>n or account2<1 or account2>n:
            return False
        if self.balance[account1-1]<money:
            return False
        self.balance[account2-1]+=money
        self.balance[account1-1]-=money
        return True

    def deposit(self, account: int, money: int) -> bool:
        n = len(self.balance)
        if account<1 or account>n:
            return False
        self.balance[account-1]+=money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        n = len(self.balance)
        if account<1 or account>n:
            return False
        if self.balance[account-1]<money:
            return False
        self.balance[account-1]-=money
        return True


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)