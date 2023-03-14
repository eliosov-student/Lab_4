'''
Contains various classes for the game
'''


class Character:
    '''
    An character object for the game
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
    '''

    def __init__(self, name, description, weakness) -> None:
        super().__init__(name, description)
        self.defeated = False
        self.weakness = weakness

    def fight(self, item):
        '''
        Simulates a fight
        '''
        if self.weakness == item:
            self.defeated += 1
            return True
        return False

    def describe(self):
        '''
        Describes the character
        '''
        print(
            f'{self.name} - {self.description}\n'
            f'Weakness: {self.weakness}'
        )


class Friend(Character):
    '''
    A friend object for the game
    '''

    def __init__(self, name, description, recruit_item) -> None:
        '''
        Initializes the object
        '''
        super().__init__(name, description)
        self.recruit_item = recruit_item

    def gift(self, item):
        '''
        Uses the gift and returns success/failure
        '''
        return item == self.recruit_item


class Student(Friend):
    '''
    A student class
    '''

    def __init__(self, name, description, recruit_item, health) -> None:
        '''
        Initializes the object
        '''
        super().__init__(name, description, recruit_item)
        self.health = health

    def give_health(self):
        '''
        Simulates the student taking a hit for you in a simple way
        '''
        return self.health


class Cavaler(Friend):
    '''
    A cavaler class
    '''

    def __init__(self, name, description, recruit_item, weapon) -> None:
        '''
        Initializes the object
        '''
        super().__init__(name, description, recruit_item)
        self.weapon = weapon

    def get_weapon(self):
        '''
        Gets the cavaler's weapon to use
        '''
        return self.weapon


class Item:
    '''
    An item object for the game
    '''

    def __init__(self, name, description) -> None:
        '''
        Initializes the object
        '''
        self.name = name
        self.description = description

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


class Gift(Item):
    '''
    A gift to make a character like you
    '''

    def __init__(self, name, description, value) -> None:
        '''
        Initialises the object
        '''
        super().__init__(name, description)
        self.value = value


class Weapon(Item):
    '''
    A weapon to fight with
    '''

    def __init__(self, name, description, uses) -> None:
        '''
        Initialises the object
        '''
        super().__init__(name, description)
        self.uses = uses

    def use(self):
        '''
        Uses the weapon and returns success/failure
        '''
        if self.uses > 0:
            self.uses -= 0
            return True
        return False


class Location:
    '''
    A room object for the game
    '''

    def __init__(self, name) -> None:
        '''
        Initializes the object
        '''
        self.name = name
        self.description = None
        self.character = None
        self.item = None
        self.north = None
        self.east = None
        self.west = None
        self.south = None

    def __str__(self) -> str:
        '''
        Returns a string description of the location
        '''
        return f'{self.name}: {self.description}'

    def set_description(self, description):
        '''
        Sets the location description
        '''
        self.description = description

    def get_character(self):
        '''
        Gets the location character
        '''
        return self.character

    def set_character(self, character):
        '''
        Sets the location character
        '''
        self.character = character

    def get_item(self):
        '''
        Gets the location item
        '''
        return self.item

    def set_item(self, item):
        '''
        Sets the location item
        '''
        self.item = item

    def link_location(self, location, direction):
        '''
        Links a location to one of the directions
        '''
        if direction not in ['north', 'east', 'west', 'south']:
            raise AttributeError('No such direction')
        setattr(self, direction, location)

    def get_details(self):
        '''
        Prints the location details
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
        Gives the location in the commanded direction
        '''
        if command not in ['north', 'east', 'west', 'south']:
            raise AttributeError('No such direction')
        return getattr(self, command)


if __name__ == '__main__':
    import doctest
    print(doctest.testmod())
