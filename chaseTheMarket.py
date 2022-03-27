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
image = pygame.image.load('chaseTheMarketLogo.png')

def get_font(size):
    return pygame.font.Font("arial", size)

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

Back_Button = button((38, 94, 92), 80, 800, 75, 225, 'Back')

def main_menu():
  pygame.display.set_caption("Chase The Market: Main Menu")
  win.fill(background_color)
  win.blit(image, (615, 0))
  Play_Button = button((38, 94, 92), 835, 250, 100, 250, 'Play')
  Play_Button.draw(win, (6, 23, 22))
  Instruction_Button = button((38, 94, 92), 835, 450, 100, 250, 'Instruction')
  Instruction_Button.draw(win, (6, 23, 22))
  pygame.display.flip()
  while True:
      for event in pygame.event.get():
          pos = pygame.mouse.get_pos()
          if event.type == pygame.QUIT:
            pygame.display.quit()
            pygame.quit()
          else:
            if event.type == pygame.MOUSEBUTTONDOWN:
              if Play_Button.isOver(pos):
                play()
              elif Instruction_Button.isOver(pos):
                instruction()
            if event.type == pygame.MOUSEMOTION:
              if Instruction_Button.isOver(pos):
                Instruction_Button.color = (29, 125, 122)
                Instruction_Button.draw(win, (6, 23, 22))
                pygame.display.flip()
              else:
                Instruction_Button.color = (38, 94, 92)
                Instruction_Button.draw(win, (6, 23, 22))
                pygame.display.flip()
              if Play_Button.isOver(pos):
                Play_Button.color=(29, 125, 122)
                Play_Button.draw(win, (6, 23, 22))
                pygame.display.flip()
              else:
                Play_Button.color = (38, 94, 92)
                Play_Button.draw(win, (6, 23, 22))
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
  totAvg = 0
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
                if Back_Button.isOver(pygame.mouse.get_pos()):
                   Back_Button.color = (29, 125, 122)
                   Back_Button.draw(win, (6, 23, 22))
                   pygame.display.flip()
                else:
                   Back_Button.color = (38, 94, 92)
                   Back_Button.draw(win, (6, 23, 22))
                   pygame.display.flip()
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
                if Back_Button.isOver(pygame.mouse.get_pos()):
                   main_menu()
                else:
                  drawing = True    
        pygame.display.update()
    pygame.time.delay(400)
    win.blit(images[i], (x_left_bound, 250))
    percent = (correctness(predictions, prices[i]))
    totAvg += percent
    dspPercent = str(round(percent, 1)) + "%"
    textsurface = fnt.render(dspPercent, False, (255, 255, 255))
    win.blit(textsurface, (x_right_bound - 90, 750))
  Analytics_Button = button((38, 94, 92), 1575, 800, 75, 225, 'Analytics')
  Analytics_Button.draw(win, (6, 23, 22))
  pygame.display.update()
  while True:
   for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          win.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if Analytics_Button.isOver(pygame.mouse.get_pos()):
              analytics(totAvg / 4)
            elif Back_Button.isOver(pygame.mouse.get_pos()):
              main_menu()
        if event.type == pygame.MOUSEMOTION:
            if Analytics_Button.isOver(pygame.mouse.get_pos()):
                Analytics_Button.color = (255, 0, 0)
                pygame.display.flip()
            else:
                Analytics_Button.color = (0, 255, 0)
                pygame.display.flip()

def play():
   pygame.display.set_caption("Play")
   Play_Mouse_Pos = pygame.mouse.get_pos()
   win.fill(background_color)
   Back_Button.draw(win, (6, 23, 22))
   pygame.display.flip()
   runGame()

