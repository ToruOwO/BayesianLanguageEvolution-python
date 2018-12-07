# The learning step of the process, where
# the learner x_n+1 sees (xn, yn) and computes
# a posterior distribution over h_(n+1) using
# Bayes' rule

from hypothesis import *

patterns = ["00", "01", "11", "10"]

# p(y|x,h)
def calc_pyxh(y, x, hypothesis, error):
	"""
	hypothesis: a tuple matching the given patterns
	"""
	if x not in patterns:
		# not a valid pattern
		return 0

	idx = patterns.index(x)
	if hypothesis[idx] == y:
		# x maps to y in h
		return 1-error
	else:
		return error/3


# p(yn|xn)
def calc_pyx(x, y, error, alpha):
	res = 0
	for c in all_compositionals:
		res += prior(alpha, True)*calc_pyxh(y, x, c, error)
	for h in all_holistics:
		res += prior(alpha, False)*calc_pyxh(y, x, h, error)
	return res


# p(h_n+1|xn,yn)
def calc_posterior(h_next, x, y, error, alpha):
	"""
	h_next = [hypothesis, is_compositional]
	"""
	pyx = calc_pyx(x, y, error, alpha)
	pyxh_next = calc_pyxh(y, x, h_next[0], error)
	ph_next = prior(alpha, h_next[1])
	return pyxh_next*ph_next/pyx