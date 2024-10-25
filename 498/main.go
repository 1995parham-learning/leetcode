package main

import (
	"fmt"
	"slices"
)

func findDiagonalOrder(mat [][]int) []int {
	arr := mat
	M := len(arr)
	N := len(arr[0])

	res := []int{arr[0][0]}

	i := 0
	j := 0
	direction := -1

	for i < M-1 || j < N-1 {
		if (j < N-1 && i == 0 && direction == -1) || (i == M-1 && direction == 1) {
			j++
			direction *= -1

		} else if (j == 0 && direction == 1) || (j == N-1 && direction == -1) {
			i++
			direction *= -1

		} else {
			j -= direction
			i += direction
		}
		res = append(res, arr[i][j])
	}

	return res
}

func main() {
	cases := []struct {
		input  [][]int
		output []int
	}{
		{
			input:  [][]int{{1, 2, 3}, {4, 5, 6}, {7, 8, 9}},
			output: []int{1, 2, 4, 7, 5, 3, 6, 8, 9},
		},
	}

	for _, c := range cases {
		if !slices.Equal(c.output, findDiagonalOrder(c.input)) {
			fmt.Printf("Expect %v but found %v\n", c.output, findDiagonalOrder(c.input))
		}
	}
}
