#CSPRNG
#Cryptographically strong Pseudo-Random Number Generator
import secrets
print('Printing integer numbers using secrets module')
secureNumber = secrets.SystemRandom()
# randomNumber = secureNumber.randint(0,10)
numer_list = [1,2,3,4,99,777]
# randomNumber = secureNumber.randrange(0,20,4)
randomNumber = secureNumber.sample(numer_list,4)
print('Secure Random Number: ',randomNumber)
