
def crowd_test(people: list):
    if len(people) > 3:
        print("Room is crowded!")
    else:
        print("Room is not crowded")


people = ["nick", "tony", "gary", "ahmed"]

crowd_test(people)

people.pop(3)
people.pop(2)

crowd_test(people)
