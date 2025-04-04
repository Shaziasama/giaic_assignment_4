#project 5 count down timmer

import time

def count_timers(seconds):
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        time_format = '{:02d}:{:02d}'.format(mins, secs)
        print(time_format, end='\r', flush=True)  # Overwrite the same line
        time.sleep(1)  # Delay of 1 second
        seconds -= 1

    print("\n00:00 \n     Time is up!")

# User input for timer
total_seconds = int(input("Enter time in seconds for countdown: "))
count_timers(total_seconds)
