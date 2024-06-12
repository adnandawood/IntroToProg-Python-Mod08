# ------------------------------------------------------------------------------------------ #
# Title: Assignment08
# Desc: Creating Applications
# Change Log: (Who, When, What)
#   Adnan Dawood,06/12/2024,Created Script
# ------------------------------------------------------------------------------------------ #

import unittest
import json
from unittest.mock import mock_open, patch
from processing_classes import FileProcessor
from data_classes import Employee

class TestFileProcessor(unittest.TestCase):
    def setUp(self):
        self.employees = [Employee("John", "Doe", "2020-01-01", 5), Employee("Jane", "Doe", "2021-01-01", 4)]

    def test_read_employee_data_from_file(self):
        mock_data = json.dumps([
            {"first_name": "John", "last_name": "Doe", "review_date": "2020-01-01", "review_rating": 5},
            {"first_name": "Jane", "last_name": "Doe", "review_date": "2021-01-01", "review_rating": 4}
        ])

        with patch('builtins.open', mock_open(read_data=mock_data)), patch('json.load', return_value=json.loads(mock_data)):
            employee_data = []
            FileProcessor.read_employee_data_from_file("dummy_file.json", employee_data)
            self.assertEqual(len(employee_data), 2)
            self.assertEqual(employee_data[0].first_name, "John")
            self.assertEqual(employee_data[1].review_rating, 4)

    def test_write_employee_data_to_file(self):
        expected_json = json.dumps([
            {"first_name": "John", "last_name": "Doe", "review_date": "2020-01-01", "review_rating": 5},
            {"first_name": "Jane", "last_name": "Doe", "review_date": "2021-01-01", "review_rating": 4}
        ], indent=4)

        with patch('builtins.open', mock_open()) as mocked_file, patch('json.dump') as mock_dump:
            FileProcessor.write_employee_data_to_file("dummy_file.json", self.employees)
            mock_dump.assert_called_once_with(json.loads(expected_json), mocked_file())

if __name__ == '__main__':
    unittest.main()
