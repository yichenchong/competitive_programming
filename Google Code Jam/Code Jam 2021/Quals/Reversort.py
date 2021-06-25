# method takes data and outputs a result
def solve(data=None):
	sumNum = 0
	for i in range(0, len(data)-1):
		j = data.index(min(data[i:]))
		parta = data[:i]
		partb = data[i:j+1]
		partb.reverse()
		partb.extend(data[j+1:])
		parta.extend(partb)
		data = parta
		sumNum += (j - i + 1)
	return sumNum


def problem():
	test_cases = int(input())
	for i in range(test_cases):
		lengthArray = input()
		data = input().split()
		data = [int(i) for i in data]
		solution = solve(data)
		print("Case #{}: {}".format(i + 1, solution))

problem()