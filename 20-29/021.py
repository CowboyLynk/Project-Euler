from math import sqrt

div_sums = {}


def get_divisors_sum(n):
	sum = 0
	for i in range(1, int(sqrt(n) + 1)):
		if n % i == 0:
			sum += i
			sum += int(n/i)
	div_sums.setdefault(sum-n, set()).update({n})
	return sum - n

for i in range(1, 10000):
	get_divisors_sum(i)

amicables = set()
for num1 in div_sums:
	for num2 in div_sums[num1]:
		try:
			if num1 in div_sums[num2] and num1 != num2:
				# print(num1, num2)
				amicables.update({num1, num2})
		except KeyError:
			pass

print(sum(amicables))
