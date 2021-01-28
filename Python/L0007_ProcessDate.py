# DateTime represents actual date and time. Date : mm-dd-yyyy Time : hh:mm:ss.ms
import datetime

# UTC = Universal Time Coordinated or Greenwich time 
print(f'''
    current DateTime is {datetime.datetime.now()}
    current UTC DateTime is {datetime.datetime.utcnow()}
    current Date is {datetime.date.today()}
''')

#create new date : year, month, date, hour, min, sec, milli sec
d1 = datetime.datetime(2020,12,13,14,15)
#weekday returns 0-6 representing mon-sun
print(f'''
    {d1}
    {d1.year}
    {d1.month}
    {d1.day}
    {d1.weekday()}
    {d1.hour}
    {d1.minute}
    {d1.second}
''')

#Addition (positive value) and subtraction(negative value) on date. You can use days, hours, minutes, seconds
d2 = datetime.datetime.now()

print(f'''
    Date before 1 hour is {d2 + datetime.timedelta(hours=-1)}
    Date after 1 day is {d2 + datetime.timedelta(days=1)}
    {d1} - {d2} = {d1-d2}
''')