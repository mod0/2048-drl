import sys
import pygame
import twozerofoureight as tzfe


if __name__ == "__main__":
    # Parse the grid dimension from the command line
    # And use that to create a game window  to
    # house that size of the grid. Here we assume 4
    grid_size = 4

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
        kinda_gray = (150,150,150)

        # Kinda orange
        kinda_orange = (252,179,83)

        # Blacky black
        blacky_black = (0, 0, 0)
        
        # Fill the screen
        screen.fill(kinda_gray)
        
        # Score string
        score_string = "Score: {0:0>-06d}".format(game.get_score())
        
        # Write out score
        score_surface       = font.render(score_string, True, blacky_black)
        score_rect          = score_surface.get_rect()
        score_rect.topright = screen_rect.topright
        screen.blit(score_surface, score_rect)

        
        # Now draw the game onto the screen
        for i in xrange(grid_size):
            for j in xrange(grid_size):
                tile_top   = i * tile_size + header_height
                tile_left  = j * tile_size
                tile_rect  = pygame.draw.rect(screen, kinda_orange, (tile_left, tile_top, tile_size, tile_size), 1)
                tile_value = game.get_tile_value(i, j)
                if tile_value > 0:
                    tile_value_string              = "{0:^4d}".format(tile_value)
                    tile_value_surface             = font.render(tile_value_string, True, blacky_black)
                    tile_value_surface_rect        = tile_value_surface.get_rect()
                    tile_value_surface_rect.center = tile_rect.center
                    screen.blit(tile_value_surface, tile_value_surface_rect)
            
        # Update the display
        pygame.display.update()
