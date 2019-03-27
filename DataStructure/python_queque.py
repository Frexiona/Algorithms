class Queue():

    # Constructor creates a list
    def __init__(self):
        self.queue = list()

    # Add element into the Queue
    def enqueue(self, data):
        self.queue.append(data)

    # Get the element from Queue (FIFO)
    def dequeue(self):
        return self.queue.pop(0)

    # Get the size of Queue
    def getSize(self):
        return len(self.queue)