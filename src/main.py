from m_parser import args

args.load()

import pygame
import importlib
import constants as csts
from table import Table
from data import Data
from algorithms import Algorithm

pygame.init()


def modules_reload():
    importlib.reload(csts)


def main():
    table = Table(screen)
    table.draw()
    algo = Algorithm(args.algo)
    algo.run(table)


while not args.destroy:
    screen = pygame.display.set_mode(csts.DIM)
    screen.fill((255, 255, 255))
    pygame.display.set_caption("Sorting Visualizer")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    main()

    args.load()
    modules_reload()
