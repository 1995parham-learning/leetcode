package main

import "fmt"

var phoneNumber = map[string][]string{
	"2": {"a", "b", "c"},
	"3": {"d", "e", "f"},
	"4": {"g", "h", "i"},
}

var ans = make([]string, 0)

func decodeMessage(msg, code string) {
	if len(code) == 0 {
		return
	}
	firstDigit := code[0]
	for _, letter := range phoneNumber[fmt.Sprintf("%c", firstDigit)] {
		if len(code) == 1 {
			ans = append(ans, msg+letter)

			continue
		}
		decodeMessage(msg+letter, code[1:])
	}
}

func main() {
	decodeMessage("", "2")

	fmt.Println(ans)
}
