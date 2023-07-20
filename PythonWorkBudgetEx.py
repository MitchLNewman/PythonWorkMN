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

print("Your food budget for this month is £" + str(food.budget))

spentF = int(
    input("Please enter the amount you have spent on food this week: £"))

food.withdraw(spentF)

print("Your remaining food budget for this month is £" + str(food.budget))


