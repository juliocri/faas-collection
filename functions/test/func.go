package kubeless

import (
	"fmt"
	"github.com/kubeless/kubeless/pkg/functions"
)

// Test returns formated data.
func Test(event functions.Event, context functions.Context) (string, error) {

	return fmt.Sprintf("Data: %v", event.Data), nil
}
