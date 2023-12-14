# Timer Demo
# Mr. Scott
# Dec 14, 2023
# Using the time library to measure elapsed time

import time, microbit

# time.sleep(s) - delay s seconds
# time.time() - reports time since EPOCH
# epoch - Jan 1, 1970 0:00 UTC

# print(time.time()) #print the current time

start_time = time.time()  #snapshot of "time"
while True:
    current_time = time.time()  #updated each iteration
    elapsed_time = current_time - start_time
#     print(f"S: {start_time} \t C: {current_time}")
    print(elapsed_time)
    if microbit.button_a.was_pressed():
        start_time = time.time()
    if elapsed_time > 5:
        print("Sorry - you forgot to press A")
        break

