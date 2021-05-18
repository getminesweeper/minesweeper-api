start:
	@poetry run start
 
tests:
	@poetry run pytest

code-analysis:
	@poetry run flake8

build:
	@poetry install

update:
	@poetry update

shell:
	@poetry shell

.PHONY: start tests code-analysis build update shell