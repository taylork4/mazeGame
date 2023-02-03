'''
***********************************************************************************************************************************
Has a core game loop that is frame limited (10)
***********************************************************************************************************************************
Must have some mechanism for easily changing the framerate (be it a run time option, or a simple easy to change final variable) (10)
***********************************************************************************************************************************
Grow and draw a maze using the prescribed cellular automata method (15)
***********************************************************************************************************************************
Draw your maze at the framerate using squares for each cell (10)
***********************************************************************************************************************************
Must handle quit events, mouse events, and keyboard events. Clicking the close button of the game window should gracefully shutdown the game. 
Clicking on a rectangle causes that rectangle to either become a new random color (if it is currently (0, 0, 0)), or become (0, 0, 0) if it has any color at all. 
Note that (0, 0, 0) is an open cell and can be traversed. Any other color is a wall. (15)
***********************************************************************************************************************************
Must have a circle that represents the player. The player will start at the top left corner of the maze. 
If there is currently a cell there, remove it before adding the player. 
The player must be able to move through the maze corridors, but cannot go through walls, attempting to get to the lower right corner. 
Making it to the lower right corner should result in a "win". 
Keep in mind that mouse clicks can turn on and off a wall; this is not intended to be a fun game, merely a project to get the absolute basics working before we move forward with more complicated coding (20)
***********************************************************************************************************************************
Fully commented and documented code that includes headers for all public classes and methods. 
If a method has a return type, or takes parameters, or throws exceptions, it should be documented. 
Use the Google Style Guide (https://google.github.io/styleguide/) when you have questions. (10)
***********************************************************************************************************************************
You must demo your project in class on the due date for full points (10)
'''
'''
Still need to do
* mouse click to kill rectangle
* collision detection for non-white rectangles
* win condition for in bottom right corner
* 
'''
import pygame
import random
import math

# Initialize pygame
pygame.init()
maze = []
mazeColor = []
width = 22
height = width

# Set the display window size, Cameron Snoap, Chase Kerr
screen = pygame.display.set_mode((440, 440))

def grid(w, h):
    hori = 0
    vert = 0
    for i in range(0, w):
        line = []
        colorRow = []
        for j in range(0, h):
            colo = random.randint(0, 4)
            line.append(pygame.Rect(hori, vert, width, height))
            colorRow.append(colo)
            hori += width
        vert += height
        hori = 0
        maze.append(line)
        mazeColor.append(colorRow)

    return maze

grid(20, 20)

# Allows for the ability to draw text on the screen (Kyle Taylor)
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

# Initialize colors (Cameron Snoap)
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
orange = (255, 165, 0)
yellow = (255, 255, 0)
grey = (211, 211, 211)

# Create a rectangle with the size 10x10 at the position (100, 100)
rect = pygame.Rect(11, 11, 0, 0)

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

# Set the frame rate
clock = pygame.time.Clock()
frame_rate = 10

def gameloop():
# Run the game loop
    running = True
    loadGame = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        kill_square()
        handle_keys()

        # Clear the screen
        screen.fill((255, 255, 255))

        # Draw the rectangle on the screen, Kyle Taylor
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

        #color logic, Chase Kerr
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