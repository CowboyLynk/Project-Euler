with open("11_grid.txt", "r") as f:
	grid = [[int(num) for num in line.strip().split(" ")] for line in f.readlines()]


def find_product():
	directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, -1), (-1, 1)]

	def gen_line_coordinates(coord, direction):  # generates a 4-element set of coordinants in a line
		x, y = coord
		x_inc, y_inc = direction
		coordinates = set()
		for i in range(4):
			new_x = x + x_inc*i
			new_y = y + y_inc*i
			if 0 <= new_x < len(grid[0]) and 0 <= new_y < len(grid) :
				coordinates.add((new_x, new_y))
			else:
				raise IndexError
		return coordinates

	def get_all_lines():
		for y in range(len(grid)):
			for x in range(len(grid[0])):
				for direction in directions:
					try:
						yield gen_line_coordinates((x, y), direction)
					except IndexError:
						continue

	largest = 0

	for line in get_all_lines():
		product = 1
		for coord in line:
			x, y = coord
			product *= grid[y][x]
		if product > largest:
			largest = product

	return largest

print(find_product())
