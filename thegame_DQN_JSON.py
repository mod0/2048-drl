import sys
import time
import pygame
import twozerofoureight as tzfe
import numpy as np
import matplotlib.pyplot as plt

import tensorflow as tf
import tensorforce
#from tensorforce.config import Configuration
from tensorforce.agents import DQNAgent
from tensorforce.core.networks import LayeredNetwork as RFN
#from tensorforce.core.networks import from_json
 
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

#QA_CNN = [{"type": "conv2d", "size": 64,"window": 2,"stride": 1},{"type": "conv2d","size": 128,"window": 2,"stride": 1},{"type": "flatten"},{"type": "dense","size": 128}]
QA_CNN = []
C1 = dict()
C1['type'] = 'conv2d'
C1['size'] = 512
C1['window'] = 2
C1['stride'] = 1
QA_CNN.append(C1)
C2 = dict()
C2['type'] = 'conv2d'
C2['size'] = 4096
C2['window'] = 2
C2['stride'] = 1
QA_CNN.append(C2)
F = dict()
F['type'] = 'flatten'
QA_CNN.append(F)
D1 = dict()
D1['type'] = 'dense'
D1['size'] = 512
QA_CNN.append(D1)

# Blinding_white
blinding_white = (255, 255, 255)

# Blacky black
blacky_black = (0, 0, 0)

# Chocolate_brown
chocolate_brown = (119, 110, 101)

# Booooo Red
booooo_red   = (200, 25, 25)

##WZ
num_episodes = 5000
artificial_delay = 0
reward_history = []

