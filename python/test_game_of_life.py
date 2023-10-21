from game_of_life import dead_state, random_state

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