import re
from enum import Enum


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDEREDLIST = "unordered_list"
    ORDEREDLIST = "ordered_list"


def extract_markdown_images(text: str) -> [tuple]:
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)


def extract_markdown_links(text: str) -> [tuple]:
    return re.findall(r"(?<!!)\[(.*?)\]\((.*?)\)", text)


def markdown_to_blocks(markdown: str):
    blocks = markdown.split("\n\n")
    trimmed_blocks = [*map(lambda s: s.strip(), blocks)]
    cleaned_blocks = [*filter(lambda s: s != "", trimmed_blocks)]
    return cleaned_blocks


def block_to_block_type(markdown_block: str):
    match markdown_block:
        case str(x) if x.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
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

