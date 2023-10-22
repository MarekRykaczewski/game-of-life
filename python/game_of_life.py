import random

def dead_state(width, height):
  arr = [[0 for _ in range(width)] for _ in range(height)]
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

def next_state(state):
    rows = len(state)
    cols = len(state[0]) if rows else 0
    new_state = dead_state(rows, cols)
    for i in range(rows):
        for j in range(cols):
            neighbors = get_neighbours((i, j), state)
            live_neighbors = sum(neighbors)

            if live_neighbors <= 1:
                new_state[i][j] = 0
            elif live_neighbors > 3:
                new_state[i][j] = 0
            elif live_neighbors == 3:
                new_state[i][j] = 1
            else:
                new_state[i][j] = state[i][j]

    return new_state