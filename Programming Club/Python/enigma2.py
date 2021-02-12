string = "take comp sci ib hl"

def replace(character):
	if character == 'z':
		return 'a'
	elif character  == 'Z':
		return 'A'
	elif character not in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
		return character
	else:
		return chr(ord(character)+1)

def replace2(character):
	if character in "aeiou":
		return character.capitalize()
	else:
		return character

output = ""
for i in string:
	x = replace(i)
	x = replace2(x)
	output = output + x

print(output)