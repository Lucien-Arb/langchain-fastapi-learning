.PHONY: help
.DEFAULT_GOAL = help

CD_DOCKER=cd Docker/
DOCKER=docker
DOCKER_COMPOSE=docker compose

## —— Docker 🐳 (Linux / OSX) ———————————————————————————————————————————————————————————————
build: ## Create all the Docker content (Container, Volume and Network)
	$(DOCKER_COMPOSE) up --build -d

build-up: ## Create all the Docker content (Container, Volume and Network)
	$(DOCKER_COMPOSE) up --build

start: ## Run the Docker containers
	$(DOCKER_COMPOSE) up

stop: ## Stop the Docker containers
	$(DOCKER_COMPOSE) stop

generate_requirements: ## Generate the requirements.txt file with dependancies
	pip freeze > requirements.txt

help: ## Commands list
	@grep -E '(^[a-zA-Z0-9_-]+:.*?##.*$$)|(^##)' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}{printf "\033[32m%-30s\033[0m %s\n", $$1, $$2}' | sed -e 's/\[32m##/[33m/'