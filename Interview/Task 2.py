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
