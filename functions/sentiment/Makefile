deploy:
	kubeless function deploy sentiment --runtime python2.7 \
	--from-file ./sentiment.py --handler kubeless.getSentiment --dependencies ./requirements.txt \
	--env http_proxy=$(http_proxy) --env https_proxy=$(https_proxy) --env no_proxy=$(no_proxy)

delete:
	kubeless function delete sentiment

update:
	kubeless function update sentiment --from-file ./sentiment.py
