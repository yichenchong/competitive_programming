string =  "66 67 68 69 70 71 72"

strlist = string.split(" ")
intlist = []

for i in strlist:
	intlist.append(int(i))


sumno = 0
lessThanSixtyFive = False
for i in intlist:
	if i <= 65:
		lessThanSixtyFive = True
	sumno += i
average = sumno/len(strlist)


if average <= 65:
	out = 2
elif lessThanSixtyFive:
	out = 1
else:
	out = 0

print(out)