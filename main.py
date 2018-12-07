import random
import matplotlib.pyplot as plt
from hypothesis import sample_hypothesis
from utils import Distribution

patterns = ["00", "01", "11", "10"]

def run_experiment(error, alpha, m, iter=1000):
	samples = []

	# empirical distributions
	dist = Distribution()

	# initialize h1 randomly
	h = sample_hypothesis(alpha)[0]
	samples.append(h[0])
	dist[h] += 1

	for i in range(iter):
		# randomly sample x, y
		x = random.choice(patterns)
		y = random.choice(patterns)

		# run Markov chain
		h_next = transition(h, m)
		samples.append(h_next)
		dist[curr] += 1

	dist.normalize()

	# make graphs

	# Markov chain visualization from samples

	# cumulative graph from empirical distribution



if __name__ == '__main__':
	n = 4 # number of experiments
	errors = [0.05, 0.05, 0.05, 0.05]
	alphas = [0.5, 0.5, 0.5, 0.01]
	m = [1, 3, 10, 3]

	for i in range(n):
		run_experiment(errors[i], alphas[i], m[i])