import sys
import math

class hashed_array_tree:
    def __init__(self, size: int):
        if size <= 0:
            print('The size cannot be smaller or equal to 0')
            sys.exit(1)
        elif pow(2, int(math.log2(size))) is not size:
            print('The size must be a power of 2')
            sys.exit(1)
        else:
            self.size = size
            self.top = [None] * size
            for i in range(0, size):
                self.top[i] = [None] * size

    def build(self, position: list, elements: list):
        position_count = len(position)
        elements_count = len(elements)
        if position_count > self.size or elements_count > self.size:
            print('amount of sub-array exceed the size limit')
            return
        else:
            index = 0
            for sub_arr in elements:
                self.top[index] = sub_arr
                index += 1
        return

    def lookup(self, lookup_position: int) -> int:
        mask = self.size - 1
        directory_index = lookup_position >> int(math.log2(self.size))
        print(f'directory: {directory_index}')
        leaf_index = lookup_position & (self.size - 1)
        print(f'leaf: {leaf_index}')
        return self.top[directory_index][leaf_index]

    def insert(self):
        pass

    def delete(self):
        pass

    def push(self):
        pass

    def pop(self):
        pass

    def resize(self):
        pass

    def traverse(self):
        pass

if __name__ == '__main__':
    arr = hashed_array_tree(4)
    position = [0, 1, 2, 3]
    elements = [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4]]
    arr.build(position, elements)
    print(arr.lookup(5))