def instruction():
    pygame.display.set_caption("Instructions")
    win.fill(background_color)
    win.blit(image, (615, 0))
    Back_Button.draw(win, (6, 23, 22))
    font = pygame.font.SysFont('arial', 20)
    Instruction_Text1 = font.render("Chase the market is game where you try to predict the trend of the given stock.", False, (255, 255, 255))
    Instruction_Text2 = font.render("To start, you are given two weeks of the stock price prior to the starting prediciton", False, (255, 255, 255))
    Instruction_Text3 = font.render("date to help you make the first prediciton. Predictions are made by drawing from the", False, (255, 255, 255))
    Instruction_Text4 = font.render("left white line to the right white line for the corrosponding week section, once the", False, (255, 255, 255))
    Instruction_Text5 = font.render("line has been drawn you are shown the correct stock trend and are shown a percentage", False, (255, 255, 255))
    Instruction_Text6 = font.render("repersenting how correct you were.", False, (255, 255, 255))
    win.blit(Instruction_Text1, (400, 250))
    win.blit(Instruction_Text2, (400, 280))
    win.blit(Instruction_Text3, (400, 310))
    win.blit(Instruction_Text4, (400, 340))
    win.blit(Instruction_Text5, (400, 370))
    win.blit(Instruction_Text6, (400, 400))
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
              pygame.display.quit()
              pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
              if Back_Button.isOver(pygame.mouse.get_pos()):
                main_menu()
            if event.type == pygame.MOUSEMOTION:
              if Back_Button.isOver(pygame.mouse.get_pos()):
                  Back_Button.color = (29, 125, 122)
                  Back_Button.draw(win, (6, 23, 22))
                  pygame.display.flip()
              else:
                  Back_Button.color = (38, 94, 92)
                  Back_Button.draw(win, (6, 23, 22))
                  pygame.display.flip()

def analytics(average):
    pygame.display.set_caption("Analytics")
    win.fill(background_color)
    win.blit(image, (615, 0))
    Back_Button.draw(win, (6, 23, 22))
    font = pygame.font.SysFont('arial', 20)
    if 0 <= average <= 50:
        Analytics_Text1 = font.render("It seems like you are having some issues with predicting future trends.", False, (255, 255, 255))
        Analytics_Text2 = font.render("Looking at the 2 weeks of stock data shown, we can see that the stock rises initially at a rather slow rate but then starts to take a dip..", False, (255, 255, 255))
        Analytics_Text3 = font.render("Based off of that we can tell that the stock will most likely repeat the same pattern in future cases", False, (255, 255, 255))
        win.blit(Analytics_Text1, (400, 250))
        win.blit(Analytics_Text2, (400, 280))
        win.blit(Analytics_Text3, (400, 310))
    elif 50 < average <= 90:
        Analytics_Text4 = font.render("It seems like you are getting really close to getting good at this!", False, (255, 255, 255))
        Analytics_Text5 = font.render("Some tips that would help your performance are maybe try and look at the general flow of the trend.", False, (255, 255, 255))
        Analytics_Text6 = font.render("A lot of trends tend to repeat themselves over time.", False, (255, 255, 255))
        win.blit(Analytics_Text4, (400, 250))
        win.blit(Analytics_Text5, (400, 280))
        win.blit(Analytics_Text6, (400, 310))
    else:
        Analytics_Text7 = font.render("Absolutely Brilliant, you are on your way to becoming a great investor", False, (255, 255, 255))
        win.blit(Analytics_Text7, (400, 250))
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
              pygame.display.quit()
              pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
              if Back_Button.isOver(pygame.mouse.get_pos()):
                main_menu()
            if event.type == pygame.MOUSEMOTION:
              if Back_Button.isOver(pygame.mouse.get_pos()):
                  Back_Button.color = (29, 125, 122)
                  Back_Button.draw(win, (6, 23, 22))
                  pygame.display.flip()
              else:
                  Back_Button.color = (38, 94, 92)
                  Back_Button.draw(win, (6, 23, 22))
                  pygame.display.flip()

pygame.display.flip()
running = True
main_menu()

