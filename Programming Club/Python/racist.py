num = 17

lastDig =  num%10
even = (lastDig%2==0)
racist = True

while num > 0 & racist == False:
	digit = int(num % 10)
	if ((digit%2==0) != even):
		racist = False
	num = int(num/10)

if racist:
	print("Racist")
else:
	print("SJW")