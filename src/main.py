from m_parser import args

args.load()

import pygame
import importlib

# to make the GIF
import os
import glob
import imageio
from moviepy.editor import *


# my classes
import constants as csts
from table import Table
from data import Data
from algorithms import Algorithm

pygame.init()


def modules_reload():
    importlib.reload(csts)


def make_gif(n, resize=0.7, speedx=1.2):
    cwd = os.path.curdir
    if args.gif:
        images = [imageio.imread(f"data/screenshot_{i}.jpeg") for i in range(n)]
        imageio.mimsave("data/movie.mov", images)
        clip = VideoFileClip("data/movie.mov").resize(resize).speedx(speedx)
        clip.write_gif("data/output.gif")

        os.remove(f"{cwd}/data/movie.mov")

    filelist = glob.glob(f"{cwd}/data/*.jpeg")
    for file in filelist:
        os.remove(file)


def main():
    table = Table(screen)
    table.draw()
    algo = Algorithm(args.algo, screen)
    algo.run(table)

    make_gif(table.idx)


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
