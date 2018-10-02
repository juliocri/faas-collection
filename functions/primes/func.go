package kubeless

import (
	"encoding/json"
	"fmt"
	"github.com/kubeless/kubeless/pkg/functions"
	"sync"
)

// Primes returns a json string with all primes number found,
// in a range of 1 to 9999.
func Primes(event functions.Event, context functions.Context) (string, error) {
	primes := make(map[int]bool)

	var wg sync.WaitGroup

	for i := 0; i <= 9999; i++ {
		wg.Add(1)
		// Go rutine:
		func(n int) {

			if n <= 1 {
				primes[n] = false
				wg.Done()
				return
			}

			for j := 2; j < n; j++ {
				if (n % j) == 0 {
					primes[n] = false
					wg.Done()
					return
				}
			}

			primes[n] = true
			wg.Done()
			return
		}(i)
	}

	// Wait for all gorutines to finish.
	wg.Wait()
	jsonOutput, _ := json.Marshal(primes)
	return string(jsonOutput), nil
}
