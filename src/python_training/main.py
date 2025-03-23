"""The entry point for the python_training package."""

import argparse
from argparse import Namespace  # used for documentation

from python_training.ascii_art import (
    ASCII_ART,
)  # full explicit imports make life easier


def parse_args() -> Namespace:
    """Parse the arguments the user is passing to the script.

    Returns:
        Namespace: The ArgumentParser namespace object.
    """
    # Argparse is way nicer than using sys.args...
    # you can add so much more detail for each argument/option.
    parser = argparse.ArgumentParser(
        description="Determine the main function's operation.",
    )
    parser.add_argument(
        "-a",
        "--ascii_print",
        action="store_true",
        required=False,
        help="Use this option to print the ASCII art.",
    )
    args = parser.parse_args()
    return args


def print_ascii() -> None:
    """Print the ASCII art."""
    print(ASCII_ART)


# The main function is usually at the bottom of the script
def main() -> None:
    """The main function to be ran in this script.
    Depending on the arguments passed, different operations will be performed.
    """
    print("Executing the main function!")

    # Parse the arguments
    args = parse_args()

    if args.ascii_print:
        print_ascii()


# This tells the Python interpreter to run this portion of code when
# executing the script in the terminal.
# Example: python main.py
if __name__ == "__main__":
    main()
