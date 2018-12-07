import random
import matplotlib.pyplot as plt
from hypothesis import *
from transition import transition_matrix
from utils import Distribution

patterns = ["00", "01", "11", "10"]

def graph_distribution(xticks, d, file_name):
	x = [i for i in range(len(xticks))]
	y = [d[xticks[i]] for i in range(len(xticks))]
	plt.xticks(x, xticks)
	plt.plot(x, y)
	# plt.show()
	plt.savefig(file_name)

def run_experiment(error, alpha, m, iter=1000):
	samples = []

	# true distribution
	true_dist = sample_distribution(alpha)

	# empirical distribution
	dist = Distribution()

	# initialize h1 randomly
	h = sample_hypothesis(alpha) # [hypothesis, is_comp]
	samples.append(h)
	dist[h] += 1

	print("simulating Markov chain with", iter, "iterations...")
	for i in range(iter):
		if i%100 == 0:
			print("iteration number:", i)

		# run Markov chain
		tm = transition_matrix(h, error, alpha, m)
		h_next = tm.sample()
		samples.append(h_next)
		dist[h_next] += 1
		h = h_next

	dist.normalize()

	return [samples, dist, true_dist]


if __name__ == '__main__':
	xs = [(c, True) for c in all_compositionals] + [(ho, False) for ho in all_holistics]

	n = 5 # number of experiments
	errors = [0.05, 0.05, 0.05, 0.05, 0.05]
	alphas = [0.5, 0.01, 0.5, 0.01, 0.5]
	ms = [1, 1, 3, 3, 10]

	for i in range(n):
		print("running experiment", i, "...")
		result = run_experiment(errors[i], alphas[i], ms[i])
		graph_distribution(xs, result[1], "dist" + str(i) + ".png")
		graph_distribution(xs, result[2], "true_dist" + str(i) + ".png")
		plt.clf()
		with open("experiment" + str(i) + ".txt", 'a+') as f:
			for item in result:
				f.write(str(item))
				f.write('\n')
				f.write('\n')

	# test
	# result = run_experiment(0.05, 0.5, 1, 500)
	# graph_distribution(xs, result[1], "dist.png")
	# graph_distribution(xs, result[2], "true_dist.png")
	# plt.clf()
	# with open('test.txt', 'a+') as f:
	# 	for item in result:
	# 		f.write(str(item))
	# 		f.write('\n')
	# 		f.write('\n')

	# make graphs

	# Markov chain visualization from samples
	# cumulative graph from empirical distribution