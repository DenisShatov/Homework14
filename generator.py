# задача 2
def flat_generator(lst):
    ex_cursor = 0
    in_cursor = 0

    try:
        while ex_cursor < len(lst):
            iterator = iter(lst[ex_cursor])
            while in_cursor < len(lst[ex_cursor]):
                yield next(iterator)
                in_cursor += 1
            ex_cursor += 1
            in_cursor = 0
    except StopIteration:
        pass


# задача 4
def flat_generator2(lst):
    for x in lst:
        if type(x) == list:
            for y in flat_generator2(x):
                yield y
        else:
            yield x


if __name__ == '__main__':
    nested_list = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f'],
        [1, 2, None],
    ]

    nested_list2 = [
        [['a', 'p'], [4, 5, 6], 'c'],
        [['s', 'g', 't'], 'e', 'f'],
        [1, 2, None],
    ]

    for item in flat_generator(nested_list):
        print(item)
    print('_______________________________')

    for item in flat_generator2(nested_list2):
        print(item)
