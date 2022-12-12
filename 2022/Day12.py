import sys
from collections import deque

row = [-1, 0, 0, 1]
col = [0, -1, 1, 0]

def day12():
    heightMap = [[0 for i in range(70)] for j in range(41)]
    possibleStarts = []

    with open('2022/inputs/day12.txt') as f:
        for i, line in enumerate(f):
            line = line.strip('\n')
            for j, char in enumerate(line):
                if char == 'a' or char == 'S':
                    possibleStarts.append((i, j))

                if char == 'S':
                    heightMap[i][j] = 1
                    start = (i, j)
                elif char == 'E':
                    heightMap[i][j] = 26
                    end = (i, j)
                else:
                    heightMap[i][j] = ord(char)-96
                    
    return heightMap, start, end, possibleStarts
 
 
def isValid(mat, visited, row, col, i, j):

    return (row >= 0) and (row < len(mat)) and (col >= 0) and (col < len(mat[0])) \
           and (mat[row][col] <= mat[i][j] or (mat[row][col]) == (mat[i][j])+1) and not visited[row][col]
 

def findShortestPathLength(mat, src, dest):
    i, j = src
    x, y = dest

    if not mat or len(mat) == 0 or mat[i][j] == 0 or mat[x][y] == 0:
        return -1
 
    (M, N) = (len(mat), len(mat[0]))
    visited = [[False for x in range(N)] for y in range(M)]
    q = deque()
    visited[i][j] = True
    q.append((i, j, 0))
    min_dist = sys.maxsize

    while q:
        (i, j, dist) = q.popleft()
 
        if i == x and j == y:
            min_dist = dist
            break
 
        for k in range(4):
            if isValid(mat, visited, i + row[k], j + col[k], i, j):
                visited[i + row[k]][j + col[k]] = True
                q.append((i + row[k], j + col[k], dist + 1))
 
    if min_dist != sys.maxsize:
        return min_dist
    else:
        return -1
 
 
if __name__ == '__main__':

    mat, src, dest, possibleStarts = day12()
    dist = []

    min_dist = findShortestPathLength(mat, src, dest)
    if min_dist != -1:
        dist.append(min_dist)
        print("Part 1", min_dist)

    for src in possibleStarts:
        min_dist = findShortestPathLength(mat, src, dest)
        if min_dist != -1:
            dist.append(min_dist)
    
    print("Part 2", min(dist))
 