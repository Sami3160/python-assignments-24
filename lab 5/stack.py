stack=[]
max=10
top = 0
def push(num):
    global top
    stack.append(num)
    top+=1
def pop():
    global top
    if top==0 :
        return -1
    else:
        top=top-1
        return stack.pop()

def size():
    global top
    return top


def empty():
    global top
    if top==0:
        return 1
    else:
        return 0

def peek():
    global top
    if top==0:
        return -1
    else:
        return stack[top-1]

def display():
    for i in stack:
        print(i, end=',')



max=int(input("enter stack size :"))
push(1)
push(2)
push(3)
print(pop())
print(pop())
print(pop())
print(empty())
print(peek())