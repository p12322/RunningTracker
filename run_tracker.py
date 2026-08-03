print("Welcome to Running Tracker!")

runs = []

def runtrack():
    distance = float(input("Enter the distance ran (miles): "))
    time = float(input("Enter the time taken (minutes): "))
    notes = input("Notes? (Press Enter to skip): ")
    mins = time / distance
    sec = mins * 60
    minutes, seconds = divmod(sec, 60)

    return distance, time, notes, sec, minutes, seconds

def printlog(distance, time, notes, sec, minutes, seconds):

    pace_str = f"{int(minutes)}:{int(seconds):02d}"

    print(f"{distance} miles in {time} minutes logged! Notes: {notes}")
    print(f"You're average pace for this run was {pace_str}/mile.")
    runs.append({
        "distance (miles)": distance,
        "time (minutes)": time,
        "notes": notes,
        "pace (min/mile)": pace_str
    })

while True:
    distance, time, notes, sec, minutes, seconds = runtrack()

    printlog(distance, time, notes, sec, minutes, seconds)

    again = input("Would you like to log another run? (y/n): ")
    if again != 'y':
        break

display_log = input("Display running log? (y/n): ")
if display_log == 'y':
    for run in runs:
        print(run)

def show_stats():
    statlog = input("Would you like to see your running stats? (y/n): ")
    if statlog == 'y':
        print(f"Total runs logged: {len(runs)}")
        print(f"Distance ran: {sum(run['distance (miles)'] for run in runs)} miles")
        print(f"Total time ran: {sum(run['time (minutes)'] for run in runs)} minutes")

show_stats() 

input("Thank you for using Running Tracker! (Press Enter to exit.)")