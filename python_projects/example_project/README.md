# Hello!

This small example project shows the basic setup of a python project,
including: a main file for running the program; classes in separate
files; automated testing set up with pytest; `conftest.py` for
fixtures, and more.

## PyTest
PyTest is a testing library for Python. It offers simple, readable
testing syntax, and is an industry favourite. Find out more about
it [here](https://realpython.com/pytest-python-testing/).

### Fixtures
A common headache for automated testing is setting up test data, such as
constructing JSON for API requests. These large objects can quickly
introduce bloat into your test functions. PyTest extracts these into
`conftest.py`, and passes them into your tests through their parameters.
Read more [here](https://realpython.com/pytest-python-testing/#fixtures-managing-state-and-dependencies).

#### Example
```python
# Person.py

class Person:
    def __init__(self, forename, surname, age, birthday):
        self.forename = forename
        self.surname = surname
        self.age = age
        self.birthday = birthday

    def has_birthday(self):
        self.age += 1
```

```python
# main.py

def parse_and_print(person):
    forename = person.forename
    surname = person.surname
    age = person.age
    birthday = person.birthday
```

```python
# conftest.py
import pytest
import datetime
import Person


@pytest.fixture(scope="function")
def person():
    return Person("Guido", "van Rossum", 65, datetime.date(1956, 1, 31))
```
