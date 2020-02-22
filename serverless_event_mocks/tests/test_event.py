from unittest import TestCase
from serverless_event_mocks.event import create_event


class TestEvent(TestCase):

    def test_create_event_aws_api_gateway(self):

        # Arrange
        provider = 'aws'
        event_type = 'api_gateway'
        event_payload = 'fuck'

        # Act
        event = create_event(provider, event_type, event_payload)

        print(event)

        # Assert
        self.assertTrue(isinstance(event, dict))
        self.assertTrue(event.get('body'))
