# Q1: Create a class called BankAccount that has four attributes: bankname, firstname,
# lastname, and balance.
# The default balance should be set to 0.
# In addition, create ...
# ● A method called deposit() that allows the user to make deposits into their balance.
# ● A method called withdrawal() that allows the user to withdraw from their balance.
# ● Withdrawal may not exceed the available balance. Hint: consider a conditional argument
# in your withdrawal() method.
# ● Use the __str__() method in order to display the bank name, owner name, and current
# balance.
# ● Make a series of deposits and withdrawals to test your class.

class BankAccount:
    def __init__(self, bankname, firstname, lastname, balance=0):
        self.bankname = bankname
        self.firstname = firstname
        self.lastname = lastname
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposit of {amount} made. New balance is {self.balance}.")
        else:
            print("Deposit amount must be positive.")

    def withdrawal(self, amount):
        if amount > self.balance:
            print(f"Unfortunately you don't have {amount} available. You can withdraw up to {self.balance}.")
        elif amount <= 0:
            print("Withdrawing no money or negative values is not possible or allowed")
        else:
            self.balance -= amount
            print(f"Success! You withdrew{amount}. You have {self.balance} left.")

    def __str__(self):
        return f"Bank: {self.bankname}\nOwner: {self.firstname} {self.lastname}\nCurrent Balance: {self.balance}"

# test class with fake account creation
account = BankAccount("Bank of Taiwan", "Ming Yen", "Wang")

# this is deposits going in
account.deposit(500)
account.deposit(200)

# The is money going out. This will throw an error since the total withdrawal amounts exceed what was deposted
account.withdrawal(100)
account.withdrawal(700)

# Display the account information
print(account)


# Q2: Create a class Box that has attributes length and width that takes values for length
# and width upon construction (instantiation via the constructor).
# In addition, create…
# ● A method called render() that prints out to the screen a box made with asterisks of
# length and width dimensions
# ● A method called invert() that switches length and width with each other
# ● Methods get_area() and get_perimeter() that return appropriate geometric calculations
# ● A method called double() that doubles the size of the box. Hint: Pay attention to return
# value here.
# ● Implement __eq__ so that two boxes can be compared using ==. Two boxes are equal if
# their respective lengths and widths are identical.
# ● A method print_dim() that prints to screen the length and width details of the box
# ● A method get_dim() that returns a tuple containing the length and width of the box
# ● A method combine() that takes another box as an argument and increases the length
# and width by the dimensions of the box passed in
# ● A method get_hypot() that finds the length of the diagonal that cuts through the middle
# ● Instantiate 3 boxes of dimensions 5,10 , 3,4 and 5,10 and assign to variables box1,
# box2 and box3 respectively
# ● Print dimension info for each using print_dim()
# ● Evaluate if box1 == box2, and also evaluate if box1 == box3, print True or False to the
# screen accordingly
# ● Combine box3 into box1 (i.e. box1.combine())
# ● Double the size of box2
# ● Combine box2 into box1

import math

class Box:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def render(self):
        for _ in range(self.length):
            print('*' * self.width)

    def invert(self):
        self.length, self.width = self.width, self.length

    def get_area(self):
        return self.length * self.width

    def get_perimeter(self):
        return 2 * (self.length + self.width)

    def double(self):
        self.length *= 2
        self.width *= 2

    def __eq__(self, other):
        return self.length == other.length and self.width == other.width

    def print_dim(self):
        print(f"Length: {self.length}, Width: {self.width}")

    def get_dim(self):
        return (self.length, self.width)

    def combine(self, other):
        self.length += other.length
        self.width += other.width

    def get_hypot(self):
        return math.sqrt(self.length**2 + self.width**2)

# 3 boxes required to be made
box1 = Box(5, 10)
box2 = Box(3, 4)
box3 = Box(5, 10)

# use dim() to get the dimensions
print("Dimensions of Box 1:")
box1.print_dim()

print("Dimensions of Box 2:")
box2.print_dim()

print("Dimensions of Box 3:")
box3.print_dim()

# check thatbox1 == box2 and box1 == box3
print(f"box1 == box2: {box1 == box2}")
print(f"box1 == box3: {box1 == box3}")

# merge box1 and box3
box1.combine(box3)
print("Box 1 after combining with Box 3:")
box1.print_dim()

# double box2
box2.double()
print("Box 2 after doubling:")
box2.print_dim()

# merge box1 and 2
box1.combine(box2)
print("Box 1 after combining with doubled Box 2:")
box1.print_dim()



