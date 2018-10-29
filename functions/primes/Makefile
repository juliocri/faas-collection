deploy:
	kubeless function deploy primes --runtime go1.10 \
	--from-file ./func.go --dependencies ./Gopkg.toml --handler kubeless.Primes

delete:
	kubeless function delete primes

update:
	kubeless function update primes --from-file ./func.go --dependencies ./Gopkg.toml
