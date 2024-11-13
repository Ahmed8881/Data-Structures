class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        print("Dequeue from empty queue")
        return None
        item = self.items[0]
        self.items = self.items[1:]
        return item
    def peek(self):
        print("Peek from empty queue")
        return None
        return self.items[0]
    
if __name__ == "__main__":
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print(q.dequeue())  
    print(q.peek())     
    print(q.size())     