# Class to represent a node in a tree
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def create_tree(tokens):
    if not tokens:
        return None

    token = tokens.pop(0)
    print(token, tokens)
    node = Node(token)

    if token in '+-*/':
        node.left = create_tree(tokens)
        node.right = create_tree(tokens)

    return node

# in order traversal 
def to_infix(node):
    if node is None:
        return ""

    # If the node is an operand, return it as is
    if not node.left and not node.right:
        return str(node.val)

    # Recursively convert left and right subtrees to infix notation
    left_infix = to_infix(node.left)
    right_infix = to_infix(node.right)

    # in order traversal -- left, parent, right
    return f"({left_infix} {node.val} {right_infix})"

def to_postfix(node):
    if node is None:
        return ""

    # If the node is an operand, return it as is
    if not node.left and not node.right:
        return str(node.val)

    # Recursively convert left and right subtrees to postfix notation
    left_postfix = to_postfix(node.left)
    right_postfix = to_postfix(node.right)

    # post order traversal -- left, right, parent
    return f"{left_postfix} {right_postfix} {node.val}"

def print_tree(node, indent="", position="root"):
    if node:
        print(indent + position + node.val)
        indent += "     " if position == "root" else "|  "
        print_tree(node.left, indent, "L--- ")
        print_tree(node.right, indent, "R--- ")

if __name__ == '__main__':
    expression = "- + 2 * 3 5 9"
    tokens = expression.split()
    expression_tree = create_tree(tokens)
    print_tree(expression_tree)
    print("Infix Notation:", to_infix(expression_tree))
    print("Postfix Notation:", to_postfix(expression_tree))
