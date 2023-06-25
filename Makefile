include .env

docker-build:
	docker build -t testapp:v1 .