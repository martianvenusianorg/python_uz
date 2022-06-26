class DayOfYear:
    def __init__(self, m, d):
        self.month = m
        self.day = d

    def output(self):
        print(self.month, self.day)

today = DayOfYear("June", 27)
today.output()

birthday = DayOfYear("January", 31)
birthday.output()
