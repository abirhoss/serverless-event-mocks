# Serverless Event Mocks
A small Python library that includes detail mocks of Serverless function events. Useful when unit testing your Serverless functions.

Supported Providers and Event Types:
- AWS:  `aws`
    - API Gateway:  `api_gateway`

This library simply uses default event source mock templates and merges them with any overwrite you provide. [Check out the JSON template files](serverless_event_mocks/event_templates/aws) to learn more about the data structure of each event source.

---

## Quick Start - Install via `pip`

```bash
pip install serverless-event-mocks
```

## Usage

---

### API Gateway

```python
from serverless_event_mocks import create_event

event = create_event(
    provider='aws',
    event_type='api_gateway',
    event_payload={
        "body" : {
            "first_name": "Sam",
            "last_name": "Smith"
        }
    }
)
```

---

## Run Tests and Linter

```bash
# Run unit tests
make test

# Run Flake8 linter
make lint
```