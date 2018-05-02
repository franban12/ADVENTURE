class Inventory:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def drop(self, item):
        self.item.remove(item)

    def list(self):
        print "You are carrying:"
        for item in self.items:
            print item.get_name()


class Item:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name


class Item:
    def __init__(self, name):
        self.name = name
        self.known_commands = {}

    def get_name(self):
        return self.name

    def process_command(self, command):
        for a_command in self.known_commands:
            if a_command in command:
                self.known_commands[a_command](command)

    def process_command(self, command, inventory):


class SpellBook(Item):
    def __init__(self, name, contents = "This item is blank"):
        Item.__init__(self, name)
        self.contents = contents

    def read(self):
        print self.contents

    def write (self, contents):
        self.contents = contents


class Lantern(Item):
    def __init__(self, name, battery_level = 100, state = "Off"):
        Item.__init__(self, name)
        self.battery_level = battery_level
        self.state = state
        
    def turn_on(self):
        self.state = "On"

    def turn_off(self):
        self.state = "Off"

    def change_batteries(self):
        self.battery_level = 100

    def compute_usage(self):
        pass


# Code below was copied from trinket page, from things edited on that page and not on Python (still my code)
class Sleeping_potion(Item):
    def __init__(self, name = "sleeping potion"):
        Item.__init__(self, name)
        self.known_commands ["get the ", "pick up ", "retrieve "]
        pass

class Knockout_potion(Item):
    def __init__(self, name = "knockout potion"):
        self.known_commands ["get the ", "pick up ", "retrieve "]
        Item.__init__(self, name)
        pass

class cell_keys(Item):
    def __init__(self, name = "keys"):
        Item.__init__(self, name)
        self.known_commands ["get the ", "pick up ", "retrieve "]
        pass

class dungeon_keys(Item):
    def __init__(self, name = "keys"):
        Item.__init__(self, name)
        self.known_commands ["get the ", "pick up ", "retrieve "]
        pass
