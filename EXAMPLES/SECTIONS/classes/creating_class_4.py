class DayOfYear:
    def __init__(self, m, d):
        self.month = m
        self.day = d

    def output(self):
        print(self.month, self.day)

    def getDay(self):
        return self.day

    def getMonth(self):
        return self.month


today = DayOfYear("June", 27)
print(today.getMonth(), today.getDay())

birthday = DayOfYear("January", 31)
print(birthday.getMonth(), birthday.getDay())