"""
class ReinforceCNN(Network):

    def tf_apply(self, x):
        input_layer = x  # 64x64x3-dim, float
        num_filter1 = 256
        num_filter2 = 512
        num_dense = 512
        initializer = tf.random_normal_initializer(mean=0.1, stddev=0.01, dtype=tf.float32)

        # CNN
        weights = tf.get_variable(name='W1', shape=(2, 2, 1, num_filter1), initializer=initializer)
        layer1 = tf.nn.conv2d(input_layer, filter=weights, strides=(1, 1, 1, 1), padding='VALID')
        C1_layer = tf.nn.relu(layer1)
        
        weights = tf.get_variable(name='W2', shape=(2, 2, num_filter1, num_filter2), initializer=initializer)
        layer2 = tf.nn.conv2d(C1_layer, filter=weights, strides=(1, 1, 1, 1), padding='VALID')
        C2_layer = tf.nn.relu(layer2)
       
        flatten_layer = tf.reshape(C2_layer, shape=(-1, 4*num_filter2))               
        W_D1 = tf.Variable(tf.truncated_normal(shape=[4*num_filter2,num_dense], stddev=0.1))
        b_D1 = tf.Variable(tf.constant(0.1, shape=[num_dense]))
        
        D1_layer = tf.nn.relu(tf.matmul(flatten_layer, W_D1) + b_D1)
        CNN_output = tf.nn.softmax(D1_layer)
        
        return  CNN_output
"""
if __name__ == "__main__":
    # Parse the grid dimension from the command line
    # And use that to create a game window  to
    # house that size of the grid. Here we assume 4
    grid_size = 4

    # # Initialize pygame
    # pygame.init()

    # # If we paint a rectangle cell of size 64 pixels
    # # Also include a header height to display score
    # header_height = 48 
    # tile_size     = 96
    # width, height = tile_size * grid_size, tile_size * grid_size + header_height

    # # Create a screen
    # screen        = pygame.display.set_mode((width, height))
    # screen_rect   = screen.get_rect()
    
    # # Create a font object
    # font  = pygame.font.Font(None, 24)

    QA_states = dict(shape=(4,4,1), type='float')
    #QA_states = dict(shape=(16,), type='float')
    QA_actions = dict(type='int', num_actions=4) 
    QA_network = RFN.from_json('RF_CNN_config.json')

    
    #QA_dummy = [dict(type='dense', size=32), dict(type='dense', size=32)]
    agent = tensorforce.agents.DQNAgent(states_spec = QA_states, 
                                        actions_spec = QA_actions, 
                                        network_spec = QA_CNN, 
                                        device=None,
                                        #session_config=None,
                                        scope='dqn',
                                        saver_spec=None, 
                                        summary_spec=None,
                                        distributed_spec=None,
                                        optimizer=dict(
                                            type='adam',
                                            learning_rate=1e-3
                                        ), 
                                        discount=0.99, 
                                        variable_noise=None,
                                        #states_preprocessing_spec=None,
                                        #explorations_spec=None,
                                        #reward_preprocessing_spec=None, 
                                        #distributions_spec=None, 
                                        entropy_regularization=None,
                                        target_sync_frequency=10000, 
                                        target_update_weight=1.0,
                                        double_q_model=False,
                                        huber_loss=None, 
                                        batched_observe=1,
                                        batch_size=10,
                                        memory=None,
                                        first_update=100,
                                        update_frequency=4,
                                        repeat_update=1)
    
    for e in range(num_episodes):
        # Create a game of that dimension
        game = tzfe.TwoZeroFourEight(grid_size)
        
        ##WZ
        ### RF INIT ###
       
        agent.reset()
        
        last_score = 0
        game_over = False
        ##WZ
    
        while not(game_over):
           
            
            # for event in pygame.event.get():
            #     if event.type == pygame.QUIT:
            #         sys.exit(0)
    
            # Generate a random move
            ##WZ
            #state = np.reshape(game.get_state(),-1)
            state = np.expand_dims(game.get_state(),axis=2) 
            action = agent.act(states=state)
            
            rand_move = action
            ##WZ
    
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
            
            ##WZ
            score = game.get_score()
            latest_reward = score-last_score
            agent.observe(reward=latest_reward, terminal=game_over)
            last_score = score
            ##WZ
            
            # # Fill the screen
            # screen.fill(kinda_gray)
            
            # # Score string
            # score_string = "Score: {0:0>-06d}".format(game.get_score())
            
            # # Write out score
            # score_surface       = font.render(score_string, True, blacky_black)
            # score_rect          = score_surface.get_rect()
            # score_rect.topright = screen_rect.topright
            # screen.blit(score_surface, score_rect)
            
            # # Now draw the game onto the screen
            # for i in range(grid_size):
            #     for j in range(grid_size):
            #         tile_top   = i * tile_size + header_height
            #         tile_left  = j * tile_size
            #         tile_value = game.get_tile_value(i, j)
            #         tile_rect  = pygame.draw.rect(screen, blacky_black, (tile_left, tile_top, tile_size, tile_size), 1)
            #         screen.fill(kinda_orange[tile_value], tile_rect)
            #         if tile_value > 0:
            #             # draw a square tile                    
            #             tile_value_string              = "{0:^4d}".format(tile_value)
            #             tile_value_surface             = font.render(tile_value_string, True, chocolate_brown)
            #             tile_value_surface_rect        = tile_value_surface.get_rect()
            #             tile_value_surface_rect.center = tile_rect.center
            #             screen.blit(tile_value_surface, tile_value_surface_rect)

            print("Current score: {}".format(score), end="\r")
            
            # check game over and paint it to top left in RED
            if game_over:
                #game_over_surface      = font.render("Game Over", True, booooo_red)
                #game_over_rect         = game_over_surface.get_rect()
                #game_over_rect.topleft = screen_rect.topleft
                #screen.blit(game_over_surface, game_over_rect)
                print("Game Over! Episode: %d Final score: %d" % (e,score))
                reward_history.append(score)
    
            # 200 ms delay
            time.sleep(artificial_delay)
            
            # # Update the display
            # pygame.display.update()
            

#evaluation:
print('--Evaluation--')
print('Mean: %d' %np.mean(reward_history))
print('Highest score: %d' %np.max(reward_history))
plt.plot(reward_history)
plt.xlabel('Episodes')
plt.ylabel('Score')
plt.grid(True)
plt.title('RandomAgent')

# pygame.quit()
sys.exit(0)
