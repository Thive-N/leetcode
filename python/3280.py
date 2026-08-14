class Solution:
    def convertDateToBinary(self, date: str) -> str:
        year, month, day = date.split('-')
        year_binary = int(format(int(year), '016b'))
        month_binary = int(format(int(month), '04b'))
        day_binary = int(format(int(day), '05b'))
        return f"{year_binary}-{month_binary}-{day_binary}"