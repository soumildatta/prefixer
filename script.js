class Node {
    constructor(value) {
        this.value = value;
        this.left = null;
        this.right = null;
    }
}

function isOperator(value) {
    return ['+', '-', '*', '/'].includes(value);
}

function createTree(tokens) {
    if (tokens.length === 0) {
        return null;
    }

    let token = tokens.shift();
    let node = new Node(token);

    if (isOperator(token)) {
        node.left = createTree(tokens);
        node.right = createTree(tokens);
    }

    return node;
}

function toInfix(node) {
    if (node === null) {
        return '';
    }

    if (!isOperator(node.value)) {
        return node.value;
    }

    return `(${toInfix(node.left)} ${node.value} ${toInfix(node.right)})`;
}

function toPostfix(node) {
    if (node === null) {
        return '';
    }

    return `${toPostfix(node.left)} ${toPostfix(node.right)} ${node.value}`;
}

function evaluate(node) {
    if (node === null) {
        return 0;
    }

    if (!isOperator(node.value)) {
        return parseFloat(node.value);
    }

    let left = evaluate(node.left);
    let right = evaluate(node.right);

    switch (node.value) {
        case '+': return left + right;
        case '-': return left - right;
        case '*': return left * right;
        case '/': return left / right;
    }
}

document.getElementById('expressionForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const prefixExpression = document.getElementById('prefixInput').value;
    const tokens = prefixExpression.split(' ');

    const tree = createTree([...tokens]);
    const infix = toInfix(tree);
    const postfix = toPostfix(tree);
    const result = evaluate(tree);

    document.getElementById('infixResult').textContent = `Infix: ${infix}`;
    document.getElementById('postfixResult').textContent = `Postfix: ${postfix}`;
    document.getElementById('evaluationResult').textContent = `Result: ${result}`;
});
