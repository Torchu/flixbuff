import pytest

from api.models.test import Test

class TestTest(object):
    def test_greet(self):
        test = Test()
        assert test.greet() == "Hello World!"