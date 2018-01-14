# given a building of 100 floors and 2 eggs
# determine the highest floor on which the egg will drop

# linear method

numFloors = 100
secretHighestFloor = 75
currentFloor = numFloors/2

# use binary search to narrow down
# the range of floors

def drop_egg(currentFloor):
        if egg_break(currentFloor) == True:
            return drop_egg(currentFloor/2)

def egg_break(input):
    if input < secretHighestFloor:
        return False
    else:
        return True