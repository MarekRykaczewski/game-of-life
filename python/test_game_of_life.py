from game_of_life import dead_state, random_state

def test_dead_state():
    width, height = 5, 5
    result = dead_state(width, height)

    assert len(result) == width
    assert all(len(row) == height for row in result)
    assert all(cell == 0 for row in result for cell in row)

def test_random_state():
    width, height = 5, 5
    result = random_state(width, height)

    assert len(result) == width
    assert all(len(row) == height for row in result)
    assert all(cell in [0, 1] for row in result for cell in row)