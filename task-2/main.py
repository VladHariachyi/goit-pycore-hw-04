from pathlib import Path

from cats_manager import get_cats_info


def main():
    """Shows the list of cats"""
    cats = get_cats_info(Path(__file__).parent / "data/cats.txt")
    
    if cats:
        print(f"Generated cats list: {cats}")
    else:
        print("There are not cats!")

if __name__ == "__main__":
    main()