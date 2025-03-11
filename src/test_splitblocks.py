import unittest
from markdown_blocks import markdown_to_blocks, block_to_block_type, BlockType

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

    def test_blocktype_paragraph(self):
        block = "This is a paragraph"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)


    def test_blocktype_heading(self):
        for i in range(6):
            heading_hash = "#" * (i+1) + " "
            block = f"{heading_hash}This is a heading"
            self.assertEqual(block_to_block_type(block), BlockType.HEADING)
        block = "####### This is not a heading"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_blocktype_code(self):
        block = "```This is a code```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)
        block = "```This is not code"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_blocktype_quote(self):
        block = ">This is a quote"
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)

    def test_blocktype_unordered_list(self):
        block = "- This is a unordered list"
        self.assertEqual(block_to_block_type(block), BlockType.UNORDEREDLIST)
        block = "-This is not an unordered list"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_blocktype_ordered_list(self):
        block = "1. This is a ordered list"
        self.assertEqual(block_to_block_type(block), BlockType.ORDEREDLIST)
        block = "1.This is not an ordered list"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)
