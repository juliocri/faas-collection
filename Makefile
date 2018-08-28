deploy:
	for DIR in ./functions/*; do \
	pushd "$${DIR}" ; \
	make deploy ; \
	popd ; \
	done

delete:
	for DIR in ./functions/*; do \
	pushd "$${DIR}" ; \
	make delete ; \
	popd ; \
	done

update:
	for DIR in ./functions/*; do \
	pushd "$${DIR}" ; \
	make update ; \
	popd ; \
	done
