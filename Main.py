# Importing modules
import pygame
import sys
import random

# Defining Globals
BOARD_SIZE = 10
SQUARE_SIZE = 40
FILLER = 80
BLACK = (0,0,0)
GRAY = (130,130,130)
WHITE = (255,255,255)

# Square class
class Square:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.value = random.randint(0,1)    # 0 => Empty; 1 => Filled
        self.rect = pygame.Rect(x,y,SQUARE_SIZE,SQUARE_SIZE)
        self.innerRect = pygame.Rect(x+1, y+1, SQUARE_SIZE-2, SQUARE_SIZE-2)
        self.mode = 0   # 1 => X; 2 => Filled
    def display(self,screen):
        pygame.draw.rect(screen, BLACK, self.rect, 1)
        if self.mode == 1:
            pygame.draw.rect(screen, GRAY, self.innerRect)
        elif self.mode == 2:
            pygame.draw.line(screen, GRAY, (self.x+1, self.y+1), (self.x+SQUARE_SIZE-2, self.y+SQUARE_SIZE-2))
            pygame.draw.line(screen, GRAY, (self.x+SQUARE_SIZE-2, self.y+1), (self.x+1, self.y+SQUARE_SIZE-2))

def update_display(screen,squares):
    # Filling background
    screen.fill(WHITE)

    # Displaying each square
    for row in squares:
        for square in row:
            square.display(screen)
    pygame.display.flip()

def handle_events(squares):
    # Checking for exits
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit()
            # Checking for clicks
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if mouse_pos[0] < FILLER or mouse_pos[1] < FILLER: continue
                row = (mouse_pos[1]-FILLER)//SQUARE_SIZE
                col = (mouse_pos[0]-FILLER)//SQUARE_SIZE
                if event.button == 1:
                    if squares[col][row].value == 1:
                        squares[col][row].mode = 1
                    else:
                        continue
                elif event.button == 3:
                    if squares[col][row].value == 0:
                        squares[col][row].mode = 2
                    else:
                        continue

def main():
    # Initializing Pygame
    pygame.init()
    screen = pygame.display.set_mode((SQUARE_SIZE*BOARD_SIZE+FILLER,SQUARE_SIZE*BOARD_SIZE+FILLER))

    # Creating square array
    squares = [[Square(FILLER + i * SQUARE_SIZE, FILLER + j * SQUARE_SIZE) for j in range(BOARD_SIZE)] for i in range(BOARD_SIZE)]
    
    # Creating game loop
    run = True
    while run:
        handle_events(squares)
        update_display(screen,squares)

if __name__ == "__main__":
    main()