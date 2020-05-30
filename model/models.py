
class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value):
        self._year = int(value)

    @property
    def month(self):
        return self._month

    @month.setter
    def month(self, value):
        try:
            m = int(value)
            if 0 < m < 13:
                self._month = m
            else:
                raise ValueError
        except ValueError:
            raise ValueError("Month must be from 1 to 12")

    @property
    def day(self):
        return self._day

    @day.setter
    def day(self, value):
        try:
            d = int(value)
            if 0 < d < 32:
                self._day = d
            else:
                raise ValueError
        except ValueError:
            raise ValueError("Day must be from 1 to 31")


class DateTime(Date):
    def __init__(self, year, month, day, hours, minutes):
        super().__init__(year, month, day)
        self.hours = hours
        self.minutes = minutes

    @property
    def hours(self):
        return self._hours

    @hours.setter
    def hours(self, value):
        try:
            h = int(value)
            if 0 < h < 24:
                self._hours = h
            else:
                raise ValueError
        except ValueError:
            raise ValueError("Hours must be from 1 to 24")

    @property
    def minutes(self):
        return self._minutes

    @minutes.setter
    def minutes(self, value):
        try:
            s = int(value)
            if 0 < s < 60:
                self._minutes = s
            else:
                raise ValueError
        except ValueError:
            raise ValueError("Minutes must be from 1 to 24")

