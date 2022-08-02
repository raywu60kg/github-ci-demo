import unittest
from unittest.mock import patch, Mock
import pytest
import datetime
from pytest_demo.utils import get_current_hour1, get_current_hour2, get_current_hour3

test_datetime = datetime.datetime(year=2012, month=1, day=1, hour=1)


class TestUtils(unittest.TestCase):

    @patch("pytest_demo.utils.datetime.datetime")
    def test_get_current_hour1(self,mock_time):
        mock_time.now = Mock(return_value=test_datetime)
        hour = get_current_hour1()
        assert hour == 1

    def test_get_current_hour2(self):
        hour = get_current_hour2(test_datetime)
        hour == 1

    @pytest.mark.skip(reason="I don't want to test this one")
    def test_get_current_hour3(self):
        assert get_current_hour3() == 1

