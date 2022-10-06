print("Press 1: For Add")
print("Press 2: For Subtract")
print("Press 3: For Multiply")
print("Press 4: For Divide")

choice = int(input("Please enter option: "))

firstNo = int(input("Please enter first number: "))

secondNo = int(input("Please enter second number: "))

if choice == 1:
	totalNumber = firstNo + secondNo
elif choice == 2:
	totalNumber = firstNo - secondNo
elif choice == 3:
	totalNumber = firstNo * secondNo
elif choice == 4:
	totalNumber = firstNo / secondNo #%
else:
	print("You must enter 1/2/3/4: ")

print(f'The number of {firstNo} {choice} {secondNo} {totalNumber}')
