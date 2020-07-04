import constants as csts


class Data:
    def __init__(self, value, color=None):
        self.value = int(value)
        self.set_color(color)

    def set_color(self, color=None):
        if not color:
            color = (127, 182, 243)
        self.color = color
