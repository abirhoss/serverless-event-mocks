from unittest import TestCase
from event_mocks_python.event import create_event


class TestEvent(TestCase):

    def test_create_event_aws_api_gateway(self):

        # Arrange
        provider = 'aws'
        event_type = 'api_gateway'
        event_payload = {
           "body": {
              "first_name": "Sam",
              "last_name": "Smith"
           }
        }

        # Act
        event = create_event(provider, event_type, event_payload)

        # Assert
        self.assertTrue(isinstance(event, dict))
        self.assertTrue(event.get('body'))
