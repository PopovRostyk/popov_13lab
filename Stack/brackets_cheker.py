from arraystack import ArrayStack


def brackets_checker(string):
    stack = ArrayStack()
    for items in string:
        if items == '(':
            stack.push('(')
    if not stack.isEmpty():
        for items in string:
            if items == ')':
                stack.pop()
    if not stack.isEmpty():
        return 'Bad brackets'
    else:
        return 'ok brackets'

print(brackets_checker('(())()'))

def polyndrom(string):
    stack = ArrayStack(string[:int(len(string)/2)])
    if len(string) % 2:
        stack = ArrayStack(string[:int(len(string) / 2)])
        lst = list([items for items in string[int(len(string)/2 + 1):]]);lst.reverse()
        lst2 = list(stack)
        for i in range(len(lst)):
            if lst[i] == lst2[i]:
                stack.pop()
    else:
        print('norm')
    return stack.isEmpty()


print(polyndrom('13344321'))