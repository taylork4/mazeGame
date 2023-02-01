import pygame

# Initialize pygame
pygame.init()

# Set the display window size
screen = pygame.display.set_mode((500, 500))

# Set the red of the rectangle
red = (255, 0, 0)

# Create a rectangle with the size 10x10 at the position (100, 100)
rect = pygame.Rect(100, 100, 10, 10)

# Move the rectangle with the arrow keys
def handle_keys():
    if keys[pygame.K_UP]:
        if rect.y > 5:
            rect.y -= 1
    if keys[pygame.K_DOWN]:
        if rect.y < 495:
            rect.y += 1
    if keys[pygame.K_LEFT]:
        if rect.x > 5:
            rect.x -= 1
    if keys[pygame.K_RIGHT]:
        if rect.x < 495:
            rect.x += 1

# Set the frame rate
clock = pygame.time.Clock()
frame_rate = 200

# Run the game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get the pressed keys
    keys = pygame.key.get_pressed()

    handle_keys()

    # Clear the screen
    screen.fill((255, 255, 255))

    # Draw the rectangle on the screen
    # pygame.draw.rect(screen, red, rect)
    pygame.draw.circle(screen, red, (rect.x, rect.y), 5, 0)

    # Update the screen
    pygame.display.update()

    # Limit the frame rate
    clock.tick(frame_rate)

# Quit pygame
pygame.quit()
