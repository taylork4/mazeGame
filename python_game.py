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

    Comments contributor: [Kyle Taylor]
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

# ****************************************************************************************************************************************************************************
""" The checkWin() function determines if the player has won or not. The player wins when they reach the
    bottom-most square.
        
    Contributors: [Kyle Taylor]
"""
# ****************
def checkWin():
    #Checks if the player is at the bottom-most square
    if (rect.x == 429 and rect.y == 429):
        pygame.draw.rect(screen, black, pygame.Rect(84, 40, 276, 142))
        pygame.draw.rect(screen, yellow, pygame.Rect(88, 44, 268, 134))
        pygame.draw.rect(screen, black, pygame.Rect(95, 51, 250, 120))
        pygame.draw.rect(screen, grey, pygame.Rect(99, 55, 242, 112))
        drawText('You Win!', pygame.font.SysFont('impact', 65), black, screen, 104, 76)


# ****************************************************************************************************************************************************************************
""" The collisionDetection() function deals with collision detection. Collision forces the player to only be able to move within
    the white/black squares. Any other square is considered a wall in the maze.
        ~ param direction = The direction at which a user is trying to move
        ~ return True/False = True indicates that the given direction is a path, whereas false indicates the 
                              direction is a wall
    
    Contributors: [Cameron Snoap, Kyle Taylor]
"""
# ****************
def collisionDetection(direction):
    # Checks walls to the player's left
    if (direction == "left" and (screen.get_at((rect.x-22, rect.y)) == white or screen.get_at((rect.x-22, rect.y)) == black)):
        return True
    
    # Checks walls to the player's right
    if (direction == "right" and (screen.get_at((rect.x+22, rect.y)) == white or screen.get_at((rect.x+22, rect.y)) == black)):
        return True

    # Checks walls above the player
    if (direction == "up" and (screen.get_at((rect.x, rect.y-22)) == white or screen.get_at((rect.x, rect.y-22)) == black)):
        return True

    # Checks walls below the player
    if (direction == "down" and (screen.get_at((rect.x, rect.y+22)) == white or screen.get_at((rect.x, rect.y+22)) == black)):
        return True
    else:
        return False

# ****************************************************************************************************************************************************************************
""" The getMousePos() function retrieves the postition of the . Collision forces the player to only be able to move within
    the white/black squares. Any other square is considered a wall in the maze.
        ~ return x = X-position
        ~ return y = Y-position

    Contributors: [Cameron Snoap]
"""
# ****************
def getMousePos():
    x, y = pygame.mouse.get_pos()
    return x, y
    

# ****************************************************************************************************************************************************************************
""" The handleKeys() function keeps track of the player movement. The player can move up, down right, and left.
    However, if a wall exists in the direction the player is attempting to move to, the player will stay in
    place.
    
    Contributors: [Chase Kerr, Cameron Snoap, Kyle Taylor]
"""
# ****************
def handleKeys():
    keys = pygame.key.get_pressed()

    # Handles the up-arrow key 
    if keys[pygame.K_UP]:
        if rect.y > 22 and collisionDetection("up"):
            rect.y -= 22
    
    # Handles the down-arrow key
    if keys[pygame.K_DOWN]:
        if rect.y < 418 and collisionDetection("down"):
            rect.y += 22

    # Handles the left-arrow key
    if keys[pygame.K_LEFT]:
        if rect.x > 22 and collisionDetection("left"):
            rect.x -= 22
    
    # Handles the right-arrow key
    if keys[pygame.K_RIGHT]:
        if rect.x < 418 and collisionDetection("right"):
            rect.x += 22

# ****************************************************************************************************************************************************************************
""" The killSquare() function handles mouse click events on the maze walls. If the player clicks on a maze square, the
    square will be converted to white.
    
    Contributors: [Chase Kerr, Cameron Snoap]
"""
# ****************
def killSquare():
    mouse_presses = pygame.mouse.get_pressed()

    # Detects if user left-clicks with their mouse on a square 
    if mouse_presses[0]:
        x, y = getMousePos()
        x = math.trunc(x/22)
        y = math.trunc(y/22)
        pygame.draw.rect(screen, white, maze[y][x])
        mazeColor[y][x] = 4

