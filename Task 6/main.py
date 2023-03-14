'''
Contains the code for running a game
'''
import game

ucu = game.Location("UCU")
ucu.set_description("Our university, the beginning and end of all journeys")
ucu.set_item(game.Weapon(
    'pen', 'Not mightier than the sword', 1))
student = game.Student(
    'Student', 'An Artes student', 'beer', 3)
student.set_conversation('I want a refreshing drink')
ucu.set_character(student)

rukavychka = game.Location("Rukavychka")
rukavychka.set_description("Has everything a student needs")
rukavychka.set_item(game.Gift('beer', 'A can of Lvivske beer'))
ucu.link_location(rukavychka, "west")
rukavychka.link_location(ucu, "east")

stryiskyi_park = game.Location("Stryiskyi Park")
stryiskyi_park.set_description(
    "Beautiful by day, dangerous by night")
stryiskyi_park.set_item(game.Weapon(
    'bottle', 'Can be used as a weapon. Once', 1))
lotr = game.Enemy('Lotr', 'A simple robber', 'bottle')
lotr.set_conversation("umm, give me your monies or I'll hurt you")
stryiskyi_park.set_character(lotr)
ucu.link_location(stryiskyi_park, "north")
stryiskyi_park.link_location(ucu, "south")

shevchenko_square = game.Location("Shevchenko Square")
shevchenko_square.set_description(
    "Tram tracks surround this quaint square")
flower_seller = game.Character('Flower Seller', 'An old woman selling flowers')
flower_seller.set_conversation('A perfect gift for any girl!')
shevchenko_square.set_character(flower_seller)
shevchenko_square.set_item(game.Gift('flower', 'A beautiful flower'))
shevchenko_square.link_location(stryiskyi_park, "south")
stryiskyi_park.link_location(shevchenko_square, "north")

danylo_monument = game.Location("King Danylo Monument")
danylo_monument.set_description(
    "A horseback monument to King Danylo of Galicia")
cavaler = game.Cavaler(
    'Cavaler', 'A confident capable man', 'flower', game.Weapon(
        'sword', 'An elegant weapon, for a more... civilized age', 2))
cavaler.set_conversation('I need something to gift my love')
danylo_monument.set_character(cavaler)
danylo_monument.link_location(shevchenko_square, "south")
shevchenko_square.link_location(danylo_monument, "north")

synagogue = game.Location("Synagogue")
synagogue.set_description(
    "An alt hangout spot")
batyar = game.Enemy(
    'Batyar', "A brutal strong man. You won't be able to fight him, not quite", 'cigarette')
batyar.set_conversation('Aye, have a cig mate?')
synagogue.set_character(batyar)
synagogue.set_item(game.Weapon(
    'cigarette', 'Not a weapon per se, but can calm an enemy', 1))
synagogue.link_location(danylo_monument, "south")
danylo_monument.link_location(synagogue, "north")

opera_theater = game.Location("Opera Theater")
zbui = game.Enemy('Zbui', 'A dangerous bandit', 'sword')
zbui.set_conversation('Your money or your life!')
opera_theater.set_character(zbui)
opera_theater.set_description(
    "A massive 19th century theater")
opera_theater.link_location(danylo_monument, "east")
danylo_monument.link_location(opera_theater, "west")

shotitam = game.Location("Shotitam")
shotitam.set_description(
    "A famous bar and your destination")
friend = game.Item(
    'Friend', 'Your drunk friend')
shotitam.set_item(friend)
laydak = game.Laydak('Drunk', "He's non-responsive")
laydak.set_conversation('...')
shotitam.set_character(laydak)
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
        if command in ['north', 'west'] \
                and inhabitant is not None and issubclass(type(inhabitant), game.Enemy):
            print('Kill the enemy to continue forward')
        else:
            if new_location := current_location.move(command):
                current_location = new_location
    elif command == "talk":
        # Talk to the inhabitant - check whether there is one!
        if inhabitant is not None:
            inhabitant.talk()
    elif command == "fight":
        if inhabitant is not None and issubclass(type(inhabitant), game.Enemy):
            # Fight with the inhabitant, if there is one
            print("What will you fight with?")
            fight_with = input()

            # Do I have this item?
            FOUND = False
            for i, item in enumerate(backpack):
                if item.get_name() == fight_with and isinstance(item, game.Weapon):
                    FOUND = True
                    if backpack[i].use():
                        if inhabitant.fight(fight_with):
                            print("Hooray, you won the fight!")
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
                print("You don't have a " + fight_with)
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
                            print(f"You've gained \
{current_location.character.get_weapon()}")
                        else:
                            HEALTH += current_location.character.give_health()
                            print(
                                f"You've gained \
{current_location.character.give_health()} health points")
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
            backpack.append(item)
            current_location.set_item(None)
            if current_location is shotitam:
                current_location.character = None
                print('You grab your friend and carry him out of the bar')
            else:
                print("You put the " + item.get_name() + " in your backpack")
        else:
            print("There's nothing here to take!")
    else:
        print("I don't know how to " + command)
