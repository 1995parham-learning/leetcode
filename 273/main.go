package main

import (
	"fmt"
	"log"
	"slices"
	"strings"
	"testing/quick"
)

func main() {
	for _, c := range []struct {
		target string
		nums   int
	}{
		{
			nums:   123,
			target: "One Hundred Twenty Three",
		},
		{
			nums:   12345,
			target: "Twelve Thousand Three Hundred Forty Five",
		},
		{
			nums:   1234567,
			target: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven",
		},
	} {
		if err := quick.Check(func() bool {
			return numberToWords(c.nums) == c.target
		}, nil); err != nil {
			log.Fatal(err)
		}
	}
}

var digitToString = map[int]string{
	1: "One",
	2: "Two",
	3: "Three",
	4: "Four",
	5: "Five",
	6: "Six",
	7: "Seven",
	8: "Eight",
	9: "Nine",
}

var twodigitToString = map[int]string{
	10: "Ten",
	11: "Eleven",
	12: "Twelve",
	13: "Thirteen",
	14: "Fourteen",
	15: "Fifteen",
	16: "Sixteen",
	17: "Seventeen",
	18: "Eighteen",
	19: "Nineteen",

	2: "Twenty",
	3: "Thirty",
	4: "Forty",
	5: "Fifty",
	6: "Sixty",
	7: "Seventy",
	8: "Eighty",
	9: "Ninety",
}

var placesToString = map[int]string{
	0: "",
	1: " Thousand",
	2: " Million",
	3: " Billion",
}

func numberToWords(num int) string {
	if num == 0 {
		return "Zero"
	}

	ds := digits(num)
	buckets := len(ds) / 3
	remain := len(ds) % 3
	if remain > 0 {
		buckets += 1
	}

	result := new(strings.Builder)

	for i := buckets - 1; i >= 0; i-- {
		var pd string
		if remain > 0 {
			pd = printDigit(ds[:remain])
			ds = ds[remain:]
			remain = 0
		} else {
			pd = printDigit(ds[:3])
			ds = ds[3:]
		}
		if len(pd) > 0 {
			if result.Len() > 0 {
				fmt.Fprintf(result, " %s", pd)
			} else {
				fmt.Fprintf(result, "%s", pd)
			}
			fmt.Fprint(result, placesToString[i])
		}
	}

	return result.String()
}

func printDigit(ds []int) string {
	slices.Reverse(ds)

	result := new(strings.Builder)

	if len(ds) > 2 && ds[2] != 0 {
		fmt.Fprintf(result, "%s Hundred", digitToString[ds[2]])
	}

	if len(ds) > 1 && ds[1] != 0 {
		if result.Len() > 0 {
			fmt.Fprint(result, " ")
		}

		if ds[1] == 1 {
			fmt.Fprintf(result, "%s", twodigitToString[10+ds[0]])

			return result.String()
		} else {
			fmt.Fprintf(result, "%s", twodigitToString[ds[1]])
		}
	}

	if ds[0] != 0 {
		if result.Len() > 0 {
			fmt.Fprint(result, " ")
		}

		fmt.Fprintf(result, "%s", digitToString[ds[0]])
	}

	return result.String()
}

func digits(n int) []int {
	result := make([]int, 0)

	for n/10 != 0 {
		result = append(result, n%10)
		n = n / 10
	}
	result = append(result, n%10)

	slices.Reverse(result)

	return result
}
