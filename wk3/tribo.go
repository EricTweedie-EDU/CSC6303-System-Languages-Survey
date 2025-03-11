// Eric Tweedie week 3
// Convert Python to Go
package main

import (
	"fmt"
	"math/big"
)

func main() {
	fmt.Println(tribonacci(200))
}

func tribonacci(n int) []*big.Int {
	if n <= 0 {
		return []*big.Int{}
	} else if n == 1 {
		return []*big.Int{big.NewInt(0)}
	} else if n == 2 {
		return []*big.Int{big.NewInt(0), big.NewInt(1)}
	} else {
		fib_seq := []*big.Int{big.NewInt(1), big.NewInt(1), big.NewInt(1)}
		for i := 3; i < n; i++ {
			next_num := new(big.Int).Add(fib_seq[i-1], fib_seq[i-2])
			next_num.Add(next_num, fib_seq[i-3])
			fib_seq = append(fib_seq, next_num)
		}
		return fib_seq
	}
}
