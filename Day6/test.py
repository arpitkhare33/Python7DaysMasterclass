# import the time module
import time


# define the countdown func.
def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = f"{mins} Minutes:{secs} Seconds"
        print(timer)
        time.sleep(1)
        t -= 1

    print('Fire in the hole!!')


# input time in seconds 
t = input("Enter the time in seconds: ")

# function call 
countdown(int(t)) 