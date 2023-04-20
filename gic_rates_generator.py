"""
Final Assignment: Gic Rates Generator 
===========================
Course:   CS 5001
Student:  Cheng Gong
Semester: Spring 2023

An application that gives people expected returns on their GIC
investment for amount and terms they want to invest.
"""


def is_positive_number(my_string):
    """Checks if input can be converted to a positive number.

    Args:
        my_string (str): the string to check

    Returns:
        bool: True if the string can be converted to a positive number, False otherwise
    """
    try:
        # Try converting the string to a float
        number = float(my_string)
        return number > 0
    except ValueError:
        return False


def get_valid_number(prompt: str) -> float:
    """Prompts the user for an int value, and keep
    repeating until a numeric value is entered.

    Args:
        prompt (str): the string to prompt the client with

    Returns:
        int: the final value
    """
    number = input(prompt)
    while not is_positive_number(number):
        print("Must be a positive number.")
        number = input(prompt)
    return float(number)


def get_input():
    """
    Prompts the user for the principal amount, terms in years, and sorts terms in order.
    Calculates the interest rate and exprected returns principal, terms, and interest_rates.

    Returns:
        Tuples,
        Returns the principal, terms, and interest rates if valid input provided, otherwise returns None, None, None.
    """
    principal = get_valid_number("Enter the principal amount: $")
    if principal < 1000:
        print("Minimum amount required is $1000.00")
        return None, None, None

    amount_increase = (principal - 10000) // 10000 if principal >= 10000 else 0
    interest_rate_increase = amount_increase * 0.001

    terms_str = input("Enter the terms in years, separated by commas (1-10): ")
    terms = []
    for term in terms_str.split(","):
        if is_positive_number(term.strip()):
            term = float(term.strip())
            if term < 1 or term > 10:
                print(
                    f"GIC term {term} is unavailable, min 1 year and max 10 years")
                return None, None, None
            terms.append(term)
    terms.sort()
    interest_rates = []
    for term in terms:
        if term < 1.5:
            interest_rate = 0.04
        elif term <= 2:
            interest_rate = 0.042
        elif term <= 3:
            interest_rate = 0.04
        elif term <= 4:
            interest_rate = 0.033
        elif term <= 5:
            interest_rate = 0.03
        elif term <= 10:
            interest_rate = 0.035
        else:
            print(
                f"GIC term {term} is unavailable, min 1 year and max 10 years")
            return None, None
        interest_rates.append(round(interest_rate + interest_rate_increase, 3))

    return principal, terms, interest_rates


def calculate_interest_earned(principal: float, term: float, interest_rate: float) -> float:
    """Calculates the interest earned for a given principal, term, and interest rate.

    Args:
        principal (float): the principal amount inputed
        term (float): the term in years they want to invest in
        interest_rate (float): the interest rate for the given term

    Returns:
        float: the interest earned
    """
    return principal * interest_rate * term


def display_table(principal, terms, interest_rates):
    """Displays a table with the expected return and total amount for each term and interest rate.

    Args:
        principal (float): the principal amount
        terms (list[float]): a list of terms in years
        interest_rates (list[float]): a list of interest rates corresponding to each term
    """
    print(f"\n{'Term (years)':<15} {'Interest Rate':<15} {'Expected Return':<20} {'Total Amount':<15}")
    for i, term in enumerate(terms):
        interest_earned = calculate_interest_earned(
            principal, term, interest_rates[i])
        total_amount = principal + interest_earned
        print(
            f"{term:<15.2f} {interest_rates[i]:<15.3f} {interest_earned:<20,.2f} {total_amount:<15,.2f}")


def gic_rates_generator():
    """Prompts the user for information about their GIC investment, displays a table of expected returns, and allows 
    the user to calculate another GIC rate or exit.

    Note:
        This function will keep repeating until the user choose to exit.

    """
    print("Welcome to the GIC rate generator!\n")
    while True:
        principal, terms, interest_rates = get_input()
        if principal is None:
            continue
        display_table(principal, terms, interest_rates)
        if principal >= 1000000:
            print(
                "Please refer to a banker advisor for further discussion for your investment")
            break
        while True:
            continue_or_exit = input(
                "Would you like to calculate another GIC rate? (Y/N) ").upper()
            if continue_or_exit == "N":
                print("Thank you for using the GIC rate generator. Goodbye!")
                exit()
            if continue_or_exit == "Y":
                break
            else:
                print("Invalid option")
                continue


gic_rates_generator()
