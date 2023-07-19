# Exercise 1 - Static Analysis 

# Answers 
# - less than sign used on final if statement - needs to be greater than 
# - apostrophe causing issues in final print statement - double quotes will fix this or a \ next to apostrophe
# - there is no numerical item price so nothing to compare the user funds to for the if statements,
# the word burger needs to be changed to an integer or float value 

user_funds = 10.31
item_price = 5.99

if item_price < user_funds:
    print("You have enough money!")
if item_price == user_funds:
    print("You have the precise amount of money")
if item_price > user_funds:
    print('Sorry you don\'t have enough money')

#Exercise 2 - Static analysis

# Answers
# - "for n" needs to be changed to "for i"

def product(n):
    total = 1
    for i in n:
        total *= i
    return total

print(product([4,4,5]))

# Exercise 3 - Dynamic Analysis

# Answers 
# - minus 1 has to be removed from for loop line 
# - elif line must be added within if statement with the elif statement returning true
# - final line "return true" needs to be pulled to outside of if statement

def is_prime(x):
    if x < 2:
        return False
    elif x == 2:
        return True
    else:
        for n in range(2, x):
            if x % n == 0:
                return False
    return True

# Exercise 4 dynamic analysis 

# Answers 
# - print statement needed to be changed 
# - "n+=1" needed to be added to stop infinite while loop 
# - print item list index reduced to 4 from 5 as the list begins from 0 not 1

item_list = ["Burger", "Hotdog", "Bun", "Ketchup", "Cheese"]
n = 0

while n < 5:
    for i in item_list:
        print(i)
    n+=1 

print(item_list[4])


