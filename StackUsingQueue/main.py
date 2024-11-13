class StackUsingQueue:
    def __init__(self):
        self.q1 = [] 
        self.q2 = []  

    def push(self, x):
        self.q2.append(x)

        while self.q1:
            self.q2.append(self.q1.pop(0))  # Simulate queue by popping from the front

        self.q1, self.q2 = self.q2, self.q1

    def pop(self):
        if not self.q1:
            print("Stack is empty.")
            return None
        return self.q1.pop(0) 

    def top(self):
        if not self.q1:
            print("Stack is empty.")
            return None
        return self.q1[0] 

    def is_empty(self):
        return len(self.q1) == 0

if __name__ == "__main__":
    stack = StackUsingQueue()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    print("Top:", stack.top()) 
    stack.pop()
    print("Top after pop:", stack.top()) 
