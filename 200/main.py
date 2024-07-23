class Solution:
    def get_lands(self, grid: list[list[str]]) -> set[tuple[int, int]]:
        lands = set()
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    lands.add((row, col))

        return lands

    def get_neighbour(self, root: tuple[int, int], lands: set[tuple[int, int]]) -> None:
        if (root[0] - 1, root[1]) in lands:
            lands.remove((root[0] - 1, root[1]))
            self.get_neighbour((root[0] - 1, root[1]), lands)
        if (root[0] + 1, root[1]) in lands:
            lands.remove((root[0] + 1, root[1]))
            self.get_neighbour((root[0] + 1, root[1]), lands)
        if (root[0], root[1] - 1) in lands:
            lands.remove((root[0], root[1] - 1))
            self.get_neighbour((root[0], root[1] - 1), lands)
        if (root[0], root[1] + 1) in lands:
            lands.remove((root[0], root[1] + 1))
            self.get_neighbour((root[0], root[1] + 1), lands)

    def num_islands(self, grid: list[list[str]]) -> int:
        lands = self.get_lands(grid)
        if len(lands) == 0:
            return 0

        num_island = 0
        while len(lands) > 0:
            land = lands.pop()
            # lands.remove(land)
            self.get_neighbour(land, lands)
            num_island = num_island + 1

        return num_island


if __name__ == "__main__":
    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"],
    ]
    assert Solution().num_islands(grid) == 1
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"],
    ]
    assert Solution().num_islands(grid) == 3
