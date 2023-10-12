import datetime


class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        year1, month1, day1 = int(date1[:4]), int(date1[5:7]), int(date1[8:-1])
        year2, month2, day2 = int(date2[:4]), int(date2[5:7]), int(date2[8:-1])
        d1 = datetime.datetime(year1, month1, day1)   # date1
        d2 = datetime.datetime(year2, month2, day2)   # date2
        return abs((d1 - d2).days)
