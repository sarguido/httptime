'''A collection of date/time functions for sqlite3.
Written out of frustration with the current datetime sqlite3 methods.'''

import sqlite3
import re
import datetime

version = '0.1'

# If your timestamp looks like 06/Dec/2011:13:12:48

class DateSlashTimeColon(object):

	def __init__(self, timestamp):
		self.timestamp = timestamp

	# Splits up timestamp
	def date_and_time(self):
		date = re.search(r'([0-9]{2}/\w{3}/[0-9]{4})', self.timestamp)
		time = re.search(r':([0-9]{2}:[0-9]{2}:[0-9]{2})', self.timestamp)
		return date.group(0), time.group(1)

class MathTime(object):

	def __init_(self, time):
		self.time = time

	# Converts time to seconds to calculation
	def time_to_seconds(self):
		h, m, s = [int(i) for i in self.time.split(':')]
		print (3600 * h) + (60 * m) + s

	# Calculates amount of time spend on item and converts seconds back to time format
	'''def calculate_time(time1, time2):
		sec = time_to_seconds(time2) - time_to_seconds(time1)
		return datetime.timedelta(seconds = sec)'''
