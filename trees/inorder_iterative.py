# Python program for iterative postorder traversal
# using one stack

# Stores the answer
ans = []

# A Binary tree node
class Node:
    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def inOrderIterative(root):
    # Check for empty tree
    if root is None:
        return
    def visit(x,S):
        while x:
            S.append(x)
            x = x.left

    stack = []
    while(True):
        visit(root, stack)
        if not stack:
            break
        root = stack.pop(-1)
        ans.append(root.data)
        root = root.right

# Driver pogram to test above function
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print("In Order traversal of binary tree is")
inOrderIterative(root)
print(ans)
