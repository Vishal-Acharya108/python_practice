from datetime import  datetime
d=datetime(2016,10,23,22,57,58,342380)
print("year=",d.year)
print("month=",d.month)

from datetime import datetime,date
t1 date(years= 2017, month=4, day=13)
t2 date(years= 2017, months=5, day=23)
t3 = t2 - t1
print(t3)
from datetime import timedelta
t1 = timedelta(weeks=3, days=5, hours=2, seconds=12)
t2 = timedelta(days=5, hours=4, minutes=6, seconds=45)
t3 = t1 - t2
print("t3=",t3)
file = open('test.txt', 'w')

file.write("This is a write operation")
file.write("Hello!! Thanks for joining the program")

