# setup:
# 	pip install pytest

# test:
# 	pytest tests/

# spec-check:
# 	echo "Checking specs alignment..."
IMAGE_NAME = chimera-tests

setup:
	pip install pytest

build:
	docker build -t $(IMAGE_NAME) .

test: build
	docker run --rm $(IMAGE_NAME)

spec-check:
	echo "Checking specs alignment..."
