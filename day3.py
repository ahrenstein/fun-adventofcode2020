#!/usr/bin/env python3
"""Advent Of Code 2020 Day 3"""


# Get the map from a file
with open('day3-input.txt', 'r') as puzzle_input:
    map_data = puzzle_input.read().splitlines()


# Count trees along the path
def count_trees(map_input):
    """
    Count the trees across the right/down path

    Args:
        map_input: Map data read from file

    Returns"
        total_trees: The total number of trees

    """
    # Instantiate counter for trees
    total_trees = 0
    # Start at position 0 for the toboggan
    toboggan_location = 0
    # Get the width of the path
    path_width = len(map_input[0])

    # Iterate over each path line by line
    for path in map_input:
        # Check if the toboggan hits a tree
        if '#' in path[toboggan_location]:
            total_trees = total_trees + 1
        # Increase the toboggan's right location by 3
        toboggan_location = toboggan_location + 3
        # Since each path repeats we cheat a bit to make that work
        if toboggan_location >= path_width:
            toboggan_location -= path_width
    return total_trees


# Count along different paths
def multi_path(map_input):
    """
    Count the trees across the right/down paths specified

    Args:
        map_input: Map data read from file

    Returns"
        multiplied_trees: The total number of trees across the paths multiplied together

    """
    # Instantiate some values
    multiplied_trees = 1
    # Get the width of the path
    path_width = len(map_input[0])
    # Paths going right
    right_paths = [1, 3, 5, 7, 1]
    # Paths going down
    down_paths = [1, 1, 1, 1, 2]
    #
    # Count the steps going down
    for i, step in enumerate(right_paths):
        total_trees = 0
        toboggan_location = 0
        # Count the steps going right
        for j, path in enumerate(map_input):
            # Make sure we stop once we run out of paths
            if down_paths[i] == 2 and j % 2 != 0:
                continue
            # Check for a tree in the path
            if "#" in path[toboggan_location]:
                total_trees = total_trees + 1
            # Increase the toboggan location by steps right
            toboggan_location = toboggan_location + step
            # Since each path repeats we cheat a bit to make that work
            if toboggan_location >= path_width:
                toboggan_location -= path_width
        # Multiply the total trees by the new total count of this path
        multiplied_trees = multiplied_trees * total_trees
    return multiplied_trees


# Main function
def main():
    """
    The main function of the puzzle

    """
    print("The total number of trees on the first trip: %s" % count_trees(map_data))
    print("The total number of trees on the second trip: %s" % multi_path(map_data))


# Script entry point
if __name__ == '__main__':
    main()
