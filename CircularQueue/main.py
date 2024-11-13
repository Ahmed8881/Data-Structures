class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = self.rear = -1

    def enqueue(self, value):
        if (self.rear + 1) % self.size == self.front:
            print("Queue is full!")
            return
        if self.front == -1:
            self.front = 0        
        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = value
        print(f"Enqueued {value}")

    def dequeue(self):
        if self.front == -1:
            print("Queue is empty!")
            return None
        value = self.queue[self.front]
        self.queue[self.front] = None
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
        
        print(f"Dequeued {value}")
        return value

    # Display the queue
    def display(self):
        if self.front == -1:
            print("Queue is empty!")
        else:
            print("Circular Queue: ", end="")
            if self.rear >= self.front:
                print(" ".join(str(x) for x in self.queue[self.front:self.rear + 1]))
            else:
                print(" ".join(str(x) for x in self.queue[self.front:self.size]), end=" ")
                print(" ".join(str(x) for x in self.queue[0:self.rear + 1]))

# Example usage
cq = CircularQueue(5)
cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)
cq.enqueue(40)
cq.display()
cq.dequeue()
cq.display()
cq.enqueue(50)
cq.enqueue(60)
cq.display()
cq.enqueue(70)  # This will show "Queue is full"
