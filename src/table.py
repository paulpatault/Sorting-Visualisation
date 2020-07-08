import pygame
import random
from data import Data
import constants as csts


class Table:
    def __init__(self, screen, data=None):
        if data:
            self.data = data
        else:
            self.data = Table.gen_data()
        self.screen = screen

        self.idx = 0

    @staticmethod
    def gen_data():
        offset = csts.HEIGHT / (csts.LEN + 1)
        array = [Data(i * offset) for i in range(1, csts.LEN + 1)]
        random.shuffle(array)
        return array

    def setVal(self, i, val):
        self.data[i] = Data(val)

    def screenshot_(self):
        pygame.image.save(self.screen, f"data/screenshot_{self.idx}.jpeg")
        self.idx += 1

    def draw(self):
        self.screen.fill((255, 255, 255))
        width = csts.WIDTH / csts.LEN
        for idx, elt in enumerate(self.data):
            rect = pygame.Rect(
                int(idx * width), csts.HEIGHT - elt.value, width - 1, elt.value,
            )
            color = elt.color
            pygame.draw.rect(self.screen, color, rect)

        pygame.display.update()

        self.screenshot_()