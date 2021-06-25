# code to solve Google Code Jam 2020 Round 1A Pascal's Walk problem
# Found on: https://codingcompetitions.withgoogle.com/codejam/round/000000000019fd74/00000000002b1353


def squareExists(location):
	return location[1] <= location[0] and location[1] >= 0 and location[0] >= 0

class Triangle:
	def __init__(self):
		self.grid = [[1],[1,1],[1,2,1]]
	def __str__(self):
		return str(self.grid)
	def generate(self):
		lastRow = self.grid[-1]
		newRow = [1]
		for i in range(len(lastRow) - 1):
			newRow.append(lastRow[i]+lastRow[i+1])
		newRow.append(1)
		self.grid.append(newRow)
	def getVal(self, location):
		x, y = location
		return self.grid[x][y]
	def minCost(self, location):
		x, y = location
		if not squareExists([x, y+1]) or not squareExists([x, y-1]):
			return 0
		return min((self.grid[x][y+1]), (self.grid[x][y-1])) - 1

class Walker:
	def __init__(self, walkSum):
		self.location = [0,0]
		self.pascal = Triangle()
		self.walkSum = walkSum - 1
		self.visited = [[0,0]]
		print(self)
	def __str__(self):
		x, y = self.location
		return str(x+1) + " " + str(y+1)
	def validMoves(self):
		moves = [[-1,-1],[-1,0],[0,-1],[0,1],[1,0],[1,1]]
		valid = []
		for i in moves:
			square = [x + y for x, y in zip(self.location, i)]
			if squareExists(square):
				valid.append(i)
		return valid
	def move(self,move):
		square = [x + y for x, y in zip(self.location, move)]
		if squareExists(square):
			self.location = square
		if square[0] >= len(self.pascal.grid) - 1:
			self.pascal.generate()
		self.walkSum -= self.pascal.getVal(self.location)
		self.visited.append(self.location)
		print(self)
	def getValue(self,move):
		fnSquare = [x + y for x, y in zip(self.location, move)]
		value = self.pascal.getVal(fnSquare) if self.pascal.minCost(fnSquare) + self.pascal.getVal(fnSquare) <= self.walkSum and fnSquare not in self.visited else -1
		return value
	def factorialNext(self):
		moves = self.validMoves()
		bestMove = max(moves, key=lambda a:(self.getValue(a), a[0], a[1]))

		self.move(bestMove)




# method takes data and outputs a result
def solve(walkSum):
	# initiate triangle and walker
	w = Walker(walkSum)
	# start the factorial path
	while w.walkSum > 0:
		w.factorialNext()


# problem mode 0 - single line problem
# problem mode 1 - multi line problem
# problem mode 2 - interactive problem
def problem():
	test_cases = int(input())
	for i in range(test_cases):
		input_data = int(input())
		solution = solve(input_data)

problem()

