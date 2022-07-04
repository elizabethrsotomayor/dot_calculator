def calculator(txt: str) -> str:
    """
    Write a calculator that receives strings for input. The dots will represent the number in the equation. There
    will be dots on one side, an operator, and dots again after the operator.
    :param txt:
    :return:
    """
    i = txt.split(" ")
    ops = {"+": (lambda x, y: x + y), "-": (lambda x, y: x - y), "*": (lambda x, y: x * y), "//": (lambda x, y: x // y)}
    result = ops[i[1]](len(i[0]), len(i[-1]))

    ans = ''

    for j in range(0, result):
        ans += '.'

    return ans
