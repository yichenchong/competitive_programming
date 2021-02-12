groups = [9999, 10, 9999, 2, 9999, 55, 222, 333, 99, 111]

totalWealth = 0
for i in groups:
	totalWealth += i

groups.sort()
bottomsix = groups[:6]
proleWealth = 0
for i in bottomsix:
	proleWealth += i

if proleWealth < 0.1 * totalWealth:
	print("Marxist")
else:
	print("Chill")


# Chill, Marxist, Marxist, Chill, Chill, Marxist