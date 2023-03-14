'''
Contains the code for running a game
'''
import game

ucu = game.Location("UCU")
ucu.set_description("Our university, the beginning and end of all journeys")
student = game.Student(
    'Student', 'An Artes student', 'Beer', 1)
student.set_conversation('I want a refreshing drink')
ucu.set_character(student)

rukavychka = game.Location("Rukavychka")
rukavychka.set_description("Has everything a student needs")
rukavychka.set_item(game.Gift('beer', 'A can of Lvivske beer', 1))
ucu.link_location(rukavychka, "west")
rukavychka.link_location(ucu, "east")

stryiskyi_park = game.Location("Stryiskyi Park")
stryiskyi_park.set_description(
    "Beautiful by day, dangerous by night")
stryiskyi_park.set_item(game.Weapon(
    'bottle', 'Can be used as a weapon. Once', 1))
ucu.link_location(stryiskyi_park, "north")
stryiskyi_park.link_location(ucu, "south")

shevchenko_square = game.Location("Shevchenko Square")
stryiskyi_park.set_description(
    "Tram tracks surround this quaint square")
shevchenko_square.link_location(stryiskyi_park, "south")
stryiskyi_park.link_location(shevchenko_square, "north")

danylo_monument = game.Location("King Danylo Monument")
danylo_monument.set_description(
    "A horseback monument to King Danylo of Galicia")
danylo_monument.link_location(shevchenko_square, "south")
shevchenko_square.link_location(danylo_monument, "north")

synagogue = game.Location("Synagogue")
synagogue.set_description(
    "An alt hangout spot")
synagogue.link_location(danylo_monument, "west")
danylo_monument.link_location(synagogue, "east")

opera_theater = game.Location("Opera Theater")
opera_theater.set_description(
    "A massive 19th century theater")
opera_theater.link_location(danylo_monument, "south")
danylo_monument.link_location(opera_theater, "north")

shotitam = game.Location("Shotitam")
shotitam.set_description(
    "A famous bar and your destination")
friend = game.Item(
    'Friend', 'Your drunk friend')
shotitam.set_item(friend)
shotitam.link_location(opera_theater, "east")
shotitam.link_location(synagogue, "south")
opera_theater.link_location(shotitam, "west")
synagogue.link_location(shotitam, "north")

current_location = ucu
backpack = []
HEALTH = 1

FINISHED = False

print("Hi!\nYou have to pick up your drunk friend from shotitam\n\
It's late and public transport is no longer running so you'll have to walk(")

while not FINISHED:
    print('\n')
    if current_location is ucu and friend in backpack:
        print("You've finally gotten home with your friend")
        FINISHED = True
        break
    current_location.get_details()

    inhabitant = current_location.get_character()
    if inhabitant is not None:
        inhabitant.describe()

    item = current_location.get_item()
    if item is not None:
        item.describe()

    command = input("> ")

    if command in ["north", "south", "east", "west"]:
        # Move in the given direction
        current_location = current_location.move(command)
    elif command == "talk":
        # Talk to the inhabitant - check whether there is one!
        if inhabitant is not None:
            inhabitant.talk()
    elif command == "fight":
        if inhabitant is not None and issubclass(type(inhabitant), game.Enemy):
            # Fight with the inhabitant, if there is one
            print("What will you fight with?")
            gift_with = input()

            # Do I have this item?
            FOUND = False
            for i, item in enumerate(backpack):
                if item.get_name() == gift_with and isinstance(item, game.Weapon):
                    FOUND = True
                    if backpack[i].use():
                        if inhabitant.fight(gift_with):
                            print("Hooray, you won the fight!")
                            backpack.append(
                                current_location.character.get_weapon())
                            current_location.character = None
                        else:
                            HEALTH -= 1
                            if HEALTH == 0:
                                print("Oh dear, you lost the fight.")
                                print("That's the end of the game")
                                FINISHED = True
                            else:
                                print(
                                    f'Ouch. You have {HEALTH} health points left')
                    else:
                        print('Item used up')
                    break
            if not FOUND:
                print("You don't have a " + gift_with)
        else:
            print("There is no one here to fight with")
    elif command == "gift":
        if inhabitant is not None and issubclass(type(inhabitant), game.Friend):
            # Give the inhabitant a gift, if there is one
            print("What will you gift?")
            gift_with = input()

            # Do I have this item?
            FOUND = False
            for i, item in enumerate(backpack):
                if item.get_name() == gift_with and isinstance(item, game.Gift):
                    FOUND = True
                    if inhabitant.gift(gift_with):
                        print(
                            f"Hooray, you have recruited {current_location.character.name}!")
                        if isinstance(current_location.character, game.Cavaler):
                            backpack.append(
                                current_location.character.get_weapon())
                        else:
                            HEALTH += current_location.character.give_health()
                        current_location.character = None
                    else:
                        print("You've used up the gift and achieved nothing")
                    break
            if not FOUND:
                print("You don't have a " + gift_with)
        else:
            print("There is no one here to gift to")
    elif command == "take":
        if item is not None:
            print("You put the " + item.get_name() + " in your backpack")
            backpack.append(item)
            current_location.set_item(None)
        else:
            print("There's nothing here to take!")
    else:
        print("I don't know how to " + command)
