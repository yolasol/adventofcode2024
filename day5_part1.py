# get the input
with open("day5_input.txt") as f:
    data = f.read().split("\n\n")

# split the data into page ordering rules and page numbers
page_order = data[0].split("\n")
page_numbers = data[1].split("\n")

# part 1
# turn the page ordering instructions into 2 dictionaries (both directions)
# page number: list of numbers that must be printed after it
forwards_ordering = {}
for pair in page_order:
    if pair[0:2] in forwards_ordering:
        existing = forwards_ordering[pair[0:2]]
        forwards_ordering.update({pair[0:2]:existing + " " + pair[3:5]})
    elif pair[0:2] not in forwards_ordering:
        forwards_ordering[pair[0:2]] = pair[3:5]

# and page number: list of numbers that it must be printed after
backwards_ordering = {}
for pair in page_order:
    if pair[3:5] in backwards_ordering:
        existing = backwards_ordering[pair[3:5]]
        backwards_ordering.update({pair[3:5]:existing + " " + pair[0:2]})
    elif pair[3:5] not in backwards_ordering:
        backwards_ordering[pair[3:5]] = pair[0:2]

# turn the values into a list because that will be MUCH easier
# should probably have done this sooner but meh
for key, value in forwards_ordering.items():
    forwards_ordering.update({key:value.split()})
for key, value in backwards_ordering.items():
    backwards_ordering.update({key:value.split()})

# turn each update into a list as well for easier parsing
updates = []
for update in page_numbers:
    new = update.split(",")
    if len(new) > 1:
        updates.append(new)

# find the correctly-ordered updates
# for each update: for each page: check if it comes before each next page
def check_correct_order(update: list):
    for i in range(len(update)-1):
        compare = update[i+1:]
        for c in compare:
            try:
                if c in forwards_ordering[update[i]]:
                    continue
                elif c not in forwards_ordering[update[i]]:
                    if c in backwards_ordering[update[i]]:
                        return False
                    elif c not in backwards_ordering[update[i]]:
                        raise AssertionError("are you sure this is possible?")
                    else:
                        raise AssertionError("het gaat niet goed")
            except KeyError:
                # try backwards ordering for all following numbers
                j = update.index(update[i])
                compare_more = update[j+1:]
                for cm in compare_more:
                    try:
                        if cm in backwards_ordering[update[i]]:
                            return False
                        elif cm not in backwards_ordering[update[i]]:
                            continue
                        else:
                            raise AssertionError("this shouldn't be possible either")
                    except KeyError:
                        print("merry merry KeyError!")
                        continue # this should be safe
    return True

# find the middle page numbers of the correctly-ordered updates
# assuming there are only uneven amounts of pages
def find_middle_page(update: list):
    middle = len(update) // 2
    return int(update[middle])

# and get the sum
def solve_part1(thing):
    result = 0
    for t in thing:
        if check_correct_order(t):
            result += find_middle_page(t)
    return result

print(f"part one: {solve_part1(updates)}")
