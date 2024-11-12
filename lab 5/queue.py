queue=[]

def enqueue(element):
    queue.append(element)
    print(queue)


def dequeue():
    if len(queue)==0:
        return -1
    else:
        return queue.pop(0)

def size():
    return len(queue)


def empty():
    if len(queue)==0:
        return 1
    else:
        return 0


def front():
    if len(queue)==0:
        return -1
    else:
        return queue[0]


enqueue(1)
enqueue(2)
enqueue(3)

print(size())
print(dequeue())
print(dequeue())

print(front())