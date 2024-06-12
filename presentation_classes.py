# ------------------------------------------------------------------------------------------ #
# Title: Assignment08
# Desc: Creating Applications
# Change Log: (Who, When, What)
#   Adnan Dawood,06/12/2024,Created Script
# ------------------------------------------------------------------------------------------ #

from data_classes import Employee
from datetime import datetime
class IO:
    """
    Handles input and output tasks for the user interface of the application.

    Methods:
        output_menu: Displays the main menu.
        input_menu_choice: Collects the user's choice from the menu.
        output_employee_data: Displays all employee data.
        input_employee_data: Collects data for a new employee from the user.
    """

    @staticmethod
    def output_menu(menu: str) -> None:
        """
        Displays the menu to the user.

        Args:
            menu (str): The menu string to be displayed.
        """
        print(menu)

    @staticmethod
    def input_menu_choice() -> str:
        """
        Gets the menu choice from the user.

        Returns:
            str: The user's menu choice.
        """
        choice = input("Please select an option (1-4): ")
        while choice not in ['1', '2', '3', '4']:
            print("Invalid choice. Please select a valid option (1-4).")
            choice = input("Please select an option (1-4): ")
        return choice

    @staticmethod
    def output_employee_data(employee_data: list) -> None:
        """
        Displays the employee data.

        Args:
            employee_data (list): A list of Employee objects.
        """
        if not employee_data:
            print("No employee data available.")
        else:
            for employee in employee_data:
                print(f"Name: {employee.first_name} {employee.last_name}, Review Date: {employee.review_date}, Rating: {employee.review_rating}")

    @staticmethod
    def input_employee_data() -> 'Employee':
        """
        Prompts the user to enter data for a new employee.

        Returns:
            Employee: The new employee object created from the user input.
        """
        first_name=""
        last_name=""
        review_date=""
        review_rating=0
        while True:
            first_name = input("Enter the employee's first name: ").strip()
            if first_name:
                break
            print("First name cannot be empty.")

        while True:
            last_name = input("Enter the employee's last name: ").strip()
            if last_name:
                break
            print("Last name cannot be empty.")

        while True:
            review_date_input = input("Enter the review date (YYYY-MM-DD): ")
            try:
                review_date = datetime.strptime(review_date_input, '%Y-%m-%d').date()
                break
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD.")

        while True:
            try:
                review_rating = int(input("Enter the review rating (1-5): "))
                if 1 <= review_rating <= 5:
                    break
                else:
                    print("Review rating must be between 1 and 5.")
            except ValueError:
                print("Please enter a valid integer for the review rating.")
        return Employee(first_name, last_name, review_date, review_rating)
