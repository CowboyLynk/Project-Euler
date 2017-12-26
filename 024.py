def get_perms(L, upto=[]):
	if len(L) == 1:
		yield upto + L
	for i in range(len(L)):
		yield from get_perms(L[:i] + L[i+1:], upto + [L[i]])

L = [x for x in range(10)]

num = 0
for i in get_perms(L):
	num += 1
	if num == 1000000:
		print(i)
		break
