import os
import random
import time
import argparse

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
      print(''.join(['🟨' if cell else '⬜' for cell in row]))

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

def run_game(initial_state, num_gen, delay):
    current_state = initial_state

    for gen in range(num_gen):

        os.system('clear')

        render(current_state)

        current_state = next_state(current_state)

        time.sleep(delay)

def load_state_from_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        state = [[int(cell) for cell in line.strip()] for line in lines]
    return state

def main():
    parser = argparse.ArgumentParser(description="Conway's Game of Life Simulator")
    parser.add_argument('--file', type=str, help='Load initial state from a file')
    parser.add_argument('--width', type=int, default=20, help='Width of the grid')
    parser.add_argument('--height', type=int, default=20, help='Height of the grid')
    parser.add_argument('--generations', type=int, default=50, help='Number of generations to simulate')
    parser.add_argument('--delay', type=float, default=0.5, help='Delay between generations')

    args = parser.parse_args()

    if args.file:
        initial_state = load_state_from_file(args.file)
    else:
        initial_state = random_state(args.width, args.height)

    run_game(initial_state, args.generations, args.delay)

if __name__ == '__main__':
    main()