def checkio(list_of_numbers, num):
	length = len(list_of_numbers)
	minimum = 1
	maximum = length
	guess = list_of_numbers[(minimum + maximum)/2]
	
	while list_of_numbers[guess] != num
	if list_of_numbers[guess] == num:
		return guess
	elif list_of_numbers[guess] < num:
		minimum = guess + 1
	else maximum = guess - 1



