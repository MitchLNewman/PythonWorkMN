def factorial(x: int) -> int:
    '''
    factorial(x): returns the product of all integers from 1 to x inclusive.
    '''
    result = 1
    for i in range(2, x + 1):
        result *= i
    return result

# if __name__ == "__main__" stops print statements from automatically being executed when this file is imported

if __name__ == "__main__":
    print(factorial(3))
    print(factorial(5))
    print(factorial(10))

# "python3 -m pydoc DocumentExamp" - shows documentation for this code
# "wrote DcoumentExamp.html" - Writes documentation to Html