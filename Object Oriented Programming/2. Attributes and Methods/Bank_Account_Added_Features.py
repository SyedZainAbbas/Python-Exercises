"""
Store the current value of the BankAccount in an attribute named balance (that should start with 0)
Add a deposit method that receives a value and adds it to balance and prints balance
Add a withdraw method that receives a value and subtracts it from balance and prints balance
Add a movements attribute to your class that should be an empty list to start.
Every time deposit or withdraw methods are called, this movement should be added to movements (eg: deposit(50) should append “DEPOSIT 50” to movements)
Add a method print_movements to print all the movements
When the balance is negative (when withdraw method is called), a warning should be printed to the user. Create a display_warning method in your class to do it.
Add a minimum_balance attribute to your instance (should be 0 by default), and a method to update this value (set_minimum_balance)
Change the warning check to be shown when balance <= minimum_balance

"""

class BankAccount:
    _movements = []

    def __init__(self):
        self.balance = 0
        self.minimum_balance = 0

    def deposit(self, value):
        self.balance += value
        BankAccount._movements.append(f'Deposit {value}')
        print(f'Your current account balance is {self.balance}')

    def withdraw(self, value):
        if (self.balance - value) > self.minimum_balance:
            self.balance -= value
            BankAccount._movements.append(f'Withdraw {value}')
        else:
            self.display_warning(self.balance, self.minimum_balance)
        print(f'Your current account balance is {self.balance}')

    def print_movements(self):
        print(self._movements)

    @staticmethod
    def display_warning(a, b):
        print('Invalid entry! The inserted value is higher than the minimum balance.'
              f'\nYou can only withdraw an amount lower than {a - b}.')

    def set_minimum_balance(self, value):
        self.minimum_balance = value


if __name__ == ' __main__':
    sample_acc = BankAccount()
    sample_acc.deposit(500)
    sample_acc.print_movements()
    sample_acc.withdraw(320)
    sample_acc.print_movements()
    sample_acc.set_minimum_balance(120)
    sample_acc.withdraw(70)
    sample_acc.print_movements()
