.PHONY: pi-lint
pi-lint:
	pip install ".[lint]"

.PHONY: pi
pi: pi-lint
	pip install .

.PHONY: lint
lint: check
	
.PHONY: check
check:
	ruff check

.PHONY: fix
fix:
	ruff check --fix

.PHONY: format
format:
	ruff format src
