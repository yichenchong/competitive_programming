import math
string = """16
-3 7 1 8
-4 5 8 2
-6 2 0 5
1 -7 2 6
-8 -3 -9 3
-2 9 -8 9
-9 -9 -4 7
6 0 -4 8
-7 -2 3 1
-2 2 2 6
-2 -3 -8 10
4 7 -1 1
5 0 7 2
0 2 5 2
9 6 -7 6
5 -6 -7 5
"""

stringlist = string.split("\n")[1:]

def findDiff(nums):
	if(len(nums)==0):
		return 0
	else:
		maxno = nums[0]
		minno = nums[0]
		for i in nums:
			if i > maxno:
				maxno = i
			if i < minno:
				minno = i
		return maxno - minno

xedgeslist = []
yedgeslist = []
zedgeslist = []

def findedgelength():
	edgelengthlist = []

	for i in range(len(xedgeslist)):
		if i%2 == 0:
			x1 = findDiff(xedgeslist[:i])
			x2 = findDiff(xedgeslist[i:])
			y1 = findDiff(yedgeslist[:i])
			y2 = findDiff(yedgeslist[i:])
			z1 = findDiff(zedgeslist[:i])
			z2 = findDiff(zedgeslist[i:])
			edgelengthlist.append(max(x1,x2,y1,y2,z1,z2))

	edgelengthlist.sort()
	return (edgelengthlist[0])



for i in stringlist:
	if len(i) > 0:
		coordinatesstrlist = i.split(" ")
		x = int(coordinatesstrlist[0])
		y = int(coordinatesstrlist[1])
		z = int(coordinatesstrlist[2])
		r = int(coordinatesstrlist[3])
		x1 = x-r
		x2 = x+r
		y1 = y-r
		y2 = y+r
		z1 = z-r
		z2 = z+r
		for i in range(len(xedgeslist)+1):
			if i%2==0 and (i >= len(xedgeslist) or xedgeslist[i]>x1):
				xedgeslist.insert(i, x2)
				xedgeslist.insert(i, x1)
				yedgeslist.insert(i, y2)
				yedgeslist.insert(i, y1)
				zedgeslist.insert(i, z2)
				zedgeslist.insert(i, z1)
xsort = findedgelength()

xedgeslist = []
yedgeslist = []
zedgeslist = []

for i in stringlist:
	if len(i) > 0:
		coordinatesstrlist = i.split(" ")
		x = int(coordinatesstrlist[0])
		y = int(coordinatesstrlist[1])
		z = int(coordinatesstrlist[2])
		r = int(coordinatesstrlist[3])
		x1 = x-r
		x2 = x+r
		y1 = y-r
		y2 = y+r
		z1 = z-r
		z2 = z+r
		for i in range(len(xedgeslist)+1):
			if i%2==0 and (i >= len(xedgeslist) or yedgeslist[i]>y1):
				xedgeslist.insert(i, x2)
				xedgeslist.insert(i, x1)
				yedgeslist.insert(i, y2)
				yedgeslist.insert(i, y1)
				zedgeslist.insert(i, z2)
				zedgeslist.insert(i, z1)
ysort = findedgelength()

xedgeslist = []
yedgeslist = []
zedgeslist = []

for i in stringlist:
	if len(i) > 0:
		coordinatesstrlist = i.split(" ")
		x = int(coordinatesstrlist[0])
		y = int(coordinatesstrlist[1])
		z = int(coordinatesstrlist[2])
		r = int(coordinatesstrlist[3])
		x1 = x-r
		x2 = x+r
		y1 = y-r
		y2 = y+r
		z1 = z-r
		z2 = z+r
		for i in range(len(xedgeslist)+1):
			if i%2==0 and (i >= len(xedgeslist) or zedgeslist[i]>z1):
				xedgeslist.insert(i, x2)
				xedgeslist.insert(i, x1)
				yedgeslist.insert(i, y2)
				yedgeslist.insert(i, y1)
				zedgeslist.insert(i, z2)
				zedgeslist.insert(i, z1)
zsort = findedgelength()

print(min(xsort,ysort,zsort))

# 27
# 3
# 16
# 295
# 3
# 20
