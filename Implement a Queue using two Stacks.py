# Simple but efficient way to implement a Queue with 2 stacks []
class Queue2Stack():

    def __init__(self):

        # Two Stacks
        self.instack = []
        self.outstack = []

    def enqueue(self, element):
        self.isntack.append(element)

    def dequeue(self):
        if not self.outstack:
            while self.instack:
                self.outstack.append(self.instack.pop())
        return self.oustack.pop()