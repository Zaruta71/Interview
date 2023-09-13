class Stack:
    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return self.stack or False

    def push(self, _item):
        self.stack.append(_item)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        if self.isEmpty():
            return self.stack[-1]

    def size(self):
        return len(self.stack)

