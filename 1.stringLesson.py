import string
# print("""
#  My Name is %$^##
#
#
#
#  HELOO
# """)

x = "abcABC123456\n"
y = x.isalnum()
z = x.isupper()
l = x.isascii()
f = x.isprintable()
print(y) #True
print(z) #False
print(l)
print(f)

#isalpha()
#isalnum()
#isdecimal()
#lower()
#title()
#islower()
#isupper()
#startsswith()
#endswith()
#replace()
#split()
#strip()
#join()
#find()

name = "ncc"
print(name.upper())

myTuple = ("Khine","NCC","Python")

x = " ".join(myTuple)
print(x)


txt = " banana "
x = txt.strip()
print(x)


txt = "Hello, welcome to my world."

x = txt.find("e")

print(x)
