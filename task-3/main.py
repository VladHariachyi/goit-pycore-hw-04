import sys
from colorama import Fore, Style
from pathlib import Path

from file_manager import get_dir_structure


def main():
    """Shows the folder structure via provided by user input with folder path which need to check"""
    try:
        dir_path = Path(__file__).parent.parent / sys.argv[1]
        dir_structure = get_dir_structure(dir_path)
    
        if dir_structure:
            for item in dir_structure:
                print(item)
        
    except IndexError:
        print(f"{Fore.RED}Input data error: the directory path is missing{Style.RESET_ALL}")

if __name__ == "__main__":
    main()