# ------------------------------------------------------------------------------------------ #
# Title: Assignment08
# Desc: Creating Applications
# Change Log: (Who, When, What)
#   Adnan Dawood,06/12/2024,Created Script
# ------------------------------------------------------------------------------------------ #

import unittest
from unittest.mock import patch
from presentation_classes import IO
from data_classes import Employee
from datetime import date
class TestIO(unittest.TestCase):
    def test_output_menu(self):
        with patch('builtins.print') as mocked_print:
            IO.output_menu("Test Menu")
            mocked_print.assert_called_with("Test Menu")

    def test_input_menu_choice(self):
        with patch('builtins.input', return_value='1'):
            choice = IO.input_menu_choice()
            self.assertEqual(choice, '1')

    def test_output_employee_data(self):
        employee = Employee("John", "Doe", "2020-01-01", 5)
        with patch('builtins.print') as mocked_print:
            IO.output_employee_data([employee])
            mocked_print.assert_called_with("Name: John Doe, Review Date: 2020-01-01, Rating: 5")

    def test_input_employee_data(self):
        with patch('builtins.input', side_effect=["John", "Doe", "2020-01-01", "5"]):
            employee = IO.input_employee_data()
            self.assertEqual(employee.review_date, date(2020, 1, 1)) 
            self.assertEqual(employee.review_rating, 5)

if __name__ == '__main__':
    unittest.main()
