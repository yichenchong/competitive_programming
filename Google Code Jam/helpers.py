class Matrix:
	def __init__(self, grid):
		self.grid = grid
	def __str__(self):
		return str(self.grid)
	def invert(self):
		newGrid = []
		for i in range(len(self.grid)):
			for j in range(len(self.grid[i])):
				if range(len(newGrid) <= j):
					newGrid.append([])
				newGrid[j].append(self.grid[i][j])
		self.grid = newGrid
	def row(self, index):
		return self.grid[index]
	def col(self, index):
		col = []
		for i in range(len(self.grid)):
			col.append(self.grid[i][index])
		return col

def frequencyMap(my_list):
	freq = {}
	for i in my_list:
		freq[i] = freq[i] + 1 if i in freq else 1
	return freq