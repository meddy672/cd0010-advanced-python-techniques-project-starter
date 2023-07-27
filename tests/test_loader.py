import unittest
import os
import itertools
import builtins


from loader import Loader
from threading import Thread
from unittest.mock import patch


class TestLoader(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.loader = Loader("Loading Data...", "Data Ready!", 0.05)


    def test_start(self):
        with patch.object(Thread, 'start', return_value=None) as mocked_method:
            self.loader.start()
            self.assertEqual(mocked_method.call_count, 1)


    def test_stop(self):
        with patch.object(os, 'get_terminal_size') as mocked_function:
            self.loader.stop()
            self.assertEqual(self.loader.done, True)
            self.assertEqual(mocked_function.call_count, 1)
        with patch.object(builtins, 'print') as mocked_function:
            self.loader.stop()
            self.assertEqual(mocked_function.call_count, 2)


if __name__ == '__main__':
    unittest.main()