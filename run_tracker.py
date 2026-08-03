import json

def load_runs():
    try:
        with open("runlog.json", "r") as file:
            runs = json.load(file)
            return runs
    except FileNotFoundError:
        return []

runs = load_runs()

print("Welcome to Running Tracker!")

def runtrack():
    distance = float(input("Enter the distance ran (miles): "))
    time = float(input("Enter the time taken (minutes): "))
    notes = input("Notes? (Press Enter to skip): ")

    mins = time / distance
    sec = mins * 60
    minutes, seconds = divmod(sec, 60)

    pace_str = f"{int(minutes)}:{int(seconds):02d}"

    run = {
        "distance (miles)": distance,
        "time (minutes)": time,
        "notes": notes,
        "pace (min/mile)": pace_str,
    }

    return run

def save_runs(runs):
    with open("runlog.json", "w") as file:
        json.dump(runs, file, indent=2, ensure_ascii=False)


while True:
    run = runtrack()

    runs.append(run)

    print(f"{run['distance (miles)']} miles in {run['time (minutes)']} minutes logged! Notes: {run['notes']}")
    print(f"You're average pace for this run was {run['pace (min/mile)']}/mile.")
    
    save_runs(runs)

    again = input("Would you like to log another run? (y/n): ")
    if again != 'y':
        break

def show_runs():
    display_log = input("Display running log? (y/n): ")
    if display_log == 'y':
        for run in runs:
            print(run)

show_runs()

def show_stats():
    statlog = input("Would you like to see your running stats? (y/n): ")
    if statlog == 'y':
        print(f"Total runs logged: {len(runs)}")
        print(f"Distance ran: {sum(run['distance (miles)'] for run in runs)} miles")
        print(f"Total time ran: {sum(run['time (minutes)'] for run in runs)} minutes")

show_stats() 

input("Thank you for using Running Tracker! (Press Enter to exit.)")