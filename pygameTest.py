# pip install pygame
# Need to import to use the module
import pygame

# Initiate pygame
pygame.init()

display_width = 800
display_height = 600

# Game surface or canvas that game is drawn onto.  Function literally returns a pygame.Surface object.
# Resolution 800px by 600px.  Double parenthesis because TUPLE. Non-tuple argument will blow-up function.
gameDisplay = pygame.display.set_mode((display_width,display_height))

# Window title
pygame.display.set_caption('A bit Racey')

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

car_width = 73

# Track time in the game
clock = pygame.time.Clock()

# Load racecar image into carImg variable
carImg = pygame.image.load('racecar.png')

# Draw the image to the game surface and place it at x and y
def car(x,y):
    gameDisplay.blit(carImg,(x,y))

def game_loop():
    # Starting points for car defined
    x =  (display_width * 0.45)
    y = (display_height * 0.8)

    # 
    x_change = 0
    
    gameExit = False

    while not crashed:
        # Game loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
        
            #############################
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    x_change = -5
                elif event.key == pygame.K_d:
                    x_change = 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a or event.key == pygame.K_d:
                    x_change = 0
            #############################
            print(event)

        #############
        x += x_change
        #############


        # Paint the game surface white.    
        gameDisplay.fill(white)
        car(x,y)
        
        # Updates a portion of the game surface. Without arguments is the same as display.flip().
        # Whole surface is updated
        pygame.display.update()

        # Frames per second
        clock.tick(60)

pygame.quit()
quit()