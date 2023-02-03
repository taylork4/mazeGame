""" The python_game.py program is a maze game designed with a simple goal. The player takes control of
    a ball and is tasked with the adventurous mission of reaching the bottom right square. However, the
    maze poses a major threat: Getting stuck. Due to the nature of the algorithm used to generate a random
    maze, a path does not always exist from the starting point to the ending point. To offset this problem,
    we have integrated the ability to turn squares off (or on) in the maze in order to navigate it fully.
    When the player reaches the bottom-most square, they win!
        author: Chase Kerr
        author: Cameron Snoap
        author: Kyle Taylor
        version: 2/6/2023
"""
# ****************************************************************************************************************************************************************************
""" Imports """
# ****************
import pygame, sys, random, math
from pygame.locals import *

# ****************************************************************************************************************************************************************************
""" Initialize game parameters """
# ****************
pygame.init()
maze = []
mazeColor = []
_width = 22
_height = _width
_gridSize = 20

# Sets up the frame rate
clock = pygame.time.Clock()
frame_rate = 10

 # Set the display window size
screen = pygame.display.set_mode((440, 440))

# Rectangle for which player is oriented
rect = pygame.Rect(11, 11, 0, 0)

# Initialize colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
orange = (255, 165, 0)
yellow = (255, 255, 0)
grey = (211, 211, 211)

# ****************************************************************************************************************************************************************************
""" The grid(w, h) function creates a grid based upon the desired width and height of the maze. Each individual cell
    in the grid is also assigned to a randomized color.
       ~ param w = Width of the grid
       ~ param h = Height of the grid

    Contributors: [Chase Kerr, Kyle Taylor]
"""
# ****************
def grid(w, h):
    hori = 0
    vert = 0

    # Nested loop for creating grid
    for i in range(0, w):
        line = []
        colorRow = []
        for j in range(0, h):
            colo = random.randint(0, 4) # Set color to a random color
            line.append(pygame.Rect(hori, vert, _width, _height))
            colorRow.append(colo)
            hori += _width
        vert += _height
        hori = 0
        maze.append(line)
        mazeColor.append(colorRow)


