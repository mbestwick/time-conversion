""" Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.

Note: Midnight is 12:00:00AM on a 12-hour clock, and 00:00:00 on a 24-hour clock.
Noon is 12:00:00pm on a 12-hour clock, and 12:00:00 on a 24-hour clock.

Input Format
A single string containing a time in 12-hour clock format
(i.e.hh:mm:ssAM or hh:mm:ssPM), where 01 <= hh <= 12 and 00 <= mm, ss <= 59.

Output Format
Convert and print the given time in 24-hour format, where 00 <= hh <= 23.

Sample Input
07:05:45PM

Sample Output
19:05:45

"""

time = raw_input().strip()

night = 0
if 'PM' in time:
    night = 12

time = time[:8].split(':')

if time[0] == '12':
    time[0] = 0

time[0] = str(int(time[0]) + night)

newtime = str()
for x in time:
    newtime += x + ':'

if len(newtime) < 9:
    newtime = '0' + newtime

print newtime[:8]
