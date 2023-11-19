package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

var (
	pc_1 = [][]uint{
		{57, 49, 41, 33, 25, 17,  9},
		{ 1, 58, 50, 42, 34, 26, 18},
		{10,  2, 59, 51, 43, 35, 27},
		{19, 11,  3, 60, 52, 44, 36},
		{63, 55, 47, 39, 31, 23, 15},
		{ 7, 62, 54, 46, 38, 30, 22},
		{14,  6, 61, 53, 45, 37, 29},
		{21, 13,  5, 28, 20, 12,  4},
	}
)

func handle_input() (key string) {
	for {
		fmt.Print("Key := ")
		scanner := bufio.NewScanner(os.Stdin)
		for scanner.Scan() {
			if key = scanner.Text(); strings.TrimSpace(key) != "" {
				return key 
			}
		}
		fmt.Println()
	}
}

func hex_to_bin(key_hex string, length int) (string) {
	var key_bin string

	format := "%0"+strconv.Itoa(length)+"b"

	for _, char := range key_hex {
		integer, err := strconv.ParseUint(string(char), 16, 64)
		if err != nil {
			panic(err)
		}
		key_bin += fmt.Sprintf(format, integer)
	}

	return key_bin
}

func print_key(key_bin string, length int) {
	for i := 0; i < len(key_bin); i+=length {
		fmt.Printf("%s ", key_bin[i:i+length])
	}
	fmt.Println()
}

func calc_key_plus(key_bin string) (string) {
	k_plus_bin := ""
	for i := 0; i < len(pc_1); i++ {
		for j := 0; j < len(pc_1[i]); j++ { 
			k_plus_bin += string(key_bin[pc_1[i][j]-1])
		}
	}
	return k_plus_bin
}

func main() {
	key_hex := handle_input()

	// For testing: 
	// key_hex := "133457799BBCDFF1"

	key_bin := hex_to_bin(key_hex, 4)
	fmt.Print("K = ")
	print_key(key_bin, 8)

	key_plus_bin := calc_key_plus(key_bin)
	fmt.Print("K+ = ")
	print_key(key_plus_bin, 7)
}