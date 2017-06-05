from arraystack import ArrayStack


def queue_to_stack(queue):
    stack = ArrayStack()
    while queue.isEmpty() != True:
        stack.push(queue.pop())
    return stack
