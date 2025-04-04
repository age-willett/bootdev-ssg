from markdown_blocks import markdown_to_html_node
import os


def extract_title(markdown: str):
    first, *_ = markdown.splitlines("\n")
    if first.startswith("# "):
        return first.lstrip("# ")
    else:
        raise Exception("Markdown does not start with a header")


def generate_page(from_path: str, template_path: str, dest_path: str, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path) as f:
        markdown = f.read()
    with open(template_path) as f:
        template = f.read()
    html_content = markdown_to_html_node(markdown).to_html()
    html_title = extract_title(markdown)
    html_page = (
        template.replace("{{ Title }}", html_title)
        .replace("{{ Content }}", html_content)
        .replace('href="/', f'href="{basepath}')
        .replace('src="/', f'src="{basepath}')
    )

    if "/" in dest_path:
        dir_path, _ = dest_path.rsplit("/", 1)
        if not os.path.isdir(dir_path) and not os.path.exists(dir_path):
            os.makedirs(dir_path)
    with open(dest_path, "w") as f:
        f.write(html_page)


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    dir_list = os.listdir(dir_path_content)
    for p in dir_list:
        source_path = f"{dir_path_content}/{p}"
        destination_path = f"{dest_dir_path}/{p}"
        if os.path.isdir(source_path):
            generate_pages_recursive(
                source_path, template_path, destination_path, basepath
            )
        else:
            destination_path = destination_path.rsplit(".", 1)[0] + ".html"
            generate_page(source_path, template_path, destination_path, basepath)
