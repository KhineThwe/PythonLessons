ls = [1,2,3,4,5]

data = 3
found = False
index = 0

while index < len(ls):
	if ls[index] == data:
		found = True
		break
	index+=1

if not found:
	ls.append(data)

if found:
	print("We found data")

print(ls)
