package main

import (
	"log"
	"slices"
	"testing/quick"
)

func twoSum(nums []int, target int) []int {
	for i := 0; i < len(nums); i++ {
		for j := i + 1; j < len(nums); j++ {
			if nums[i]+nums[j] == target {
				return []int{i, j}
			}
		}
	}
	return nil
}

func main() {
	for _, c := range []struct {
		target int
		nums   []int
		output []int
	}{
		{
			target: 9,
			nums:   []int{2, 7, 11, 15},
			output: []int{0, 1},
		},
		{
			target: 6,
			nums:   []int{3, 2, 4},
			output: []int{1, 2},
		},
		{
			target: 6,
			nums:   []int{3, 3},
			output: []int{0, 1},
		},
	} {
		if err := quick.Check(func() bool {
			return slices.Equal(
				twoSum(c.nums, c.target),
				c.output,
			)
		}, nil); err != nil {
			log.Fatal(err)
		}
	}
}
