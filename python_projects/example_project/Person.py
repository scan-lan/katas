import datetime


class Person:
    def __init__(self, forename, surname, age, birthday):
        self.forename = forename
        self.surname = surname
        self.age = age
        self.birthday = birthday

    def has_birthday(self):
        if datetime.date.today() > self.birthday:
            self.age += 1

        print("Happy birthday!")
