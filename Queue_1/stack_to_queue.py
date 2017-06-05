from arrayqueue import ArrayQueue


def stack_to_queue(stack):
    queue = ArrayQueue()
    while stack.isEmpty() != True:
        queue.add(stack.pop())
    return queue