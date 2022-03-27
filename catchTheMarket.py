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
win.fill(background_color)
image = pygame.image.load('catchTheMarketLogo.png')

class button():
   def __init__(self, color, x, y, height, width, text=''):
       self.color = color
       self.x = x
       self.y = y
       self.width = width
       self.height = height
       self.text = text

   def draw(self, win, outline=None):
       if outline:
           pygame.draw.rect(win, outline, (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 0)
       pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), 0)

       if self.text != '':
           font = pygame.font.SysFont('arial', 20)
           text = font.render(self.text, 1, (255, 255, 255))
           win.blit(text, (self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))

   def isOver(self, pos):
       if pos[0] > self.x and pos[0] < self.x + self.width:
           if pos[1] > self.y and pos[1] < self.y + self.height:
               return True
       return False

def main_menu():
  pygame.display.set_caption("Catch The Market: Main Menu")
  win.blit(image, (615, 0))
  Play_Button = button((38, 94, 92), 150, 225, 250, 100, 'Play')
  Play_Button.draw(win, (6, 23, 22))
  pygame.display.flip()
  running = True
  while running:
      for event in pygame.event.get():
          pos = pygame.mouse.get_pos()
          if event.type == pygame.QUIT:
            running = False
          if event.type == pygame.MOUSEBUTTONDOWN:
              if Play_Button.isOver(pos):
                play()
          if event.type == pygame.MOUSEMOTION:
              if Play_Button.isOver(pos):
                  Play_Button.color=(255,0,0)
                  pygame.display.flip()
              else:
                  Play_Button.color = (0, 255, 0)
                  pygame.display.flip()

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
  win.blit(image, (615, 0))
  tsla1 = pygame.image.load('TSLA1.png')
  win.blit(tsla1, (50, 250))
  WHITE = (255, 255, 255)
  TEAL = (56, 255, 232)
  pygame.draw.line(win, WHITE, (630, 270), (630, 790), width=3)
  pygame.display.flip()
  y_upper_bound = 270
  y_lower_bound = 780
  pygame.font.init()
  fnt = pygame.font.SysFont('arial', 30)
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
                      pygame.draw.line(win, TEAL, last_pos, mouse_position, 3)
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
    percent = (correctness(predictions, prices[i]))
    dspPercent = str(round(percent, 1)) + "%"
    textsurface = fnt.render(dspPercent, False, (255, 255, 255))
    win.blit(textsurface, (x_right_bound - 90, 750))
  pygame.display.update()

def play():
   pygame.display.set_caption("Play")
   running = True
   Play_Mouse_Pos = pygame.mouse.get_pos()
   win.fill(background_color)
   Back_Button = button((0, 255, 0), 0, 0, 250, 100, 'Back')
   Back_Button.draw(win, (0, 0, 0))
   pygame.display.flip()
   runGame()
   while running:
       for event in pygame.event.get():
           if event.type == pygame.QUIT:
              running = False
           if event.type == pygame.MOUSEBUTTONDOWN:
               if Back_Button.isOver(Play_Mouse_Pos):
                   main_menu()
           if event.type == pygame.MOUSEMOTION:
               if Back_Button.isOver(Play_Mouse_Pos):
                   Back_Button.color = (255, 0, 0)
                   pygame.display.flip()
               else:
                   Back_Button.color = (0, 255, 0)
                   pygame.display.flip()


pygame.display.flip()
running = True
main_menu()
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

