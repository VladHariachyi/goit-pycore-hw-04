def parse_cat_info(cat_info: str) -> dict[str, str] | None:
    """Parse the string with cat info.

    Arguments:
    cat_info (str) -- The string which containes cat info, such as "id", "name", "age", 
    where each property separated by comma.

    Returns:
    cats_info (dict[str, str] | None) -- the generated dictionary with the cat info.
    "None" will be returned if error happen during parsing the data. 
    """
    id, name, age = cat_info.split(',')

    if id and name and age:
        try:
            return { "id": id, "name": name,"age": int(age) }
        except ValueError:
            print(f"Data parsing error: The 'age' is not numeric value in '{cat_info}'")
    else:
        print(f"Data parsing error: The provided data '{cat_info}' has missiing preprties") 
        return None

def get_cats_info(file_path: str) -> list[dict[str, str]] | None:
    """Loads the cat info and parse it generating the list of cat dictionaries.

    Arguments:
    file_path (str) -- The cats info file path

    Returns:
    cats_info (list[dict[str, str]] | None) -- the list of generated dictionaries with cat info.
    "None" will be returned if file does not exist. 
    """
    try: 
        with open(file_path) as file:
            cats = []

            for line in file:
                cat = parse_cat_info(line) 

                if cat is None:
                    continue

                cats.append(cat)      

            return cats
    except FileNotFoundError:
        print("File loading error: The file is not found by provided path, check your input")
        return None 