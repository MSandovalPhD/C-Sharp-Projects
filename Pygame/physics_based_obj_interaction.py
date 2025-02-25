import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up display (800x600 window)
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Physics Object Interaction")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Object properties
objects = []  # List of objects (circles) with position, velocity, and size
for _ in range(5):
    objects.append({
        "pos": [random.randint(50, WIDTH-50), random.randint(50, HEIGHT-50)],
        "vel": [random.uniform(-2, 2), random.uniform(-2, 2)],
        "size": 20
    })

# Player (user) properties (blue circle)
player_pos = [WIDTH // 2, HEIGHT // 2]
player_size = 20
speed = 5

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

    # Get keyboard input for player movement (mimics VR input)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_pos[0] -= speed
    if keys[pygame.K_RIGHT]:
        player_pos[0] += speed
    if keys[pygame.K_UP]:
        player_pos[1] -= speed
    if keys[pygame.K_DOWN]:
        player_pos[1] += speed

    # Keep player within screen
    player_pos[0] = max(player_size, min(WIDTH - player_size, player_pos[0]))
    player_pos[1] = max(player_size, min(HEIGHT - player_size, player_pos[1]))

    # Update objects (physics simulation)
    for obj in objects:
        obj["pos"][0] += obj["vel"][0]
        obj["pos"][1] += obj["vel"][1]

        # Bounce off walls (simple physics)
        if obj["pos"][0] <= obj["size"] or obj["pos"][0] >= WIDTH - obj["size"]:
            obj["vel"][0] *= -1
        if obj["pos"][1] <= obj["size"] or obj["pos"][1] >= HEIGHT - obj["size"]:
            obj["vel"][1] *= -1

        # Collision with player (mimics VR object interaction)
        dx = obj["pos"][0] - player_pos[0]
        dy = obj["pos"][1] - player_pos[1]
        distance = (dx * dx + dy * dy) ** 0.5
        if distance < player_size + obj["size"] and pygame.mouse.get_pressed()[0]:  # Left-click to "throw"
            force = 10
            obj["vel"][0] += dx / distance * force
            obj["vel"][1] += dy / distance * force

    # Clear screen
    screen.fill(WHITE)

    # Draw player (blue circle)
    pygame.draw.circle(screen, BLUE, [int(player_pos[0]), int(player_pos[1])], player_size)

    # Draw objects (red circles)
    for obj in objects:
        pygame.draw.circle(screen, RED, [int(obj["pos"][0]), int(obj["pos"][1])], obj["size"])

    # Update display
    pygame.display.flip()

    # Control frame rate for real-time performance (optimization)
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
sys.exit()
