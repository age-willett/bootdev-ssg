import re

def extract_markdown_images(text: str) -> [tuple]:
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)

def extract_markdown_links(text: str) -> [tuple]:
    return re.findall(r"(?<!!)\[(.*?)\]\((.*?)\)", text)

def markdown_to_blocks(markdown: str):
    blocks = markdown.split("\n\n")
    trimmed_blocks = [*map(lambda s: s.strip(), blocks)]
    cleaned_blocks = [*filter(lambda s: s != "", trimmed_blocks)]
    return cleaned_blocks
