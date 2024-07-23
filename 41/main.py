def first_missing_positive(numbers: list[int]):
    numbers_set = set(numbers)  # O(n)

    current = 1
    while True:  # O(n)
        if current not in numbers_set:
            return current
        current += 1


if __name__ == "__main__":
    assert first_missing_positive([1, 3, 6, 4, 1, 2]) == 5
    assert first_missing_positive([3, 4, -1, 1]) == 2
    assert first_missing_positive([7, 8, 9, 11, 12]) == 1
