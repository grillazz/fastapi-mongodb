.PHONY: help
help: ## Show this help
	@egrep -h '\s##\s' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

.PHONY: build
build:	## Build project with compose
	docker-compose build

.PHONY: up
up:	## Run project with compose
	docker-compose up

.PHONY: down
down: ## Reset project containers with compose
	docker-compose down -v --remove-orphans

.PHONY: test
test:	## Run project tests
	docker-compose run --rm web pytest -vv

.PHONY: test-snapshot
test-snapshot:	## Run project tests
	docker-compose run --rm web pytest -vv --inline-snapshot=create

.PHONY: mypy
mypy:	## mypy check.
	mypy --ignore-missing-imports .

.PHONY: lint
lint:  ## Lint project code.
	poetry run ruff check --fix .

.PHONY: safety
safety:  ## apply safety check in project.
	safety check

.PHONY: format
format:  ## format project code.
	black --line-length=120 .
	isort -rc -m 3 --tc .