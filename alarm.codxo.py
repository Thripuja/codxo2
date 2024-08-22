import time
from datetime import datetime


def set_alarm(target_time):

    try:
        target_time = datetime.strptime(target_time, "%H:%M").time()
    except ValueError:
        print("Time must be in HH:MM format.")
        return

    print(f"Alarm set for {target_time}.")

    while True:
        # Get the current time
        now = datetime.now().time()

        # Check if it's time to trigger the alarm
        if now >= target_time:
            print("ALARM! Time to wake up!")
            break

        # Sleep for a short period to avoid busy waiting
        time.sleep(30)


# Example usage
if __name__ == "__main__":
    alarm_time = input("Enter alarm time (HH:MM): ")
    set_alarm(alarm_time)