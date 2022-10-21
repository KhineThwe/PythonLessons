#3.Bitwise Not or One's complement
#(eg:1s complement ka convert lote 1 ကို 0)
#~sign
#~a = -(a+1)
#a = 10
#~a = 11

#Decimal value of 10
#1 0 1 0
#      1
#-------------
# 1  0  1 1
#-11
a = ~10
print("bitwise not or one's complement",a)


#2's complement
#Decimal value of 10 = 1010
#1st step convert 0--->1,1--->0
#2nd step 1+
#1 0 1 0
#1st step(convert)
#0 1 0 1
#      1
#---------------
# 0 1 0 0
# 8 4  2 1


