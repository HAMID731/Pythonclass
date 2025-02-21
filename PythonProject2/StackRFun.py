class StackRFun:
    def __init__(self):
        self.elements = [None] * 10
        self.stack_size = 0

    def is_empty(self):
        return self.stack_size == 0

    def is_not_empty(self):
        return self.stack_size != 0

    def add(self, element):
        if self.stack_size < len(self.elements):
            self.elements[self.stack_size] = element
            self.stack_size += 1

    def peek(self):
        if self.stack_size == 0:
            raise IndexError("Stack is empty")
        return self.elements[self.stack_size - 1]

    def push(self, element):
        if self.stack_size == len(self.elements):
            raise IndexError("Stack is full")
        self.elements[self.stack_size] = element
        self.stack_size += 1