# ymdhms.py
#
# Usage: python3 ymdhms_to_jd.py year month day hour minute second
#  Converts year, month, day, hour, minute, second to fractional Julian date
# Parameters:
#  year: year
#  month: month
#  day: day
#  hour: hour
#  minute: minute
#  second: second
#  ...
# Output:
#  Fractional Julian Date
#
# Written by Tejas Vinod
# Other contributors: None
#
# Optional license statement, e.g., See the LICENSE file for the license.
#
# Test 
# python3 ymdhms_to_jd.py 1965 6 3 19 46 0
# 2438915.323611
# python3 ymdhms_to_jd.py 1966 6 5 15 02 0
# 2439282.126389

# import Python modules
import math # math module
import sys # argv

# "constants"

# helper functions
## function description


# initialize script arguments
year = float('nan') 
month = float('nan') 
day = float('nan') 
hour = float('nan') 
minute = float('nan') 
second = float('nan') 

# parse script arguments
if len(sys.argv)==7:
    year = float(sys.argv[1])
    month = float(sys.argv[2])
    day = float(sys.argv[3])
    hour = float(sys.argv[4]) 
    minute = float(sys.argv[5])
    second = float(sys.argv[6])
else:
  print(\
   'Usage: '\
   'python3 ymdhms_to_jd.py year month day hour minute second'\
  )
  exit()

# write script below this line

JD = day - 32075 + int((1461 * (year + 4800 + int((month - 14) / 12))) / 4) + int((367 * (month - 2 - 12 * int((month - 14) / 12))) / 12) - int((3 * int(int(year + 4900 + (month - 14) / 12) / 100)) / 4)
JD_midnight = JD - 0.5
D_fractional = (second + 60 * (minute + 60 * hour)) / 86400
JD_fractional = JD_midnight + D_fractional

print(JD_fractional)