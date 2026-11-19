"""Safe arithmetic-expression parser and evaluator for x and y."""
import ast
import operator

BINARY_OPERATORS = {
    ast.Add: operator.add, ast.Sub: operator.sub, ast.Mult: operator.mul,
    ast.Div: operator.truediv, ast.Pow: operator.pow, ast.Mod: operator.mod,
}
UNARY_OPERATORS = {ast.UAdd: operator.pos, ast.USub: operator.neg}

class ExpressionError(ValueError):
    pass

def parse_expression(expression):
    try:
        tree = ast.parse(expression, mode="eval")
    except SyntaxError as exc:
        raise ExpressionError("The expression has invalid syntax.") from exc
    for node in ast.walk(tree):
        if isinstance(node, (ast.Expression, ast.Load)):
            continue
        if isinstance(node, ast.Constant):
            if not isinstance(node.value, (int, float)) or isinstance(node.value, bool):
                raise ExpressionError("Only numeric constants are allowed.")
            continue
        if isinstance(node, ast.Name):
            if node.id not in {"x", "y"}:
                raise ExpressionError("Only variables x and y are allowed.")
            continue
        if isinstance(node, ast.BinOp) and type(node.op) in BINARY_OPERATORS:
            continue
        if isinstance(node, ast.UnaryOp) and type(node.op) in UNARY_OPERATORS:
            continue
        if type(node) in tuple(BINARY_OPERATORS) + tuple(UNARY_OPERATORS):
            continue
        raise ExpressionError("Unsupported expression element.")
    return tree

def evaluate_expression(expression, x, y):
    tree = parse_expression(expression)
    def visit(node):
        if isinstance(node, ast.Expression): return visit(node.body)
        if isinstance(node, ast.Constant): return node.value
        if isinstance(node, ast.Name): return {"x": x, "y": y}[node.id]
        if isinstance(node, ast.UnaryOp): return UNARY_OPERATORS[type(node.op)](visit(node.operand))
        if isinstance(node, ast.BinOp):
            left, right = visit(node.left), visit(node.right)
            if isinstance(node.op, ast.Pow) and abs(right) > 10:
                raise ExpressionError("Exponent magnitude is limited to 10.")
            result = BINARY_OPERATORS[type(node.op)](left, right)
            if isinstance(result, complex): raise ExpressionError("Complex results are not supported.")
            return result
        raise ExpressionError("Unsupported expression element.")
    return visit(tree)

def reference_result(expression, x, y):
    # Separate calculation path for the prototype's expected-result oracle.
    tree = parse_expression(expression)
    return eval(compile(tree, "<validated-expression>", "eval"), {"__builtins__": {}}, {"x": x, "y": y})
