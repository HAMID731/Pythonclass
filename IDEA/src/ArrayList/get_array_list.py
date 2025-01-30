class ArrayList:
    def __init__(self):
        self.size = 0
        self.capacity = self.size
        self.data = [None] * self.capacity

    def add(self, value):
        self.data[self.size] = value
        self.size += 1

    def remove(self, index):
        for i in range(index, self.size - 1):
            self.data[i] = self.data[i + 1]
        self.size -= 1

    def __str__(self):
        return str(self.data)


