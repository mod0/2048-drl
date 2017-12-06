import sys
import time
import pygame
import twozerofoureight as tzfe
import numpy.random as nr


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
    font  = pygame.font.Font(None, 24)
    
    while True:
        game_over = False
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)

        # Generate a random move
        rand_move = nr.randint(4)

        # all moves
        all_moves = ["LEFT", "UP", "RIGHT", "DOWN"]
        
        # Now figure out what key it is
        # run the game
        if all_moves[rand_move]   == "LEFT":
            game.slide_left()
            game_over, new_tile = game.insert_new_tile()
        elif all_moves[rand_move] == "UP":
            game.slide_up()
            game_over, new_tile = game.insert_new_tile()
        elif all_moves[rand_move] == "RIGHT":
            game.slide_right()
            game_over, new_tile = game.insert_new_tile()
        elif all_moves[rand_move] == "DOWN":
            game.slide_down()
            game_over, new_tile = game.insert_new_tile()

        # Some kinda gray
        kinda_gray = (150,150,150)

        # Kinda orange
        kinda_orange = dict()
        kinda_orange[0]    = (238, 228, 218, 0.35)
        kinda_orange[2]    = (238, 228, 218)
        kinda_orange[4]    = (237, 224, 200)
        kinda_orange[8]    = (242, 177, 121)
        kinda_orange[16]   = (245, 149,  99)
        kinda_orange[32]   = (246, 124,  95)
        kinda_orange[64]   = (246,  94,  59)
        kinda_orange[128]  = (237, 207, 114)
        kinda_orange[256]  = (237, 204,  97)
        kinda_orange[512]  = (237, 200,  80)
        kinda_orange[1024] = (237, 197,  63)
        kinda_orange[2048] = (237, 194,  46)

        # Blinding_white
        blinding_white = (255, 255, 255)

        # Blacky black
        blacky_black = (0, 0, 0)

        # Chocolate_brown
        chocolate_brown = (119, 110, 101)

        # Booooo Red
        booooo_red   = (200, 25, 25)
        
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
                tile_value = game.get_tile_value(i, j)
                tile_rect  = pygame.draw.rect(screen, blacky_black, (tile_left, tile_top, tile_size, tile_size), 1)
                screen.fill(kinda_orange[tile_value], tile_rect)
                if tile_value > 0:
                    # draw a square tile                    
                    tile_value_string              = "{0:^4d}".format(tile_value)
                    tile_value_surface             = font.render(tile_value_string, True, chocolate_brown)
                    tile_value_surface_rect        = tile_value_surface.get_rect()
                    tile_value_surface_rect.center = tile_rect.center
                    screen.blit(tile_value_surface, tile_value_surface_rect)

        # check game over and paint it to top left in RED
        if game_over:
            game_over_surface      = font.render("Game Over", True, booooo_red)
            game_over_rect         = game_over_surface.get_rect()
            game_over_rect.topleft = screen_rect.topleft
            screen.blit(game_over_surface, game_over_rect)
            print "Game Over"
            sys.exit(0)

        # 200 ms delay
        time.sleep(0.2)
                    
        # Update the display
        pygame.display.update()
