class Util:
	@staticmethod
	#def range (vector): return max (vector) - min (vector) + 1
	def range (min_value, max_value): return max_value - min_value + 1
	@staticmethod
	def approxEqual(x, y, tolerance=0.001):
		return abs (x-y) <= 0.5 * tolerance * (x + y)
	@staticmethod
	def rangeIntersection (min1, max1, min2, max2):
		if max1 < min2: return 1
		if max2 < min1: return 2
		if min1 < min2 and max1 < max2: return 3
		if min2 < min1 and max2 < max1: return 4
		if min1 < min2 and max2 < max1: return 5
		if min2 < min1 and max1 < max2: return 6
		return 0