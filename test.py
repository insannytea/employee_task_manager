from datetime import date, datetime

some_day = "10 March 2023"

#some_day_date = datetime.strptime(some_day, "%d/%m/%Y")
some_day_date = some_day.strftime("%d %B %Y")
#some_day_date = date(some_day)

print(some_day_date)