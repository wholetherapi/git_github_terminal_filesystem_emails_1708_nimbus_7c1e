test:
	python -m pytest tests

lint:
	python -m compileall src vendor
