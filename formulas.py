#takes the time as formated in the txt file as the input, and outputs it as the time in minutes
def time_in_minutes(time):
    total_time = 0
    #split the time into hour, minutes and seconds sections, and calculate them into minutes, before adding them together and return the result
    time = time.split(":")
    total_time += int(time[0]) * 60
    total_time += int(time[1])
    total_time += int(time[2]) / 60
    return total_time

#calculates the calories burned for an activity using MET value, bodyweight, and time of activity
def calories_burned_formula(MET, bodyweight, time):
    return ((3.5 * MET * bodyweight) / 200) * time

#estimates weight loss assuming a diet approximately equaling the user's resting metabolic rate
def weight_lost(calories_burned):
    #3500 calories is approximately 0.45kg in weight loss
    return calories_burned / 3500 * 0.45