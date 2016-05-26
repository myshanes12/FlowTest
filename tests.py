from mockito import mock, verify
import unittest

from hello import hellow

class HelloWorldTest(unittest.TestCase):
    def test_should_issue_hello_world_message(self):
        out = mock()

        hello(out)

        verify(out).write("Hello world of Python\n")
