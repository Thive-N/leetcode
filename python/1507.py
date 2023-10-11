class Solution:
    def reformatDate(self, date: str) -> str:
        dates = date.split(" ")
        months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        day = dates[0][:-2].zfill(2)
        month = str(months.index(dates[1]) + 1).zfill(2)
        year = dates[2]
        return "-".join([year, month, day])
