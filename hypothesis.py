import random
import numpy as np
from utils import *

all_compositionals = make_all_compositionals()
all_holistics = make_all_holistics()

def prior(alpha, is_compositional):
	if is_compositional:
		return alpha/4
	else:
		return (1-alpha)/256

def sample_hypothesis(alpha):
	"""
	Return a hypothesis with a hierachical prior, 
	allocating a probability of alpha to the set of compositional 
	languages and 1-alpha to the set of holistic languages.

	Return value: [hypothesis, is_compositional]
	Return type: list
	"""
	is_compositional = np.random.binomial(1, alpha)

	if is_compositional:
		# make a compositional prior
		h = random.choice(all_compositionals)
		return [h, True]
	else:
		# make a holistic prior
		h = random.choice(all_holistics)
		return [h, False]

def sample_distribution(alpha):
	dist = Distribution()
	for c in all_compositionals:
		dist[c] += prior(alpha, True)
	for h in all_holistics:
		dist[h] += prior(alpha, False)
	dist.normalize()
	return dist

# test
# print(all_compositionals)
# print(sample_hypothesis(0.5))
# print(sample_distribution(0.5))