def factorial(x: int) -> int:
    '''
    factorial(x): returns the product of all integers from 1 to x inclusive.
    '''
    result = 1
    for i in range(2, x + 1):
        result *= i
    return result

if __name__ == "__main__":
    print(factorial(3))
    print(factorial(5))
    print(factorial(10))

