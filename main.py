# ------------------------------------------------------------------------------------------ #
# Title: Assignment08
# Desc: Creating Applications
# Change Log: (Who, When, What)
#   Adnan Dawood,06/12/2024,Created Script
# ------------------------------------------------------------------------------------------ #

from presentation_classes import IO
from processing_classes import FileProcessor
from data_classes import Employee

FILE_NAME = "EmployeeRatings.json"
MENU = '''
---- Employee Ratings ------------------------------
  Select from the following menu:
    1. Show current employee rating data.
    2. Enter new employee rating data.
    3. Save data to a file.
    4. Exit the program.
--------------------------------------------------
'''

def main():
    employees = []  
    try:
        employees = FileProcessor.read_employee_data_from_file(FILE_NAME, employees)
    except FileNotFoundError:
        print("Starting with an empty dataset.")
    except Exception as e:
        print(f"An error occurred: {e}")

    while True:
        IO.output_menu(MENU)
        menu_choice = IO.input_menu_choice()

        if menu_choice == '1':
            IO.output_employee_data(employees)
        elif menu_choice == '2':
            employee = IO.input_employee_data()
            employees.append(employee)
            print("New employee data added.")
        elif menu_choice == '3':
            FileProcessor.write_employee_data_to_file(FILE_NAME, employees)
            print("Data successfully saved to file.")
        elif menu_choice == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid option, please choose from 1 to 4.")

if __name__ == '__main__':
    main()
