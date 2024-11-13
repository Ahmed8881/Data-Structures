class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            print("pop from empty stack")
        item = self.items[-1]
        self.items = self.items[:-1]
        return item

    def peek(self):
        if self.is_empty():
            print("peek from empty stack")
        return self.items[-1]

    def size(self):
        return len(self.items)

# Example usage:
if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack.pop())  
    print(stack.peek())  
    print(stack.size())  
    print(stack.is_empty())  