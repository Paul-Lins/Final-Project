#imports the formula file
import formulas

class person_profile():

    #data of calories burned in each activity type stored in a dictionary
    calories_per_activity = {
        "Running" : 0,
        "Biking" : 0,
        "Swimming" : 0
    }

    #initiation of the object
    def __init__(self, name = "Unknown", bodyweight = 80):
        self.name = name
        self.bodyweight = bodyweight

    #gets the MET values for each activity and difficulty, and puts them into a formula with the user's weight to determine their calories burned
    def calories_burned(self, activity, difficulty, time):
        time = formulas.time_in_minutes(time)
        #nested selection statements to determine the MET value for each activity and difficulty
        if activity == "Biking":
            if difficulty == "E":
                MET = 4
            elif difficulty == "M":
                MET = 8
            elif difficulty == "H":
                MET = 12
        elif activity == "Running":
            if difficulty == "E":
                MET = 8
            elif difficulty == "M":
                MET = 11
            elif difficulty == "H":
                MET = 14
        elif activity == "Swimming":
            if difficulty == "E":
                MET = 6
            elif difficulty == "M":
                MET = 7
            elif difficulty == "H":
                MET = 10
        #The formula that calculates calories burned
        return formulas.calories_burned_formula(MET, self.bodyweight, time)
    

    #appends an activity to the user's txt file
    def add_activity(self, activity, time, difficulty):
        #open file, write the data in the correct format, and close the file
        file = open(self.name + ".txt", "a")
        file.write(f"\n{activity} {time} {difficulty}")
        file.close()


    #prints the total calories burned to the console, both seperated by activity, and all put together
    def print_total_calories_burned(self):
        file = open(self.name + ".txt", "r")
        #this data is stored in a list
        file_parse = file.read().split()
        total = 0
        for i in range(5, len(file_parse), 3):
            self.calories_per_activity[file_parse[i]] += self.calories_burned(file_parse[i], file_parse[i + 2], file_parse[i + 1])
            total += self.calories_burned(file_parse[i], file_parse[i + 2], file_parse[i + 1])
        file.close()
        print(f"Calories burned running: {self.calories_per_activity['Running']:0.2f}")
        print(f"Calories burned biking: {self.calories_per_activity['Biking']:0.2f}")
        print(f"Calories burned swimming: {self.calories_per_activity['Swimming']:0.2f}")
        print(f"Total calories burned: {total:0.2f}")

    #gets the total calories burned, and returns it
    def get_total_calories_burned(self):
        file = open(self.name + ".txt", "r")
        file_parse = file.read().split()
        total = 0
        for i in range(5, len(file_parse), 3):
            total += self.calories_burned(file_parse[i], file_parse[i + 2], file_parse[i + 1])
        file.close()
        return total

    #prints an estimation of weight loss to the console (assumes a diet that approximately matches the user's resting metabolic rate)
    def estimated_total_weight_loss(self):
        calories_burned = self.get_total_calories_burned()
        print(f"Estimated weight loss: {formulas.weight_lost(calories_burned):0.2f} kg")