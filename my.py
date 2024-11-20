def calculator():
    print("Welcome to the Simple Calculator!")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    try:
    
        choice = input("Enter the number of the operation you'd like to perform (1/2/3/4): ")
        if choice not in ['1', '2', '3', '4']:
            print("Invalid input. Please select a valid operation.")
            return

        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        
        if choice == '1':
            print(f"The result of addition: {num1} + {num2} = {num1 + num2}")
        elif choice == '2':
            print(f"The result of subtraction: {num1} - {num2} = {num1 - num2}")
        elif choice == '3':
            print(f"The result of multiplication: {num1} * {num2} = {num1 * num2}")
        elif choice == '4':
            if num2 != 0:
                print(f"The result of division: {num1} / {num2} = {num1 / num2}")
            else:
                print("Error: Division by zero is not allowed.")

    except ValueError:
        print("Invalid input. Please enter numeric values.")

# Run the calculator
if __name__ == "__main__":
    calculator()
