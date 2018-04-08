def fib(last=1, s_last=0):
	counter = 1
	new = last + s_last
	while len(str(new)) < 1000:
		new = last + s_last
		s_last = last
		last = new
		counter += 1
	return counter

print(fib())
