docker-build:
	docker build . -f Dockerfile -t formula-1

run:
	docker run -it --net=host -v `pwd`:/formula-1 /bin/bash

run-gpu:
	docker run --gpus all -it --net=host -v `pwd`:/formula-1 /bin/bash