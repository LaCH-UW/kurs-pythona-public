
from datetime import datetime, timedelta
from dateutil import relativedelta

now = datetime.now()
print(now)

long_time_ago = datetime(year=2010, month=4, day=6, hour=10, minute=59, second=7)
print(long_time_ago)

time_passed = now - long_time_ago
print(time_passed)

three_days_from_now = now + timedelta(days=3)
print(three_days_from_now)

three_months_from_now = now + relativedelta.relativedelta(months=+2)
print(three_months_from_now)