class Queue:
    def __init__(self):
        self.nodes = []

    def enqueue(self, node):  # enqueue a tuple
        self.nodes.append(node)

    def dequeue(self):  # dequeue a tuple
        a, *b,  = self.nodes
        self.nodes = []
        for _ in b:
            self.enqueue(_)
        return a

    def isInQueue(self, node):  # tuple is in queue
        if node in self.nodes:
            return True
        else:
            return False

    def isEmpty(self):  # no tuple in the queue
        if len(self.nodes) == 0:
            return True
        else:
            return False

    def showQueue(self):    # show ordered tuple
        for node in self.nodes:
            print(node, end="->")


"""
Q = Queue()
Q.enqueue((0, 0))
Q.enqueue((0, 1))
Q.enqueue((1, 0))
print("dequeue", Q.dequeue())
print("dequeue", Q.dequeue())

Q.enqueue((1, 2))
print("Is in Queue", Q.isInQueue((1, 2)))
print("is Empty", Q.isEmpty())

Q.showQueue()
"""
