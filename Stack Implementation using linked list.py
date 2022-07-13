class Node:
    def __init__(Self, Data=None, next=None):
        Self.Data = Data
        Self.next = next


class Stack:

    def __init__(Self):
        Self.top = None


    def push(Self, Data):
        if Self.top is None:
            Self.top = Node(Data, None)
            return
        Self.top = Node(Data, Self.top)


    def pop(Self):
        if Self.top is None:
            return
        temp = Self.top
        if Self.top is not None:
            Self.top = Self.top.next
        temp.next = None
        return temp.Data

    def peek(Self):
        return Self.top.Data


    def clear_stack(Self):
        Self.top = None


    def empty_stack(Self):
        if Self.top is None:
            return True
        return False


    def display(Self):
        ITR = Self.top
        sstr = ' '
        while ITR:
            sstr += str(ITR.Data) + '-->'
            ITR = ITR.next
        print(sstr)


if __name__ == "__main__":
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(40)
    stack.peek()
    stack.display()
    stack.pop()
    stack.push(30)
    stack.display()
    stack.clear_stack()
    stack.display()




