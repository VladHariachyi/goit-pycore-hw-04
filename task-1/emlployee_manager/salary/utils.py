def load_and_parse_salary_data(file_path) -> list[float] | None:
    """Loads the salary report file and generates a list of all employee salaries.

    Arguments:
    file_path (str) -- The employee salary report path

    Returns:
    employee salaries (list[float]) | None -- the generated list of employee salaries.
    "None" will be returned if file does not exist.
    """
    try: 
        with open(file_path) as file:
            salaries = []

            for line in file:
                try:
                    salary = line.split(',')[1]
                    salaries.append(float(salary))
                except IndexError, ValueError:
                    continue    

            return salaries
    except FileNotFoundError:
        print('File loading error: The file is not found by provided path, check your input')
    return None   
        
def total_salary(file_path: str) -> tuple[float] | None:
    """Loads the salary report file and culaculates total and average salary.

    Arguments:
    file_path (str) -- The employee salary report path

    Returns:
    statistic (tuple[int]) -- the tumple with calculated total and average salaries.
    The tuple with "zero" values will be returned if salaries report was not generated.
    """
    all_salaries = load_and_parse_salary_data(file_path)

    if all_salaries is None:
        return (0, 0)

    total_salary = round(sum(all_salaries), 2)
    average_salary = round(sum(all_salaries) / len(all_salaries), 2)

    return (total_salary, average_salary)

