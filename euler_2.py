def fibonacci():
	even_sum = 0
	first_number, second_number = 1, 1
	while second_number <= 4000000:
		first_number, second_number = second_number, first_number + second_number
		if first_number % 2 == 0:
			even_sum += first_number
	return even_sum

print(fibonacci())
