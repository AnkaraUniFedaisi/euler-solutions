sum = 0
border = 1000
for i in range(border):
	if (i % 3) == 0 and not (i % 5) == 0:
		sum += i
	elif (i % 5) == 0 and not (i % 3) == 0:
		sum += i
	elif (i % 3) == 0 and (i % 5) == 0:
		sum += i
	else:
		pass

print(sum)
