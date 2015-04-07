#khan academy
def insertion_sort(list_of_num):
	for index in range(1, len(list_of_num)):
		#iterate over elements at index 1 until the last element

		value = list_of_num[index]
		#set calue to current element

		i = index - 1
		while i >= 0:# until we reach the first element .
			if value < list_of_num[i]:
				list_of_num [i + 1] = list_of_num[i]
				list_of_num[i] = value
				i = i - 1
			else:
				break		

a = [7, 1, 3, 5, 9, 2, 3]
insertion_sort(a)
print a 