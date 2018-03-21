from Inventory import Inventory, Sleeping_potion, Keys
from adventure import Room, LockedRoom, GuardRoom, EndRoom

cell = Room('Cell', 'You are stuck in a dark, grimy dungeon cell', 'c')
doorway = LockedRoom('doorway', 'd')
hallway1 = Room('Hallway 1', 'You are in a hallway', 'h1')
hallway2 = Room('Hallway 2', 'You are in a hallway, you see something on the floor', 'h2')
hallway3 = Room('Hallway 3', 'The hallway darkens, you find a sleeping potion', 'h3')
hallway4 = Room('Hallway 4', 'You are again in another hallway. Be careful.', 'h4')
guard_room1 = GuardRoom('Guard', 'You see a guard', 'g1')
hallway5 = Room('Hallway 5', 'You are in a brighter hallway', 'h4')
stairs = Room('Set of Stairs', 'You find a set of set of stairs. You find a knock-out potion', 's')
dungeon_door = LockedRoom('Locked door', 'The door is locked, find the key to unlock it. ', 'dd')
guard_room2 = GuardRoom('Another Guard', 'Oh no, another guard!', 'g2')
free = EndRoom('Free', 'You did it. You are now free!' 'f')
hallway3.add_item(Sleeping_potion())
hallway5.add_item(Sleeping_potion())
cell.add_item(Keys())
stairs.add_item(Keys())

cell.add_connection(doorway, "passage", ["east", "e"])
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
dungeon_door.add_connection(guard_room2, "passage", ["east", "e",])
guard_room2.add_connection(free, "passage", ["east", "e"])
exit()



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
