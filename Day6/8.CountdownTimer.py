# Take input from user: target_time
import time


# Define countdown function
def countdown(target_time):
    while target_time >= 0:
        mins, secs = divmod(target_time, 60)
        print(f"{mins} Minutes: {secs} Seconds")
        time.sleep(1)
        target_time = target_time - 1
    print("Timer Fired.")
# Trigger function


t_time = int(input("Enter the number of seconds for the timer: "))
countdown(t_time)

