class Node:
    def __init__(self, value):
        self.value = value

def evaluate_prefix(expression):
    stack = []
    tokens = expression.split()

    # Iterate over the tokens in reverse order
    for token in reversed(tokens):
        if token in '+-*/':

            # Pop two operands from stack
            a = stack.pop()
            b = stack.pop()

            # Perform operation
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(a // b)
        else:
            #Its not an operator, so push the operand to the stack
            stack.append(int(token))

    return stack.pop()

# Testing
expression = "- + 2 * 3 5 8"
print(evaluate_prefix(expression))
