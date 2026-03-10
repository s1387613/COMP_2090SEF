class hashed_array_tree:
    def __init__(self, power):
        if power < 0:
            raise ValueError('HAT: invalid size for initialize')
        self.power = power
        self.size = 1 << power
        self.directory = [None] * self.size
        self.count = 0

    def __lookup_index(self, index, power, mask):
        directory_index = index >> power
        leaf_index = index & mask
        return directory_index, leaf_index

    def __resize(self):
        flatten_array = self.flatten()

        self.power += 1
        self.size = 1 << self.power
        self.directory = [None] * self.size
        self.count = 0

        for item in flatten_array:
            self.append(item)

    def append(self, value):
        if self.count == self.size * self.size:
            self.__resize()

        directory_index, leaf_index = self.__lookup_index(self.count, self.power, self.size - 1)

        if self.directory[directory_index] is None:
            self.directory[directory_index] = [None] * self.size

        self.directory[directory_index][leaf_index] = value
        self.count += 1

    def get_value(self, index):
        if index >= self.count or index < 0:
            raise IndexError('HAT: index out of range')

        directory_index, leaf_index = self.__lookup_index(index, self.power, self.size - 1)
        return self.directory[directory_index][leaf_index]

    def flatten(self):
        flat = []
        for dir in self.directory:
            if dir is not None:
                for item in dir:
                    if item is not None:
                        flat.append(item)
        return flat

if __name__ == '__main__':
    # size per sub_array -> 2 ** 2 = 4
    # full size -> 4 * 4 = 16
    arr = hashed_array_tree(2)
    print(f'Capacity: {arr.size * arr.size} | Power: {arr.power} | Item count: {arr.count}')

    for i in range(0, 100):
        arr.append(i)

    print(f'Capacity: {arr.size * arr.size} | Power: {arr.power} | Item count: {arr.count}')

    # expected output: 5
    print(arr.get_value(5))

    print(*arr.flatten())
