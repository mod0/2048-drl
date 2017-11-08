import sys
import pygame
import twozerofoureight as tzfe


if __name__ == "__main__":
    # Parse the grid dimension from the command line
    # And use that to create a game window  to
    # house that size of the grid. Here we assume 4
    grid_size = 5

    # Create a game of that dimension
    game = tzfe.TwoZeroFourEight(grid_size)

    # If we paint a rectangle cell of size 64 pixels
    # Also include a header height to display score
    header_height = 48 
    tile_size     = 96
    width, height = tile_size * grid_size, tile_size * grid_size + header_height
    
    # Initialize pygame
    pygame.init()

    # Create a screen
    screen        = pygame.display.set_mode((width, height))
    screen_rect   = screen.get_rect()

    # Create a font object
    font  = pygame.font.Font(None, 48)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            elif event.type == pygame.KEYDOWN:            
                # Now figure out what key it is
                # run the game
                if event.key == pygame.K_LEFT:
                    game.slide_left()
                    game_over, new_tile = game.insert_new_tile()
                elif event.key == pygame.K_UP:
                    game.slide_up()
                    game_over, new_tile = game.insert_new_tile()
                elif event.key == pygame.K_RIGHT:
                    game.slide_right()
                    game_over, new_tile = game.insert_new_tile()
                elif event.key == pygame.K_DOWN:
                    game.slide_down()
                    game_over, new_tile = game.insert_new_tile()

        # Some kinda gray
        kinda_gray = (200,200,200)

        # Kinda orange
        kinda_orange = (252,179,83)
        
        # Fill the screen
        screen.fill(kinda_gray)
        
        # Score string
        score_string = "Score: {0:0>-06d}".format(game.get_score())
        
        # Write out score
        score               = font.render(score_string, True, (0, 0, 0))
        score_rect          = score.get_rect()
        score_rect.topright = screen_rect.topright
        screen.blit(score, score_rect)

        
        # Now draw the game onto the screen
        for i in xrange(grid_size):
            for j in xrange(grid_size):
                pass
            
        # Update the display
        pygame.display.update()
