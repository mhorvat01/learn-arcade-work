def main():
    import random
    print("""Welcome to Formula Drift Heist!
You have stolen an Formula Drift car from Formula Drift to make your way across New York City.
Formula D wants their car back and are chasing you down! Survive your
drift adventure and make it out of the city!
""")
    milestraveled = 0
    wheels = 0
    gas = 0
    formulacrew = -20
    wheelsleft = 3
    done = False
    found_tireshop = False
    tireshop_chance = random.randrange(1, 21)
    while not done:
        crewbehind = milestraveled - formulacrew
        fullspeed = random.randrange(10,21)
        moderatespeed = random.randrange(5, 13)
        print("""
        A. Change your tires.
        B. Go slowly through traffic.
        C. Drift Between cars.
        D. Get gas.
        E. Status check
        Q. Quit.""")
        print()
        userinput = input("Your choice: ")
        if userinput.lower() == "q":
            done = True

        elif userinput.lower() == "e":
            print("Miles traveled: ", milestraveled)
            print("Tire Sets Left: ", wheelsleft)
            print("Your car has ", gas, "of gas left.")
            print("The Formula D crew is ", crewbehind, "miles behind you.")
        elif userinput.lower() == "d":
            gas *= 0
            print("Your car is refueled. ")
            formulacrew += random.randrange(7, 15)
        elif userinput.lower() == "c":
            print("You traveled ", fullspeed, "miles!")
            milestraveled += fullspeed
            wheels += 1
            gas += random.randrange(1, 4)
            formulacrew += random.randrange(7, 15)
            if tireshop_chance == 5:
                found_tireshop = True
            if found_tireshop:
                gas *= 0
                wheels *= 0
                wheelsleft = 3
                print("You found a tire shop! After getting a new set of tires, you put another three sets in the trunk.")
        elif userinput.lower() == "b":
            print("You traveled ", moderatespeed, "miles!")
            milestraveled += moderatespeed
            wheels += 1
            gas += 1
            formulacrew += random.randrange(7, 15)
            tireshop = random.randrange(1, 21)
        elif userinput.lower() == "a":
            if wheelsleft == 0:
                print("You're out of tires.")
            else:
                wheelsleft -= 1
                wheels *= 0
                print("You have ", wheelsleft, "tire sets left.")
            if tireshop_chance == 5:
                found_tireshop = True
            if found_tireshop:
                gas *= 0
                wheels *= 0
                wheelsleft = 3
                print("You found a tire shop! After getting a new set of tires, you put another three sets in the trunk.")
        if crewbehind <= 15:
            print("The formula drift crew is drawing near!")
        if milestraveled >= 200 and not done:
            print("You made it across the city, you win!")
            done = True
        if formulacrew >= milestraveled:
            print("The Formula Drift crew caught and imprisoned you.")
            print("You are in prison!")
            done = True
        if wheels > 4 and wheels <= 6 and not done:
            print("You need new tires!")
        if wheels > 6:
            print("Your tires blew and you hit a semi-truck, you instantly died!")
            done = True
        if gas > 5 and gas <= 8 and not done:
            print("Your car is low on gas!")
        if gas > 1:
            print("Your car is out of gas, you were captured!")

            done = True
main()