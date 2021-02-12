# code to solve Google Code Jam 2020 Round 1B Expogo problem

import math
dire = ["E", "W", "S", "N"]

def impossible(distance, steps):
	distance = abs(distance)
	return distance - ((distance >> (steps - 1)) << (steps - 1)) != 0


# method takes data and outputs a result

def solve(coordinate):
	coordinateMax = max([abs(i) for i in coordinate])
	stepMax = 2 * ((math.log(coordinateMax)/math.log(2)) // 1 + 1)
	return tryHit(tuple(coordinate), 1, min(max([abs(i) for i in coordinate]), stepMax))

def tryHit(target, step, maxi):
	jumpDist = 2 ** (step - 1)
	if tuple(target) == (0,0):
		return ""
	if impossible(abs(target[0]), step) or impossible(abs(target[1]), step):
		return None
	if(step > maxi):
		return None
	tries = []
	tryEast = tryHit([target[0] - jumpDist,target[1]], step + 1, maxi)
	tryWest = tryHit([target[0] + jumpDist,target[1]], step + 1, maxi)
	trySouth = tryHit([target[0],target[1] - jumpDist], step + 1, maxi)
	tryNorth = tryHit([target[0],target[1] + jumpDist], step + 1, maxi)
	tries = [tryEast, tryWest, tryNorth, trySouth]
	mini = None
	minij = None
	for j, i in enumerate(tries):
		if mini == None:
			mini = i
			minij = j
		elif i != None and len(i) < len(mini):
			mini = i
			minij = j
	if mini == None:
		return None
	return dire[minij] + mini


	


def problem():
	test_cases = int(input())
	for i in range(test_cases):
		input_data = tuple([int(i) for i in input().split(" ")])
		solution = solve(input_data)
		solution = solution if solution != None else "IMPOSSIBLE"
		print("Case #{}: {}".format(i + 1, solution))

problem()

