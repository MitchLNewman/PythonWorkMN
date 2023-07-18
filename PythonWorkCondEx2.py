user_mark = int(input("Please enter user mark: "))

if user_mark > 85:
    print("Distinction")
elif user_mark >= 65 and user_mark <= 85:
    print("Pass")
else:
    print("Fail")