import numpy as np

patterns = ["00", "01", "11", "10"]

# hypothesis

def make_all_holistics():
	res = [()]

	for i in range(len(patterns)):
		temp = []
		for r in res:
			for p in patterns:
				temp.append(r+(p,))
		res = temp

	return res

def make_all_compositionals():
	res = []
	for p in patterns:
		mappings = {"0":p[0], "1":p[1]}
		temp = ()
		for pp in patterns:
			temp += (mappings[pp[0]]+mappings[pp[1]],)
		res.append(temp)
	return res


# (x, y) pairs

def make_all_xy():
	res = []
	for x in patterns:
		for y in patterns:
			res.append((x,y))
	return res


def make_all_data(m):
	"""
	All size-m lists of (x,y) pairs
	"""
	all_xy = make_all_xy()
	res = [[]]
	for i in range(m):
		temp = []
		for r in res:
			for xy in all_xy:
				temp.append(r+[xy])
		res = temp
	return res


class Distribution(dict):
	"""
	The Distribution class extend the Python dictionary such that
    each key's value should correspond to the probability of the key.
    """
	def __missing__(self, key):
		# if the key is missing, return probability 0
		return 0

	def normalize(self):
		z = sum(self.values()) # normalization constant
		for key in self.keys():
			self[key] /= z

	def sample(self):
		# randomly choose a sample based on the distribution
		keys = []
		probs = []
		for key, prob in self.items():
			keys.append(key)
			probs.append(prob)

		rand_idx = np.where(np.random.multinomial(1, probs))[0][0]
		return keys[rand_idx]
		