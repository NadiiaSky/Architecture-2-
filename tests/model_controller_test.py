import unittest
from unittest.mock import patch

import mock

from controller.controller import DateTimeController
from model.models import Date, DateTime
from view.views import DateView, DateTimeView


class TestModel(unittest.TestCase):
    @mock.patch('view.views.DateView.enter_data', lambda _: (2020, 12, 31))
    def test__date_object_creation(self):
        view = DateView()
        model = Date(*view.enter_data())
        assert (model.year, model.month, model.day) == (2020, 12, 31)

    def test__incorrect_year_daises_error(self):
        with self.assertRaises(ValueError):
            Date("Year", 12, 31)

    def test__incorrect_month_daises_error(self):
        with self.assertRaises(ValueError):
            Date(2020, 13, 31)

    def test__incorrect_day_daises_error(self):
        with self.assertRaises(ValueError):
            Date(2020, 12, 32)

    @mock.patch('view.views.DateTimeView.enter_data', lambda _: (2020, 12, 31, 23, 59))
    def test__datetime_object_creation(self):
        view = DateTimeView()
        model = DateTime(*view.enter_data())
        assert (model.year, model.month, model.day, model.hours, model.minutes) == (2020, 12, 31, 23, 59)

    def test__incorrect_hours_daises_error(self):
        with self.assertRaises(ValueError):
            DateTime(2020, 12, 31, 25, 59)

    def test__incorrect_minutes_daises_error(self):
        with self.assertRaises(ValueError):
            DateTime(2020, 12, 31, 23, 60)


class ControllerTest(unittest.TestCase):
    def test__controller_singleton(self):
        controller1 = DateTimeController()
        controller2 = DateTimeController()
        assert controller1 is controller2

    @mock.patch("controller.controller.print", mock.MagicMock(return_value=None))
    def test__process_time(self):
        controller = DateTimeController()
        controller.data = DateTime(2020, 12, 31, 15, 45)
        assert controller.process_time() == "3:45pm"

    def test__run_exit_success(self):
        my_input = patch("controller.controller.input", mock.MagicMock(return_value="0"))
        my_print = patch("view.views.View.show_menu", mock.MagicMock(return_value=None))
        my_input.start()
        my_print.start()
        controller = DateTimeController()
        controller.run()
        my_input.stop()
        my_print.stop()

    @mock.patch("controller.controller.input", mock.MagicMock(return_value="MY_SUPER_SECRET"))
    def test__factory_data(self):
        controller = DateTimeController()
        controller.factory_data('date')
        assert controller.model == Date

        controller.factory_data('datetime')
        assert controller.model == DateTime


if __name__ == '__main__':
    unittest.main()
