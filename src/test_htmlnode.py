import unittest

from htmlnode import HTMLNode

class TestHtmlNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(props={"tag": "testtag", "value":"testvalue"})
        self.assertEqual(node.props_to_html(), 'tag="testtag" value="testvalue"')

    def test_eq(self):
        node = HTMLNode("testtag", "testvalue", HTMLNode("nestedtest"), {"test": "value"})
        node2 = HTMLNode("testtag", "testvalue", HTMLNode("nestedtest"), {"test": "value"})
        self.assertEqual(node, node2)

    def test_eq_empty(self):
        node = HTMLNode()
        node2 = HTMLNode()
        self.assertEqual(node, node2)

    def test_neq(self):
        node = HTMLNode("testtag", "testvalue", HTMLNode("nestedtest"), {"test": "value"})
        node2 = HTMLNode("testtag", "testvalue", HTMLNode(""), {"test": "value"})
        self.assertNotEqual(node, node2)

