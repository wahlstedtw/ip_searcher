import unittest

from argument import arg_handler

class TestArg(unittest.TestCase):

# Only testing that the arguments don't exist. We really don't need to test argument handling.
    def test_arg_not_exists(self):
        with self.assertRaises(SystemExit):
            arg_handler.process_args()

if __name__ == '__main__':
    unittest.main()