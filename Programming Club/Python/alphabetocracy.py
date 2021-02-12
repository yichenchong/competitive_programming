string = """2
QEIPWMUOXRKLDFYSLFYSLGNXRKJABLVTHZTHIJUVDZOPQEGMNAWB
QYSCEGMNOPDUVWXABTHIJZFLYSCEGMNOPDUVWXABTHIJZFQRRKKL
"""


stringlist = string.split("\n")[1:]
stringlist.sort()

uniqueList = []

for i in stringlist:
	wordSet = set(list(i))
	length = 0
	for j in wordSet:
		if j in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
			length += 1
	uniqueList.append(length)

index = 0
maxLength = 0
for i in range(len(uniqueList)):
	if uniqueList[i] > maxLength:
		maxLength = uniqueList[i]
		index = i

print(stringlist[index])

# AAAA, KYLE LIANG, SMITH BAKER, JOHN QUINCY ADAMS, QRKLYSCEGMNOPDUVWXABTHIJZF, QYSCEGMNOPDUVWXABTHIJZFLYSCEGMNOPDUVWXABTHIJZFQRRKKL