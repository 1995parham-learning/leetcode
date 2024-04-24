def tribonacci(n: int) -> int:
    match n:
        case 0:
            return 0
        case 1:
            return 1
        case 2:
            return 1
        case _:
            pass

    index = 3
    # when index % 3 == 0
    a = 0
    # when index % 3 == 1
    b = 1
    # when index % 3 == 2
    c = 1

    while index <= n:
        res = a + b + c
        match index % 3:
            case 0:
                a = res
            case 1:
                b = res
            case 2:
                c = res

        if index == n:
            return res
        index += 1
    raise RuntimeError()


if __name__ == "__main__":
    assert tribonacci(4) == 4
    assert tribonacci(25) == 1389537
