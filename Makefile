
APP_NAME := web
# HELP
# This will output the help for each task
# thanks to https://marmelab.com/blog/2016/02/29/auto-documented-makefile.html
.PHONY: help

help: ## This help.
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

.DEFAULT_GOAL := help

build: ## Build Container
		docker-compose build --no-cache ${APP_NAME}

rebuild: ## Rebuild Container
		docker system prune -f
		docker-compose build --no-cache ${APP_NAME}
		docker-compose up -d ${APP_NAME}

up: ## Bring up the Container Services
	docker-compose up -d ${APP_NAME}

down: ## Bring Down App Services
	docker-compose down
	