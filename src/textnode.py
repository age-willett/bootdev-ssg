from enum import Enum
from leafnode import LeafNode
from itertools import zip_longest


class TextType(Enum):
    TEXT = "text"
    NORMAL = "normal"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"


class TextNode:
    def __init__(self, text: str, text_type: TextType, url: str = None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, o):
        return (
            self.text == o.text and self.text_type == o.text_type and self.url == o.url
        )

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"


def text_node_to_html_node(text_node: TextNode):
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(tag=None, value=text_node.text)
        case TextType.BOLD:
            return LeafNode(tag="b", value=text_node.text)
        case TextType.ITALIC:
            return LeafNode(tag="i", value=text_node.text)
        case TextType.CODE:
            return LeafNode(tag="code", value=text_node.text)
        case TextType.LINK:
            return LeafNode(
                tag="a", value=text_node.text, props={"href": text_node.url}
            )
        case TextType.IMAGE:
            return LeafNode(
                tag="img",
                value="",
                props={"src": text_node.url, "alt": text_node.text},
            )
        case _:
            raise ValueError("invald text type")


def split_nodes_delimiter(old_nodes: [TextNode], delimiter: str, text_type: TextType) -> [TextNode]:
    def split_node(node: TextNode):
        split_text = node.text.split(delimiter)
        outer_text = split_text[::2]
        inner_text = split_text[1::2]
        if len(outer_text) == len(inner_text): #unclosed delimiter
            outer_text.append(delimiter + inner_text[-1])
            inner_text.pop()
        outer_nodes = [*map(lambda s: TextNode(s, TextType.TEXT), outer_text)]
        inner_nodes = [*map(lambda s: TextNode(s, text_type), inner_text)]
        return [val for t in zip_longest(outer_nodes, inner_nodes) for val in t if val is not None]

    new_nodes = []
    for node in old_nodes:
        new_nodes.extend(split_node(node))
    return new_nodes
