class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = TreeNode(data)
        else:
            self._insert(self.root, data)

    def _insert(self, node, data):
        if data < node.data:  # Insert in the left subtree
            if node.left is None:
                node.left = TreeNode(data)
            else:
                self._insert(node.left, data)
        else:  # Insert in the right subtree
            if node.right is None:
                node.right = TreeNode(data)
            else:
                self._insert(node.right, data)

    def in_order_traversal(self, node):
        if node:
            self.in_order_traversal(node.left)
            print(node.data, end=" ")
            self.in_order_traversal(node.right)

    def pre_order_traversal(self, node):
        if node:
            print(node.data, end=" ")
            self.pre_order_traversal(node.left)
            self.pre_order_traversal(node.right)

    def post_order_traversal(self, node):
        if node:
            self.post_order_traversal(node.left)
            self.post_order_traversal(node.right)
            print(node.data, end=" ")

    def level_order_traversal(self):
        if self.root is None:
            return
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            print(node.data, end=" ")
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    def search(self, data):
        return self._search(self.root, data)

    def _search(self, node, data):
        if node is None or node.data == data:
            return node
        if data < node.data:
            return self._search(node.left, data)
        return self._search(node.right, data)

bt = BinaryTree()
bt.insert(10)
bt.insert(20)
bt.insert(5)
bt.insert(15)
bt.insert(30)

print("In-order Traversal:")
bt.in_order_traversal(bt.root)  

print("\nPre-order Traversal:")
bt.pre_order_traversal(bt.root)  

print("\nPost-order Traversal:")
bt.post_order_traversal(bt.root)  

print("\nLevel-order Traversal:")
bt.level_order_traversal()  

node = bt.search(15)
if node:
    print(f"\nNode with value {node.data} found.")
else:
    print("\nNode not found.")
