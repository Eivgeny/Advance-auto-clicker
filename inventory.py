from pyscreeze import pixelMatchesColor, pixel


class Inv:
    color = None
    position = None

    def check_color(self):
        if self.color is None:
            print('No record for inventory')
            return False
        else:
            return pixelMatchesColor(self.position[0], self.position[1], self.color, tolerance=2)

    def set_color(self, position):
        self.position = position
        self.color = pixel(position[0], position[1])
        print('\n\tDone setting up inventory parameters\n')
