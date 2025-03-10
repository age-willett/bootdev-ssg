import unittest
from markdown_helper import markdown_to_blocks

class TestSplitBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_extra_split_blocks_1(self):
        md = """
This is the first block


This is the second block
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is the first block",
                "This is the second block",
            ],
        )

    def test_extra_split_blocks_2(self):
        md = """
This is the first block



This is the second block
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is the first block",
                "This is the second block",
            ],
        )

    def test_extra_split_blocks_3(self):
        md = """
This is the first block
With an extra line



This is the second block
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is the first block\nWith an extra line",
                "This is the second block",
            ],
        )
    def test_extra_split_blocks_4(self):
        md = """
This is the first block



This is the second block
With an extra line
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is the first block",
                "This is the second block\nWith an extra line",
            ],
        )
