#!/usr/bin/python
from icalendar import Calendar, Event
import requests

start = {}
stop = {}
circ = {1: 'Main', 2: 'Water', 3: 'Bed'}

url = "https://www.google.com/calendar/ical/mkrasnay80%40gmail.com/public/basic.ics"
r = requests.get(url)
#writing to file for troubleshooting only
f = open('mycal.ics' , 'w')
f.write(r.content)
f.close


g = open('mycal.ics','rb')
gcal = Calendar.from_string(r.content)
for component in gcal.walk():
    if component.name == "VEVENT":
	if component.get('summary') == 'cottage main':
		start[1] = component.get('dtstart')
		stop[1] = component.get('dtend')

        if component.get('summary') == 'cottage water':
                start[2] = component.get('dtstart')
                stop[2] = component.get('dtend')
            
        if component.get('summary') == 'cottage bed':
                start[3] = component.get('dtstart')
                stop[3] = component.get('dtend')


g.close()

#format the dtstart and dtend times to that matching the cottage file format
#the google calendar format has a T character separating date and time
#which would screw up <> time calculations in the setcottage.py script
for x in range(1, 4):
	start[x] = str(start[x])
	start[x] = start[x].translate(None, 'T')
	start[x] = start[x][:12]
	stop[x] = str(stop[x])
	stop[x] = stop[x].translate(None, 'T')
	stop[x] = stop[x][:12]


f = open('/home/pi/cottage.txt', 'w')

for y in range(1, 4):
	f.write(circ[y])
	f.write(' ')
	f.write(start[y])
	f.write(' ')
	f.write(stop[y])
	f.write('\n')
f.close

