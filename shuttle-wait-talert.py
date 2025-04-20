import time
from datetime import datetime, timedelta

# Bus details
bus_arrival_time = datetime.strptime("07:30", "%H:%M")  # Bus arrives at 7:30 AM

# Function to check if the bus should wait
def should_bus_wait(student_distance, current_time):
    if student_distance <= 3:
        print("The bus is waiting for the student.")
    else:
        print("The bus is leaving.")

# Function to calculate the time remaining before the bus leaves
def time_remaining(bus_time, current_time):
    remaining_time = bus_time - current_time
    return remaining_time.total_seconds() / 60  # Return time in minutes

# Function to simulate getting the distance of the student
def get_student_distance():
    # Simulate the student being 5 minutes away
    return 3  # Simulate that the student is 3 minutes away

# Main loop that checks the condition every minute
def main():
    while True:
        current_time = datetime.now()
        student_distance = get_student_distance()

        # Check if the student will make it
        remaining_minutes = time_remaining(bus_arrival_time, current_time)

        if remaining_minutes <= 3:  # If the bus is within 3 minutes of leaving
            should_bus_wait(student_distance, current_time)

        time.sleep(60)  # Check every minute

if __name__ == "__main__":
    main()

#bus_arrival_time: This is the time the bus is scheduled to arrive.
#should_bus_wait: This function checks if the bus should wait for the student based on the student's distance.
#time_remaining: Calculates the time remaining before the bus leaves.
#get_student_distance: Simulates getting the student's current distance. Right now, it's set to 3 minutes, but this could be replaced by actual data.
#main: Continuously checks if the bus should wait for the student, checking the time every minute.
# List of students and how many minutes away they are
students = {
    "Alex": 2,
    "Brianna": 4,
    "Chris": 3,
    "Dana": 1,
    "Eli": 6
}

# Max wait time in minutes
MAX_WAIT_TIME = 3

# Check who the bus should wait for
def check_students(students):
    for name, minutes_away in students.items():
        if minutes_away <= MAX_WAIT_TIME:
            print(f"The bus will wait for {name} (they are {minutes_away} minutes away).")
        else:
            print(f"The bus will NOT wait for {name} (they are {minutes_away} minutes away).")

# Run the check
check_students(students)
