deploy:
	kubeless function deploy primes --runtime go1.10 \
	--from-file ./func.go --dependencies ./Gopkg.toml --handler kubeless.Primes \
	--env HTTP_PROXY=${http_proxy} --env HTTPS_PROXY=${https_proxy} --env NO_PROXY=${no_proxy}

delete:
	kubeless function delete primes

update:
	kubeless function update primes --from-file ./func.go --dependencies ./Gopkg.toml
