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

import pygame
import random

# Initialize pygame
pygame.init()
maze = []

# Set the display window size
screen = pygame.display.set_mode((500, 500))

def grid(w, h):
    hori = 0
    vert = 0
    for i in range(0, w):
        line = []
        vert += 22
        for j in range(0, h):
            line.append(pygame.Rect(hori, vert, 22, 22))
            hori += 22
        hori = 0
        maze.append(line)
        # print(line)

    return maze

grid(20, 20)

# Set the display window size
screen = pygame.display.set_mode((500, 500))

# Set the red of the rectangle
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
orange = (255, 165, 0)

# Create a rectangle with the size 10x10 at the position (100, 100)
rect = pygame.Rect(10, 10, 10, 10)

# Move the rectangle with the arrow keys
def handle_keys():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        if rect.y > 10:
            rect.y -= 20
    if keys[pygame.K_DOWN]:
        if rect.y < 490:
            rect.y += 20
    if keys[pygame.K_LEFT]:
        if rect.x > 10:
            rect.x -= 20
    if keys[pygame.K_RIGHT]:
        if rect.x < 490:
            rect.x += 20

# Set the frame rate
clock = pygame.time.Clock()
frame_rate = 10

def gameloop():
# Run the game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        handle_keys()

        # Clear the screen
        screen.fill((255, 255, 255))

        # Draw the rectangle on the screen
        # pygame.draw.rect(screen, red, (0,0), 5, 0)
        for i in range(0, 20):
            for j in range(0,20):
                colo = random.randint(0, 3)
                if (colo == 0):
                    pygame.draw.rect(screen, red, maze[i][j])
                if (colo == 1):
                    pygame.draw.rect(screen, green, maze[i][j])
                if (colo == 2):
                    pygame.draw.rect(screen, blue, maze[i][j])
                if (colo == 3):
                    pygame.draw.rect(screen, orange, maze[i][j])
        
        pygame.draw.circle(screen, black, (rect.x, rect.y), 15, 10)
        #draw player circle on the screen
        pygame.draw.circle(screen, red, (rect.x, rect.y), 10, 0)

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