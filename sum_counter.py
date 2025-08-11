#Sum Counter

sum = 0
counter = 0

number = int(input('Enter a number: [999 to stop]:\n'))

while number != 999:
	sum = sum + number
	counter += 1
	number = int(input('Enter a number: [999 to stop]\n'))
	
print(f'You entered {counter} numbers and the sum of them was {sum}!')