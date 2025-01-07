"""Day 4 Solve"""
from utilities.input import read_grid

def find_sprite_count(grid, sprites):
    """Find all occurrences of multiple sprites (subgrids) in a grid"""
    total_count = 0
    rows = len(grid)
    cols = len(grid[0])

    def search_sprite(x, y, sprite):
        """Search for the sprite starting at (x, y)"""
        sprite_rows = len(sprite)
        sprite_cols = len(sprite[0])
        for i in range(sprite_rows):
            for j in range(sprite_cols):
                if sprite[i][j] == '':
                    continue
                if x + j >= cols or y + i >= rows or grid[y + i][x + j] != sprite[i][j]:
                    return False
        return True

    for sprite in sprites:
        sprite_count = 0
        sprite_rows = len(sprite)
        sprite_cols = len(sprite[0])
        for y in range(rows - sprite_rows + 1):
            for x in range(cols - sprite_cols + 1):
                if search_sprite(x, y, sprite):
                    sprite_count += 1
        total_count += sprite_count

    return total_count

def find_word_count(grid, word):
    """Find all occurrences of a word in a grid"""
    count = 0
    rows = len(grid)
    cols = len(grid[0])

    def search_direction(x, y, dx, dy):
        """Search in a direction"""
        for i, _ in enumerate(word):
            if x + i * dx >= rows or y + i * dy >= cols or x + i * dx < 0 or y + i * dy < 0:
                return False
            if grid[y + i * dy][x + i * dx] != word[i]:
                return False
        return True

    for y in range(cols):
        for x in range(rows):
            if grid[y][x] == word[0]:
                for dx, dy in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
                    if search_direction(x, y, dx, dy):
                        count += 1

    return count

def generate_cross_sprites(letters):
    """Generate all possible cross-shaped sprites for the given letters"""
    sprites = []

    cross = [
        [letters[0], '', letters[0]],
        ['', letters[1], ''],
        [letters[2], '', letters[2]]
    ]
    sprites.append(cross)

    for _ in range(3):
        cross = list(zip(*cross[::-1]))
        sprites.append([list(row) for row in cross])

    return sprites


def day4():
    """Day 4""" 
    part1 = 0
    part2 = 0
    data = read_grid(2024, 4)
    target_p1 = 'XMAS'
    target_p2 = generate_cross_sprites('MAS')

    part1 = find_word_count(data, target_p1)
    part2 = find_sprite_count(data, target_p2)


    return part1, part2

print(day4())
