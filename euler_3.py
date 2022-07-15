import math

def get_factors(number):
	l = list()
	n = math.sqrt(number)
	for i in range(1, int(n)):
		if number % i == 0:
			l.append(i)
		else: pass
	return l

k = get_factors(600851475143)
print(k)

def p(array):
	l = list()
	for number in array:	
		for i in range(2, number):
			if number % i == 0:
				break
		else: l.append(number)
	return l		

print(p(k))
print(max(p(k)))
