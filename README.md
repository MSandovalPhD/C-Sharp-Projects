# Python code using Pygame

Pygame is used to create the game screen and handle events, while Numpy is used for vector operations to move the player and enemy and check for collision.

# main_pygame.py

This code creates a simple game where the player (represented by a yellow circle) can be moved with the arrow keys, while an enemy (represented by a red circle) moves towards the player. If the player and enemy collide, the game ends.

# character_movement.py

This script creates a simple 2D character (e.g., an avatar) that moves in real time based on keyboard or mouse inputs, mimicking VR character animation and user interaction. It includes basic optimisation (e.g., frame rate control).

# physics_based_obj_interaction.py

This script creates a 2D physics simulation where a user can “throw” or move objects in real-time, mimicking physics and object manipulation (e.g., for Workrooms or gameplay). It includes basic collision detection and optimisation.

# General Setup Instructions

- Install Python (3.8+) and Pygame are installed (pip install pygame).
- Save each script as .py files, run in a Python environment, and test with a keyboard/mouse. For VR relevance, document how these could scale to 3D/VR (e.g., in a README).
- Add mouse or joystick inputs to mimic VR controllers (e.g., using pygame.joystick).  
- Optimise further by reducing draw calls or adding LOD concepts, reflecting your real-time optimization expertise.
