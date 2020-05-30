from functools import wraps

MENU_ITEMS = """
1: Select 1 for input date
2. Select 2 for input date and time
0: Select 0 for exit
"""


class View:
    def show_menu(self):
        print(MENU_ITEMS)

    def show_incorrect_input_message(self):
        print("You enter incorrect option")

    def error(self, msg):
        print('Error: {}'.format(msg))


# Decorator pattern
def american_formatter(obj_type):
    def obj_wrapper(func):
        @wraps(func)
        def wrapper(data):
            data_fmt = f"{data.year}/{data.month}/{data.day}"
            if obj_type == 'datetime':
                data_fmt += f" {data.hours}:{data.minutes}"
            print("American format is:", data_fmt)
            return func(data)

        return wrapper

    return obj_wrapper


class DateView:
    @staticmethod
    @american_formatter('date')
    def show(date):
        print(f'EU date: {date.day}.{date.month}.{date.year}')

    def enter_data(self):
        y = input("Enter year: ")
        m = input("Enter month: ")
        d = input("Enter day: ")
        return y, m, d


class DateTimeView:
    @staticmethod
    @american_formatter('datetime')
    def show(datetime):
        print(f'EU datetime: {datetime.hours}:{datetime.minutes} {datetime.day}.{datetime.month}.{datetime.year}')

    def enter_data(self):
        y = input("Enter year: ")
        m = input("Enter month: ")
        d = input("Enter day: ")
        h = input("Enter hours: ")
        mins = input("Enter minutes: ")

        return y, m, d, h, mins
