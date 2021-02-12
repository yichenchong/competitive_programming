testCases = [67864, 83145, 97531, 16446, 99999, 25368]

def allEvenFun(num):
	lastDig =  num%10
	even = True

	while num > 0 & even:
		digit = int(num % 10)
		if (digit%2==1):
			even = False
		num = int(num/10)

	return even

def testNum(number):
	allEven = False
	numberPresses = 0
	while not allEven:
		minus = number - numberPresses
		plus = number + numberPresses
		allEven = allEvenFun(minus) or allEvenFun(plus)
		numberPresses += 1

	print(numberPresses - 1)

for i in testCases:
	testNum(i)

# 136
# 257
# 8643
# 3554
# 11111
# 480