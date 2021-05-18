# minesweeper-api

## Dependencies

- Python 3.8.5
- Poetry 1.1.6

## Install Python
```
brew install python@3.8
```

## Install Poetry
Poetry is a tool for dependency management and packaging in Python. It allows you to declare the libraries your project depends on and it will manage (install/update) them for you.

### Using Homebrew
```
brew install poetry
```

### Using Shell Script
To install Poetry using shell:
```
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
```

## Install Development Environment

### Install Python Dependencies
Run the following command inside the application root: 
```
make build
```

### Run Application
```
make start
```

### Run Tests
```
make tests
```

### Run Code Analysis
```
make code-analysis
```
