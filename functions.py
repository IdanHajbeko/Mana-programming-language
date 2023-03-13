import math

variables = {}


def parse_line(line):
    if line.startswith("//"):  # ignore comments
        return

    if "write " in line:
        if "{" and "}" in line or "num[" and "]" in line:
            print(evaluate_expression(line[6:]))
        else:
            print(line[6:])
        return

    if "input " in line:
        var_name, prompt = line.split("input ")[1].split(", ")
        value = input(prompt)
        set_variable(var_name.strip(), value)
        return

    if "=" in line:
        var_name, expression = line.split("=", 1)
        set_variable(var_name.strip(), evaluate_expression(expression))
        return
    else:
        evaluate_expression(line.strip())


def set_variable(name, value):
    global variables
    variables[name] = value


def evaluate_expression(expression):
    while "{" in expression and "}" in expression:
        var_name = expression[expression.index("{") + 1: expression.index("}")]
        var_value = variables.get(var_name)
        if var_value is None:
            raise ValueError(f"Undefined variable: {var_name}")
        expression = expression.replace("{" + var_name + "}", str(var_value))

    if expression.startswith("num[") and expression.endswith("]"):
        return eval(expression[4:-1])

    try:
        return int(expression)
    except ValueError:
        pass

    try:
        return float(expression)
    except ValueError:
        pass

    return expression.strip()
