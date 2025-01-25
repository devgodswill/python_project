# goal of the project
# allow users to convert between different units like length, weight, and temperature.

from colorama import Fore, Style, init

# unit converter program

init(autoreset=True)

def validate_input(prompt):
    """
    Ensures that the user enters a valid float number.
    """

    while True:
        user_input = input(prompt)
        try:
            return float(user_input)
        except ValueError:
            print(Fore.RED + "Invalid input! please enter a number.")

def length_converter():
    """
    converts between meters, kilometers, miles and centimeters
    """

    print(Fore.CYAN + 'Length Conversion:')
    print('1. Meters to Kilometers')
    print('2. Kilometers to Meters')
    print('3. Miles to Kilometers')
    print('4. Kilometers to Miles')
    print('5. Centimeters to Meters')
    print('6. Meters to Centimeters')

    choice = input(Fore.YELLOW + "Choose a conversion (1/2/3/4/5/6): ")

    value = validate_input('Enter the value to convert: ')

    if choice == '1':
        result = value / 1000
        print(Fore.GREEN + f"{value} meters is {result:.3f} kilometers.")
    elif choice == '2':
        result = value * 1000
        print(Fore.GREEN + f"{value} kilometers is {result:.3f} meters")
    elif choice == '3':
        result = value * 1.609
        print(Fore.GREEN + f"{value} mile is {result:.3f} kilometers.")
    elif choice == '4':
        result = value / 1.609
        print(Fore.GREEN + f"{value} kilometers is {result:.3f} miles.")
    elif choice == '5':
        result = value / 100
        print(Fore.GREEN + f"{value} centimeters is {result:.3f} meters.")
    elif choice == '6':
        result = value * 100
        print(Fore.GREEN + f"{value} meters is {result:.3f} centimeters.")
    else:
        print(Fore.RED + "Invalid choice! Please try again")

def weight_converter():
    """
    converts between Kilogram, pounds, and grams.
    """

    print(Fore.CYAN + 'Weight Conversion:')
    print('1. Kilograms to Pounds')
    print('2. Pounds to Kilograms')
    print('3. Grams to Kilograms')
    print('4. Kilograms to Grams')


    choice = input(Fore.YELLOW + "Choose a conversion (1/2/3/4/): ")

    value = validate_input('Enter the weight to convert: ')

    if choice == '1':
        result = value * 2.205
        print(Fore.GREEN + f"{value} kilograms is {result:.3f} pounds.")
    elif choice == '2':
        result = value / 2.205
        print(Fore.GREEN + f"{value} pounds is {result:.3f} kilograms")
    elif choice == '3':
        result = value / 1000
        print(Fore.GREEN + f"{value} grams is {result:.3f} kilograms.")
    elif choice == '4':
        result = value * 1000
        print(Fore.GREEN + f"{value} kilograms is {result:.3f} grams.")
    else:
        print(Fore.RED + "Invalid choice! Please try again")

def temperature_converter():
    """
    converts between Celsius, Fahrenheit, and Kelvin.
    """

    print(Fore.CYAN + 'Temperature Conversion:')
    print('1. Celsius to Fahrenheit')
    print('2. Fahrenheit to Celsius')
    print('3. Celsius to Kelvin')
    print('4. Kelvin to Celsius')


    choice = input(Fore.YELLOW + "Choose a conversion (1/2/3/4/): ")

    value = validate_input('Enter the temperature to convert: ')

    if choice == '1':
        result = (value * 9/5) + 32
        print(Fore.GREEN + f"{value}°C is {result:.2f}°F.")
    elif choice == '2':
        result = (value - 32) * 5/9
        print(Fore.GREEN + f"{value}°F is {result:.2f}°C.")
    elif choice == '3':
        result = value + 273.15
        print(Fore.GREEN + f"{value}°C is {result:.2f} Kelvin.")
    elif choice == '4':
        result = value - 273.15
        print(Fore.GREEN + f"{value} Kelvin is {result:.2f}°C.")
    else:
        print(Fore.RED + "Invalid choice! Please try again")

def speed_converter():
    """
    converts between kilometers per hour, and miles per hour.
    """

    print(Fore.CYAN + 'Speed Conversion:')
    print('1. Kilometers per hour to Miles per hour')
    print('2. Miles per hour to Kilometers per hour')


    choice = input(Fore.YELLOW + "Choose a conversion (1/2): ")

    value = validate_input('Enter the speed to convert: ')

    if choice == '1':
        result = value / 1.609
        print(Fore.GREEN + f"{value} km/h is {result:.3f} mph.")
    elif choice == '2':
        result = value * 1.609
        print(Fore.GREEN + f"{value} mph is {result:.3f} km/h.")
    else:
        print(Fore.RED + "Invalid choice! Please try again.")

def unit_converer():
    """
    Main menu for the unit converter program
    """

    print(Fore.BLUE + Style.BRIGHT + "Welcome to the Unit Converter!")

    while True:
        print(Fore.YELLOW + Style.BRIGHT + "What would you like to convert?")
        print(Fore.CYAN + "1. Length")
        print(Fore.CYAN + "2. Weight")
        print(Fore.CYAN + "3. Temperature")
        print(Fore.CYAN + "4. Speed")
        print(Fore.RED + "5. Exit")

        choice = input(Fore.YELLOW + "Enter your choice (1/2/3/4/5): ")

        if choice == "1":
            length_converter()
        elif choice == "2":
            weight_converter()
        elif choice == "3":
            temperature_converter()
        elif choice == "4":
            speed_converter()
        elif choice == "5":
            print(Fore.BLUE + "Goodebye!")
            break
        else:
            print(Fore.RED + "Invalid choice! Please try again.")

# run the unit converter
unit_converer()