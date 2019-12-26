build:
	docker-compose build --force-rm --pull -q

clean:
	docker-compose rm -f app || true
	docker rmi thesheriff/thesheriff || true

run: clean build
	docker-compose up

lint:
	pipenv run pycodestyle thesheriff tests

tests:
	pipenv run pytest

purge:
	docker-compose rm -f || true
	docker rmi thesheriff/thesheriff || true

.PHONY: build clean lint purge run tests