# pip install pygame
# Need to import to use the module
import pygame

# Initiate pygame
pygame.init()

# Game surface or canvas that game is drawn onto.  Function literally returns a pygame.Surface object.
# Resolution 800px by 600px.  Double parenthesis because TUPLE. Non-tuple argument will blow-up function.
gameDisplay = pygame.display.set_mode((800,600))

# Window title
pygame.display.set_caption('A bit Racey')

# Track time in the game
clock = pygame.time.Clock()

# Sets to True when user exits window
crashed = False

# Game loop
while not crashed:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        # Prints every event that occurs in the game window to the console
        print(event)
    
    # Updates a portion of the game surface. Without arguments is the same as display.flip().
    # Whole surface is updated
    pygame.display.update()

    # Frames per second
    clock.tick(60)