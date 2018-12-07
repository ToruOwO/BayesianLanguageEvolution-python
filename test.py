from hypothesis import *
from learning import *
from transition import *
from main import run_experiment, graph_distribution

# test hypothesis.py
def test_hypothesis():
	print(all_compositionals)
	print(sample_hypothesis(0.5))
	print(sample_distribution(0.5))

# test learning.py
def test_learning():
	h_next = [("00","11","11","01"), False]
	print(calc_posterior(h_next, "01", "00", 0.05, 0.5))

# test transition.py
def test_transition():
	h = (("00","11","11","10"), False)
	res = transition_matrix(h, 0.05, 0.3, 1)
	print(res)

def test_main():
	result = run_experiment(0.05, 0.5, 1, 500)
	graph_distribution(xs, result[1], "dist.png")
	graph_distribution(xs, result[2], "true_dist.png")
	plt.clf()
	with open('test.txt', 'a+') as f:
		for item in result:
			f.write(str(item))
			f.write('\n')
			f.write('\n')

if __name__ == '__main__':
	test_hypothesis()
	test_learning()
	test_transition()
	test_main()