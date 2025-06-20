import collections.abc
import itertools


def open_lock(deadends: collections.abc.Collection[str], target: str) -> int:
    deadends = set(deadends)

    if "0000" in deadends:
        return -1

    queue: list[tuple[str, int]] = [
        ("0000", 0),
    ]

    seen: set[str] = set()

    while len(queue) > 0:
        current, height = queue.pop(0)

        if current == target:
            return height

        for i, d in itertools.product(range(4), [1, -1]):
            current_list = list(current)
            current_list[i] = str((int(current_list[i]) + d) % 10)
            t = "".join(current_list)

            if t not in seen and t not in deadends:
                seen.add(t)
                queue.append((t, height + 1))

    return -1


if __name__ == "__main__":
    assert (
        open_lock(
            deadends=["0201", "0101", "0102", "1212", "2002"],
            target="0202",
        )
        == 6
    )
    assert (
        open_lock(
            deadends=["8888"],
            target="0009",
        )
        == 1
    )
