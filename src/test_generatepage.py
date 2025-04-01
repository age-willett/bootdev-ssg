import unittest
from pagemaker import extract_title


class TestGeneratePage(unittest.TestCase):

    def test_extract_title(self):
        self.assertEqual("Hello", extract_title("# Hello"))

    def test_except_extract_title(self):
        self.assertRaises(Exception, extract_title, "Hello")

