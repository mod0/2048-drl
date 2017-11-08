import sys
import pygame


if __name__ == "__main__":
    # Parse the grid dimension from the command line
    # And use that to create a game window  to
    # house that size of the grid. Here we assume 4
    grid_size = 5

    # If we paint a rectangle cell of size 64 pixels
    # Also include a header height to display score
    header_height = 48 
    tile_size     = 96
    width, height = tile_size * grid_size, tile_size * grid_size + header_height
    
    # Initialize pygame
    pygame.init()

    # Create a screen
    screen = pygame.display.set_mode((width, height))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            elif event.type == pygame.KEYDOWN:
                # Now figure out what key it is
                # run the game
                # update the display
                pass

            
        # Some kinda gray
        screen.fill((200, 200, 200))
        
        # Update the display
        pygame.display.update()
