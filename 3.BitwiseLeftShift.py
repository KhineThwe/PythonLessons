#Bitwise Left Shift <<
#value increase
x  = 20
y = x << 4
print('Afer left shift',y)


#Decimal value of 10 =====>  1 0 1 0
#After Left Shift ====>    1 0 1 0 0 0
#                         32 16 8  4 2 1

#Decimal value of 20 =======> 1 0 1 0 0
#After Left Shift ====> 1 0 1 0 0 0 0 0 0

#python မှာ int data type 4bytes = 32 bits


#Decimal Value of 20 = 10100
#0000 0000 0000 0000 0000 0000 0000 0000   = 32 bits
#0000 0000 0000 0000 0000 0000 0001 0100
#After left shift 0000
#0000 0000 0000 0000 0000 0001 0100 0000
