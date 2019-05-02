deploy:
	kubeless function deploy primes --runtime go1.10 \
	--from-file ./func.go --dependencies ./Gopkg.toml --handler kubeless.Primes \
	--env http_proxy=$(http_proxy) --env https_proxy=$(https_proxy) --env no_proxy=$(no_proxy)

delete:
	kubeless function delete primes

update:
	kubeless function update primes --from-file ./func.go --dependencies ./Gopkg.toml
