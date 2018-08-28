deploy:
	kubeless function deploy test --runtime go1.10 \
	--from-file ./func.go --dependencies ./Gopkg.toml --handler kubeless.Test \
	--env HTTP_PROXY=${http_proxy} --env HTTPS_PROXY=${https_proxy} --env NO_PROXY=${no_proxy}

delete:
	kubeless function delete test

update:
	kubeless function update test --from-file ./func.go --dependencies ./Gopkg.toml
