import heapq

class PriorityQueue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, value, priority):
        self.queue.append((priority, value))
        self.queue.sort()
        print(f"Enqueued {value} with priority {priority}")

    def dequeue(self):
        if not self.queue:
            print("Queue is empty!")
            return None
        
        priority, value = heapq.heappop(self.queue)
        print(f"Dequeued {value} with priority {priority}")
        return value

    def peek(self):
        if not self.queue:
            print("Queue is empty!")
            return None
        priority, value = self.queue[0]
        print(f"Peek: {value} with priority {priority}")
        return value

    def display(self):
        if not self.queue:
            print("Queue is empty!")
        else:
            print("Priority Queue: ", end="")
            print(", ".join(f"{value}({priority})" for priority, value in self.queue))

pq = PriorityQueue()
pq.enqueue("Task1", 3)
pq.enqueue("Task2", 1)
pq.enqueue("Task3", 2)
pq.display()
pq.peek()
pq.dequeue()
pq.display()
pq.dequeue()
pq.display()
