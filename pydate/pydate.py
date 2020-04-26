#!/usr/bin/env python3

class Year:
    def __init__(self, year):
        if (type(year) is not int):
            raise TypeError("The year argument isn't an int!")

        if (len(str(year)) > 4 or len(str(year)) < 4):
            raise ValueError("The year argument must have 4 digits!")

        self.year = year

    def get_year(self):
        return self.year()

    def set_year(self, year):
        if (type(year) is not int):
            raise TypeError("The year argument isn't an int!")

        if (len(str(year)) > 4 or len(str(year)) < 4):
            raise ValueError("The year argument must have 4 digits!")

        self.year = year

    def tostring(self):
        return str(self.year)

class Date(Year):
    def __init__(self, year, month, day):
        super().__init__(year)

        if (type(month) is not int):
            raise TypeError("The month argument isn't an int!")

        if (type(day) is not int):
            raise TypeError("The day argument isn't an int!")

        if (month < 1 or month > 12):
            raise ValueError("The month argument must be between 1 and 12!")

        if (day < 1 or day > 31):
             raise ValueError("The day argument must be between 1 and 31!")

        self.month = month
        self.day = day

    def get_month(self):
        return self.month

    def get_day(self):
        return self.day

    def set_month(self, month):
        if (type(month) is not int):
            raise TypeError("The month argument isn't an int!")

        if (month < 1 or month > 12):
            raise ValueError("The month argument must be between 1 and 12!")

        self.month = month

    def set_day(self, day):
        if (type(day) is not int):
            raise TypeError("The day argument isn't an int!")
        
        if (day < 1 or day > 31):
            raise ValueError("The day argument must be between 1 and 31!")

        self.day = day

    def tostring(self):
        return str("{0}-{1}-{2}").format(self.year, self.month, self.day)

class Time:
    def __init__(self, hour, minute, second):
        if (type(hour) is not int):
            raise TypeError("The hour argument isn't an int!")

        if (type(minute) is not int):
            raise TypeError("The minute argument isn't an int!")

        if (type(second) is not int):
            raise TypeError("The second argument isn't an int!")

        if (hour < 0 or hour > 23):
            raise ValueError("The hour argument must be between 0 and 23!")

        if (minute < 0 or minute > 59):
            raise ValueError("The minute argument must be between 0 and 59!")

        if (second < 0 or second > 59):
            raise ValueError("The second argument must be between 0 and 59!")

        self.hour = hour
        self.minute = minute
        self.second = second

    def get_hour(self):
        return self.hour

    def get_minute(self):
        return self.minute

    def get_second(self):
        return self.second

    def set_hour(self, hour):
        if (type(hour) is not int):
            raise TypeError("The hour argument isn't an int!")

        if (hour < 0 or hour > 23):
            raise ValueError("The hour argument must be between 0 and 23!")

        self.hour = hour

    def set_minute(self, minute):
        if (type(minute) is not int):
            raise TypeError("The minute argument isn't an int!")

        if (minute < 0 or minute > 59):
            raise ValueError("The minute argument must be between 0 and 59!")

        self.minute = minute

    def set_second(self, second):
        if (type(second) is not int):
            raise TypeError("The second argument isn't an int!")

        if (second < 0 or second > 59):
            raise ValueError("The second argument must be between 0 and 59!")

        self.second = second

    def tostring(self):
        return str("{0}:{1}:{2}").format(self.hour, self.minute, self.second)

class DateTime(Date, Time):
    def __init__(self, year, month, day, hour, minute, second):
        Date.__init__(self, year, month, day)
        Time.__init__(self, hour, minute, second)

    def tostring(self):
        return str("{0}-{1}-{2} {3}:{4}:{5}").format(self.year, self.month, self.day, self.hour, self.minute, self.second)