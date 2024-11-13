class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyCircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.head.next = self.head
            self.head.prev = self.head
        else:
            last = self.head.prev
            last.next = new_node
            new_node.prev = last
            new_node.next = self.head
            self.head.prev = new_node

    def display(self):
        if not self.head:
            print("List is empty")
            return
        temp = self.head
        while True:
            print(temp.data, end=" ")
            temp = temp.next
            if temp == self.head:
                break
        print()

    def prepend(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.head.next = self.head
            self.head.prev = self.head
        else:
            last = self.head.prev
            new_node.next = self.head
            new_node.prev = last
            self.head.prev = new_node
            last.next = new_node
            self.head = new_node

    def delete(self, key):
        if self.head is None:
            print("List is empty")
            return
        curr = self.head
        while True:
            if curr.data == key:
                if curr == self.head and curr.next == self.head:  # Only one node in the list
                    self.head = None
                else:
                    curr.prev.next = curr.next
                    curr.next.prev = curr.prev
                    if curr == self.head:
                        self.head = curr.next
                return
            curr = curr.next
            if curr == self.head:
                print("Node not found")
                break

dll = DoublyCircularLinkedList()
dll.append(10)
dll.append(20)
dll.append(30)
dll.prepend(5)
dll.display()  
dll.delete(20)
dll.display()  
