from hypothesis import *
from learning import *
from utils import *

def transition_matrix(hypothesis, m):
	if m > 4:
		# MCMC approximation
		pass

	else:
		# obtain transition matrix by summing over
		# all paris of (x, y)
		data = make_all_data(m)

		tm = Distribution() # p(hn+1|hn), key=hn+1

		for data_point in data:
			for h in all_compositionals+all_holistics:
				tm[h] = 


# test
h = ("00","11","11","10")
res = transition_matrix(h, 3)
print(res)