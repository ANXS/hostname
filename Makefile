.PHONY = test testenv lint

ifndef CI
	CI_ENV=$(shell pwd)/.ci-env/bin/
endif

testenv:
	test -z $(CI) && (test -d .ci-env || ( mkdir .ci-env && virtualenv -p python3 .ci-env )) || true
	test -z $(CI) && \
		(echo "Outside CI" && .ci-env/bin/pip install -r requirements.txt --upgrade) || \
		(echo "Within CI" && pip install -r requirements.txt)

test: testenv
	rm -rf molecule/default/roles/ANXS.hostname && mkdir -p molecule/default/roles/ANXS.hostname
	cp -r defaults vars meta tasks molecule/default/roles/ANXS.hostname
	$(CI_ENV)molecule test

lint: testenv
	$(CI_ENV)yamllint tasks/*.yml vars/*.yml defaults/*.yml ; do \

clean:
	$(CI_ENV)molecule destroy
	rm -rf molecule/default/roles/ANXS.hostname
