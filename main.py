import pygame

main = pygame.image.load(os.getcwd() + "\\img\\blocks.png")

block_1 = main.subsurface(32, (32, 32))
block_2 = main.subsurface(64, (32, 32))
