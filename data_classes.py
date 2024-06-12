# ------------------------------------------------------------------------------------------ #
# Title: Assignment08
# Desc: Creating Applications
# Change Log: (Who, When, What)
#   Adnan Dawood,06/12/2024,Created Script
# ------------------------------------------------------------------------------------------ #

from datetime import date

class Person:
    """
    A class representing a person.

    Attributes:
        first_name (str): The person's first name, defaults to an empty string.
        last_name (str): The person's last name, defaults to an empty string.
    """

    def __init__(self, first_name: str = "", last_name: str = ""):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value: str):
        if isinstance(value, str) and all(x.isalpha() or x.isspace() for x in value):
            self._first_name = value
        else:
            raise ValueError("First name must be alphabetic or spaces.")

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value: str):
        if isinstance(value, str) and all(x.isalpha() or x.isspace() for x in value):
            self._last_name = value
        else:
            raise ValueError("Last name must be alphabetic or spaces.")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Employee(Person):
    """
    A class representing an employee, inheriting from Person.

    Attributes:
        review_date (date): The date of the employee's review, defaults to January 1, 1900.
        review_rating (int): The employee's review rating, defaults to 3.
    """

    def __init__(self, first_name: str = "", last_name: str = "", review_date: str = "1900-01-01", review_rating: int = 3):
        super().__init__(first_name, last_name)
        self._review_date = date.fromisoformat(str(review_date))
        self.review_rating = review_rating

    @property
    def review_date(self):
        return self._review_date

    @review_date.setter
    def review_date(self, value: str):
        try:
             self._review_date = date.fromisoformat(str(value)) 
        except ValueError:
            raise ValueError("Incorrect data format, should be YYYY-MM-DD")

    @property
    def review_rating(self):
        return self._review_rating

    @review_rating.setter
    def review_rating(self, value: int):
        if 1 <= value <= 5:
            self._review_rating = value
        else:
            raise ValueError("Review rating must be between 1 and 5")

    def __str__(self):
        return f"{super().__str__()}, Review Date: {self.review_date}, Review Rating: {self.review_rating}"
