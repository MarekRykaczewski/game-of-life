import random

def dead_state(width, height):
  arr = [[0]*width]*height
  return arr

def random_state(width, height):
    state = dead_state(width, height)
    
    for i in range(height):
        state[i] = [random.randint(0, 1) for _ in range(width)]
    
    return state