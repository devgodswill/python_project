from colorama import Fore, Style

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return Fore.RED + "Error! Division by Zero"
    return a / b

def calculator():
    print("Welcome to the calculator program")

    while True:
        # displays operations

        print(Fore.YELLOW + 'Select and Operation:')
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Exit")

        # get user choice
        choice = input(Fore.BLUE + "Enter your choice (1/2/3/4/5): ")

        if choice == '5':
            print(Fore.GREEN + 'Goodbye!' + Style.RESET_ALL)
            break

        # validate choice
        if choice not in ['1', '2', '3', '4']:
            print(Fore.RED + "Invalid choice. Please try again.")
            continue

        #Get numbers from user


        try:
            num1 = float(input('Enter the first number: '))
            num2 = float(input('Enter the second number: '))
        except ValueError:
            print(Fore.RED + "Invalid input. Please enter numbers only." + Style.RESET_ALL)
            continue

        # Perform the chosen operation

        if choice == '1':
            print(Fore.GREEN + f"Result: {add(num1, num2)}" + Style.RESET_ALL)
        elif choice == '2':
            print(Fore.GREEN + f"Result: {subtract(num1, num2)}" + Style.RESET_ALL)
        elif choice == '3':
            print(Fore.GREEN + f"Result: {multiply(num1, num2)}" + Style.RESET_ALL)
        elif choice == '4':
            print(Fore.GREEN + f"Result: {divide(num1, num2)}" + Style.RESET_ALL)

# Run the calculator
calculator()