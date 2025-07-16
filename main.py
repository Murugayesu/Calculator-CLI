import math

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Error: Please enter a valid number.")

def get_operation():
    valid_operations = ["+", "-", "*", "/", "**", "sqrt"]
    while True:
        op = input("Enter the operation (+, -, *, /, **, sqrt): ").strip().lower()
        if op in valid_operations or op == "sqrt":
            return op
        print(f"Error: Invalid operation. Please choose from: {', '.join(valid_operations)}")

def calculate(a, op, b=None):
    try:
        if op == "+":
            return a + b
        elif op == "-":
            return a - b
        elif op == "*":
            return a * b
        elif op == "/":
            if b == 0:
                return "Error: Division by zero is not allowed"
            return a / b
        elif op == "**":
            if a == 0 and b < 0:
                return "Error: Cannot raise 0 to a negative power"
            return a ** b
        elif op == "sqrt":
            if a < 0:
                return "Error: Cannot calculate square root of a negative number"
            return math.sqrt(a)
        else:
            return "Error: Invalid operation"
    except OverflowError:
        return "Error: Result is too large to calculate"
    except Exception as e:
        return f"Error: {str(e)}"

def program():
    print("\n--- Simple Calculator ---")
    
    a = get_number("Enter the first number: ")
    
    op = get_operation()
    
    b = None
    if op != "sqrt":
        b = get_number("Enter the second number: ")
    
    result = calculate(a, op, b)
    
    if op == "sqrt":
        print(f"√{a} = {result}")
    else:
        print(f"{a} {op} {b} = {result}")

def main():
    print("Welcome to the Enhanced Calculator!")
    print("Supported operations: +, -, *, /, ** (power), sqrt")
    
    while True:
        try:
            program()
            while True:
                continue_choice = input("\nDo you want to perform another calculation? (y/n): ").strip().lower()
                if continue_choice in ['y', 'yes']:
                    break
                elif continue_choice in ['n', 'no']:
                    print("\nThank you for using the calculator! Goodbye!")
                    return
                else:
                    print("Please enter 'y' for yes or 'n' for no.")
        
        except KeyboardInterrupt:
            print("\n\nCalculator interrupted. Goodbye!")
            return
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            print("Restarting calculator...")
            
if __name__ == "__main__":
    main()
