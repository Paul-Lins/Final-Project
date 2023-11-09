#a time variable for testing, in the final we will get this from the file
time = "00:51:13"
bodyweight = 70

def time_in_minutes(time):
    total_time = 0
    time = time.split(":")
    total_time += int(time[0]) * 60
    total_time += int(time[1])
    total_time += int(time[2]) / 60
    return total_time


def biking_calories_burned(difficulty, time):
    time = time_in_minutes(time)
    if difficulty == "E":
        MET = 4
    elif difficulty == "M":
        MET = 8
    elif difficulty == "H":
        MET = 12
    return ((3.5 * MET * bodyweight) / 200) * time

