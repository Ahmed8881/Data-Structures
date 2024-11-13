class CNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = CNode(data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head  # Point to itself
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head  # Make it circular

    def prepend(self, data):
        new_node = CNode(data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head  # Point to itself
        else:
            new_node.next = self.head

            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node

            self.head = new_node

    def delete(self, data):
        if self.head is None:
            return "List is empty."

        current = self.head

        if current.data == data:
            if current.next == self.head:  # Only one node
                self.head = None
            else:
                while current.next != self.head:
                    current = current.next
                current.next = self.head.next  # Update circular reference
                self.head = self.head.next
            return

        prev = None
        while current.next != self.head and current.data != data:
            prev = current
            current = current.next

        if current.data == data:
            prev.next = current.next
        else:
            print("Node not found.")

    def print_list(self):
        if self.head is None:
            print("List is empty.")
            return
        
        current = self.head
        while True:
            print(current.data, end=" -> ")
            current = current.next
            if current == self.head:
                break
        print("(back to head)")

cll = CircularLinkedList()
cll.append(10)
cll.append(20)
cll.append(30)
cll.prepend(5)
cll.print_list() 
cll.delete(20)
cll.print_list()  
