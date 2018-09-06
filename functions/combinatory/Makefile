deploy:
	kubeless function deploy combinatory --runtime python2.7 \
	--from-file ./combinatory.py --handler kubeless.combinatory

delete:
	kubeless function delete combinatory

update:
	kubeless function update combinatory --from-file ./combinatory.py
