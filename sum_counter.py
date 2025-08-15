#Sum Counter v2
sum = counter = number = 0

while True:
	number = int(input('Enter a number: [999 to stop]:\n'))
	if number == 999:
		break
	sum += number
	counter +=1
print(f'You entered {counter} numbers and the sum was {sum}')