# get the data
with open("day4_input.txt") as f:
    data = f.readlines()

# turn the input into a dictionary of coordinate:letter
# assuming the crossword is actually square
wordsearch = {(x,y):data[x][y] for y in range(len(data)) for x in range(len(data))}

# find all the starting positions
def find_a(thing: dict):
    a = []
    for coordinate in thing:
        if thing.get(coordinate) == "A":
            a.append(coordinate)
    return a

def look_around(coordinates: list):
    directions = [(-1, -1), (-1,1), (1,-1), (1,1)] # up left, up right, down left, down right
    potential = []
    for coordinate in coordinates:
        check = []
        for d in directions:
            check.append(tuple(map(sum, zip(coordinate, d)))) # you could check range if you wanted to
        potential.append(check)
    return potential

def find_x_mas(thing, coordinates):
    x_mas = 0
    correct = ["MMSS", "MSMS", "SMSM", "SSMM"]
    # up left, up right, down left, down right
    # this has to be in violation of the Geneva convention, the Helsinki declaration, and several others
    for coordinate in coordinates:
        print(coordinate)
        word = ''
        for c in coordinate:
            try:
                word += thing.get(c)
            except TypeError:
                continue
        print(word)
        if word in correct:
            x_mas += 1
    return x_mas

def solve_part2():
    start = find_a(wordsearch)
    return find_x_mas(wordsearch, look_around(start))

print(f"part two: {solve_part2()}")