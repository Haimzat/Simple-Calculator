# Simple Calculator

def calculator():
    print("--- Welcome to the Simple Calculator ---")
    print("Available operations: +, -, *, /")
    
    try:
        # Get user input for numbers and operation
        num1 = float(input("Enter the first number: "))
        operation = input("Choose an operation (+, -, *, /): ")
        num2 = float(input("Enter the second number: "))

        # Perform calculations based on the chosen operation
        if operation == "+":
            result = num1 + num2
            print(f"Result: {num1} + {num2} = {result}")
        elif operation == "-":
            result = num1 - num2
            print(f"Result: {num1} - {num2} = {result}")
        elif operation == "*":
            result = num1 * num2
            print(f"Result: {num1} * {num2} = {result}")
        elif operation == "/":
            # Check for division by zero
            if num2 != 0:
                result = num1 / num2
                print(f"Result: {num1} / {num2} = {result}")
            else:
                print("Error: Division by zero is not allowed!")
        else:
            print("Invalid operation. Please try again.")
            
    except ValueError:
        print("Error: Please enter valid numbers!")

# Run the calculator
if __name__ == "__main__":
    calculator()
