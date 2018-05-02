from Inventory import Inventory, Slepping_potion, Knockout_potion, cell_keys, dungeon_keys

class Room():
    def __init__(self, name = "", description = "", id = ""):
        self.name = name
        self.description = description
        self.id = id
        self.items = []
        self.connectors = []
        self.rooms = {}

    def add_item(self, item):
        self.items.append(item)

    def add_room(self, direction, room):
        self.rooms[direction] = room

    def add_connection(self, room, connector, actions):
        for direction in actions:
            self.rooms[direction] = room
        self.connectors.append((connector, actions[0]))

    def enter_room(self, inventory):
        print self.name
        print
        print self.description
        print
        if len(self.connectors) > 0:
            for connector in self.connectors:
                print "There is a " + connector[0] + \
                    " that goes " + connector[1]


    def get_name(self):
        return self.name

    def is_valid_direction(self, direction):
        return direction in self.rooms.keys()

    def next_room(self, direction):
        return self.rooms[direction]

    def process_command(self, command, inventory):
       if command in self.rooms.keys():
           new_room = self.next_room(command)
           return new_room
       elif "get" in command:
           for item in self.items:
               if item.name in command:
                   inventory.add(item)
                   self.items.remove(item)
                   return "You picked up the "+item.name+"."
               else:
                   return "I don't know what you want to pick up."
       else:
           return None


class EndRoom(Room):
    def enter_room(self, inventory):
        print "You've escaped!"
        exit()


#Need to figure out to add two items into this:
class LockedRoom(Room):
    def __init__(self, forward_room, back_room):
        self.forward_room = forward_room
        self.back_room = back_room
        Room.__init__(self)

    def enter_room(self, inventory):
        if inventory.contains(cell_keys):
            self.forward_room.enter_room()
            return self.forward_room
        else:
            if inventory.contains(dungeon_keys):
                self.forward_room.enter_room()
                return self.forward_room
    elif:
        print "The door is locked."
        self.back_room.enter_room()
        return self.back_room


class GuardRoom(Room):
    def __init__(self, name, description, id):
        Room.__init__(self, name, description, id)
        def enter_room(self, inventory):
            if inventory.contains(Sleeping_potion):
                self.forward_room.enter_room()
                return self.forward_room
            else:
                if inventory.contians(Knockout_potion):
                    self.forward_room.enter_room()
                    return self.forward_room
        elif:
            print "Uh oh! You have been caught!"
            self.back_room.enter_room()
            return self.back_room

#DarkRoom like a gru room, need to add to map
class DarkRoom(Room):
    def __init__(self, name, description, id):
        Room.__init__(self, name, description, id)
        def enter_room(self, inventory):
            if inventory.contains(Lantern):
                self.forward_room.enter_room()
                return self.forward_room
            else:
                print "Uh oh! Guess you're dead."
                self.back_room.enter_room()
                return self.back_room


