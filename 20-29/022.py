with open("022_names.txt", "r") as f:
	names = f.read().split("\",\"")
names[0] = names[0][1:]
names[-1] = names[-1][:-1]
names.sort()

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

sum = 0
for i in range(len(names)):
	index = i + 1
	for letter in names[i]:
		sum += index * (alpha.index(letter) + 1)

print(sum)
