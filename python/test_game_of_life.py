import os
from game_of_life import dead_state, next_state, get_neighbours, random_state, load_state_from_file, render

def test_dead_state():
    width, height = 5, 5
    result = dead_state(width, height)

    # Width of the result matches the specified width
    assert len(result) == width
    # Height of each row in the result matches the specified height
    assert all(len(row) == height for row in result)
    # All cells in the result are set to 0 (dead state)
    assert all(cell == 0 for row in result for cell in row)

def test_random_state():
    width, height = 5, 5
    result = random_state(width, height)

    # Width of the result matches the specified width
    assert len(result) == width
    # Height of each row in the result matches the specified height
    assert all(len(row) == height for row in result)
    # All cells in the result are either 0 or 1 (random state)
    assert all(cell in [0, 1] for row in result for cell in row)

def test_neighbours():
    state = [
        [1, 0, 1, 0],
        [1, 1, 1, 0],
        [0, 0, 0, 0]
    ]

    position = (0, 1)
    # Lists all neighbours of cell at position
    assert list(get_neighbours(position, state)) == [1, 1, 1, 1, 1]

def test_next_state():
    # Empty grid remains empty
    input_state = dead_state(3, 3)
    expected_output = dead_state(3, 3)
    assert next_state(input_state) == expected_output

    # Cell should die (underpopulation)
    input_state = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    expected_output = dead_state(3, 3)
    assert next_state(input_state) == expected_output

    # Blinker (periodic oscillation)
    input_state = [[0, 1, 0], [0, 1, 0], [0, 1, 0]]
    expected_output = [[0, 0, 0], [1, 1, 1], [0, 0, 0]]
    assert next_state(input_state) == expected_output

def test_render():
    # Ensure state remains unchanged after render
    state = [
        [1, 0, 1],
        [0, 1, 0],
        [1, 0, 1]
    ]

    expected_output = state
    render(state)

    assert state == expected_output

def test_load_state_from_file():
    # Create a temporary test file with a known content
    with open('test_initial_state.txt', 'w') as test_file:
        test_file.write("01010\n00100\n11111\n00100\n01010\n")

    # Call the function to load the state from the test file
    state = load_state_from_file('test_initial_state.txt')

    # Define the expected state based on the content of the test file
    expected_state = [
        [0, 1, 0, 1, 0],
        [0, 0, 1, 0, 0],
        [1, 1, 1, 1, 1],
        [0, 0, 1, 0, 0],
        [0, 1, 0, 1, 0]
    ]

    # Loaded state matches the expected state
    assert state == expected_state

    # Clean up the test file
    os.remove('test_initial_state.txt')