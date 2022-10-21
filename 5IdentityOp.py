#Identity op =====> (is,is not===> memory location တွေကိုစစ်ချင်တဲ့အခါသုံး)

a = 10
b =10
print(id(a))
print(id(b))

if a is not b:
	print("They are same location")
else:
	print("They are not same location")
	
string1 = "hello"
string2 = "hello"
print(id(string1),id(string2))
if string1 is string2:
	print("Same")
