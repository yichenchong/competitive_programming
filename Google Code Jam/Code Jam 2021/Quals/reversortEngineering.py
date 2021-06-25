def transformationList(n, c):
	transformationList = [1 for i in range(n-1)]
	pointer = 0
	tempCost = c - n + 1
	while tempCost > 0:
		if transformationList[pointer] >= n - pointer:
			pointer += 1
		transformationList[pointer] += 1
		tempCost -= 1
	transformationList = [i - 1 for i in transformationList]
	return transformationList

# method takes data and outputs a result
def solve(data=None):
	n = int(data[0])
	c = int(data[1])
	
	maxCost = sum([(n-i) for i in range(n-1)])
	if c > maxCost or c < n - 1:
		return "IMPOSSIBLE"

	transforms = transformationList(n, c)

	order = list(range(n - 1))
	order.reverse()

	arr = list(range(n))
	for i in order:
		transform = transforms[i]
		parta = arr[:i]
		partb = arr[i:i+transform+1]
		partc = arr[i+transform+1:]
		partb.reverse()
		partb.extend(partc)
		parta.extend(partb)
		arr = parta
	return " ".join([str(i+1) for i in arr])

def problem():
	test_cases = int(input())
	for i in range(test_cases):
		data = input().split()
		solution = solve(data)
		print("Case #{}: {}".format(i + 1, solution))

problem()

