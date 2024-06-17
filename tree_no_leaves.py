import pygame
import random

class Tree_no_leaves:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image_list = ["tree-no-leaves.png", "tree-no-leaves_1.png", "tree-no-leaves_2.png", "tree-no-leaves_3.png"]
        self.image_number = 0
        self.image = pygame.image.load(self.image_list[0])
        self.rescale_image(self.image)
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        self.delta = 5
        self.up = True

    def rescale_image(self, image):
        self.image_size = self.image.get_size()
        scale_size = (self.image_size[0] * .7, self.image_size[1] * .7)
        self.image = pygame.transform.scale(self.image, scale_size)


    def move_tree_no_leaves(self):
        self.x = self.x - self.delta
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        if self.x<0:
            self.x=850
            self.y=random.randint(20,580)

    def switch_image(self):
        image_number = 0
        if not self.up:
            image_number = 1
        self.image = pygame.image.load(self.image_list[image_number])
        self.rescale_image(self.image)
        self.image_size = self.image.get_size()
        self.up = not self.up
    def switch_image2(self):
        image_number = 1
        if not self.up:
            image_number = 2
        self.image = pygame.image.load(self.image_list[image_number])
        self.rescale_image(self.image)
        self.image_size = self.image.get_size()
        self.up = not self.up
    def switch_image3(self):
        image_number = 2
        if not self.up:
            image_number = 3
        self.image = pygame.image.load(self.image_list[image_number])
        self.rescale_image(self.image)
        self.image_size = self.image.get_size()
        self.up = not self.up
    def switch_image4(self):
        image_number = 3
        if not self.up:
            image_number = 0
        self.image = pygame.image.load(self.image_list[image_number])
        self.rescale_image(self.image)
        self.image_size = self.image.get_size()
        self.up = not self.up





