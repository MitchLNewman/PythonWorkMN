# Exercise 1 program to find numbers between 1500 and 2700 that are divisible by 5 and 7 

numbers =[]

for x in range(1500, 2701):
    if (x % 7 == 0) and (x % 5 == 0):
        numbers.append(str(x))
print(",".join(numbers))

# Exercise 2 convert temperatures to and from celcius and fahrenheit

temp = input("Input the temperature that you would like to convert: ")
degrees = int(temp[:-1])
i_convention = temp[-1]


if i_convention.upper() == "C":
    result = int(round((9 * degrees) / 5 + 32))
    o_convention = "Fahrenheit"
elif i_convention.upper() == "F":
    result = int(round((degrees - 32) * 5 / 9))
    o_convention = "Celcius"
else:
    print("Input temp in right format.")
    quit()
print("The temperature in", o_convention, "is", result, "degrees.")

# Exercise 3 guess a number between 1 and 9 

import random 
targetNum, guessNum = random.randint(1, 10), 0
while targetNum != guessNum:
    guessNum = int(input("Guess a number between 1 and 10 until you get it right: "))
print("Well Done! You got it right")

# Exercise 4  Construct a specified pattern, using a nested for loop

n=5
for i in range(n):
    for j in range(i):
        print('* ', end="")
    print("")

for i in range(n,0,-1):
    for j in range(i):
        print('* ', end="")
    print('')

# Exercise 5 Reverse a word 

word = input("Input a word that you would like reversed: ")

for char in range(len(word) - 1, -1, -1):
    print(word[char], end="")
print("\n")