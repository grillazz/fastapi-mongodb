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

.PHONY: lock
lock:	## Refresh pipfile.lock
	pipenv lock --pre

.PHONY: requirements
requirements:	## Refresh requirements.txt from pipfile.lock
	pipenv lock --requirements --dev >| requirements.txt

.PHONY: test
test:	## Run project tests
	docker-compose run --rm web pytest -vv

.PHONY: lint
lint:	## Linter project code.
	isort  -rc -m 3 --tc .
	black --line-length=120 .

.PHONY: mypy
mypy:	## mypy check.
	mypy --ignore-missing-imports .

.PHONY: flake8
flake8:  ## flake8 check.
	flake8 .

.PHONY: safety
safety:  ## apply safety check in project.
	safety check

.PHONY: format
format:  ## format project code.
	isort -rc -m 3 --tc .
	black --line-length=120 .
