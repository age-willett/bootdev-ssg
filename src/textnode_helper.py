from textnode import TextNode, TextType
import re
from itertools import zip_longest


def extract_markdown_images(text: str) -> [tuple]:
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)


def extract_markdown_links(text: str) -> [tuple]:
    return re.findall(r"(?<!!)\[(.*?)\]\((.*?)\)", text)


def _re_split_by_ends(text, start_block, end_block):
    return re.split(re.escape(start_block) + r"(.*?)" + re.escape(end_block), text)


def split_nodes_delimiter(
    old_nodes: [TextNode], delimiter: str, text_type: TextType
) -> [TextNode]:
    new_nodes = []
    for node in old_nodes:
        if node.text_type == TextType.TEXT:
            new_nodes.extend(split_node(node, delimiter, delimiter, text_type))
        else:
            new_nodes.extend([node])

    return new_nodes


def split_node(
    node: TextNode, start_block: str, end_block: str, text_type: TextType
) -> [TextNode]:
    node_type = node.text_type
    node_url = node.url
    split_text = _re_split_by_ends(node.text, start_block, end_block)
    for i in range(0, len(split_text), 2):
        split_text[i] = TextNode(split_text[i], node_type)
    for i in range(1, len(split_text), 2):
        split_text[i] = TextNode(split_text[i], text_type, node_url)
    return [new_node for new_node in split_text if new_node.text != ""]


def split_nodes_image(old_nodes: [TextNode]) -> [TextNode]:
    def inner_split_node(node: TextNode):
        node_url = node.url
        node_type = node.text_type
        node_text = node.text
        images_in_text = extract_markdown_images(node_text)
        image_nodes = [
            *map(lambda t: TextNode(t[0], TextType.IMAGE, t[1]), images_in_text)
        ]
        split_text = re.split(r"!\[(?:.*?)\]\((?:.*?)\)", node_text)
        split_text = [*filter(lambda s: s != "", split_text)]
        text_nodes = [*map(lambda s: TextNode(s, node_type, node_url), split_text)]
        return [
            val
            for t in zip_longest(text_nodes, image_nodes)
            for val in t
            if val is not None
        ]

    new_nodes = []
    for node in old_nodes:
        new_nodes.extend(inner_split_node(node))
    return new_nodes


def split_nodes_links(old_nodes: [TextNode]) -> [TextNode]:
    def inner_split_node(node: TextNode):
        node_url = node.url
        node_type = node.text_type
        node_text = node.text
        links_in_text = extract_markdown_links(node_text)
        link_nodes = [
            *map(lambda t: TextNode(t[0], TextType.LINK, t[1]), links_in_text)
        ]
        split_text = re.split(r"(?<!!)\[(?:.*?)\]\((?:.*?)\)", node_text)
        split_text = [*filter(lambda s: s != "", split_text)]
        text_nodes = [*map(lambda s: TextNode(s, node_type, node_url), split_text)]
        return [
            val
            for t in zip_longest(text_nodes, link_nodes)
            for val in t
            if val is not None
        ]

    new_nodes = []
    for node in old_nodes:
        new_nodes.extend(inner_split_node(node))
    return new_nodes


def text_to_textnodes(text) -> [TextNode]:
    text_node = [TextNode(text, TextType.TEXT)]
    new_nodes = split_nodes_image(text_node)
    new_nodes = split_nodes_links(new_nodes)
    new_nodes = split_nodes_delimiter(new_nodes, "**", TextType.BOLD)
    new_nodes = split_nodes_delimiter(new_nodes, "_", TextType.ITALIC)
    new_nodes = split_nodes_delimiter(new_nodes, "`", TextType.CODE)
    return new_nodes
