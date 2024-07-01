<<<<<<< HEAD
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a numeric value.")

def get_operation():
    operations = {
        '1': add,
        '2': subtract,
        '3': multiply,
        '4': divide
    }
    while True:
        print("Select operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        choice = input("Enter choice (1/2/3/4): ")
        if choice in operations:
            return operations[choice], choice
        else:
            print("Invalid choice! Please select a valid operation.")

def main():
    print("Welcome to the Simple Calculator!")
    
    num1 = get_number("Enter the first number: ")
    num2 = get_number("Enter the second number: ")
    operation, op_choice = get_operation()
    
    result = operation(num1, num2)
    
    operation_names = {'1': 'Addition', '2': 'Subtraction', '3': 'Multiplication', '4': 'Division'}
    print(f"{operation_names[op_choice]} of {num1} and {num2} is: {result}")

if __name__ == "__main__":
    main()
>>>>>>>>>
