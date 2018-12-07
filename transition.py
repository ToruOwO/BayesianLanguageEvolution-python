from hypothesis import *
from learning import *
from utils import *

def transition_matrix(hypothesis, error, alpha, m):
	qx = 1/(4**m) # uniform distribution

	if m > 2:
		# MCMC approximation
		tm = Distribution()

		for i in range(1000):
			# generate random data for (x, y)
			data_instance = [(random.choice(patterns), random.choice(patterns)) for i in range(m)]
			for h in all_compositionals:

				p = 1 # p(hn+1|x,y)*p(y|x,hn)

				# iterate through all (x,y), assuming independence
				for (x, y) in data_instance:
					p *= calc_posterior((h, True), x, y, error, alpha) # p(hn+1|xi,yi)
					p *= calc_pyxh(y, x, hypothesis[0], error) # p(y|x,hn)

				tm[(h,True)] += qx*p

			for h in all_holistics:

				p = 1 # p(hn+1|x,y)*p(y|x,hn)

				# iterate through all (x,y), assuming independence
				for (x, y) in data_instance:
					p *= calc_posterior((h, False), x, y, error, alpha) # p(hn+1|xi,yi)
					p *= calc_pyxh(y, x, hypothesis[0], error) # p(y|x,hn)

				tm[(h, False)] += qx*p


	else:
		# obtain transition matrix by summing over
		# all paris of (x, y)
		data = make_all_data(m)

		tm = Distribution() # p(hn+1|hn), key=hn+1

		for data_instance in data:
			for h in all_compositionals:

				p = 1 # p(hn+1|x,y)*p(y|x,hn)

				# iterate through all (x,y), assuming independence
				for (x, y) in data_instance:
					p *= calc_posterior((h, True), x, y, error, alpha) # p(hn+1|xi,yi)
					p *= calc_pyxh(y, x, hypothesis[0], error) # p(y|x,hn)

				tm[(h,True)] += qx*p

			for h in all_holistics:

				p = 1 # p(hn+1|x,y)*p(y|x,hn)

				# iterate through all (x,y), assuming independence
				for (x, y) in data_instance:
					p *= calc_posterior((h, False), x, y, error, alpha) # p(hn+1|xi,yi)
					p *= calc_pyxh(y, x, hypothesis[0], error) # p(y|x,hn)

				tm[(h, False)] += qx*p

	tm.normalize()
	return tm