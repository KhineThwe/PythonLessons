#Relational Operator

#1.Equals: a == b
#2.Not Equals: a!=b
#3.Less than a<b
#4.Less than or equal to : a<=b
#5.Greater than a>b
#6.Greater than or equal to: a>=b


#Logical op -----> and or

a = 10
b = 20
c = 30
if (a>b) and (a>c):
	largestNumber = a
elif (b>a) and (b>c):
	largestNumber = b
else:
	largestNumber = c

print("Largest Number is ",largestNumber)
