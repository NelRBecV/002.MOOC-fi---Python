# Write your solution here
from datetime import datetime, timedelta

filename: str = input("Filename: ")
start_date: str = input("Starting date (e.g 10.10.1999): ")
sd: datetime = datetime.strptime(start_date, '%d.%m.%Y')
days: int = int(input("How many days?: "))
limit: datetime = datetime.now() - timedelta(days=-days)
total_time: int = 0

#checks if date range is valid
if limit > sd:
    print("Please type in screen time in minutes on each day (TV computer mobile): ")
    minutes_per_day: dict = {}
    start_date: str = datetime.strftime(sd, "%d.%m.%Y")
    end_date: str = datetime.strftime(sd + timedelta(days=(days - 1)), "%d.%m.%Y")

    # Adds minutes per day for each date
    for day in range(days):
        current_day = datetime.strftime(sd + timedelta(days=day), "%d.%m.%Y")
        minutes = input(f'Screen time {current_day} (e.g 99 99 99): ').replace(" ", "/")
        minutes_per_day[f'{current_day}'] = minutes
        total_time += sum([int(i) for i in minutes.split("/")])

    # Saves all data into a txt file
    if ".txt" in filename:
        with open(filename, "w") as records:
            records.write(f"Time period: {start_date}-{end_date}\n")
            records.write(f"Total minutes: {total_time}\n")
            records.write(f"Average minutes: {total_time / len(minutes_per_day):.1f}\n")
            
            for date, time in minutes_per_day.items():
                records.write(f"{date}: {time}\n")
              
        print(f"Data stored in file {filename}")
    else:
        print("ERROR: Not valid filename.")

else:
    print("ERROR: There is no time enough to carry on with analysis")
