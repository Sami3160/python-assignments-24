# Base class
class Bank:
    def __init__(self, name):
        self.name = name

    def display_info(self):
        print(f"Bank Name: {self.name}")

# Single Inheritance
class Branch(Bank):
    def __init__(self, name, branch_name):
        super().__init__(name)
        self.branch_name = branch_name

    def display_info(self):
        super().display_info()
        print(f"Branch Name: {self.branch_name}")

# Multiple Inheritance
class Customer:
    def __init__(self, customer_name):
        self.customer_name = customer_name

    def display_customer(self):
        print(f"Customer Name: {self.customer_name}")

class BankCustomer(Bank, Customer):
    def __init__(self, name, customer_name):
        Bank.__init__(self, name)
        Customer.__init__(self, customer_name)

    def display_info(self):
        Bank.display_info(self)
        Customer.display_customer(self)

# Multilevel Inheritance
class Account(Branch):
    def __init__(self, name, branch_name, account_number):
        super().__init__(name, branch_name)
        self.account_number = account_number

    def display_info(self):
        super().display_info()
        print(f"Account Number: {self.account_number}")

# Hierarchical Inheritance
class Loan(Bank):
    def __init__(self, name, loan_amount):
        super().__init__(name)
        self.loan_amount = loan_amount

    def display_info(self):
        super().display_info()
        print(f"Loan Amount: {self.loan_amount}")

# Hybrid Inheritance
class Employee:
    def __init__(self, employee_name):
        self.employee_name = employee_name

    def display_employee(self):
        print(f"Employee Name: {self.employee_name}")

class BankEmployee(Bank, Employee):
    def __init__(self, name, employee_name):
        Bank.__init__(self, name)
        Employee.__init__(self, employee_name)

    def display_info(self):
        Bank.display_info(self)
        Employee.display_employee(self)
bank = Bank("National Bank")
bank.display_info()

branch = Branch("National Bank", "Downtown Branch")
branch.display_info()

customer = BankCustomer("National Bank", "malhar boi")
customer.display_info()

account = Account("National Bank", "Downtown Branch", "123456789")
account.display_info()

loan = Loan("National Bank", 50000)
loan.display_info()

employee = BankEmployee("National Bank", "samiiiiiiii")
employee.display_info()