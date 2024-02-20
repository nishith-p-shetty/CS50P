import math
from support import add, subtract, multiply, divide, exponentiate, modulus, square_root

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y

def exponentiate(x, y):
    return x ** y

def modulus(x, y):
    return x % y

def square_root(x):
    if x < 0:
        raise ValueError("Cannot calculate square root of a negative number")
    return math.sqrt(x)

def main():
    print("Welcome to Calculator")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exponentiate")
    print("6. Modulus")
    print("7. Square Root")

    choice = input("Enter choice (1/2/3/4): ")

    if choice == '1':
        print(num1, "+", num2, "=", add(num1, num2))
    elif choice == '2':
        print(num1, "-", num2, "=", subtract(num1, num2))
    elif choice == '3':
        print(num1, "*", num2, "=", multiply(num1, num2))
    elif choice == '4':
        try:
            print(num1, "/", num2, "=", divide(num1, num2))
        except ValueError as e:
            print(e)
    elif choice == '5':
        print(num1, "^", num2, "=", exponentiate(num1, num2))
    elif choice == '6':
        print(num1, "%", num2, "=", modulus(num1, num2))
    elif choice == '7':
        try:
            print(f"sqrt({num1}) = {square_root(num1)}")
        except ValueError as e:
            print(e)
    else:
        print("Invalid input")

if __name__ == "__main__":
    main()