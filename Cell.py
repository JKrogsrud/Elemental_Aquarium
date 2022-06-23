import random


class Fire:
    #  A Fire cell spreads by burning nearby vegetation
    #  A fire cell lives for 3 generations
    #  A fire cell adjacent to a water cell dies immediately and creates fertile ground
    def __init__(self, age=0, lifespan=5, location=(0, 0)):
        self.age = age
        self.lifespan = lifespan
        self.future_state = []
        self.location = location

    def __str__(self):
        return "F"


class Water:
    #  A water cell spreads and is consumed by vegetation
    #  A water cell extinguishes Fire and creates age 0 vegetation
    def __init__(self, age=0, lifespan=2, direction=(1, 0), location=(0, 0)):
        self.age = age
        self.lifespan = lifespan
        self.future_state = []
        # determine a direction that this water will travel
        directions = ((0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1))
        self.direction = directions[directions.index(direction) + random.randrange(-1, 2)]
        self.location = location

    def __str__(self):
        return "W"


class Vegetation:
    def __init__(self, age=0, location=(0, 0)):
        self.age = age
        self.future_state = []
        self.location = location

    def __str__(self):
        return "V"