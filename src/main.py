import os
import shutil
from pagemaker import generate_pages_recursive


def _copy_directory(from_directory, to_directory):
    """
    Takes a directory 'from_directory' and copies it over 'to_directory'
    """
    dir_list = os.listdir(from_directory)
    for p in dir_list:
        path_to_file = f"{from_directory}/{p}"
        if os.path.isdir(path_to_file):
            new_dir = f"{to_directory}/{p}"
            os.mkdir(new_dir)
            print(f"Created directory at {new_dir}")
            _copy_directory(path_to_file, new_dir)
        else:
            shutil.copy(path_to_file, to_directory)
            print(f"Copied file {path_to_file} to {to_directory}")


def populate_public(static_dir="static", public_dir="public"):
    if not os.path.isdir(static_dir):
        raise FileNotFoundError(
            f"Directory '{static_dir}' either does not exist or is not a directory."
        )
    if os.path.isdir(public_dir):
        shutil.rmtree(public_dir)
        print(f"Removed directory {public_dir}")
    if os.path.exists(public_dir):
        raise FileExistsError(
            f"A file named '{public_dir}' already exists.\nPlease ensure '{public_dir}' is either a directory or does not exist."
        )
    os.mkdir(public_dir)
    print(f"Created directory {public_dir}")
    _copy_directory(static_dir, public_dir)


def main():
    populate_public()
    generate_pages_recursive("content", "template.html", "public")
    # dummy = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    # print(dummy)


if __name__ == "__main__":
    main()
