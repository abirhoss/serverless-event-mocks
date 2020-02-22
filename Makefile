test:
	python -m unittest discover -s serverless_event_mocks_python/tests

lint:
	flake8 .