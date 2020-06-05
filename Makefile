BLACK_OPTIONS=--line-length 120 --target-version py38

.PHONY: lint
lint:
	docker-compose run --rm web black ${BLACK_OPTIONS} --check .

.PHONY: format
format:
	docker-compose run --rm web black ${BLACK_OPTIONS} .