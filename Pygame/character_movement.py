import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display (800x600 window)
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Character Movement Simulation")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Character properties
character_pos = [WIDTH // 2, HEIGHT // 2]  # Center of screen
character_size = 30  # Size of character (circle)
speed = 5  # Movement speed

# Clock for frame rate control (real-time optimization)
clock = pygame.time.Clock()
FPS = 60  # Target frame rate

# Main loop
running = True
while running:
    # Handle events (user input, like VR controls)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get keyboard input for movement (mimics VR input)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        character_pos[0] -= speed
    if keys[pygame.K_RIGHT]:
        character_pos[0] += speed
    if keys[pygame.K_UP]:
        character_pos[1] -= speed
    if keys[pygame.K_DOWN]:
        character_pos[1] += speed

    # Keep character within screen (boundary check)
    character_pos[0] = max(character_size, min(WIDTH - character_size, character_pos[0]))
    character_pos[1] = max(character_size, min(HEIGHT - character_size, character_pos[1]))

    # Clear screen
    screen.fill(WHITE)

    # Draw character (simple circle for avatar)
    pygame.draw.circle(screen, BLUE, [int(character_pos[0]), int(character_pos[1])], character_size)

    # Update display
    pygame.display.flip()

    # Control frame rate for real-time performance (optimization)
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
sys.exit()
