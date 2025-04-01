def extract_title(markdown: str):
    first, _ = markdown.splitlines("\n") if "\n" in markdown else [markdown, ""]
    if first.startswith("# "):
        return first.lstrip("# ")
    else:
        raise Exception("Markdown does not start with a header")

def generate_pate(from_path, template_path, dest_path):
    pass
