# implementation of a Stack class using a list

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    # pushes an item onto the end of the list using append()
    def push(self, item):
        self.items.append(item)

    # pops the last item off the end of the list
    def pop(self):
        return self.items.pop()

    # returns the last item off the end of the list but doesn't modify the list
    def peek(self):
        return self.items[len(self.items) - 1]
    
    def size(self):
        return len(self.items)


# implementation of a Queue class using a list

class Queue:
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []
    
    # inserts an item at the "front" of the list
    def enqueue(self, item):
        self.items.insert(0, item)
    
    # pops the last item off the end of the list
    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)
