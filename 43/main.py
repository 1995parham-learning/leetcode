import itertools


def add(num1: str, num2: str) -> str:
    res = ""
    addition = 0

    for i, j in itertools.zip_longest(reversed(num1), reversed(num2), fillvalue="0"):
        d = int(i) + int(j) + addition
        res = str(d % 10) + res
        addition = d // 10

    if addition != 0:
        res = str(addition) + res

    res = res.lstrip("0")
    if res == "":
        res = "0"

    return res


def multiply_digit(num: str, d: str) -> str:
    assert len(d) == 1

    res = ""
    addition = 0

    for i in reversed(num):
        _d = int(i) * int(d) + addition
        res = str(_d % 10) + res
        addition = _d // 10

    if addition != 0:
        res = str(addition) + res

    res = res.lstrip("0")
    if res == "":
        res = "0"

    return res


def multiply(num1: str, num2: str) -> str:
    res = ""

    for i, d in enumerate(reversed(num2)):
        res = add(res, multiply_digit(num1 + ("0" * i), d))

    res = res.lstrip("0")
    if res == "":
        res = "0"

    return res


if __name__ == "__main__":
    assert add("2", "3") == "5"
    assert add("123", "456") == "579"
    assert add("1", "456") == "457"

    assert multiply_digit("3", "2") == "6"
    assert multiply_digit("123", "2") == "246"
    assert multiply_digit("9", "9") == "81"

    assert multiply("123", "456") == "56088"
    assert multiply("9", "9") == "81"
