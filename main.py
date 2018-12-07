import random
import matplotlib.pyplot as plt
from hypothesis import sample_hypothesis
from transition import transition_matrix
from utils import Distribution

patterns = ["00", "01", "11", "10"]

def run_experiment(error, alpha, m, iter=1000):
	samples = []

	# empirical distributions
	dist = Distribution()

	# initialize h1 randomly
	h = sample_hypothesis(alpha) # [hypothesis, is_comp]
	samples.append(h)
	dist[h] += 1

	for i in range(iter):
		# randomly sample x, y
		x = random.choice(patterns)
		y = random.choice(patterns)

		# run Markov chain
		tm = transition_matrix(h, error, alpha, m)
		h_next = tm.sample()
		samples.append(h_next)
		dist[h_next] += 1
		h = h_next

	dist.normalize()

	print(dist)
	print(samples)

	# make graphs

	# Markov chain visualization from samples

	# cumulative graph from empirical distribution



if __name__ == '__main__':
	# n = 4 # number of experiments
	# errors = [0.05, 0.05, 0.05, 0.05]
	# alphas = [0.5, 0.5, 0.5, 0.01]
	# m = [1, 3, 10, 3]

	# for i in range(n):
	# 	run_experiment(errors[i], alphas[i], m[i])

	# test
	run_experiment(0.05, 0.5, 1, 10)