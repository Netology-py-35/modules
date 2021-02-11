import datetime
from application.salary import calculate_salary
from application.db.people import get_employees


def current_date():
    return datetime.datetime.now()


if __name__ == '__main__':
    print(current_date())
    calculate_salary()
    for emploer in get_employees():
        print(emploer)
