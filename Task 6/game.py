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
        return self.conversation

    def describe(self):
        '''
        Describes the character
        '''
        print(self)


class Enemy(Character):
    '''
    An enemy object for the game
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
            Enemy.defeated_count += 1
            return True
        return False

    def get_defeated(self):
        '''
        Returns the number of defeats for the character
        '''
        return Enemy.defeated_count

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


class Item:
    '''
    An item object for the game
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
        print(self)


class Gift(Item):
    '''
    A weapon to make a character like you
    '''

    def __init__(self, name, value) -> None:
        '''
        Initialises the object
        '''
        super().__init__(name)
        self.value = value

    def use(self, threshold_value):
        '''
        Uses the gift and returns success/failure
        '''
        return self.value > threshold_value


class Weapon(Item):
    '''
    A weapon to fight with
    '''

    def __init__(self, name, uses) -> None:
        '''
        Initialises the object
        '''
        super().__init__(name)
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

    def link_room(self, location, direction):
        '''
        Links a location to one of the directions
        '''
        if direction not in ['north', 'east', 'west', 'south']:
            raise AttributeError('No such direction')
        setattr(self, direction, location)

    def get_details(self):
        '''
        Prints the room details
        '''
        print(
            f'{self.name} - {self.description}\n'
            f'North - {self.north}\n'
            f'East - {self.east}\n'
            f'West - {self.west}\n'
            f'South - {self.south}\n'
            f'Character: {self.character}\n'
            f'Item: {self.item}'
        )

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
