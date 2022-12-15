def day14(part):
    sand = 0
    depth = 159
    width = 1000
    cave = [['.' for i in range(width)] for j in range(depth+1)]
    offset = 490
    
    for q in range(width):
        cave[depth][q] = '#'
    
    with open('2022/inputs/day14.txt') as f:
        for line in f:
            coords = line.strip('\n').split(' -> ')
            for i, coord in enumerate(coords):
                if i == (len(coords)-1):
                    break
                coords1 = coords[i:i+2]
                x1, y1 = coords1[0].split(',')
                x2, y2 = coords1[1].split(',')
                minX = min(x1, x2)
                maxX = max(x1, x2)
                minY = min(y1, y2)
                maxY = max(y1, y2)
                for x in range((int(minX)-offset), (int(maxX)-offset)+1):
                    for y in range(int(minY), int(maxY)+1):
                        cave[int(y)][int(x)] = '#'
                   
    cave[0][500-offset] = '+'

    abyss = 0

    while abyss == 0:
        i = 500-offset
        for n in range(depth):
            match part:
                case 1:
                    if n == (depth-1):
                        abyss = 1
                        break
                case 2:
                    if cave[0][500-offset] == 'o':
                        abyss = 1
                        break

            if cave[n+1][i] == '#' or cave[n+1][i] == 'o':
                if cave[n+1][i-1] == '.':
                    i -= 1                   
                elif cave[n+1][i+1] == '.':
                    i += 1
                else:
                    cave[n][i] = 'o'
                    sand += 1
                    break                
        
    return sand

print(day14(1))
print(day14(2))