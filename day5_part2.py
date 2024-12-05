# reuse data and functions from part 1
from day5_part1 import page_order, page_numbers, updates, forwards_ordering, backwards_ordering
from day5_part1 import check_correct_order, find_middle_page

# adjusted from check_correct_order
def correct_order(update):
    for i in range(len(update)-1):
        compare = update[i+1:]
        for c in compare:
            try:
                if c in forwards_ordering[update[i]]:
                    continue
                elif c not in forwards_ordering[update[i]]:
                    if c in backwards_ordering[update[i]]:
                        x = i-1
                        if x < 0:
                            x = 0
                        update.remove(c)
                        update.insert(x, c)
                        return update
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
                            x = i - 1
                            if x < 0:
                                x = 0
                            update.remove(c)
                            update.insert(x, c)
                            return update
                        elif cm not in backwards_ordering[update[i]]:
                            continue
                        else:
                            raise AssertionError("this shouldn't be possible either")
                    except KeyError:
                        print("merry merry KeyError!")
                        return
    print("this is correct!")
    return update

def get_incorrect_updates(updates):
    incorrect_updates = []
    for update in updates:
        if not check_correct_order(update):
            incorrect_updates.append(update)
    return incorrect_updates

nope = get_incorrect_updates(updates)

def solve_part2(thing):
    result = 0
    for t in thing:
        print(f"working on {nope.index(t)+1} of {len(nope)}")
        while not check_correct_order(t):
            correct_order(t)
        if check_correct_order(t):
            result += find_middle_page(t)
    return result

print(f"part two: {solve_part2(nope)}")
