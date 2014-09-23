import datetime
start = datetime.datetime(1901, 1, 1)
end = datetime.datetime(2000, 12,31)
increase = datetime.timedelta(1)
cur = start
count = 0
for x in range(0,(end-start).days):
	if cur.weekday()==6 and cur.day==1:
		count += 1
	cur += increase
print count
