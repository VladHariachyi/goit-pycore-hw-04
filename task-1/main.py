from pathlib import Path

from emlployee_manager import total_salary


def main():
    """Shows the total and average employee salaries report."""
    total, average = total_salary(Path(__file__).parent / 'data/employee-salaries.txt')

    print(f"The total salary amount is -- {total} \nThe average salary amount is -- {average}")

if __name__ == "__main__":
    main()