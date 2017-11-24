# This is parameter setting for all deep learning algorithms
import sys
# Import games
sys.path.append("DQN_GAMES/")

Gamma = 0.99
Learning_rate = 0.001
Epsilon = 1
Final_epsilon = 0.01

Num_action = 2

Num_replay_memory = 500
Num_start_training = 2000
Num_training = 8000
Num_test = 200

Num_plot_episode = 20





Num_update = 5000
Num_batch = 32
Num_skipFrame = 4
Num_stackFrame = 4
Num_colorChannel = 1
Num_step_save = 50000
GPU_fraction = 0.3
Is_train = True
img_size = 80
first_conv   = [8,8,Num_colorChannel * Num_stackFrame,32]
second_conv  = [4,4,32,64]
third_conv   = [3,3,64,64]
first_dense  = [10*10*64, 512]
second_dense = [512, Num_action]
