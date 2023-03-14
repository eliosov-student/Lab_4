'''
Contains various classes for the game
'''


class Character:
    '''
    An character object for the game
    >>> dave = Character("Dave", "A smelly zombie")
    >>> dave.set_conversation("What's up, dude! I'm hungry.")
    >>> print(dave)
    Dave: A smelly zombie
    >>> dave.talk()
    [Dave says]: What's up, dude! I'm hungry.
    >>> dave.describe()
    Dave is here!
    A smelly zombie
    '''

    def __init__(self, name, description) -> None:
        '''
        Initializes the object
        '''
        self.name = name
        self.description = description
        self.conversation = None
        self.weakness = None

    def __str__(self) -> str:
        '''
        Returns a string description of the character
        '''
        return f'{self.name}: {self.description}'

    def set_conversation(self, conversation):
        '''
        Sets the character conversation
        '''
        self.conversation = conversation

    def talk(self):
        '''
        Returns the character conversation
        '''
        print(f'[{self.name} says]: {self.conversation}')

    def describe(self):
        '''
        Describes the character
        '''
        print(f'{self.name} is here!\n{self.description}')


class Enemy(Character):
    '''
    An enemy object for the game
    >>> dave = Enemy("Dave", "A smelly zombie")
    >>> dave.set_conversation("What's up, dude! I'm hungry.")
    >>> dave.set_weakness("cheese")
    >>> tabitha = Enemy(\
    "Tabitha", "An enormous spider with countless eyes and furry legs.")
    >>> tabitha.set_conversation("Sssss....I'm so bored...")
    >>> tabitha.set_weakness("book")
    >>> dave.get_defeated()
    0
    >>> dave.fight('book')
    Dave crushes you, puny adventurer!
    False
    >>> dave.get_defeated()
    0
    >>> dave.fight('cheese')
    You fend Dave off with the cheese
    True
    >>> dave.get_defeated()
    1
    >>> tabitha.fight('book')
    You fend Tabitha off with the book
    True
    >>> dave.get_defeated()
    2
    '''
    defeated_count = 0

    def set_weakness(self, weakness):
        '''
        Sets the character weakness
        '''
        self.weakness = weakness

    def fight(self, item):
        '''
        Simulates a fight
        '''
        if self.weakness == item:
            print(f'You fend {self.name} off with the {item}')
            Enemy.defeated_count += 1
            return True
        print(f'{self.name} crushes you, puny adventurer!')
        return False

    def get_defeated(self):
        '''
        Returns the number of defeats for the character
        '''
        return Enemy.defeated_count


class Friend(Character):
    '''
    A friend object for the game
    >>> dave = Friend("Dave", "A smelly zombie")
    >>> dave.set_conversation("What's up, dude! I'm hungry.")
    >>> print(dave)
    Dave: A smelly zombie
    >>> dave.talk()
    [Dave says]: What's up, dude! I'm hungry.
    >>> dave.describe()
    Dave is here!
    A smelly zombie
    '''


class Item:
    '''
    An item object for the game
    >>> cheese = Item("cheese")
    >>> cheese.set_description("A large and smelly block of cheese")
    >>> print(cheese)
    cheese: A large and smelly block of cheese
    >>> cheese.get_name()
    'cheese'
    >>> cheese.describe()
    The [cheese] is here - A large and smelly block of cheese
    '''

    def __init__(self, name) -> None:
        '''
        Initializes the object
        '''
        self.name = name
        self.description = None

    def __str__(self) -> str:
        '''
        Returns a string description of the item
        '''
        return f'{self.name}: {self.description}'

    def get_name(self):
        '''
        Gets the item name
        '''
        return self.name

    def set_description(self, description):
        '''
        Sets the item description
        '''
        self.description = description

    def describe(self):
        '''
        Describes the item
        '''
        print(f'The [{self.name}] is here - {self.description}')


class Room:
    '''
    A room object for the game
    >>> kitchen = Room("Kitchen")
    >>> kitchen.set_description("A dank and dirty room buzzing with flies.")
    >>> dining_hall = Room("Dining Hall")
    >>> dining_hall.set_description(\
        "A large room with ornate golden decorations on each wall.")
    >>> ballroom = Room("Ballroom")
    >>> ballroom.set_description(\
        "A vast room with a shiny wooden floor. Huge candlesticks guard the entrance.")
    >>> kitchen.link_room(dining_hall, "south")
    >>> dining_hall.link_room(kitchen, "north")
    >>> dining_hall.link_room(ballroom, "west")
    >>> ballroom.link_room(dining_hall, "east")
    >>> dave = Enemy("Dave", "A smelly zombie")
    >>> dave.set_conversation("What's up, dude! I'm hungry.")
    >>> dave.set_weakness("cheese")
    >>> dining_hall.set_character(dave)
    >>> tabitha = Enemy(\
    "Tabitha", "An enormous spider with countless eyes and furry legs.")
    >>> tabitha.set_conversation("Sssss....I'm so bored...")
    >>> tabitha.set_weakness("book")
    >>> ballroom.set_character(tabitha)
    >>> cheese = Item("cheese")
    >>> cheese.set_description("A large and smelly block of cheese")
    >>> ballroom.set_item(cheese)
    >>> book = Item("book")
    >>> book.set_description("A really good book entitled 'Knitting for dummies'")
    >>> dining_hall.set_item(book)
    >>> print(ballroom)
    Ballroom: A vast room with a shiny wooden floor. Huge candlesticks guard the entrance.
    >>> ballroom.get_character().name
    'Tabitha'
    >>> ballroom.get_item().name
    'cheese'
    >>> ballroom.set_item(None)
    >>> ballroom.get_item()

    >>> ballroom.move('east').name
    'Dining Hall'
    >>> ballroom.move('west')

    '''

    def __init__(self, name) -> None:
        '''
        Initializes the object
        '''
        self.name = name
        self.description = None
        self.character = None
        self.north = None
        self.east = None
        self.west = None
        self.south = None
        self.item = None

    def __str__(self) -> str:
        '''
        Returns a string description of the room
        '''
        return f'{self.name}: {self.description}'

    def set_description(self, description):
        '''
        Sets the room description
        '''
        self.description = description

    def get_character(self):
        '''
        Gets the room character
        '''
        return self.character

    def set_character(self, character):
        '''
        Sets the room character
        '''
        self.character = character

    def get_item(self):
        '''
        Gets the room item
        '''
        return self.item

    def set_item(self, item):
        '''
        Sets the room item
        '''
        self.item = item

    def link_room(self, room, direction):
        '''
        Links a room to one of the directions
        '''
        if direction not in ['north', 'east', 'west', 'south']:
            raise AttributeError('No such direction')
        setattr(self, direction, room)

    def get_details(self):
        '''
        Prints the room details
        '''
        text = f'{self.name}\n--------------------\n{self.description}\n'
        if self.north:
            text += f'The {self.north.name} is north\n'
        if self.east:
            text += f'The {self.east.name} is east\n'
        if self.west:
            text += f'The {self.west.name} is west\n'
        if self.south:
            text += f'The {self.south.name} is south\n'
        print(text)

    def move(self, command):
        '''
        Gives the room in the commanded direction
        '''
        if command not in ['north', 'east', 'west', 'south']:
            raise AttributeError('No such direction')
        return getattr(self, command)


if __name__ == '__main__':
    import doctest
    print(doctest.testmod())
