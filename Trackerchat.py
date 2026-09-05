#--------------------------TITLE------------------------------------------------

print("Daily Wellbeing Check-In\n")

#--------------------------INPUT FUNCTIONS----------------------------------

def getname():
    name = input("Enter your name: ")

def getmood():
    while True:
        mood = float(input("\nRate your mood (1-10): "))
        if mood > 10 or mood < 1:
            print("Please enter a value between 1 - 10")
        else:
            return mood
            break

def getstress():
    while True:
        stress = float(input("Rate your stress (1-10): "))
        if stress > 10 or stress < 1:
            print("Please enter a value between 1 - 10")
        else:
            return stress
            break

def getanxiety():
    while True:
        anxiety = float(input("Rate your anxiety (1-10): "))
        if anxiety > 10 or anxiety < 1:
            print("Please enter a value between 1 - 10")
        else:
            return anxiety
            break

def getenergy():
    while True:
        energy = float(input("Rate your energy (1-10): "))
        if energy > 10 or energy < 1:
            print("Please enter a value between 1 - 10")
        else:
            return energy
            break

def getsleep():
    while True:
        sleep = float(input("How many hours did you sleep? "))
        if sleep<1:
            print("Please enter a correct value")
        else:
            return sleep
            break

#-----------------------------------------MAIN CODE BLOCK-----------------------------------

def welltrack():

    name = getname()
    mood = getmood()
    stress = getstress()
    anxiety = getanxiety()
    energy = getenergy()
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
