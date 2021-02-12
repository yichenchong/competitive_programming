finishedNums = [];
primeList = [];
count = 0
def checkDivisibility(inputNum):
	for i in range(len(finishedNums)):
		finishedNumber = finishedNums[i]
		if(inputNum%finishedNumber==0):
			return True
			break
	return False

for i in range(2,100):
	if (checkDivisibility(i)==False):
		print(i)
		finishedNums.append(i)