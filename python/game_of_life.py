import random

def dead_state(width, height):
  arr = [[0]*width]*height
  return arr

def random_state(width, height):
    state = dead_state(width, height)
    
    for i in range(height):
        state[i] = [random.randint(0, 1) for _ in range(width)]
    
    return state

def get_neighbours(pos, state):
    rows = len(state)
    cols = len(state[0]) if rows else 0

    for i in range(max(0, pos[0] - 1), min(rows, pos[0] + 2)):
        for j in range(max(0, pos[1] - 1), min(cols, pos[1] + 2)):
            if (i, j) != pos:
                yield state[i][j]
      
def render(state):
  for row in state:
      print(' '.join(['X' if cell else 'O' for cell in row]))
