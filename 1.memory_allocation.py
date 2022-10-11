#Memory allocation
#stack memory      heap memory
#  function          10
#int a = 10
#variables are memory references.
#a => 0x10002 => 10
a = 10
b = 10
print(id(a))
print(hex(a))
print(id(b))
print(hex(b))
if id(a) == id(b):
	print("They are same memory address!")
else:
	print("They are not same memory address!")
