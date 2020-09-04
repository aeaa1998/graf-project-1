





"""
import sys
import pygame
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((800,600))
x = 0
while True:
  clock.tick(60)
  r.clear()
  r.lookAt(V3(10, 1, x), V3(0, 0, 0), V3(0, 1, 0))
  r.load('./models/model.obj', texture=t, shader=gourad)
  r.write('frame.bmp')
  frame = pygame.image.load("frame.bmp").convert()
  screen.blit(frame, (0,0))
  for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_LEFT:
        x -= 10
      if event.key == pygame.K_RIGHT:
        x += 10
    if event.type == pygame.QUIT:
        sys.exit()
  print('frame', x)
  pygame.display.update()
"""