test:
	python -m unittest discover -s event_mocks_python/tests

lint:
	flake8 .