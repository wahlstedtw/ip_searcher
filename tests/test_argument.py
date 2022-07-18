import unittest, sys

from argument import arg_handler

class TestArg(unittest.TestCase):

    def test_arg_exists(self):
        self.assertTrue(arg_handler.process_args("myarg"), "It exists")

    def test_arg_empty(self):
        self.assertFalse(arg_handler.process_args(""), "It doesn't exists")

if __name__ == '__main__':
    unittest.main()