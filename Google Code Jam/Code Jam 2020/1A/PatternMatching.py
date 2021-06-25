# code to solve Google Code Jam 2020 Round 1A Pattern Matching problem

# method takes data and outputs a result
def solve(data=None):
	data.pop()
	starts = []
	ends = []
	middles = []
	for i in data:
		if i[0] != "*":
			starts.append(i[0:i.find('*')])
			i = i[i.find('*'):]
		if i[-1] != "*":
			ends.append(i[-i[::-1].find('*'):])
			i = i[:-i[::-1].find('*')-1]
		middles.extend(i.split("*"))
	for i in starts:
		for j in starts:
			if len(i) == len(j) and i != j:
				return "*"
			if len(i) > len(j):
				if not i.startswith(j):
					return "*"
	for i in ends:
		for j in ends:
			if len(i) == len(j) and i != j:
				return "*"
			if len(i) > len(j):
				if not i.endswith(j):
					return "*"
	return (max(starts, key=len) if len(starts) > 0 else "") + "".join(middles) + (max(ends, key=len) if len(ends) > 0 else "")



def problem():
	test_cases = int(input())
	for i in range(test_cases):
		info = input()
		data = []
		for j in range(int(info.split(" ")[0])):
			data.append(input())
		data.append(info)
		solution = solve(data)
		print("Case #{}: {}".format(i + 1, solution))

problem()

