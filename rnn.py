"""
Adapted from
https://github.com/burliEnterprises/tensorflow-shakespeare-poem-generator/blob/master/rnn_train.py
"""

from __future__ import absolute_import, division, print_function
import tensorflow as tf
from tensorflow.contrib import layers
from tensorflow.contrib import rnn
import time
import math
import numpy as np
tf.set_random_seed(0)

SEQLEN = 30
BATCHSIZE = 200
ALPHASIZE = txt.ALPHASIZE
INTERNALSIZE = 512
NLAYERS = 3
learning_rate = 0.001  # fixed learning rate
dropout_pkeep = 0.8    # some dropout

datadir = "./tweets.csv"
codetext, valitext, bookranges = txt.read_data_files(shakedir, validation=True)

print(codetext)