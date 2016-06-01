

- https://pypi.python.org/pypi/icalendar/
- http://icalendar.readthedocs.io/en/latest/


サンプル:

~~~py
import requests
from icalendar import Calendar
from datetime import datetime

url = 'https://www.google.com/calendar/ical/ja.japanese%23holiday%40group.v.calendar.google.com/public/basic.ics'

res = requests.get(url)
cal = Calendar.from_ical(res.content)
now = datetime.now()
for ev in cal.walk('vevent'):
    date = ev.get('dtstart')
    if date.dt.year == now.year:
        summary = ev.get('summary')
        print u"{}: {}".format(date.dt, summary)
~~~        
