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


def check_balance(string_):
    balansed = True
    stack = Stack()
    for i in string_:
        if i in '({[':
            stack.push(i)
        else:
            if not stack.isEmpty():
                balansed = False
                break
            elif stack.peek() == '(' and i == ')':
                stack.pop()
                continue
            elif stack.peek() == '{' and i == '}':
                stack.pop()
                continue
            elif stack.peek() == '[' and i == ']':
                stack.pop()
                continue
            else:
                balansed = False
                break
    if balansed == True:
        return 'Сбалансировано'
    else:
        return 'Не сбалансировано'


if __name__ == '__main__':
    print(check_balance('[([])((([[[]]])))]{()}]'))
