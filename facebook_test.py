"""Test for facebook.py"""
# TODO: Finish unit test file. 

from unittest.mock import Mock
from unittest.mock import patch
from facebook import Facebook
import yaml
import unittest


class FacebookTests(unittest.TestCase):

  @patch('yaml.load')
  @patch('facebook.requests.get')
  def setUp(self, requests_get_mock, config_yaml_mock):
    """Create mock config file and start facebook.."""
    print(requests_get_mock)
    requests_get_mock.return_value.status_code = 200
    requests_get_mock.return_value = {
      "id": "4206969420",
      "name": "Tester McTestface"
    }

  @patch('facebook.requests.get')
  def test_exchange_short_token_for_long_token(self, requests_get_mock):
    Facebook()
    self.assertEqual(1, 1)


if __name__ == "__main__":
  unittest.main()
