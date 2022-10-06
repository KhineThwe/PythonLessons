#random
#random.random() return floating point 0.0 and 1.0
#randint
#randrange

import random
random_no = random.random()
print("Random no is : ",random_no)


#for randint -> return int no ----> randint(lower,upper)
random_no1 = random.randint(4,10)
print("Random no from randint is : ",random_no1)


#for randrange -> return int no ----> randrange(start,stop,step)
random_no2 = random.randrange(0,20,4)
print("Random no from randrange is : ",random_no2)

#For random.choice
name = ['susu','aungaung','kaykay','soesoe']
print("Selected element is(random.choice): ",random.choice(name))

#For random.sample
name = ['susu','aungaung','kaykay','soesoe']
print("Selected element is(random.sample): ",random.sample(name,2))

#For random.shuffle
name1 = ['susu','aungaung','kaykay','soesoe','khine','zar']
print("Before shuffle",name1)
random.shuffle(name1)
print("After shuffle",name1)

#For random.seed()
random.seed(10)
print("Random no from seed() ",random.random())



#for random.uniform -> return floating no ----> random.uniform(lower,upper)
random_no1 = random.uniform(4.5,10.6)
print("Random no from uniform is : ",random_no1)


#for random.triangular -> return floating no ----> random.triangular(low,high,mode)
random_no2 = random.triangular(10.5,20.5,2.5)
print("Random no from triangular is : ",random_no2)
