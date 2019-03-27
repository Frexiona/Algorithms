class Stack():

    # Constructor creates a list
    def __init__(self):
        self.stack = list()

    # Add element into the Stack
    def enqueue(self, data):
        self.stack.append(data)

    # Get the element from Stack (LIFO)
    def dequeue(self):
        return self.stack.pop()

    # Get the size of Stack
    def getSize(self):
        return len(self.stack)