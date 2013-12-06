from sqltime import DateSlashTimeColon
import sqltime as s

timestamp = DateSlashTimeColon('06/Dec/2011:13:12:48')
timestamp2 = DateSlashTimeColon('24/Mar/2009:06:45:08')

date, time = timestamp.date_and_time()
date2, time2 = timestamp2.date_and_time()
print date, time

d, m, y = timestamp.date_pieces()
d2, m2, y2 = timestamp2.date_pieces()
print d, m, y

h, m, s = timestamp.time_pieces()
print h, m, s

hour, minute, second = [int(i) for i in time.split(':')]
print (3600 * hour) + (60 * minute) + second


print s.time_to_seconds(time)

print s.calculate_time_difference(time, time2)
print s.calculate_time_addition(time, time2)

print s.month_number(m)

print s.month_difference(m, m2)