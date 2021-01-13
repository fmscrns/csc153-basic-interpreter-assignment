def resolve(_expr, target=0):
    for or_item in _expr.split("|"):
        or_result = True
        for and_item in or_item.split("&"):
            if and_item == "F":
                or_result = False
        if or_result == True:
            return "T"
    return "F"

def simplify(_expr, target=0):
    awaiting_operand = True
    negator_count = 0
    result = ""
    while target < len(_expr):
        if _expr[target] == "T" and awaiting_operand is True:
            awaiting_operand = False
            result += "T" if negator_count % 2 == 0 else "F"
            negator_count = 0
            target += 1
        elif _expr[target] == "F" and awaiting_operand is True:
            awaiting_operand = False
            result += "F" if negator_count % 2 == 0 else "T"
            negator_count = 0
            target += 1
        elif _expr[target] == "&" and awaiting_operand is False and target != len(_expr) - 1:
            awaiting_operand = True
            result += _expr[target]
            target += 1
        elif _expr[target] == "|" and awaiting_operand is False and target != len(_expr) - 1:
            awaiting_operand = True
            result += _expr[target]
            target += 1
        elif _expr[target] == "!" and awaiting_operand is True and target != len(_expr) - 1:
            negator_count += 1
            target += 1
        elif _expr[target] == "(" and awaiting_operand is True and target != len(_expr) - 1:
            awaiting_operand = False
            sub_result = simplify(_expr, target=target+1)
            if isinstance(sub_result, tuple):
                sub_result, target = sub_result
                result += sub_result
            else:
                return sub_result
        elif _expr[target] == ")" and awaiting_operand is False:
            return resolve(result), target + 1
        elif _expr[target] == " ":
            target += 1
        else:
            return "Syntax error. Try again."
    return resolve(result), target + 1

while True:
    _input = input("resolve ")
    if _input[0] == '"' and _input[-1:] == '"':
        result = simplify(_input[1:-1])
        print(result[0]) if isinstance(result, tuple) else print(result)
    else:
        print("Syntax error. Try again.")
        