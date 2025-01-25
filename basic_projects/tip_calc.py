def validate_input(prompt):
    """
    validate that the user inputs a valid positive float number.
    """

    while True:
        user_input = input(prompt)
        try:
            value = float(user_input)
            if value <= 0:
                print('Please enter a positive number.')
                continue
            return value
        except ValueError:
            print('Invalid input! Please enter a valid number')

def tip_calculator():
    """
    calculates the total tip and splits the bill among people.
    """

    print('Welcome to the Tip calculator!')

    # get total bill amount
    total_bill = validate_input('Enter the total bill amount: ')

    # get tip percentage
    tip_percentage = validate_input('Enter the tip percentage you would like to give (eg., 10 for 10%): ')

    # number of people splitting the bill
    num_people = validate_input('Enter the number of people splitting the bill: ')

    # calculate the tip amount and total bill

    tip_amount = (tip_percentage / 100) * total_bill
    total_amount = total_bill + tip_amount
    per_person_amount = total_amount / num_people


    # results
    print('Calulation Results')
    print(f"Total Bill amount: ${total_bill:.2f}")
    print(f"Tip Percentage: {tip_percentage:.2f}%")
    print(f"Tip Amount: ${tip_amount:.2f}")
    print(f"Total Amount (Including Tip): ${total_amount:.2f}")
    print(f"Amount Per Person: ${per_person_amount:.2f}")

    print("Thank you for using the Tip Calculator!")

# run tip calculator
tip_calculator()
