from model.DateTime import Date, DateTime
from view.DateTimeView import DateView, View, DateTimeView


class Protector:  # proxy pattern
    def __init__(self, secret='1234'):
        self.secret = secret

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            sec = input("Enter secret")
            if sec == self.secret:
                return func(*args, **kwargs)
            else:
                raise ValueError("Wrong secret key")

        return wrapper


class DateTimeController:
    instance = None
    commands = ['enter_data', 'show_data']

    def __new__(cls, *args, **kwargs):  # Singleton
        if cls.instance is None:
            cls.instance = super().__new__(cls, *args, **kwargs)
        return cls.instance

    def __init__(self):
        self.data = None
        self.model = None
        self.data_view = None
        self.view = View()

    def show_data(self):
        self.data_view.show(self.data)

    def process_time(self):
        if self.data.hours > 12:
            print("Converting hours to pm format")
            return f"{self.data.hours-12}:{self.data.minutes}pm"

    def enter_data(self):
        while True:
            try:
                self.data = self.model(*self.data_view.enter_data())
                break
            except ValueError as err:
                self.view.error(err)

    @Protector("MY_SUPER_SECRET")
    def factory_data(self, obj_type):  # Factory method
        if obj_type == 'date':
            self.model = Date
            self.data_view = DateView()
        elif obj_type == 'datetime':
            self.model = DateTime
            self.data_view = DateTimeView()

    def run(self):
        while True:
            self.view.show_menu()
            option = input("Select menu's item: ")
            if option == "1":
                try:
                    self.factory_data('date')
                    commands = ['enter_data', 'show_data']
                except ValueError as e:
                    print(e)
                    continue
            elif option == "2":
                try:
                    self.factory_data('datetime')
                    commands = ['enter_data', 'show_data', 'process_time']
                except ValueError as e:
                    print(e)
                    continue
            elif option == "0":
                break
            else:
                self.view.show_incorrect_input_message()
                commands = []

            # command pattern
            [getattr(self, command)() for command in commands]


ProtectedController = Protector()(DateTimeController)
