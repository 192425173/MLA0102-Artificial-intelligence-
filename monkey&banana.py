monkey_position = 'A'
box_position = 'B'
banana_position = 'C'
monkey_on_box = False
bananas_grabbed = False

def move_monkey(to_position):
    global monkey_position
    print(f"Monkey moves from {monkey_position} to {to_position}")
    monkey_position = to_position

def push_box(to_position):
    global monkey_position, box_position
    if monkey_position == box_position:
        print(f"Monkey pushes box from {box_position} to {to_position}")
        box_position = to_position
        monkey_position = to_position
    else:
        print("Monkey is not at the box to push it!")

def climb_box():
    global monkey_on_box
    if monkey_position == box_position:
        monkey_on_box = True
        print("Monkey climbs on the box")
    else:
        print("Monkey is not at the box to climb!")

def grab_bananas():
    global bananas_grabbed
    if monkey_on_box and monkey_position == banana_position:
        bananas_grabbed = True
        print("Monkey grabs the bananas! 🎉")
    else:
        print("Monkey cannot reach the bananas yet!")

move_monkey('B')
push_box('C')
climb_box()
grab_bananas()
