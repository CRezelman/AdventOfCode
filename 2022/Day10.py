def day10():
	signals = []
	totalCycles = 1
	width = 40
	x = 1
	crt = ''
	opCycles = 0
	with open('2022/day10.txt') as f:
		for line in f:
			line = line.strip('\n')

			if 'noop' in line:
				opCycles = 1
			elif 'addx' in line:
				opCycles = 2

			for cycle in range(opCycles):
				if totalCycles == 20 or not (totalCycles - 20) % width:
					signals.append(x*totalCycles)

				if not (totalCycles - 1) % width:
					crt += '\n'
				if abs(x - ((totalCycles - 1) % width)) < 2:
					crt += '#'
				else:
					crt += '.'

				totalCycles += 1
			
			if 'addx' in line:
				x += int(line.split(' ')[1])
	
	print(sum(signals))

	return crt

print(day10())

