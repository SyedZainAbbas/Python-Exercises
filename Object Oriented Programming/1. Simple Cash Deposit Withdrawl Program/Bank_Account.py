class BalanceError(Exception):
    pass

class BankAccount:
    def __init__(self, name):
        self.name = name
        self.balance = 0

    def deposit(self,value):
        if not value.isdigit():
            raise ValueError('Invalid entry! Please enter a positive integer.')
        value = int(value)
        self.balance += value
        return self.balance

    def withdrawl(self,value):
        if not value.isdigit():
            raise ValueError('Invalid entry! Please enter a positive integer')
        value = int(value)
        self.balance -= value
        if self.balance >=0:
            return self.balance
        else:
            self.balance+=value
            raise BalanceError(f'Your account balance({self.balance}) is insufficinet')

    def __str__(self):
        return f"{self.name}'s account balance is {self.balance}"

if __name__=='__main__':
        Jack_Waters = BankAccount('Jack Waters')
        print('This account belongs to Mr. Jack Waters')
        mode = ''
        while mode not in ['B','D','W']:
            mode = input('This is a bank account app.\nPress D for cash deposit and W for cash withdrawl.\n'
              'Press B for checking the balance.\n\n').upper()
        if mode == 'B':
            print(Jack_Waters)
        elif mode == 'D':
            while True:
                try:
                    value = input('How much money would you like to deposit: ')
                    Jack_Waters.deposit(value)
                    print(Jack_Waters)
                    break
                except ValueError as e:
                    print(e)
        else:
            while True:
                try:
                    value = input('How much money would you like to withdraw: ')
                    Jack_Waters.withdrawl(value)
                    print(Jack_Waters)
                except ValueError as e:
                    print(e)
                except BalanceError as b:
                    print(b)

        # CHECK IF JACK WATERS IS AN INSTANCE OR NOT
        print(isinstance(Jack_Waters,BankAccount))
