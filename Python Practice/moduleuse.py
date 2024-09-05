# from module1 import mul 
# print(mul(8,2))
import datetime
import pytz
d = datetime.date(2002,12,18) # Working with years, months & dates 
print(d)
tday = datetime.date.today()
print(tday)
print(tday.year)
# To get day of week : 2 ways:
# weekday: mon: 0, sun: 6
print(tday.weekday())
# or 
# Isoweekday: mon: 1, sun:7
print(tday.isoweekday())
# Timedeltas: diff betn 2 dates or times : used to perform operations on dates & times 
tdelta = datetime.timedelta(days=7)
# If I want date after 7 days from today : see below code 
print(tday + tdelta) 
# If I want date before 7 days from today : see below code 
print(tday - tdelta)
# date1 = date2 + timedelta 
# timedelta = date1 + date2 
bday = datetime.date(2023,12,6)
till_bday = bday-tday 
print(till_bday.total_seconds()) 

t = datetime.time(9,30,45,100000) # Working with hrs,mins,seconds,microseconds  
print(t.hour)

dt = datetime.datetime(2023,9,1,6,45,50,100000) # Working with hrs,mins,seconds,microseconds,years, months & dates i.e.: working with everything 
print(dt)
print(dt.date())
print(dt.time())
print(dt.month)
tdelta = datetime.timedelta(hours = 5)
print(dt + tdelta)

# dt_today = datetime.datetime.today()
# dt_now = datetime.datetime.now()
# dt_utcnow = datetime.datetime.utcnow() 
# print(dt_today)
# print(dt_now)
# print(dt_utcnow)

# Always work with utc when dealing with timezones 
# dt_new = datetime.datetime(2023,9,1,6,45,50,tzinfo=pytz.UTC)
# print(dt_new)

# 2 ways to get timezone info 
# dt_now = datetime.datetime.now(tz=pytz.UTC) # Passing timezone : 1st way: recommended to use mostly 
# print(dt_now)
# dt_utcnow = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC) # can't pass timezone : 2nd way 
# print(dt_utcnow)

dt_utcnow = datetime.datetime.now(tz=pytz.UTC) # Passing timezone : 1st way: recommended to use mostly 
print(dt_utcnow)
# dt_ind = dt_utcnow().astimezone(pytz.timezone('Asia/Calcutta'))
# print(dt_ind)

# for tz in pytz.all_timezones:
#     print(tz)

dt_ind = datetime.datetime.now()
mtn_tz = pytz.timezone('Asia/Oral')
dt_east = dt_ind.astimezone(pytz.timezone('Asia/Calcutta'))
print(dt_east)
dt_ind = mtn_tz.localize(dt_ind)
# print(dt_ind)


dt_ind = datetime.datetime.now(tz=pytz.timezone('US/Mountain'))
print(dt_ind.isoformat())

print(dt_ind.strftime('%B %d, %Y'))

dt_str = 'October 07, 2023'
dt = datetime.datetime.strptime(dt_str,'%B %d, %Y')
print(dt) 

# strftime - Datetime to String 
# strptime - String to Datetime 