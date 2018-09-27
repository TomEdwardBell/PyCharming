from room import Room

kitchen = Room("Kitchen")
kitchen.set_desc("Where you cook")

dining = Room("Dining Room")
dining.set_desc("Where you eat")

kitchen.link_room (dining, "south", True)

kitchen.get_details()
dining.get_details()