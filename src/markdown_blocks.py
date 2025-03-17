from enum import Enum
from htmlnode import HTMLNode
from parentnode import ParentNode
from textnode_helper import text_to_textnodes
from textnode import TextNode, text_node_to_html_node


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDEREDLIST = "unordered_list"
    ORDEREDLIST = "ordered_list"


def markdown_to_blocks(markdown: str):
    blocks = markdown.split("\n\n")
    trimmed_blocks = [*map(lambda s: s.strip(), blocks)]
    cleaned_blocks = [*filter(lambda s: s != "", trimmed_blocks)]
    return cleaned_blocks


def block_to_block_type(markdown_block: str):
    match markdown_block:
        case str(x) if x.startswith(
            ("# ", "## ", "### ", "#### ", "##### ", "###### ")
        ):
            return BlockType.HEADING
        case str(x) if x.startswith("```") and x.endswith("```"):
            return BlockType.CODE
        case str(x) if x.startswith(">"):
            return BlockType.QUOTE
        case str(x) if x.startswith("- "):
            return BlockType.UNORDEREDLIST
        case str(x) if x.startswith("1. "):
            return BlockType.ORDEREDLIST
        case _:
            return BlockType.PARAGRAPH
        
def block_to_html_nodes(block:str) -> [HTMLNode]:
    text_nodes = text_to_textnodes(block)
    return [text_node_to_html_node(node) for node in text_nodes]

def _make_header_node(block: str) -> HTMLNode:
    header_bar, header_text = block.split(" ", 1)
    hcount = header_bar.count("#")
    return HTMLNode(f"h{hcount}", None, block_to_html_nodes(header_text))

def text_to_children(block: (str, BlockType)) -> HTMLNode:
    content, block_type = block
    match block_type:
        case BlockType.HEADING:
            return _make_header_node(content)
        case BlockType.CODE:
            code_content = content[3:-3]
            return text_node_to_html_node(code_content)
        case BlockType.QUOTE:
            pass
        case BlockType.UNORDEREDLIST:
            pass
        case BlockType.ORDEREDLIST:
            pass
        case BlockType.PARAGRAPH:
            return ParentNode("p", block_to_html_nodes(content))


def markdown_to_html_node(markdown: str) -> HTMLNode:
    blocks = markdown_to_blocks(markdown)
    block_types = [*map(lambda b: block_to_block_type(b), blocks)]
    html_nodes = [*map(lambda b: text_to_children(b), zip(blocks, block_types))]
    parent_html = ParentNode("div", html_nodes)
    return parent_html
