castle = [1, 2, 2, 1, 3, 5, 5, 3, 4, 4]
rows = []
cols = []
for i  in range(len(castle)):
	if i%2 == 0:
		rows.append(castle[i])
	else:
		cols.append(castle[i])

rows = list(set(rows))
cols = list(set(cols))


if len(rows)!=5 or len(cols)!= 5:
	print("Threat")
else:
	print("No threat")
