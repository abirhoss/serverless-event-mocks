# Event Mocks
A small Python library that includes details mocks of Serverless function events. Useful when unit testing your Serverless functions.

Supported Providers and Event Sources:
- [x] AWS: `aws`
    - [x] API Gateway: `api-gateway`

This library simply uses default event source mock templates and merges them with any overwrite you provide. [Check out the JSON template files](event_mocks/event_templates/aws) to learn more about the data structure of each event source.

---

## Quick Start - Usage

Install the Stream Client package and it's dependencies using:

```bash
pip install git+ssh://git@bitbucket.org:Abir_Hossain/event-mocks.git
```

Import and use the `create_event` function into any Python code using

```python
from event_mocks.event import create_event

provider = 'aws'
event_type = 'api_gateway'
event_payload = {
    "body" : {
        "first_name": "Sam",
        "last_name": "Smith"
    }
}

event = create_event(provider, event_type, event_payload)
```

---

## Run Tests and Linter

```bash
# Run unit tests
make test

# Run linter
make lint
```
