def longest_ideal_string(s: str, k: int) -> int:
    d: list[int] = []
    d.append(1)

    for i in range(1, len(s)):
        d.append(1)
        for j in range(i):
            if abs(ord(s[j]) - ord(s[i])) <= k:
                d[i] = max(d[i], d[j] + 1)

    return max(d)


if __name__ == "__main__":
    assert longest_ideal_string(s="acfgbd", k=2) == 4
    assert longest_ideal_string(s="abcd", k=3) == 4
