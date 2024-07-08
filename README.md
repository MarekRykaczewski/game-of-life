# Conway's Game of Life Simulator

## Description

This project implements Conway's Game of Life, a cellular automaton devised by the British mathematician John Horton Conway in 1970. The game is a zero-player game, meaning its evolution is determined by its initial state, requiring no further input.

## Setup Instructions

Clone the repository:

```bash
Copy code
git clone https://github.com/MarekRykaczewski/game-of-life.git
cd GameOfLife
```

## Usage

You can run the Game of Life simulator with different options using command-line arguments.

Command-Line Arguments:

- --file: Load initial state from a file.
- --width: Width of the grid (default: 20).
- --height: Height of the grid (default: 20).
- --generations: Number of generations to simulate (default: 50).
- --delay: Delay between generations in seconds (default: 0.5).

## Running the Simulator:

To run the simulator with a random initial state:

```bash
python game_of_life.py --width 30 --height 30 --generations 100 --delay 0.1
```

To run the simulator with an initial state loaded from a file:

```bash
python game_of_life.py --file initial_state.txt --generations 100 --delay 0.1
```

## Example Initial State File

The file should contain a grid of 0s and 1s, representing dead and alive cells respectively. For example:

```
01000
00100
11100
00000
00000
```
