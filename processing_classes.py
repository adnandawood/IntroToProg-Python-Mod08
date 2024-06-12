# ------------------------------------------------------------------------------------------ #
# Title: Assignment08
# Desc: Creating Applications
# Change Log: (Who, When, What)
#   Adnan Dawood,06/12/2024,Created Script
# ------------------------------------------------------------------------------------------ #

import json
from data_classes import Employee

class FileProcessor:
    """
    Processes data to and from a file.

    Methods:
        read_employee_data_from_file: Reads employee data from a JSON file and populates a list of Employee objects.
        write_employee_data_to_file: Writes employee data to a JSON file from a list of Employee objects.
    """

    @staticmethod
    def read_employee_data_from_file(file_name: str, employee_data: list) -> None:
        """
        Reads employee data from a JSON file.

        Args:
            file_name (str): The name of the file to read from.
            employee_data (list): The list to populate with Employee objects.

        Raises:
            FileNotFoundError: If the specified file does not exist.
            json.JSONDecodeError: If the file is not valid JSON.
        """
        try:
            with open(file_name, 'r') as file:
                data = json.load(file)
            for item in data:
                employee = Employee(item['first_name'], item['last_name'], item['review_date'], int(item['review_rating']))
                employee_data.append(employee)
        except FileNotFoundError as e:
            print(f"Error: The file {file_name} does not exist.")
            raise FileNotFoundError(f"The file {file_name} does not exist.") from e
        except json.JSONDecodeError as e:
            print("Error: The file is not valid JSON.")
            raise json.JSONDecodeError("The file is not valid JSON.", file_name, 0) from e
        return employee_data
    @staticmethod
    def write_employee_data_to_file(file_name: str, employee_data: list) -> None:
        """
        Writes employee data to a JSON file.

        Args:
            file_name (str): The name of the file to write to.
            employee_data (list): The list of Employee objects to write.

        Raises:
            PermissionError: If the file cannot be written to.
        """
        try:
            with open(file_name, 'w') as file:
                json_data = [{'first_name': emp.first_name, 'last_name': emp.last_name, 'review_date': str(emp.review_date), 'review_rating': emp.review_rating} for emp in employee_data]
                json.dump(json_data, file)
        except PermissionError:
            print(f"Error: Cannot write to the file {file_name}.")
            raise PermissionError(f"Cannot write to the file {file_name}.")
        except TypeError:
            print("Error: Data format error.")
            raise TypeError("Data format error.")