# ****************************************************************************************************************************************************************************
""" The drawText(text, font, color, surface, x, y) function draws text on the screen.
       ~ param text = Text that will display on screen
       ~ param font = Font of the text
       ~ param color = Color of the text
       ~ param surface = Where the text will be displayed
       ~ param x = Horizontal 'x' position of text on screen
       ~ param y = Vertical 'y' position of text on screen
        
    Contributors: [Kyle Taylor]
"""
# ****************
def drawText(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

# Checks if the player has one or not (Kyle Taylor)
def checkWin():
    if (rect.x == 429 and rect.y == 429):
        pygame.draw.rect(screen, black, pygame.Rect(84, 40, 276, 142))
        pygame.draw.rect(screen, yellow, pygame.Rect(88, 44, 268, 134))
        pygame.draw.rect(screen, black, pygame.Rect(95, 51, 250, 120))
        pygame.draw.rect(screen, grey, pygame.Rect(99, 55, 242, 112))
        drawText('You Win!', pygame.font.SysFont('impact', 65), black, screen, 104, 76)


# Collision detection (Cameron Snoap)
def collistion_detection(direction):
    if (direction == "left" and (screen.get_at((rect.x-22, rect.y)) == white or screen.get_at((rect.x-22, rect.y)) == black)):
        return True
    if (direction == "right" and (screen.get_at((rect.x+22, rect.y)) == white or screen.get_at((rect.x+22, rect.y)) == black)):
        return True
    if (direction == "up" and (screen.get_at((rect.x, rect.y-22)) == white or screen.get_at((rect.x, rect.y-22)) == black)):
        return True
    if (direction == "down" and (screen.get_at((rect.x, rect.y+22)) == white or screen.get_at((rect.x, rect.y+22)) == black)):
        return True
    else:
        return False

#gets mouse position, Cameron Snoap
def get_mouse_pos():
    x, y = pygame.mouse.get_pos()
    return x, y
    

# Move the circle with the arrow keys, Cameron Snoap
def handle_keys():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        if rect.y > 22 and collistion_detection("up"):
            rect.y -= 22
    if keys[pygame.K_DOWN]:
        if rect.y < 418 and collistion_detection("down"):
            rect.y += 22
    if keys[pygame.K_LEFT]:
        if rect.x > 22 and collistion_detection("left"):
            rect.x -= 22
    if keys[pygame.K_RIGHT]:
        if rect.x < 418 and collistion_detection("right"):
            rect.x += 22

#kills a square (makes them disappear), Cameron Snoap
def kill_square():
    mouse_presses = pygame.mouse.get_pressed()
    if mouse_presses[0]: #mouse left click
        x, y = get_mouse_pos()
        x = math.trunc(x/22)
        y = math.trunc(y/22)
        pygame.draw.rect(screen, white, maze[y][x])
        mazeColor[y][x] = 4


def gameloop():
# Run the game loop
    running = True
    #color logic check variable
    colorLogic = True
    colorLogicCount = 0
    grid(_gridSize, _gridSize)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

        kill_square()
        handle_keys()

        # Clear the screen
        screen.fill((255, 255, 255))

        # Draw the rectangle on the screen (Kyle Taylor)
        for i in range(0, 20):
            for j in range(0,20):
                if (mazeColor[i][j] == 0):
                    pygame.draw.rect(screen, red, maze[i][j])
                if (mazeColor[i][j] == 1):
                    pygame.draw.rect(screen, green, maze[i][j])
                if (mazeColor[i][j] == 2):
                    pygame.draw.rect(screen, blue, maze[i][j])
                if (mazeColor[i][j] == 3):
                    pygame.draw.rect(screen, orange, maze[i][j])
                if (mazeColor[i][j] == 4):
                    pygame.draw.rect(screen, white, maze[i][j])
                if (mazeColor[i][j] == 5):
                    pygame.draw.rect(screen, black, maze[i][j])

        #color logic, Chase Kerr
        #this will turn off once the colors have stabilized, so the mouse killing of squares doesn't end up creating more
        
        mazeColorCheck = mazeColor #check variable to compare current color set against previous
        if colorLogic:
            neighborsCount = 0
            for i in range(0,20):
                for j in range(0,20):
                    #checks left neighbor
                    if (i - 1 > 0 and mazeColor[i-1][j] != 4):
                        neighborsCount += 1
                    #checks right neighbor
                    if (i + 1 < 20 and mazeColor[i+1][j] != 4):
                        neighborsCount += 1
                    #checks lower neighbor
                    if (j - 1 > 0 and mazeColor[i][j-1] != 4):
                        neighborsCount += 1
                    #checks upper neighbor
                    if (j + 1 < 20 and mazeColor[i][j+1] != 4):
                        neighborsCount += 1
                    #checks upper diagonal 1 neighbor
                    if (j - 1 > 0 and i - 1 > 0 and mazeColor[i-1][j-1] != 4):
                        neighborsCount += 1
                    #checks upper diagonal 2 neighbor
                    if (j - 1 > 0 and i + 1 < 20 and mazeColor[i+1][j-1] != 4):
                        neighborsCount += 1
                    #checks lower diagonal 1 neighbor
                    if (j + 1 < 20 and i - 1 > 0 and mazeColor[i-1][j+1] != 4):
                        neighborsCount += 1
                    #checks lower diagonal 2 neighbor
                    if (j + 1 < 20 and i + 1 < 20 and mazeColor[i+1][j+1] != 4):
                        neighborsCount += 1
                    #if 3 neighbors and dead, rectangle is reborn
                    if (neighborsCount == 3 and mazeColor[i][j] == 4):
                        pygame.draw.rect(screen, red, maze[i][j])
                        mazeColor[i][j] = 0
                    #if < 1 neighbors and alive, rectangle dies
                    if (neighborsCount < 1 and mazeColor[i][j] != 4):
                        pygame.draw.rect(screen, white, maze[i][j])
                        mazeColor[i][j] = 4
                    #if > 4 neighbors and alive, rectangle dies
                    if (neighborsCount > 4 and mazeColor[i][j] != 4):
                        pygame.draw.rect(screen, white, maze[i][j])
                        mazeColor[i][j] = 4
                    #maze[19][19] and maze[0][0] are always dead
                    if (i == 19 and j == 19 or i == 0 and j == 0):
                        pygame.draw.rect(screen, black, maze[i][j])
                        mazeColor[i][j] = 4
                    neighborsCount = 0
                #end for j
            #end for i
        if (mazeColorCheck == mazeColor): #stop loop once the colors stabilize
            colorLogicCount += 1
            if colorLogicCount == 10:
                colorLogic = False
                mazeColor[0][0] = 5
                mazeColor[19][19] = 5
        #end if colorLogic


        
        pygame.draw.circle(screen, black, (rect.x, rect.y), 10, 10)
        #draw player circle on the screen
        pygame.draw.circle(screen, red, (rect.x, rect.y), 5, 0)

        # Checks if player has won
        checkWin()

        # Update the screen
        pygame.display.update()

        # Limit the frame rate
        clock.tick(frame_rate)

    # Quit pygame
    pygame.quit()

def main():
    gameloop()

if (__name__ == "__main__"):
    main()