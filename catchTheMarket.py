import pygame

pygame.init()

prices = [[1199.78, 1149.59, 1088.12, 1064.7, 1026.96],
          [1058.12, 1064.4, 1106.22, 1031.56, 1049.61], 
          [1030.51, 955.65, 996.27, 943.9],
          [930, 918.4, 937.41, 829.1, 846.35]]

boundaries = [(632, 936), (939, 1300), (1303, 1547), (1550, 1795)]
images = [pygame.image.load('TSLA2.png'), pygame.image.load('TSLA3.png'),
          pygame.image.load('TSLA4.png'), pygame.image.load('TSLA5.png')]

background_color = (19, 57, 68)
win = pygame.display.set_mode((1900, 900))
pygame.display.set_caption('Chase The Market')
win.fill(background_color)
image = pygame.image.load('catchTheMarketLogo.png')
win.blit(image, (615, 0))

def correctness(predictions, prices):
  tot = 0
  coef = len(predictions) / len(prices)
  for i in range(0, len(predictions), int(coef)):
    tot += abs(predictions[i] - prices[int(i / coef)])
  
  tot /= len(prices)
  return 100 - (tot * .3)

def runGame():
  # update visual with indicators for new section drawing
  # show correct stock line and compute percentage
  # repeat for each stock section
  tsla1 = pygame.image.load('TSLA1.png')
  win.blit(tsla1, (50, 250))
  WHITE = (255, 255, 255)
  TEAL = (56, 255, 232)
  pygame.draw.line(win, WHITE, (630, 270), (630, 790), width=3)
  pygame.display.flip()
  y_upper_bound = 270
  y_lower_bound = 780
  for i in range(len(prices)):
    predictions = []
    x_left_bound = boundaries[i][0]
    x_right_bound = boundaries[i][1]
    pygame.draw.line(win, WHITE, (x_right_bound + 1, 270), (x_right_bound + 1, 790), width=3)
    pygame.display.update()
    mouse_position = (0, 0)
    drawing = False
    last_pos = None
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                win.exit()
            elif event.type == pygame.MOUSEMOTION:
                if (drawing):
                    x, y = pygame.mouse.get_pos()
                    if (x < x_left_bound):
                      x = x_left_bound
                    if (x > x_right_bound):
                      x = x_right_bound
                    if (y < y_upper_bound):
                      y = y_upper_bound
                    if (y > y_lower_bound):
                      y = y_lower_bound
                    mouse_position = (x, y)
                    if last_pos is None:
                      if x < (x_left_bound + 5):
                        last_pos = mouse_position
                    else:
                      predictions.append(840 + (.71 * (780 - y)))
                      pygame.draw.line(win, TEAL, last_pos, mouse_position, 2)
                      if (x == x_right_bound):
                        run = False
                      last_pos = mouse_position
            elif event.type == pygame.MOUSEBUTTONUP:
                last_pos = None
                predictions = []
                pygame.draw.rect(win, background_color, [x_left_bound, y_upper_bound, (x_right_bound - x_left_bound), (y_lower_bound - y_upper_bound)])
                pygame.display.update()
                mouse_position = (0, 0)
                drawing = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                drawing = True
        pygame.display.update()
    pygame.time.delay(400)
    win.blit(images[i], (x_left_bound, 250))
    print(correctness(predictions, prices[i]))
  pygame.display.update()

pygame.display.flip()
running = True
runGame()
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

