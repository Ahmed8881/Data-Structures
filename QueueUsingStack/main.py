class QueueUsingStack:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def enqueue(self, x):
        self.s1.append(x)

    def dequeue(self):
        if not self.s1 and not self.s2:
            print("Queue is empty.")
            return None

        # If s2 is empty, transfer all elements from s1 to s2
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())

        return self.s2.pop()

    def front(self):
        if not self.s1 and not self.s2:
            print("Queue is empty.")
            return None

        # If s2 is empty, move elements from s1 to s2
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())

        return self.s2[-1]

    def is_empty(self):
        return not self.s1 and not self.s2

queue = QueueUsingStack()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
print("Front:", queue.front())  
queue.dequeue()
print("Front after dequeue:", queue.front())  
