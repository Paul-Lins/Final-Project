#imports the file that controls the profiles
import person_profile
#imports os, which is used to check for txt files in order to determine if a user already has a profile
import os


#declaration of variables
programRunning = True
loggedIn = False

#while loop that keeps the program running until it is exited
while programRunning == True:
    #gets the user's name. if they have a profile, they will be logged in with that data, if they do not have a profile, one will be made and they will then be logged into it
    user = input("What is your name? ")

    #I had to look this up. globals() is all the global variables, and can be used to check if a profile has been created for that person
    if user in globals():
        #there is a profile for this person
        print("Profile found")
    #also looked this up. os.path.isfile checks if there is a file under that name, which would mean we have data on that person, and therefore they should have a profile
    elif os.path.isfile(user + ".txt"):
        file = open(user + ".txt", "r")
        #gets the person's bodyweight from the txt file
        bodyweight = int(file.read().split()[1])
        #had to look this up. execues a line of code that creates a profile object under that person's name (the exec function is necesary because i want to create the object named after the user, whos name changes)
        exec(user + " = person_profile.person_profile(user, bodyweight)")
        print("Profile found")
        file.close()
    else:
        #there is no profile for this person
        #get their bodyweight
        bodyweight = int(input("What is your bodyweight in kg? "))
        #executes a line of code that creates a profile object under that person's name
        exec(user + " = person_profile.person_profile(user, bodyweight)")
        file = open(user + ".txt", "a")
        file.write(user + " " + str(bodyweight))
        file.write("\nActivity Time Difficulty")
        file.close()
        print("Profile created")
    #after this process, the user is logged in, so the next while loop can start running
    print("logged in")
    loggedIn = True

    while loggedIn == True:
        print("")
        print("What would you like to do?")
        print("To add activity, enter 1")
        print("To get total calories burned, enter 2")
        print("To estimate weight loss, enter 3")
        print("To logout, enter 4")
        print("To exit the program, enter 5")
        #depending on the input, respond with the requested data
        action = input("")
        if action == "1":
            activity = input("What activity did you do? (Running, Biking, or Swimming) ")
            time = input("How long did you do it for? format (hh:mm:ss) ")
            difficulty = input("What was the difficulty? E(easy), M(meidum), or H(hard) ")
            exec(user + ".add_activity(activity, time, difficulty)")
        if action == "2":
            exec(user + ".print_total_calories_burned()")
        if action == "3":
            exec(user + ".estimated_total_weight_loss()")
        if action == "4":
            break
        if action == "5":
            exit()