class Solution:
  def dayOfYear(self, date: str) -> int:
    year = int(date[:4])
    days = [31, 29 if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0 else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return sum(days[:int(date[5:7]) - 1]) + int(date[8:])

