class Node:

	def __init__(self, value):
		self.value = value
		self.children = []
		self.distance = float("-inf")

	def add_children(self, nodes):
		self.children.extend(nodes)

# parse the text file and represent it as a tree
with open("018_triangle.txt", "r") as f:
	triangle = [[Node(int(num)) for num in line.strip().split()] for line in f.readlines()]

# adds all the children
for i in range(len(triangle)):
	row = triangle[i]
	for j in range(len(row)):
		node = row[j]
		try:
			next_row = i+1
			node.add_children([triangle[next_row][j], triangle[next_row][j+1]])
		except IndexError:
			pass


initial = triangle[0][0]
initial.distance = 0


def update_distance(node):
	for child in node.children:
		if child.distance < child.distance + child.value:
			child.distance = child.distance + child.value
	# for each child update the distance
	# call recursively on each child
	pass
