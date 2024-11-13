class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def is_empty(self):
        return self.head is None
    def insert_at_head(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    def insert_at_tail(self, data):
        if self.is_empty():
            self.head = Node(data)
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = Node(data)
    def delete_at_head(self):
        if self.is_empty():
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        return temp.data
    def delete_at_tail(self):
        if self.is_empty():
            return None
        if self.head.next is None:
            temp = self.head
            self.head = None
            return temp.data
        temp = self.head
        while temp.next.next:
            temp = temp.next
        data = temp.next.data
        temp.next = None
        return data
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()
        
if __name__ == "__main__":
    linkedlist=LinkedList()
    linkedlist.insert_at_head(1)
    linkedlist.insert_at_head(2)
    linkedlist.insert_at_head(3)
    linkedlist.insert_at_tail(4)
    linkedlist.print_list()
    linkedlist.delete_at_head()
    linkedlist.print_list()
    linkedlist.delete_at_tail()
    linkedlist.print_list()
  
    