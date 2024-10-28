install:
	pip install --upgrade pip &&\
	pip install -r requirements.txt

test:
	python -m pytest -vv -cov=mylib -cov=main test_*.py

format:
	black *.py

lint:
	ruff check *.py mylib/*.py test_*.py

run:
	python main.py

container-lint:
	docker run --rm -i hadolint/hadolint < Dockerfile
	
all: install format test lint run