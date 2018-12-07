from hypothesis import *
from learning import *
from transition import *

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

if __name__ == '__main__':
	test_hypothesis()
	test_learning()
	test_transition()