deploy:
	kubeless function deploy test --runtime go1.10 \
	--from-file ./func.go --dependencies ./Gopkg.toml --handler kubeless.Test

delete:
	kubeless function delete test

update:
	kubeless function update test --from-file ./func.go --dependencies ./Gopkg.toml
