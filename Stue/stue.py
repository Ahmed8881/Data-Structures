class Stue:
    def __init__(self):
        self.s1 = []
        self.s2 = []
       

    def push(self, x):
        self.s1.append(x)

    def enqueue(self, x):
        self.s1.append(x)

    def pop(self):
        if not self.s1:
            print("Stack is empty.")
            return None
        return self.s1.pop()

    def dequeue(self):
        if not self.s1 and not self.s2:
            print("Queue is empty.")
            return None
        
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())

        return self.s2.pop()

    def peek_stack(self):
        if not self.s1:
            print("Stack is empty.")
            return None
        return self.s1[-1]

    def peek_queue(self):
        if not self.s1 and not self.s2:
            print("Queue is empty.")
            return None
        
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())

        return self.s2[-1]

    def is_empty(self):
        return not self.s1 and not self.s2

stue = Stue()
stue.push(10)   
stue.push(20)   
print("Stack Top:", stue.peek_stack())  
stue.pop()      
print("Stack Top after pop:", stue.peek_stack())  # Output: 10

stue.enqueue(30)  
stue.enqueue(40)  
print("Queue Front:", stue.peek_queue())  
stue.dequeue()    
print("Queue Front after dequeue:", stue.peek_queue())  # Output: 30
