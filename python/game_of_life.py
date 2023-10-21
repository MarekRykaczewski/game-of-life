import random

def dead_state(width, height):
  arr = [[0]*width]*height
  return arr

def random_state(width, height):
  state = dead_state(width, height)

  for i in range(width):
    for j in range(height):
      state[i][j] = random.randint(0, 1)
  return state