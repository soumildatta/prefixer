# class to represent a node in a tree
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# functin to create a tree from a list of tokens
def create_tree(tokens):
    if not tokens:
        return None

    token = tokens.pop(0)
    # print(token, tokens)
    node = Node(token)

    if token in '+-*/':
        node.left = create_tree(tokens)
        node.right = create_tree(tokens)

    return node

# in order traversal 
def to_infix(node):
    if node is None:
        return ""

    # return the node if it is an operand/leaf
    if not node.left and not node.right:
        # print(node.val)
        return str(node.val)

    # recursively call for left and right subtrees
    left_infix = to_infix(node.left)
    # print(left_infix)
    right_infix = to_infix(node.right)

    # in order traversal -- left, parent, right for the subtrees
    return f"{left_infix} {node.val} {right_infix}"

# post order traversal
def to_postfix(node):
    if node is None:
        return ""

    # If the node is an operand, return it as is
    if not node.left and not node.right:
        return str(node.val)

    # recursively call for left and right subtrees
    left_postfix = to_postfix(node.left)
    right_postfix = to_postfix(node.right)

    # post order traversal -- left, right, parent for the subtrees
    return f"{left_postfix} {right_postfix} {node.val}"

# function to get the result of the expression

# function to print the tree
def print_tree(node, indent="", position="root"):
    if node:
        print(indent + position + node.val)
        indent += "     " if position == "root" else "|  "
        print_tree(node.left, indent, "L--- ")
        print_tree(node.right, indent, "R--- ")

if __name__ == '__main__':
    # read the expression from a file
    filename = str(input("Enter the filename: "))
    with open(filename, 'r') as file:
        expression = file.read()

    tokens = expression.split()
    expression_tree = create_tree(tokens)
    # print_tree(expression_tree)
    print("Infix Notation:", to_infix(expression_tree))
    print("Postfix Notation:", to_postfix(expression_tree))
