class FormulaError(Exception):
    def __init__(self):
        super()


input_val = input("Enter expression ")
items = input_val.split(" ")
# print(items)
try:
    exp_len = len(items)
    if exp_len != 3:
        raise FormulaError

except FormulaError:
    print("Invalid expression")


def cal(val1, val2, operation):
    switcher = {
        "+": val1 + val2,
        "-": val1 - val2,
    }
    return switcher.get(operation)


try:
    num1 = float(items[0])
    num2 = float(items[2])
    operator = items[1]
    # print(num1)
    # print(num2)
    # print(operator)
    res = cal(num1, num2, operator)
    print("expression result is  :- ", res)
except ValueError as e:
    print(e)
