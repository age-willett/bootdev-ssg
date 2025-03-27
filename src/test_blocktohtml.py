import unittest
from markdown_blocks import markdown_to_html_node


class TestBlockToHTML(unittest.TestCase):
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_heading(self):
        for i in range(1, 7):
            md = f"""
{"#" * (i)} Heading Level {i}
"""
            node = markdown_to_html_node(md)
            html = node.to_html()
            self.assertEqual(html, f"<div><h{i}>Heading Level {i}</h{i}></div>")

    def test_quote(self):
        md = """
>This is a quoted block
>This is a quote that spans
multiple lines
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><quote>This is a quoted block\nThis is a quote that spans multiple lines</quote></div>",
        )
