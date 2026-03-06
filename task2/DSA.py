class hashed_array_tree:
    def __init__(self, size: int):
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

    def insert(self):
        pass

    def delete(self):
        pass

    def push(self):
        pass

    def pop(self):
        pass

    def traverse(self):
        pass

if __name__ == '__main__':
    arr = hashed_array_tree(4)
    position = [0, 1, 2, 3]
    elements = [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4]]
    arr.build(position, elements)
