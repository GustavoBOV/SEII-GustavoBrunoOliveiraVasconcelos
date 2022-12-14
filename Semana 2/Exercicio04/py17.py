import datetime

d = datetime.date(2016, 7, 24)
print(d)

tday = datetime.date.today()
print(tday)
print(tday.weekday())

tdelta = datetime.timedelta(days=7)
print(tday + tdelta)
print(tday + tdelta)

bday = datetime.date(2021, 10, 2)
till_bday = bday - tday

print(till_bday)
print(till_bday.days)
print(till_bday.total_seconds())

t = datetime.time(9, 30, 45, 100000)
print(t)
print(t.hour)

dt = datetime.datetime(2016, 7, 26, 12, 30, 45, 100000)
print(dt)  

tdelta = datetime.timedelta(hours=12)
print(dt + tdelta)

dt_today = datetime.datetime.today()
dt_now = datetime.datetime.now()
dt_utcnow = datetime.datetime.utcnow()
print(dt_today)
print(dt_now)
print(dt_utcnow)

import pytz

dt = datetime.datetime(2016, 7, 27, 12, 30, 45, tzinfo=pytz.UTC)
print(dt)

dt_now = datetime.datetime.now(tz=pytz.UTC)
print(dt_now)

dt_utcnow = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
print(dt_utcnow)

print('')
for tz in pytz.all_timezones:
    print(tz)

dt_utcnow = datetime.datetime.now(tz=pytz.UTC)
print(dt_utcnow)

dt_mtn = dt_utcnow.astimezone(pytz.timezone('US/Mountain'))
print(dt_mtn)

dt_mtn = datetime.datetime.now()
mtn_tz = pytz.timezone('US/Mountain')
dt_mtn = mtn_tz.localize(dt_mtn)
dt_east = dt_mtn.astimezone(pytz.timezone('US/Eastern'))
print(dt_east)

print('')
dt_mtn = datetime.datetime.now(tz=pytz.timezone('US/Mountain'))
print(dt_mtn.isoformat())
print(dt_mtn.strftime('%B %d, %Y'))
dt_str = 'March 14, 2021'
dt = datetime.datetime.strptime(dt_str, '%B %d, %Y')
print(dt)
