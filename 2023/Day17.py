from heapq import heappop, heappush

grid = [[int(y) for y in x] for x in open('2023/inputs/day17.txt').read().strip().split('\n')]

DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def inRange(pos, arr):
	return pos[0] in range(len(arr)) and pos[1] in range(len(arr[0]))

def run(mindist, maxdist):
	# cost, x, y, disallowedDirection
	q = [(0, 0, 0, -1)]
	visited = set()
	costs = {}
	while q:
		cost, x, y, dd = heappop(q)
		if x == len(grid) - 1 and y == len(grid[0]) - 1: # goal x, goal y
			return cost
		
		if (x, y, dd) in visited:
			continue
		
		visited.add((x, y, dd))
		
		for direction in range(4):
			costincrease = 0
			
			if direction == dd or (direction + 2) % 4 == dd:
				# can't go this way
				continue
			
			for distance in range(1, maxdist + 1):
				xx = x + DIRS[direction][0] * distance
				yy = y + DIRS[direction][1] * distance
				if inRange((xx, yy), grid):
					costincrease += grid[xx][yy]
					if distance < mindist:
						continue
					nc = cost + costincrease
					if costs.get((xx, yy, direction), 1e100) <= nc:
						continue
					costs[(xx, yy, direction)] = nc
					heappush(q, (nc, xx, yy, direction))



def day17(): 
    part1 = run(1, 3)
    part2 = run(4, 10)

    return part1, part2

print(day17())
