import time

while (True):
    date_and_time = time.ctime()
    time_only = date_and_time[11:20]
    week_day = date_and_time[0:4]
    date = date_and_time[4:11]
    print(f"Day: {week_day} Date: {date} Time: {time_only}", end="\r")
    # print(time_only, end='\r')
    time.sleep(1)