# ****************************************************************************************************************************************************************************
""" The colorLogic(cl) function is responsible for dispersing the colors for the maze. The maze is auto-generated in a randomized
    fashion. Once the maze finishes generating, the color logic is set to False so that no more maze generation occurs.
        ~ param cl = Determines whether the color logic needs to be ran (True) or not (False)
        ~ return cl = When 'cl = False', color logic is complete 
    
    Contributors: [Chase Kerr]
"""
# ****************
def colorLogic(cl):
    colorLogicCount = 0
    mazeColorCheck = mazeColor # Compares current color set against previous
    # Color logic only gets checked when cl is set to True
    if cl:
        neighborsCount = 0
        # Nested loop for checking neighbors
        for i in range(0,20):
            for j in range(0,20):
                # Checks left neighbor
                if (i - 1 > 0 and mazeColor[i-1][j] != 4):
                    neighborsCount += 1

                # Checks right neighbor
                if (i + 1 < 20 and mazeColor[i+1][j] != 4):
                    neighborsCount += 1

                # Checks lower neighbor
                if (j - 1 > 0 and mazeColor[i][j-1] != 4):
                    neighborsCount += 1

                # Checks upper neighbor
                if (j + 1 < 20 and mazeColor[i][j+1] != 4):
                    neighborsCount += 1

                # Checks upper-left diagonal neighbor
                if (j - 1 > 0 and i - 1 > 0 and mazeColor[i-1][j-1] != 4):
                    neighborsCount += 1

                # Checks upper-right diagonal neighbor
                if (j - 1 > 0 and i + 1 < 20 and mazeColor[i+1][j-1] != 4):
                    neighborsCount += 1

                # Checks lower-left diagonal neighbor
                if (j + 1 < 20 and i - 1 > 0 and mazeColor[i-1][j+1] != 4):
                    neighborsCount += 1

                # Checks lower-right diagonal 2 neighbor
                if (j + 1 < 20 and i + 1 < 20 and mazeColor[i+1][j+1] != 4):
                    neighborsCount += 1

                # When 3 neighbors and dead, rectangle is reborn
                if (neighborsCount == 3 and mazeColor[i][j] == 4):
                    pygame.draw.rect(screen, red, maze[i][j])
                    mazeColor[i][j] = 0

                # When < 1 neighbors and alive, rectangle dies
                if (neighborsCount < 1 and mazeColor[i][j] != 4):
                    pygame.draw.rect(screen, white, maze[i][j])
                    mazeColor[i][j] = 4

                # When > 4 neighbors and alive, rectangle dies
                if (neighborsCount > 4 and mazeColor[i][j] != 4):
                    pygame.draw.rect(screen, white, maze[i][j])
                    mazeColor[i][j] = 4

                # Both maze[19][19] and maze[0][0] are always dead
                if (i == 19 and j == 19 or i == 0 and j == 0):
                    pygame.draw.rect(screen, black, maze[i][j])
                    mazeColor[i][j] = 4

                neighborsCount = 0

            #Loop stops as soon as the colors stabilize
            if (mazeColorCheck == mazeColor):
                colorLogicCount += 1
                if colorLogicCount == 10:
                    cl = False
    mazeColor[0][0] = 5
    mazeColor[19][19] = 5
    return cl

# ****************************************************************************************************************************************************************************
""" The drawMaze() function is responsible for drawing the maze.
    
    Contributors: [Chase Kerr, Kyle Taylor]
"""
# ****************
def drawMaze():
        # Clear the screen
        screen.fill((255, 255, 255))
        
        # Nested loop to display maze on screen
        for i in range(0, 20):
            for j in range(0,20):
                # Maze square will be red (wall block)
                if (mazeColor[i][j] == 0):
                    pygame.draw.rect(screen, red, maze[i][j])

                # Maze square will be green (wall block)
                if (mazeColor[i][j] == 1):
                    pygame.draw.rect(screen, green, maze[i][j])
                
                # Maze square will be blue (wall block)
                if (mazeColor[i][j] == 2):
                    pygame.draw.rect(screen, blue, maze[i][j])

                # Maze square will be orange (wall block)
                if (mazeColor[i][j] == 3):
                    pygame.draw.rect(screen, orange, maze[i][j])

                # Maze square will be white (path block)
                if (mazeColor[i][j] == 4):
                    pygame.draw.rect(screen, white, maze[i][j])

                # Maze square will be black (start/end block)
                if (mazeColor[i][j] == 5):
                    pygame.draw.rect(screen, black, maze[i][j])

# ****************************************************************************************************************************************************************************
""" The drawPlayer() function is responsible for drawing the player.
    
    Contributors: [Cameron Snoap]
"""
# ****************
def drawPlayer():
    #draw player circle on the screen
    pygame.draw.circle(screen, black, (rect.x, rect.y), 10, 10)
    pygame.draw.circle(screen, red, (rect.x, rect.y), 5, 0)


# ****************************************************************************************************************************************************************************
""" The gameLoop() function is responsible for running and generating the game. The loop continues to run until the player
    clicks the ESC key or the 'X' button in the corner to close out the game.
    
    Contributors: [Chase Kerr, Cameron Snoap, Kyle Taylor]
"""
# ****************
def gameloop():
    running = True
    colorLogicBool = True
    grid(_gridSize, _gridSize)

    # Game loop continues until player closes game
    while running:

        # Handles events for closing the game
        for event in pygame.event.get():
            # Closes game from 'X' in the corner
            if event.type == pygame.QUIT:
                running = False
            # Closes game from ESC key on keyboard
            elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
        killSquare()
        handleKeys()
        drawMaze()
        drawPlayer()
        colorLogicBool = colorLogic(colorLogicBool)
        checkWin()

        # Update the screen
        pygame.display.update()

        # Limit the frame rate
        clock.tick(frame_rate)

    # Quit pygame
    pygame.quit()

# ****************************************************************************************************************************************************************************
""" The main() function is responsible for starting the game
    
    Contributors: [Cameron Snoap]
"""
# ****************
def main():
    gameloop()

# ****************************************************************************************************************************************************************************
""" Runs the main() function
    
    Contributors: [Cameron Snoap]
"""
# ****************
if (__name__ == "__main__"):
    main()