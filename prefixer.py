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

def is_valid(tokens):
    # reversing tokens so we can iterate from operands to operators
    tokens = tokens[::-1]
    stack = []

    for token in tokens:
        # handle operand case
        if token in '+-*/':
            # operator should have at least two operands available
            if len(stack) < 2:
                return False
            
            # pop two operands out, calculate using current operator, then put back into stack
            stack.pop()
            stack.pop()
            stack.append('result')

        else:
            # this case is an operand, simply push to stack
            stack.append(token)

    # after all operations, the result remains in stack
    return len(stack) == 1

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
    return f"({left_infix} {node.val} {right_infix})"

# post order traversal and finding result
def to_postfix(node):
    if node is None:
        return ""

    # if the node is an operand, return it as is
    if not node.left and not node.right:
        return str(node.val), int(node.val)

    # recursively call for left and right subtrees
    left_postfix, left_result = to_postfix(node.left)
    right_postfix, right_result = to_postfix(node.right)

    # post order traversal -- left, right, parent for the subtrees
    expression = f"{left_postfix} {right_postfix} {node.val}"

    # need to calcualte the result
    if node.val == '+':
        result = left_result + right_result
    elif node.val == '-':
        result = left_result - right_result
    elif node.val == '*':
        result = left_result * right_result
    elif node.val == '/':
        result = left_result / right_result

    return expression, result

# function to print the tree
def print_tree(node, indent="", position="root"):
    if node:
        print(indent + position + node.val)
        indent += "    " if position == "root" else "|  "
        print_tree(node.left, indent, "L--- ")
        print_tree(node.right, indent, "R--- ")

if __name__ == '__main__':
    filename = str(input("Enter the filename: "))

    try:
        with open(filename, 'r') as file:
            # replace line breaks with spaces
            expression = file.read().replace('\n', ' ')

        tokens = expression.split()

        if not tokens or not is_valid(tokens):
            print("The file is empty or does not contain a valid expression.")
        else:
            # create expression tree
            expression_tree = create_tree(tokens)
            print_tree(expression_tree)
            print()

            print("Infix Notation:", to_infix(expression_tree))

            postfix_expr, result = to_postfix(expression_tree)
            print("Postfix Notation:", postfix_expr)
            print("Evaluation Result:", result)

    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        
    except Exception as e:
        print(f"An error occurred: {e}")
