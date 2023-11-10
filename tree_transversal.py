class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def in_order_traversal(node):
    if node:
        in_order_traversal(node.left)
        print(node.value, end=" ")
        in_order_traversal(node.right)


# Create a binary tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

# Perform in-order traversal
in_order_traversal(root)
# Output: 4 2 5 1 3
