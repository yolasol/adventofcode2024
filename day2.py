# get input as list of lists of numbers
with open("day2_input.txt") as f:
    data = [list(map(int, line.split())) for line in f.readlines()]

# part 1
# check if levels are increasing or decreasing
def consistent(report: list):
    decreasing = False
    increasing = False
    for l1, l2 in zip(report, report[1:]):
        diff = l1 - l2
        if diff < 0:
            decreasing = True
        if diff > 0:
            increasing = True
        if increasing and decreasing:
            return False
    return True

# check if adjacent levels differ by at least 1 and at most 3
# this is slightly redundant, maybe clean up later
def gradual(report:list):
    for l1, l2 in zip(report, report[1:]):
        if abs(l1 - l2) < 1 or abs(l1 - l2) > 3:
            return False
    return True

# combine both functions
def is_it_safe(report: list):
    if consistent(report) and gradual(report):
        return True
    return False

result = [is_it_safe(report) for report in data]
print(f"part one: {result.count(True)}")

# part 2
def can_it_be_safe(report: list):
    for i in range(len(report)):
        # try all possible reports leaving one number out
        dampener = report[:i] + report[i+1:]
        if is_it_safe(dampener):
            return True
    return False

result = [can_it_be_safe(report) for report in data]
print(f"part two: {result.count(True)}")

