class Node:
    def __init__(self, value):
        self.value = value

def is_valid_prefix(expression):
    def is_operator(c):
        return c in '+-*/'

    def is_operand(c):
        return c.isdigit() or c.isalpha()
    
    tokens = expression.split()

    if not tokens or not is_operator(tokens[0]):
        return False

    operand_count = 0

    for token in reversed(tokens):
        if is_operand(token):
            operand_count += 1
        elif is_operator(token):
            if operand_count < 2:
                return False
            operand_count -= 1 

    return operand_count == 1

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

if __name__ == '__main__':
    expression = input('Enter prefix expression: ')

    print(evaluate_prefix(expression))
