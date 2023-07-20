class Budget:
    def __init__(self, budget, category):
        self.budget = budget
        self.category = category

    def deposit(self, amount):
        self.budget += amount

    def withdraw(self, amount):
        if (self.budget - amount) < 0:
            print("You're Broke! Transfer some money from another account.")
        else:
            self.budget -= amount

    def transfer(self, amount, obj):
        if (self.budget - amount) < 0:
            print("You're Broke! Transfer some money from another account.")
        else:
            obj.deposit(amount)
            self.withdraw(amount)

food = Budget(200, "Food")
clothing = Budget(150, "Clothing")
entertainment = Budget(100, "Entertainment")

# Food Budget inputs
print("Your food budget for this month is £" + str(food.budget))

spentF = int(
    input("Please enter food expenditure for the week: £"))

food.withdraw(spentF)

print("Your remaining food budget for this month is £" + str(food.budget))

# Clothing budget inputs

print("Your clothing budget for this month is £" + str(clothing.budget))

spentC = int(
    input("Please enter clothing expenditure for the week: £"))

clothing.withdraw(spentC)

print("Your remaining food budget for this month is £" + str(clothing.budget))

# Entainment budget Inputs 

print("Your entertainment budget for this month is £" + str(entertainment.budget))

spentE = int(
    input("Please enter entertainment expenditure for the week: £"))

entertainment.withdraw(spentE)

print("Your remaining entertainment budget for this month is £" + str(entertainment.budget))
