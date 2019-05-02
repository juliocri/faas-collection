deploy:
	kubeless function deploy sentiment --runtime python2.7 \
	--from-file ./sentiment.py --handler kubeless.getSentiment --dependencies ./requirements.txt

delete:
	kubeless function delete sentiment

update:
	kubeless function update sentiment --from-file ./sentiment.py
