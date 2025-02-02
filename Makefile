.PHONY: help
help: ## Show this help
	@egrep -h '\s##\s' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

.PHONY: build
build:	## Build project with compose
	docker compose -f compose.yml up

.PHONY: up
up:	## Run project with compose
	docker compose -f compose.yml up

.PHONY: down
down: ## Reset project containers with compose
	docker compose -f compose.yml down -v --remove-orphans

.PHONY: test
test:	## Run project tests
	docker compose -f compose.yml run --rm web pytest -vv tests

.PHONY: test-snapshot
test-snapshot:	## Run project tests
	docker compose -f compose.yml run --rm web pytest --inline-snapshot=fix tests

.PHONY: mypy
mypy:	## mypy check.
	mypy --ignore-missing-imports .

.PHONY: lint
lint:  ## Lint project code.
	uv run ruff check --fix .

.PHONY: safety
safety:  ## apply safety check in project.
	safety check

.PHONY: format
format:  ## format project code.
	black --line-length=120 .
	isort -rc -m 3 --tc .

.PHONY: clean
clean: ## Clean Reset project containers and volumes with compose
	docker compose -f compose.yml down -v --remove-orphans | true
	docker compose -f compose.yml rm -f
