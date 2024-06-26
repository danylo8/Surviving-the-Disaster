import pygame

class Gameicon1:

   def __init__(self, x, y):
       self.x=x
       self.y=y
       self.image=pygame.image.load("gameicon_tornado.png")
       self.image_size=self.image.get_size()
       self.rect=pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
       self.image_size=self.image.get_size()
       scale_size=(self.image_size[0] * .6, self.image_size[1] * .6)
       self.image=pygame.transform.scale(self.image, scale_size)
       self.image_size=self.image.get_size()

   def set_location(self, new_x, new_y):
       self.x=new_x
       self.y=new_y
       self.rect=pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
