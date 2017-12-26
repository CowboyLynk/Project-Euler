from math import sqrt

abundants = set()


def get_divisors_sum(n):
	sum = 0
	for i in range(1, int(sqrt(n) + 1)):
		if n % i == 0:
			sum += i
			div = int(n/i)
			if div != i:
				sum += int(n/i)
	sum -= n
	if sum > n:
		abundants.add(n)
	return sum - n

for i in range(30):
	get_divisors_sum(i)

print(abundants)
