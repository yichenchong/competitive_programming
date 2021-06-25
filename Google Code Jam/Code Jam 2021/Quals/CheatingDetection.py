import math

def computeQDifficulty(data):
	difficulties = []
	for i in range(len(data[0])):
		sumNum = 0
		for j in range(len(data)):
			sumNum += data[j][i]
		c = sumNum / len(data)
		if c == 0:
			difficulties.append(3.0)
		difficulty = math.log(1/c - 1)
		if difficulty > 3:
			difficulty = 3
		if difficulty < -3:
			difficulty = -3
		difficulties.append(difficulty)
	return difficulties

def computeSkill(data):
	skills = []
	for i in range(len(data)):
		c = sum(data[i])/len(data[0])
		if c == 0:
			skills.append(-3.0)
		skill = -math.log(1/c - 1)
		if skill > 3:
			skill = 3
		if skill < -3:
			skill = -3
		skills.append(skill)
	return skills

def solve(data):
	difficulties = computeQDifficulty(data)
	skills = computeSkill(data)
	errors = []
	for i in range(len(skills)):
		totalError = 0
		for j in range(len(difficulties)):
			expected = 1/(1+math.pow(math.e, difficulties[j]-skills[i]))
			actual = data[i][j]
			error = math.pow(expected-actual, 2)
			totalError += error
		errors.append(totalError)
	average = sum(errors)/len(errors)
	errors = [abs(i-average) for i in errors]
	return errors.index(max(errors))+1

def problem(numLines):
	test_cases = int(input())
	p = int(input())
	for i in range(test_cases):
		data = []
		for j in range(numLines):
			data.append([int(k) for k in list(input())])
		solution = solve(data)
		print("Case #{}: {}".format(i + 1, solution))

def problemFile(numLines):
	file = open("cheat.txt","r")
	test_cases = int(file.readline()[:-1])
	p = int(file.readline()[:-1])
	for i in range(test_cases):
		data = []
		for j in range(numLines):
			data.append([int(k) for k in list(file.readline())[:-1]])
		solution = solve(data)
		print("Case #{}: {}".format(i + 1, solution))


problemFile(100)