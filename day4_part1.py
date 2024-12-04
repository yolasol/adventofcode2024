# get the data
with open("day4_input.txt") as f:
    data = f.readlines()

# turn the input into a dictionary of coordinate:letter
# assuming the crossword is actually square
wordsearch = {(x,y):data[x][y] for y in range(len(data)) for x in range(len(data))}

# find all the starting positions
def find_x(thing: dict):
    x = []
    for coordinate in thing:
        if thing.get(coordinate) == "X":
            x.append(coordinate)
    return x

def look_around(coordinates: list, direction: str):
    # this sucks but my brain cell is tired
    if direction == "right":
        d = [(0,1), (0,2), (0,3)]
    elif direction == "left":
        d = [(0,-1), (0,-2), (0,-3)]
    elif direction == "up":
        d = [(-1,0), (-2,0), (-3,0)]
    elif direction == "down":
        d = [(1,0), (2,0), (3,0)]
    elif direction == "up right":
        d = [(-1,1), (-2,2), (-3,3)]
    elif direction == "down right":
        d = [(1,1), (2,2), (3,3)]
    elif direction == "up left":
        d = [(-1,-1), (-2,-2), (-3,-3)]
    elif direction == "down left":
        d = [(1,-1), (2,-2), (3,-3)]
    else:
        print("I am not a biblically accurate angel, where do you want me to look?")
        return

    potential = []
    for coordinate in coordinates:
        check = []
        for c in d:
            check.append(tuple(map(sum, zip(coordinate, c)))) # you could check range if you wanted to
        potential.append(check)
    return potential

def find_xmas(thing, coordinates):
    xmas = 0
    for coordinate in coordinates:
        word = ''
        for c in coordinate:
            try:
                word += thing.get(c)
            except TypeError:
                continue
        if word == "MAS":
            xmas += 1
    return xmas

def solve_part1():
    start = find_x(wordsearch)
    directions = ["up", "down", "left", "right", "up left", "up right", "down left", "down right"]
    return sum(find_xmas(wordsearch, look_around(start, direction)) for direction in directions)

print(f"part one: {solve_part1()}")
