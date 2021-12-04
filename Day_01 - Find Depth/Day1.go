package main

import (
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
)

func main() {
	content, err := ioutil.ReadFile("input")
	_ = err
	lines := strings.Split(string(content), "\n")
	acc := 0
	for i := 3; i < len(lines); i++ {
		l_s, err := strconv.Atoi(lines[i])
		_ = err
		r_s, err := strconv.Atoi(lines[i-3])
		_ = err
		if l_s > r_s {
			acc += 1
		}
	}
	fmt.Println(acc)
}
