HOSTIP := $(shell hostname -I | awk '{print $$1}' )

deploy:
	@sed -i s/'$${HOSTIP}'/$(HOSTIP)/g ./deployment.yaml && sed -i s/'localhost'/$(HOSTIP)/g ./sentiment-mq.py; \
	kubectl apply -f ./deployment.yaml && sleep 60s; \
	kubeless function deploy sentiment-mq --runtime python2.7 \
	--from-file ./sentiment-mq.py --handler kubeless.getSentimentKafka --dependencies ./requirements.txt \
	--env http_proxy=$(http_proxy) --env https_proxy=$(https_proxy) --env no_proxy=$(no_proxy);

delete:
	kubectl delete -f ./deployment.yaml; \
	kubeless function delete sentiment-mq; \
	git checkout .; \

update:
	kubeless function update sentiment --from-file ./sentiment-mq.py --dependencies ./requirements.txt;
