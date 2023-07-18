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
