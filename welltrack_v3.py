#--------------------------TITLE-------------------------------------------------

print("Daily Wellbeing Check-In\n")

#--------------------------INPUT FUNCTION----------------------------------

def getname():
    name = input("Enter your name: ")
    return name

def getrating(label):
    while True:
        rating = float(input("Rate your " + label + " : "))
        if rating > 10 or rating < 1:
            print("Please enter a value between 1-10")
        else:
            return rating

def getsleep():
    while True:
        sleep = float(input("\nHow many hours did you sleep? "))
        if sleep < 1:
            print("Please enter a correct value")
        else:
            return sleep

#-----------------------------------------MAIN CODE BLOCK-----------------------------------

def welltrack():

    name = getname()
    mood = getrating("mood")
    stress = getrating("stress")
    anxiety = getrating("anxiety")
    energy = getrating("energy")
    sleep = getsleep()

    print("Today's Check-In\n")

    print("Name: ", name,"\n")
    print("Mood: ", mood, "/10\n")
    print("Stress: ", stress, "/10\n")
    print("Anxiety: ", anxiety, "/10\n")
    print("Energy: ", energy, "/10\n")
    print("Sleep: ", sleep, "hours\n")

    print("Check-In saved successfully!")

welltrack()
