"""
Final Assignment: tests for Gic Rates Generator 
===========================
Course:   CS 5001
Student:  Cheng Gong
Semester: Spring 2023

All possible tests are created, the remaining display_table()
and gic_rates_generator() returns prints are not testable.
"""

import unittest
from unittest import mock
from gic_rates_generator import is_positive_number, get_valid_number, get_input, calculate_interest_earned


def test_is_positive_number() -> int:
    """
    This function tests the is_positive_number function.

    Test cases:
    - Check if "0" returns False
    - Check if "1" returns True
    - Check if "-1" returns False
    - Check if "ds" returns False
    - Check if "1.5" returns True

    Returns:
    An integer representing the number of failed tests.
    """
    failed_count = 0
    if (is_positive_number("0")):
        failed_count += 1
    if (not is_positive_number("1")):
        failed_count += 1
    if (is_positive_number("-1")):
        failed_count += 1
    if (is_positive_number("ds")):
        failed_count += 1
    if (not is_positive_number("1.5")):
        failed_count += 1
    return failed_count


def test_get_valid_number() -> int:
    """
    This function tests the get_valid_number function.

    Test case:
    - Mock the built-in input function to return "42" and
    check if get_valid_number returns 42.0.

    Returns:
    An integer representing the number of failed tests.
    """
    failed_count = 0
    original_input = mock.builtins.input
    mock.builtins.input = lambda _: "42"
    if (get_valid_number('Enter a number: ') != 42.0):
        failed_count += 1
    mock.builtins.input = original_input
    return failed_count


def test_get_input() -> int:
    """
    This function tests the get_input function.

    Test case:
    - Mock the built-in input function to return "900" and
    check if get_input returns (None, None, None).

    Returns:
    An integer representing the number of failed tests.
    """
    failed_count = 0
    original_input = mock.builtins.input
    mock.builtins.input = lambda _: "900"
    if (get_input() != (None, None, None)):
        failed_count += 1
    mock.builtins.input = original_input
    return failed_count


def test_calculate_interest_earned() -> int:
    """
    This function tests the calculate_interest_earned function.

    Test case:
    - Check if calculate_interest_earned(10000, 1, 2) returns the
    result of 10000*1*2 which is 20000.

    Returns:
    An integer representing the number of failed tests.
    """
    failed_count = 0
    if (calculate_interest_earned(10000, 1, 2) != 20000):
        failed_count += 1
    return failed_count


def main():
    failed_count = test_is_positive_number()
    failed_count += test_get_valid_number()
    failed_count += test_get_input()
    failed_count += test_calculate_interest_earned()
    print(f"Failed {failed_count} tests.")


if __name__ == '__main__':
    main()
