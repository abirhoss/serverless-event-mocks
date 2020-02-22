import json
from pathlib import Path

VALID_PROVIDERS = ['aws']
VALID_EVENT_TYPES = ['api_gateway']
EVENT_TEMPLATES_EXT = 'json'
EVENT_TEMPLATES_DIR = Path(__file__).resolve().parent / 'event_templates'


def create_event(provider: str, event_type: str, event_payload: dict) -> dict:
    """Create a mock serverless event"""

    # Validate provider
    if not _validate_provider(provider):
        raise Exception(f"Invalid provider '{provider}'. Valid providers: {VALID_PROVIDERS}")

    # Validate event type
    if not _validate_event_type(event_type):
        raise Exception(f"Invalid event type '{event_type}'. Valid event types: {VALID_EVENT_TYPES}")

    # Load event template
    event_template = _load_event_template(provider, event_type)

    # Return new merged event
    return {**event_template, **event_payload}


def _load_event_template(provider: str, event_type: str) -> dict:

    event_template_path = Path(f"{EVENT_TEMPLATES_DIR}/{provider}/{event_type}.{EVENT_TEMPLATES_EXT}")

    with open(event_template_path) as event_template_file:
        return json.load(event_template_file)


def _validate_provider(provider: str) -> bool:
    return provider in VALID_PROVIDERS


def _validate_event_type(event_type: str) -> bool:
    return event_type in VALID_EVENT_TYPES
