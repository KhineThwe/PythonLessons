numList = [1,2,3,45,44,88,99]
# print(max(numList))
# print(min(numList))

#reverse method
# numList.reverse()
# print('After reversing',numList)

#index method
myIndex = numList.index(99)
print(myIndex)

#sum function
sumAllvalues = sum(numList)
print(sumAllvalues)

#sort
#default ငယ်စဉ်ကြီးလိုက်
numList.sort(reverse = True)
print(numList)
fruitList = ['apple','banana','wahjhjdhddjddjjdjjdjdjdj','orange','watermelon']
fruitList.sort(key = len,reverse = True)
print(fruitList)
