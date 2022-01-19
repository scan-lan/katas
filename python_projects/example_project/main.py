from datetime import datetime

from Person import Person


def obtain_person_from_input():
    forename = input("What is your forename?\n").title()
    surname = input("What is your surname?\n").title()
    age = int(input("What age are you?\n"))
    birthday = datetime.strptime(input("What is your birthday? (yyyy-mm-dd)\n"), "%Y-%m-%d")
    return Person(forename, surname, age, birthday)


def parse_and_print(person):
    message = f"{person.forename} {person.surname} is {person.age} and " \
              f"their birthday is {datetime.strftime(person.birthday, '%d/%m/%Y')}"
    print(message)


def main():
    person = obtain_person_from_input()
    parse_and_print(person)


main()
