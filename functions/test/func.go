package kubeless

import (
	"fmt"
	"github.com/kubeless/kubeless/pkg/functions"
	"github.intel.com/wtd/dbaas/api/logger"
)

// Test returns formated data.
func Test(event functions.Event, context functions.Context) (string, error) {
	logger.Info(logger.Fields{
		"tag": "dbass-kubeless",
	}, "Test function call")
	return fmt.Sprintf("Data: %v", event.Data), nil
}
