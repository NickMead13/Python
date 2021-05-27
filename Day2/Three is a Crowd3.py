
def crowd_test(people: list):
    if len(people) > 5:
        print("There is a mob")
    elif len(people) >= 3:
        print("Room is crowded!")
    elif len(people) > 0:
        print("Room is not crowded")
    else:
        print("No one is in the room")


people = ["nick", "tony", "gary", "ahmed", "riley", "isabella"]

crowd_test(people)

people.pop(5)
people.pop(4)

crowd_test(people)

people.pop(3)
people.pop(2)

crowd_test(people)

people.pop(1)
people.pop(0)

crowd_test(people)
