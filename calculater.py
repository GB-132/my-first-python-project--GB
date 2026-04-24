while True:
    num1 = float(input("\nEnter first number: "))
    num2 = float(input("Enter second number: "))

    op = input("Enter operation (+, -, *, /): ")

    if op == "+":
        print("Result:", num1 + num2)
    elif op == "-":
        print("Result:", num1 - num2)
    elif op == "*":
        print("Result:", num1 * num2)
    elif op == "/":
        if num2 != 0:
            print("Result:", num1 / num2)
        else:
            print("Cannot divide by zero!")
    else:
        print("Invalid operator!")

    choice = input("Do you want to continue? (yes/no): ").lower()
    if choice != "yes":
        break

print("Calculator closed.")