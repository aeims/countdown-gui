from datetime import datetime, timedelta
from time import sleep

our_date = datetime(year=2022, month=7, day=6, hour=14, minute=56)
def cnt():
    countdown = our_date - datetime.now().replace(microsecond=0)
    print(f"\rCountdown to date: {countdown}", end='')

    if countdown == timedelta(0):
        print('\n🥳🍾yeeeaaah time to dance!🎉😎')
    else:
        sleep(1)
        cnt()

cnt()