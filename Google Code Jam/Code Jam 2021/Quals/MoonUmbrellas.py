# method takes data and outputs a result
def solve(data=None):
	x = int(data[0])
	y = int(data[1])
	string = data[2]
	string = string.replace("?", "")
	if len(string) <= 1:
		return 0
	costSum = 0
	for i in range(len(string) - 1):
		if string[i] == "C" and string[i+1] == "J":
			costSum += x
		else:
			if string[i] == "J" and string[i+1] == "C":
				costSum += y
	return costSum




def problem():
	test_cases = int(input())
	for i in range(test_cases):
		data = input().split()
		solution = solve(data)
		print("Case #{}: {}".format(i + 1, solution))

problem()

