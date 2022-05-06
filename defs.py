import random
SIZE = 1
NORMALIZE = 93
NORMALIZE_LR = 46 #half of the original normalize to cover each half of the grid
ROTATE_PROB = 0.25
LEFT_RIGHT_PROB = 0.5
NNET_INPUT = 2
NNET_HIDDEN = 2
NNET_OUTPUT = 1
#Range of the x-axis
POS_RANGE = 7
NEG_RANGE = -3

POS_FLOAT = random.uniform(0.90, 1.05)
NEG_FLOAT = random.uniform(1.00, 1.05) 