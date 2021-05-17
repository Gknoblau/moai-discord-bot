APP_NAME=gknoblauch/moai-discord-bot
TAG=1.0

build:
	docker build -t $(APP_NAME):$(TAG) .

build-nc:
	docker build --no-cache -t $(APP_NAME):$(TAG) .

run:
	docker run --env-file .env  -it $(APP_NAME):$(TAG)