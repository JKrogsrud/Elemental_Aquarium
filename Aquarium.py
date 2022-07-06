import Cell
import Neighbor_tools as nt
import random

class Aquarium:

    def __init__(self, row=20, column=20, generations=0):
        self.row = row
        self.column = column
        self.grid = []
        self.generations = generations

        for x in range(0, self.column):
            new_row = []
            for y in range(0, self.row):
                new_row.append(Cell.Vegetation())
            self.grid.append(new_row)

    def populate(self):
        for x in range(0, self.column):
            for y in range(0,self.row):
                index = random.randrange(0,3)
                choices = [Cell.Fire(location=(x, y)), Cell.Water(location=(x, y)), Cell.Vegetation(location=(x, y))]
                self.grid[x][y] = choices[index]

    def step(self):

        # Run through the cells in the aquarium and update the things that need to be updated
        # future_aquarium = Aquarium(self.row,self.column)

        for x in range(0, self.column):

            for y in range(0,self.row):

                current_cell = self.grid[x][y]

                if isinstance(self.grid[x][y], Cell.Fire):

                    # check neighbors for water pointing at this fire cell
                    for crd in nt.generate_neighborhood((x, y), 1, 2):
                        try:
                            neighbor = self.grid[crd[0]][crd[1]]

                            # Check if it's a water cell pointing at this fire cell
                            if isinstance(neighbor, Cell.Water) and (neighbor.direction[0] + neighbor.location[0], neighbor.direction[1] + neighbor.location[1]) == (x, y) and neighbor.age == 0:

                                # We have a water neighbor pointing at our fire
                                # We should create new vegetation at age 0

                                future_cell = Cell.Vegetation(age=0, location=(x, y))

                                # add this to the possible next generation

                                current_cell.future_state.append(future_cell)
                        except IndexError:
                            continue

                    if len(current_cell.future_state) == 0:
                        current_cell.age += 1
                        current_cell.color = (int(255/current_cell.age), 20*current_cell.age, 0*current_cell.age)
                        if current_cell.age == current_cell.lifespan:

                            current_cell.future_state.append(Cell.Vegetation(age=0, location=(x, y)))

                if isinstance(self.grid[x][y], Cell.Vegetation):

                    # vegetation grow in the proximity of Water
                    # vegetation burns adjacent to fire if age > 3
                    # vegetation hit by water becomes water

                    water_count = 0

                    for crd in nt.generate_neighborhood((x, y), 1, 4):

                        try:
                            neighbor = self.grid[crd[0]][crd[1]]
                            if isinstance(neighbor, Cell.Water):
                                water_count += 1
                                if (neighbor.direction[0] + neighbor.location[0], neighbor.direction[1] + neighbor.location[1]) == (x, y):
                                    future_cell = Cell.Water(age=0, lifespan=2, direction=neighbor.direction, location=(x, y))
                                    current_cell.future_state.append(future_cell)
                        except IndexError:
                            continue

                    for crd in nt.generate_neighborhood((x, y), 1, 1):
                        try:
                            neighbor = self.grid[crd[0]][crd[1]]
                            if isinstance(neighbor, Cell.Fire):
                                if current_cell.age > 3:
                                    current_cell.future_state.append(Cell.Fire(age=0, lifespan=3, location=(x, y)))
                        except IndexError:
                            continue

                    if water_count > 2:
                        current_cell.age += 1
                        R, G, B = current_cell.color
                        G += 40
                        if G > 255:
                            G = 255
                        current_cell.color = (R, G, B)


                if isinstance(self.grid[x][y], Cell.Water):
                    if current_cell.age < current_cell.lifespan:
                        current_cell.age += 1
                        R, G, B = current_cell.color
                        B = int(B/2)
                        current_cell.color = (R, G, B)
                    else:
                        current_cell.future_state.append(Cell.Vegetation(age=2, location=(x, y)))

        for x in range(0, self.column):
            for y in range(0, self.row):
                current_cell = self.grid[x][y]
                if len(current_cell.future_state) > 0:
                    self.grid[x][y] = current_cell.future_state[random.randrange(0,len(current_cell.future_state))]

        self.generations += 1

    def rain(self, num_cells):
        # determine a number of random cells to become Water
        rain_count = 0
        while rain_count < num_cells:
            x_coord = random.randrange(0, self.row)
            y_coord = random.randrange(0, self.column)
            self.grid[x_coord][y_coord] = Cell.Water(age=0, lifespan=2, direction=(1, 0), location=(x_coord, y_coord), color=(0, 0, 255))
            rain_count += 1

    def lightning(self, num_strikes):
        # determine a number of random cells to become Fire
        # determine a number of random cells to become Water
        strike_count = 0
        while strike_count < num_strikes:
            x_coord = random.randrange(0, self.row)
            y_coord = random.randrange(0, self.column)
            self.grid[x_coord][y_coord] = Cell.Fire(age=0, lifespan=5, location=(x_coord, y_coord), color=(255, 0, 0))
            strike_count += 1

    def display(self):
        for y in range(0, self.row):
            row_display = ''
            for x in range(0, self.column):
                current_cell = self.grid[x][y]
                row_display += current_cell.__str__()
            print(row_display)
