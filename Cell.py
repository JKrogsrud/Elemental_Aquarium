import random

class Fire:
    #  A Fire cell spreads by burning nearby vegetation
    #  A fire cell lives for 3 generations
    #  A fire cell adjacent to a water cell dies immediately and creates fertile ground

class FertileGround:
    # Fertile ground given enough proximity to Wet tiles is

class Vegetation:
    #  A Vegetation Cell stays alive indefinitely
    #  A Vegetation Cell catches fire and becomes a Fire Cell if adjacent to a fire Cell

class WaterHead:
    #  A water Cell has a direction it flows creating new water cells in front of it
    #  it pits out fires and immediately dissapears
    #  it picks a new direction as it travels

    def __init__(self, direction = (0,1), age = 0, current = 3, lifespan = 20):
        # direction is one of of the cardinal directions or the half cardinals
        self.direction = direction
        self.age = age
        self.current = current
        self.lifespan = lifespan

    def step(self):
        # return a new WaterHead to be placed in a new location
        self.age += 1
        if self.age == self.lifespan:
            return
        if self.age%self.current == 0:
            directions = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
            index = directions.index(self.direction)
            index_dx = random.randrange(-1,2)
            self.direction = directions[index + index_dx]
        return WaterHead(self.direction, self.age, self.current, self.lifespan)

    def __str__(self):
        return "WH"

class WaterSource:
    # Creates water heads and sends them on their way
    # creates a new water head every a to b steps
    def __init__(self, direction = (0,1), age = 0):
        self.direction = direction
        self.age = age

    def __str__(self):
        return "WS"

class Wet:
    #  A wet cell is the tail of a water_head cell
    def __init__(self,age=0, lifespan = 3):
        self.age = age
        

    def step(self):
        self.age