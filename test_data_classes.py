# ------------------------------------------------------------------------------------------ #
# Title: Assignment08
# Desc: Creating Applications
# Change Log: (Who, When, What)
#   Adnan Dawood,06/12/2024,Created Script
# ------------------------------------------------------------------------------------------ #

import unittest
from data_classes import Person, Employee

class TestPerson(unittest.TestCase):
    def test_person_creation(self):
        p = Person("John", "Doe")
        self.assertEqual(p.first_name, "John")
        self.assertEqual(p.last_name, "Doe")

    def test_person_name_validation(self):
        with self.assertRaises(ValueError):
            Person("John3", "Doe")

class TestEmployee(unittest.TestCase):
    def test_employee_inheritance(self):
        e = Employee("Jane", "Doe", "2020-01-01", 4)
        self.assertEqual(e.first_name, "Jane")
        self.assertEqual(e.last_name, "Doe")

    def test_review_date_validation(self):
        with self.assertRaises(ValueError):
            Employee("Jane", "Doe", "2020-13-01", 4)

    def test_review_rating_validation(self):
        with self.assertRaises(ValueError):
            Employee("Jane", "Doe", "2020-01-01", 6)

if __name__ == '__main__':
    unittest.main()
