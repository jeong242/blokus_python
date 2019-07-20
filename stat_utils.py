from math import sqrt

def mean(list):
	return 1.0*reduce(lambda a, b: a+b, list) / len(list)

def sd(list):
	if len(list) == 1:
		print("Sample size == 1. Get more sample")
		return None

	mu = mean(list)
	dist_sqrd = map(lambda a: (a-mu)**2, list)
	return sqrt( 1.0*sum(dist_sqrd) / (len(list) - 1) )
