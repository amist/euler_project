size = 21
grid = []
for i in range(size):
	grid_line = [0] * size
	grid.append(grid_line)
	
for i in range(size):
	grid[0][i] = 1
	grid[i][0] = 1
	
for i in range(1, size):
	for j in range(1, size):
		grid[i][j] = grid[i-1][j] + grid[i][j-1]
		
print grid[size - 1][size - 1]
		