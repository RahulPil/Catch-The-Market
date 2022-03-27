import pygame

pygame.init()

prices = [[1199.78, 1149.59, 1088.12, 1064.7, 1026.96],
          [1058.12, 1064.4, 1106.22, 1031.56, 1049.61], 
          [1030.51, 955.65, 996.27, 943.9],
          [930, 918.4, 937.41, 829.1, 846.35]]

background_colour = (19, 57, 68)
win = pygame.display.set_mode((1800, 900))
pygame.display.set_caption('Chase The Market')
win.fill(background_colour)
image = pygame.image.load('catchTheMarketLogo.png')
win.blit(image, (525, 0))

def runGame():
  # update visual with indicators for new section drawing
  # show correct stock line and compute percentage
  # repeat for each stock section
  tsla1 = pygame.image.load('TSLA1.png')
  win.blit(tsla1, (50, 250))
  WHITE = (255, 255, 255)
  TEAL = (56, 255, 232)
  pygame.draw.line(win, WHITE, (630, 280), (630, 760), width=3)
  pygame.display.flip()
  for i in range(len(prices)):
    mouse_position = (0, 0)
    drawing = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                win.exit()
            elif event.type == pygame.MOUSEMOTION:
                if (drawing):
                    mouse_position = pygame.mouse.get_pos()
                    pygame.draw.line(win, TEAL, mouse_position, mouse_position, 1)
            elif event.type == pygame.MOUSEBUTTONUP:
                mouse_position = (0, 0)
                drawing = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                drawing = True

        pygame.display.update()

pygame.display.flip()
running = True
runGame()
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

