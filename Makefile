build:
	docker-compose build --force-rm --pull -q

run: build
	docker-compose up

tests:
	pipenv run pytest

clean:
	docker-compose rm -f || true
	docker rmi thesheriff/thesheriff || true

.PHONY: build dockerup tests clean