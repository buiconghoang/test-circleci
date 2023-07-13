include .env

gitHash = $(shell git log --format="%h" -n 1) 
imagetag = hbc08/bch:${gitHash}

test-make-file:
	@echo ${gitHash}
	@echo ${imagetag}

build-image:
	docker build -t ${imagetag} .

push-image:
	docker push ${imagetag}