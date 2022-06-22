class Aquarium():

    def __init__(self, row=20, column=20):
        self.row = row
        self.column = column

        for x in range(0, self.column):
            new_row = []
            for y in range(0, self.row):
                new_row.append(Cell.Cell())
            self.grid.append(new_row)

    def populate(self):
        # TODO: create a means for the aquarium to populate itself in a nice way

    def step(self):
        # TODO: Update Fire, Update Water, Update Earth
        check_fire()
        check_water()
        check_vegetation()
        return change

    def display(self):
