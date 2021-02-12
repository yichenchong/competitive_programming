string = "IF#U^GET\\\THIS PROBLEM RIGHT YOU GET 6 KUAI"

import re

string = string.replace("(", " ")
string = string.replace("*", " ")
string = string.replace("\\", " ")
strList = re.split("""&|!| |1|2|3|4|5|6|7|8|9|0|#|\"|!|,|%|^""", string)

maxLen = ""

for i in strList:
	if len(i) > len(maxLen):
		maxLen = i

print(maxLen)