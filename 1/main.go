package main

import (
	"log"
	"slices"
)

func twoSum(nums []int, target int) []int {
	for i := range len(nums) {
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
		cal := twoSum(c.nums, c.target)

		if !slices.Equal(
			cal,
			c.output,
		) {
			log.Fatalf("%v is not equal to expected value %v", cal, c.output)
		}
	}
}
