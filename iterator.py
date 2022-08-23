# задача 1
class FlatIterator:

    def __init__(self, lst):
        self.lst = lst
        self.ex_cursor = 0
        self.in_cursor = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.ex_cursor < len(self.lst):
            if self.in_cursor < len(self.lst[self.ex_cursor]):
                res = self.lst[self.ex_cursor][self.in_cursor]
                self.in_cursor += 1
                return res
            self.ex_cursor += 1
            self.in_cursor = 0
        raise StopIteration


# задача 3
class FlatIterator2:

    def __init__(self, lst):
        self.lst = self.flattenlist(lst)
        self.ex_cursor = 0
        self.in_cursor = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.ex_cursor < len(self.lst):
            if self.in_cursor < len(self.lst[self.ex_cursor]):
                res = self.lst[self.ex_cursor][self.in_cursor]
                self.in_cursor += 1
                return res
            self.ex_cursor += 1
            self.in_cursor = 0
        raise StopIteration

    def flattenlist(self, flst):
        queue = []
        for lst_item in flst:
            if type(lst_item) == list:
                for i in lst_item:
                    queue.append(i)
            else:
                queue.append(lst_item)
        return queue


if __name__ == '__main__':
    nested_list = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None],
    ]

    nested_list2 = [
        ['a', [9, 4, False], 'c'],
        [['d', 'y'], 'e', 'f', 'h'],
    ]

    for item in FlatIterator(nested_list):
        print(item)

    flat_list = [item for item in FlatIterator(nested_list)]
    print(f'\n\n{flat_list}')

    for item in FlatIterator2(nested_list2):
        print(item)
