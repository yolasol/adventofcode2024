from collections import Counter

# get input and make 2 lists
with open("day1_input.txt")as f:
    data = f.readlines()

# part 1
left, right = [], []

for line in data:
    l, r = line.split()
    left.append(int(l))
    right.append(int(r))

# sort both lists and get the difference between each pair
left.sort()
right.sort()

print(f"part one: {sum(abs(l - r) for l,r in zip(left, right))}")

# part 2
count = Counter(right)

# get the sum of multiplying each number from the left list (l)
# by the amount of times it occurs in the right list (count(l))
print(f"part two: {sum(l * count[l] for l in left)}")