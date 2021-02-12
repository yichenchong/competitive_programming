array = ["1234547", "1001100", "378730", "2233443", "15", "347473"]

def get_all_substrings(input_string):
  length = len(input_string)
  return [input_string[i:j+1] for i in range(length) for j in range(i,length)]

def isPalindrome(string):
	return string[::-1]==string

def testString(uinput):
	substrings = get_all_substrings(uinput)
	palindromicsubs = []
	for i in substrings:
		if isPalindrome(str(int(i))):
			palindromicsubs.append(int(i))

	palindromicsubs.sort()
	print(palindromicsubs[-1])


for i in array:
 	testString(i)


# 454
# 1001
# 37873
# 3443
# 5
# 747