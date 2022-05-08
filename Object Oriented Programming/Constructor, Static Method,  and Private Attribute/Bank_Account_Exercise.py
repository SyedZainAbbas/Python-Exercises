"""
Create a BankAccount class, it should:
  1. Have a maximum_loan class variable. Decide if it’s gonna be public or private.
  2. Store the name of the client and account number upon instantiation.
  
Create a method that grants a loan, it should:  
  1. Add money in the client's account
  2. Record the number of days until the client has to pay back

Create a get_customer_service_address method that: 
  1. Returns an email address.
  2. This email address should be the same for all instances. Decide where and how you will store this email address.
  
Add logic to the class so that:
  1. Requesting a loan above the maximum allowed amount raises a ValueError.
  2. Requesting a loan to be paid in less than 30 days raises an ArithmeticError (it does not fit properly, just for the sake of exercise)
 
Important assumptions:
  1. The maximum amount for a loan should not exceed 1,000,000.
  2. The least amount of days to pay back a loan should be 30.
  
"""

class BankAccount:
    maximum_loan = 1_000_000
    _email_address = 'abc@def.com'
    _client_record = {}

    def __init__(self, account_number, client_name):
        self.account_number = account_number
        self.balance = 0
        self.client_name = client_name
        BankAccount._client_record[account_number] = {
            'Name': client_name, 'Account Number': account_number, 'Loan Amount': 0, 'Days to Pay Back': 0,
            'Balance': self.balance
        }

    def grant_loan(self, amount: int, days_to_pay: int) -> None:
        self.raise_value_error(amount)
        self.raise_arith_error(days_to_pay)
        self.days_to_pay_loan = days_to_pay
        BankAccount._client_record[self.account_number]['loan'] = amount
        BankAccount._client_record[self.account_number]['days'] = days_to_pay
        self.balance += amount
        BankAccount._client_record[self.account_number]['balance'] = self.balance

    @staticmethod
    def raise_value_error(amount: int) -> None:
        if amount > 1_000_000:
            raise ValueError

    @staticmethod
    def raise_arith_error(days: int) -> None:
        if days < 30:
            raise ArithmeticError

    @staticmethod
    def get_customer_service_address() -> str:
        return BankAccount._email_address
