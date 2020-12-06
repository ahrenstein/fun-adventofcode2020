#!/usr/bin/env python3
"""Advent Of Code 2020 Day 2"""

import re
import sys


# Check password compliance
def passwd_compliance(min_count, max_count, char, password):
    """
    Count the characters of a password for compliance with the puzzle

    Args:
        min_count: Minimum appearances
        max_count: Maximum appearances
        char: The character
        password: The password

    Returns"
        test_result: Pass/fail bool of puzzle

    """
    counted_chars = password.count(char)
    test_result = 0
    if counted_chars <= max_count:
        if counted_chars >= min_count:
            test_result = 1
    return test_result


# Check password compliance under new policy
def new_compliance(pos_a, pos_b, char, password):
    """
    Count the characters of a password for compliance with the puzzle

    Args:
        pos_a: One of two positions the character must appear in
        pos_b: One of two positions the character must appear in
        char: The character
        password: The password

    Returns"
        test_result: Pass/fail bool of puzzle

    """
    test_result = 0
    if password[pos_a-1] is char or password[pos_b-1] is char:
        if password[pos_a-1] is not password[pos_b-1]:
            test_result = 1
    return test_result


# Main function
def main():
    """
    The main function of the puzzle

    """

    # Compliant passwords
    compliant_passwds = 0
    new_policy_compliant = 0
    # Get the db from a file
    puzzle_input = open('day2-input.txt', 'r')
    db_lines = puzzle_input.readlines()
    for line in db_lines:
        # Split the line in to variables using the most bootleg way possible
        min_count = int(line.split('-')[0])
        max_count = int(line.split('-')[1].split(' ')[0])
        char = line.split(' ')[1].split(':')[0]
        passwd = line.split (' ')[2]

        # Check the password
        if passwd_compliance(min_count, max_count, char, passwd):
            compliant_passwds = compliant_passwds + 1

        # Check the password under the new policy
        if new_compliance(min_count, max_count, char, passwd):
            new_policy_compliant = new_policy_compliant + 1

    print("Total compliant passwords: %s" % compliant_passwds)
    print("Total compliant passwords under the new policy: %s" % new_policy_compliant)


# Script entry point
if __name__ == '__main__':
    main()
