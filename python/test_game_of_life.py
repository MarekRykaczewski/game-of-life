from game_of_life import dead_state

def test_dead_state():
  assert dead_state(5, 5) == [
      [0,0,0,0,0],
      [0,0,0,0,0],
      [0,0,0,0,0],
      [0,0,0,0,0],
      [0,0,0,0,0]
  ]