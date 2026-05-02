from pathlib import Path
from colorama import Fore, Style


def get_indent_template(indent_amount: int) -> str:
    """Generates the indent template.

    Arguments:
    indent_amount (int) -- The indent amount which is used to build template.

    Returns:
    indent_template (str) -- The string with calculated amount of spacings to represent indent.
    """
    return " " * (indent_amount - 1)

def get_dir_structure(path: str, indent_amount = 0) -> list[str] | None:
    """Generates the dir scructure.

    Arguments:
    dir_path (str) -- The dir which need to parse. 
    indent_amount (int) -- The indent amount to show the nesting of dir content.

    Returns:
    dir_structure (list[str] | None) -- The list of strings, where each item represents the current dir and its children.
    "None" will be returned if provided path is not a dir. 
    """
    dir_path = Path(path)

    if not dir_path.is_dir():
        print(f"{Fore.RED}Parsing error: The provided path is not a dir{Style.RESET_ALL}")
        return None
    
    indent_template = get_indent_template(indent_amount)
    dir_structure = [f"{indent_template}{Fore.BLUE}{dir_path.name}/{Style.RESET_ALL}"]

    for child_path in dir_path.iterdir():
        child_indent_amount = indent_amount + 4

        if child_path.is_dir():
            child_structure = get_dir_structure(child_path, child_indent_amount)

            if child_structure:
                dir_structure = [*dir_structure, *child_structure]

        if child_path.is_file():
            dir_structure.append(f"{get_indent_template(child_indent_amount)}{Fore.YELLOW}{child_path.name}{Style.RESET_ALL}")

    return dir_structure