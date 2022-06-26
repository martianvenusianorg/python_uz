`class`ni yaratish

```bash
class DayOfYear:
    def __init__(self, month, day):
        self.m = month
        self.d = day

    def output(self):
        print(self.m, self.d)


today = DayOfYear("June", 27)
birthday = DayOfYear("January", 31)

today.output()
birthday.output()
```