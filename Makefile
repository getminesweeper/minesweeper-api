start:
	@poetry run start
 
tests:
	@poetry run pytest

code-analysis:
	@poetry run flake8

.PHONY: start tests code-analysis