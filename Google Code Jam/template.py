# method takes data and outputs a result
def solve(data=None):
	return None

# problem mode 0 - single line problem
# problem mode 1 - multi line problem
# problem mode 2 - interactive problem
def problem(mode=0):
	test_cases = int(input())
	for i in range(test_cases):
		if mode == 2:
			result = None
			while(result == None):
				result = solve()
			print(result)
			feedback = input()
			if(feedback == "N" or feedback == "-1"):
				quit()
		if mode == 0:
			input_data = input()
			solution = solve(input())
			print("Case #{}: {}".format(i + 1, solution))
		if mode == 1:
			info = input()
			data = []
			for i in range(int(info.split(" ")[0])):
				data.append(input())
			data.append(info)
			solution = solve(data)
			print("Case #{}: {}".format(i + 1, solution))

problem()

