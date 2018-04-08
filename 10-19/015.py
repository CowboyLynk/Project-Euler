import math


def num_paths_brute(size, i=0, j=0):
	if i == size and j == size:
		return 1
	else:
		right, down = 0, 0
		if i < size:
			right = num_paths_brute(size, i+1, j)
		if j < size:
			down = num_paths_brute(size, i, j+1)
		return right + down


def num_paths(size):
	# using bookkeeper principle
	return int(math.factorial(size*2)/(math.factorial(size)**2))


# print(num_paths_brute(20))
print(num_paths(20))
