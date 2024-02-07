#!/usr/bin/env python3

def add_numbers(first_number, second_number):
    """Calculates the sum of two numbers.

    Args:
        first_number (int or float): The first number to add.
        second_number (int or float): The second number to add.

    Returns:
        float: The sum of the two numbers.

    Raises:
        TypeError: If either `first_number` or `second_number` is not an integer or float.
    """

    if not isinstance(first_number, (int, float)):
        raise TypeError("First number must be an integer or float.")
    if not isinstance(second_number, (int, float)):
        raise TypeError("Second number must be an integer or float.")

    return first_number + second_number

def main():
    """Provides entry point for the script and handles parameter parsing."""

    import argparse

    parser = argparse.ArgumentParser(description="Calculates the sum of two numbers.")
    parser.add_argument("--first_number", type=float, required=True, help="The first number to add.")
    parser.add_argument("--second_number", type=float, required=True, help="The second number to add.")

    args = parser.parse_args()

    sum_of_numbers = add_numbers(args.first_number, args.second_number)
    print(f"The sum of {args.first_number} and {args.second_number} is: {sum_of_numbers}")

if __name__ == "__main__":
    main()
