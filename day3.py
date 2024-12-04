import re

# get the data
with open("day3_input.txt") as f:
    data = f.read()

# part 1
# find the pattern 'mul(x, y)', using capturing groups for easy multiplication
def solve_part_one(thing: str):
    multiply = re.findall(r"mul\((\d*),(\d*)\)", thing)

    return sum((int(a) * int(b) for a,b in multiply))

print(f"part one: {solve_part_one(data)}")

# part 2
def solve_part_two(thing: str):
    # for some reason re.findall cannot handle CRLF in the input
    # I feel like '|$' or '|[\r\n]' in the pattern should fix this but somehow it doesn't
    no_crnl = re.sub(r"[\r\n]", '', thing)
    pattern = re.findall(r"do\(\)(.*?)(?=don\'t\(\))", "do()" + no_crnl)
    return solve_part_one(''.join(pattern))

print(f"part two: {solve_part_two(data)}")
