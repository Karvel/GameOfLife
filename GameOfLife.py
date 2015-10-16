#Elanna Grossman
#October 16, 2015
#Simple python script to create first iteration of Conway's Game of Life

import sys
import random

neighbors = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
dead = ' '

def set_grid(argv):
	with open(argv, 'r') as f: #Enter text or file as command-line argument
		input = f.read().splitlines()
		x_rows = max([len(line) for line in input])
		return [line.ljust(x_rows) for line in input]

def find_neighbors(grid, x, y):
	y_cols, x_rows = len(grid), len(grid[0])
	return [grid[y + dy][x + dx] for dx, dy in neighbors
		if (y + dy) in range(y_cols) and (x + dx) in range(x_rows)]

def filter_func(x):
    return x != dead
		
def cell_generation(cell, neighbors):
	alive= list(filter(filter_func, neighbors))
	if cell != dead:
		if len(alive) in [2, 3]: #Rule 2
			return cell
		else:
			return dead #Rules 1 & 4			
	else:				
		if len(alive) == 3: #Rule 3
			return random.choice(alive) #Creates a new cell using only values from neighbors
		else:
			return dead

def repaint(grid):
	return [[cell_generation(cell, find_neighbors(grid, x, y))
		for x, cell in enumerate(line)] for y, line in enumerate(grid)]

def main(argv):
	for line in repaint(set_grid(sys.argv[1])):
		print(''.join(line))
		
if __name__ == '__main__':
	main(sys.argv[1])