import unittest

from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_no_tag(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode(None, [child_node])
        self.assertRaises(ValueError,parent_node.to_html)

    def test_blank_tag(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("", [child_node])
        self.assertRaises(ValueError,parent_node.to_html)

    def test_no_children(self):
        parent_node = ParentNode("div", None)
        self.assertRaises(ValueError, parent_node.to_html)

    def test_wrong_children_type(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", child_node)
        self.assertRaises(TypeError,parent_node.to_html)
