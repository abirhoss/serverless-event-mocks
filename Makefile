test:
	python -m unittest discover -s serverless_event_mocks/tests

lint:
	flake8 .