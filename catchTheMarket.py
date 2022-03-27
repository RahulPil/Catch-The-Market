import pygame

pygame.init()

prices = [1199.78, 1149.59, 1088.12, 1064.7, 1026.96, 1058.12, 1064.4, 1106.22, 1031.56, 1049.61, 
          1030.51, 955.65, 996.27, 943.9, 930, 918.4, 937.41, 829.1, 846.35]


def runGame():
  # update visual with indicators for new section drawing
  # show correct stock line and compute percentage
  # repeat for each stock section
  print("bruh")

background_colour = (19, 59, 68)
win = pygame.display.set_mode((1800, 900))
pygame.display.set_caption('Chase The Market')
win.fill(background_colour)
image = pygame.image.load('catchTheMarketLogo.png')
win.blit(image, (525, 0))
pygame.display.flip()
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

