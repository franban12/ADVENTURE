from Inventory import Inventory
from adventure import Room

cell = Room('Cell', 'You are stuck in a dark, grimy dungeon cell', 'c')
keys1 = Room('Keys', 'Who left these here?', 'k1')
doorway = Room('doorway', 'You have unlocked the cell door.', 'd')
hallway1 = Room('Hallway 1', 'You are in a hallway', 'h1')
hallway2 = Room('Hallway 2', 'You are in a hallway, you see something on the floor', 'h2')
hallway3 = Room('Hallway 3', 'The hallway darkens, you find a sleeping potion', 'h3')
hallway4 = Room('Hallway 4', 'You are again in another hallway. You hear faint breathing. Be careful.', 'h4')
guard_room1 = Room('Guard', 'You see a guard', 'g1')
hallway5 = Room('Hallway 5', 'You are in a brighter hallway', 'h4')
stairs = Room('Set of Stairs', 'You find a set of set of stairs. You find a knock-out potion', 's')
dungeon_door = Room('Locked door', 'The door is locked, find the key to unlock it. ', 'dd')
keys2 = Room('Keys', 'You found keys! Hmm, maybe it would work with the door', 'k2')
guard_room2 = ('Another Guard', 'Oh no, another guard!', 'g2')
free = ('Free', 'You did it. You are now free!' 'f')

cell.add_connection(doorway, "passage", ["east", "e"])
cell.add_connection(keys1, "key", ["south", "s"])
keys1.add_connection(cell, "passage",["north", "n"] )
doorway.add_connection(hallway1, "passage", ["north", "n"])
hallway1.add_connection(hallway2, "passage", ["east", "e"])
hallway2.add_connection(hallway3, "passage", ["east", "e"])
hallway3.add_connection(hallway4, "passage", ["north", "n"])
hallway4.add_connection(guard_room1, "passage", ["west", "w"])
guard_room1.add_connection(hallway5, "passage", ["north", "n"])
guard_room1.add_connection(hallway2, "passage", ["south", "s"])
hallway5.add_connection(stairs, "passage", ["east", "e", "go up", "climb stairs", "go up stairs"])
hallway5.add_connection(guard_room1, "passage", ["south", "s"])
stairs.add_connection(hallway5, "passage", ["west", "w", "go down", "down"])
stairs.add_connection(dungeon_door, "passage", ["north east", "ne"])
dungeon_door.add_connection(keys2, "passage", ["south", "s"])
keys2.add_connection(dungeon_door, "passage", ["north", "n"])
dungeon_door.add_connection(guard_room2, "passage", ["east", "e",])



#cell.add_room('e', doorway)
#keys.add_room('n', cell)
#doorway.add_room('n', hallway1)
#hallway1.add_room('s', doorway)
#hallway2.add_room('s', hallway3)
#hallway3.add_room('s', guard_room)
#guard_room.add_room('s', hallway4)
#hallway4.add_room('s', stairs)
#hallway2.add_room('n', bedroom1)
#hallway2.add_room('e', bedroom2)
#hallway2.add_room('w', bedroom3)
#bedroom1.add_room('s', hallway2)
#bedroom2.add_room('w', hallway2)
#bedroom3.add_room('e', hallway2)

inventory = Inventory()
current_room = cell

while True:
    current_room.enter_room()
    command = raw_input("What direction do you want to?")
    if command == ["exit", "x", "quit", "q"]:
        break

    result = current_room.process_command(command, inventory)
    if isinstance(result, Room):
        current_room = result
        continue
    elif isinstance(result, str):
        print result
        continue
    else:
            print "I don't know what you mean"
