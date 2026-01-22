import calendar
year = int(input("Enter a valid year:"))
month = int(input("Enter a valid month:"))
month_calendar = calendar.month(year, month)
print(month_calendar)
