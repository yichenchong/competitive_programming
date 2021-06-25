def placeInArray(arr, i):
	if len(arr) == 0:
		return [i]
	pointer2 = len(arr) // 3 # the lower pointer
	pointer1 = (len(arr) * 2) // 3 # the higher pointer
	print(str(arr[pointer2]), str(arr[pointer1]), i)
	median = int(input())
	if median == -1:
		quit()
	if median == i:
		recArray = arr[pointer2+1:pointer1]
		if len(recArray) != 1:
			return arr[:pointer2+1] + placeInArray(recArray, i) + arr[pointer1:]
		else:
			return arr[:pointer2] + placeInArray(arr[pointer2:pointer1], i)+arr[pointer1:]
	if median == arr[pointer1]:
		recArray = arr[pointer1+1:]
		if len(recArray) != 1:
			return arr[:pointer1+1] + placeInArray(recArray, i)
		else:
			return arr[:pointer1] + placeInArray(arr[pointer1:], i)
	if median == arr[pointer2]:
		recArray = arr[:pointer2]
		if len(recArray) != 1:
			return placeInArray(recArray, i) + arr[pointer2:]
		else:
			return placeInArray(arr[:pointer2+1], i) + arr[pointer2+1:]


# method takes data and outputs a result
def solve(data=None):
	arr=[1,2]
	for i in range(3, data+1):
		arr = placeInArray(arr, i)
	return " ".join([str(i) for i in arr])



# problem mode 0 - single line problem
# problem mode 1 - multi line problem
# problem mode 2 - interactive problem
def problem():
	tnq = input().split()
	test_cases = int(tnq[0])
	arr_size = int(tnq[1])
	queries = int(tnq[2])
	for i in range(test_cases):
		result = None
		while(result == None):
			result = solve(arr_size)
		print(result)
		feedback = input()
		if(feedback == "N" or feedback == "-1"):
			quit()

problem()

