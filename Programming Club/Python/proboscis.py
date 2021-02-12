string = """1000 5
64 -8388608 -65536 -1 524288
968 204 936 999 872
"""

yourSpeed = int(string.split("\n")[0].split(" ")[0])

class Monkey:
	def __init__(self, position, speed):
		self.position = float(position)
		self.speed = float(speed)
	def posAtTime(self, time, yourPosition):
		if yourPosition == self.position:
			return self.position
		if yourPosition < self.position:
			return float(self.position + float(self.speed * time))
		else:
			return float(self.position - float(self.speed * time))
	def updatePosition(self, time, yourPosition):
		self.position = self.posAtTime(time, yourPosition)
	def posFromYou(self, yourPosition):
		return yourPosition - self.position
	def distanceFromYou(self, yourPosition):
		return abs(yourPosition - self.position)
	def timeFromYou(self, yourPosition):
		return self.distanceFromYou(yourPosition)/(yourSpeed-self.speed)
	def catch(self, yourPosition):
		time = self.timeFromYou(yourPosition)
		return (time, self.posAtTime(time, yourPosition))

def copy(monkey):
	nm = Monkey(monkey.position, monkey.speed)
	return nm
def copyList(ml):
	nl = []
	for i in ml:
		nl.append(copy(i))
	return nl

posstring = string.split("\n")[1]
poslist = posstring.split(" ")
speedstring = string.split("\n")[2]
speedlist = speedstring.split(" ")

monkeyList = []
for i in range(len(poslist)):
	newMonkey = Monkey(float(poslist[i]), float(speedlist[i]))
	monkeyList.append(newMonkey)

def chase(monkeyList, position):
	if len(monkeyList) == 0:
		return 0
	if len(monkeyList) == 1:
		catchResult = monkeyList[0].catch(position)
		return catchResult[0]
	minimum = 2000000000
	for i in range(len(monkeyList)):
		monkey = monkeyList[i]
		newList = copyList(monkeyList)
		newList.remove(newList[i])
		catchResult = monkey.catch(position)
		catchTime = catchResult[0]
		catchPos = catchResult[1]

		for j in newList:
			j.updatePosition(catchTime, position)

		timeToFinish = chase(newList, catchPos) + catchTime
		if timeToFinish < minimum:
			minimum = timeToFinish
	return minimum

print(chase(monkeyList, 0))


# 128881.05614805521
# 129205.28522012579
# 129042.96702261307
# 129042.96702261307

