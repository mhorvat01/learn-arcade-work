def main():
    import random
    import arcade
    print("""Welcome to Formula Drift Heist!
You have stolen a Formula Drift car from Formula Drift to make your way across New York City.
Formula D wants their car back and are chasing you down! Survive your
drift adventure and make it out of the city!
""")

    SCREEN_WIDTH = 1340
    SCREEN_HEIGHT = 800

    def imprison_screen():
        arcade.open_window(1340, 800, "Imprison Screen")
        arcade.set_background_color(arcade.csscolor.BLACK)

        def imprison_message():
            arcade.draw_text("YOU WERE IMPRISONED", 430, 400, arcade.csscolor.RED, 30)

        arcade.start_render()
        imprison_message()
        arcade.finish_render()
        arcade.run()

    def death_screen():
        arcade.open_window(1340, 800, "Death Screen")
        arcade.set_background_color(arcade.csscolor.BLACK)

        def death_message():
            arcade.draw_text("YOU DIED", 550, 400, arcade.csscolor.RED, 30)

        arcade.start_render()
        death_message()
        arcade.finish_render()
        arcade.run()


    def victory_screen():
        arcade.open_window(1340, 800, "Drift Game")
        arcade.set_background_color(arcade.csscolor.BLUE)

        def building(x, y):
            arcade.draw_rectangle_filled(200 + x, 500 + y, 100, 620, arcade.csscolor.WHITE)
            arcade.draw_rectangle_filled(180 + x, 760 + y, 30, 50, arcade.csscolor.BLACK)
            arcade.draw_rectangle_filled(220 + x, 760 + y, 30, 50, arcade.csscolor.BLACK)
            arcade.draw_rectangle_filled(180 + x, 700 + y, 30, 50, arcade.csscolor.BLACK)
            arcade.draw_rectangle_filled(220 + x, 700 + y, 30, 50, arcade.csscolor.BLACK)
            arcade.draw_rectangle_filled(180 + x, 640 + y, 30, 50, arcade.csscolor.BLACK)
            arcade.draw_rectangle_filled(220 + x, 640 + y, 30, 50, arcade.csscolor.BLACK)
            arcade.draw_rectangle_filled(180 + x, 580 + y, 30, 50, arcade.csscolor.BLACK)
            arcade.draw_rectangle_filled(220 + x, 580 + y, 30, 50, arcade.csscolor.BLACK)
            arcade.draw_rectangle_filled(180 + x, 520 + y, 30, 50, arcade.csscolor.BLACK)
            arcade.draw_rectangle_filled(220 + x, 520 + y, 30, 50, arcade.csscolor.BLACK)
            arcade.draw_rectangle_filled(180 + x, 460 + y, 30, 50, arcade.csscolor.BLACK)
            arcade.draw_rectangle_filled(220 + x, 460 + y, 30, 50, arcade.csscolor.BLACK)
            arcade.draw_rectangle_filled(180 + x, 400 + y, 30, 50, arcade.csscolor.BLACK)
            arcade.draw_rectangle_filled(220 + x, 400 + y, 30, 50, arcade.csscolor.BLACK)
            arcade.draw_rectangle_filled(180 + x, 340 + y, 30, 50, arcade.csscolor.BLACK)
            arcade.draw_rectangle_filled(220 + x, 340 + y, 30, 50, arcade.csscolor.BLACK)
            arcade.draw_rectangle_filled(180 + x, 280 + y, 30, 50, arcade.csscolor.BLACK)
            arcade.draw_rectangle_filled(220 + x, 280 + y, 30, 50, arcade.csscolor.BLACK)
            arcade.draw_rectangle_filled(180 + x, 220 + y, 30, 50, arcade.csscolor.BLACK)
            arcade.draw_rectangle_filled(220 + x, 220 + y, 30, 50, arcade.csscolor.BLACK)

        def street():
            arcade.draw_rectangle_filled(670, 150, 1340, 300, arcade.csscolor.GRAY)

        def dotted_yellow(x, y):
            arcade.draw_rectangle_filled(0 + x, 150 + y, 40, 20, arcade.csscolor.YELLOW)

        def race_car():
            arcade.draw_rectangle_filled(540, 185, 10, 200, arcade.color.BLACK, -50)
            arcade.draw_rectangle_filled(480, 250, 150, 20, arcade.color.BLACK)
            arcade.draw_arc_filled(700, 185, 200, 100, arcade.csscolor.BLACK, 0, 180)
            arcade.draw_rectangle_filled(670, 150, 300, 70, arcade.csscolor.RED)
            arcade.draw_triangle_filled(820, 185, 820, 115, 1020, 115, arcade.csscolor.RED)
            arcade.draw_circle_filled(560, 120, 40, arcade.csscolor.BLACK)
            arcade.draw_circle_filled(820, 120, 40, arcade.csscolor.BLACK)

        def victory_message():
            arcade.draw_rectangle_filled(670, 600, 800, 100, arcade.csscolor.BLACK)
            arcade.draw_text("CONGRATULATIONS, YOU WON!", 350, 600, arcade.csscolor.GREEN, 30)
        def balloon(x, y):
            arcade.draw_circle_filled(x, y, 40, arcade.csscolor.ORANGE_RED)
            arcade.draw_line(x, y - 40, x, y - 200, arcade.csscolor.BLUE_VIOLET, 5)
        arcade.start_render()
        street()
        i = 0
        x = 0
        while i < 17:
            x += 80
            i += 1
            dotted_yellow(x, 0)
        race_car()
        c = -300
        for i in range(15):
            c += 100
            building(c, 100)
        balloon(200, 500)
        balloon(600, 700)
        balloon(900, 500)
        balloon(1000, 720)
        balloon(320, 400)
        balloon(440, 500)
        balloon(1200, 640)
        balloon(100, 300)
        victory_message()
        arcade.finish_render()
        arcade.run()


    milestraveled = 0
    wheels = 0
    gas = 10
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
            print("Your car has ", gas, " gas left.")
            print("The Formula D crew is ", crewbehind, "miles behind you.")
        elif userinput.lower() == "d":
            gas += 10
            print("Your car is refueled. ")
            formulacrew += random.randrange(7, 15)
        elif userinput.lower() == "c":
            print("You traveled ", fullspeed, "miles!")
            milestraveled += fullspeed
            wheels += 1
            gas -= random.randrange(1, 4)
            formulacrew += random.randrange(7, 15)
            if tireshop_chance == 5:
                found_tireshop = True
            if found_tireshop:
                gas += 10
                wheels *= 0
                wheelsleft = 3
                print("You found a tire shop! After getting a new set of tires, you put another three sets in the trunk.")
        elif userinput.lower() == "b":
            print("You traveled ", moderatespeed, "miles!")
            milestraveled += moderatespeed
            wheels += 1
            gas -= 1
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
                gas += 10
                wheels *= 0
                wheelsleft = 3
                print("You found a tire shop! After getting a new set of tires, you put another three sets in the trunk.")
        if crewbehind <= 15:
            print("The formula drift crew is drawing near!")
        if milestraveled >= 200 and not done:
            print("You made it across the city, you win!")
            victory_screen()
            done = True
        if formulacrew >= milestraveled:
            print("The Formula Drift crew caught and imprisoned you.")
            print("You are in prison!")
            imprison_screen()
            done = True
        if wheels > 4 and wheels <= 6 and not done:
            print("You need new tires!")
        if wheels > 6:
            print("Your tires blew and you hit a semi-truck, you instantly died!")
            death_screen()
            done = True
        if gas < 5 and gas <= 6 and not done:
            print("Your car is low on gas!")
        if gas < 1:
            print("Your car is out of gas, you were caught and imprisoned")
            imprison_screen()
            done = True
main()