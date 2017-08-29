from Util.util import Util

from Operations.operations import Operations

class PowerDifference (Operations):
	@staticmethod
	def sop (value1, value2, p=2):
		#return abs (value1 ** p - value2 ** p) ** (1.0 / p)
		if p % 2 is not 0:
			value1 = abs (value1)
			value2 = abs (value2)
		diff = value1 ** p - value2 ** p
		if (1.0 / p) % 2 is not 0:
			diff = abs (diff)
		return diff ** (1.0 / p)
	def __init__ (self,
		min_value1, max_value1,
		min_value2, max_value2, p=2):
		if p is 0: raise Exception (
			"p:%s is 0" % p)
		
		extrema = [
			PowerDifference.sop (min_value1, max_value2, p),
			PowerDifference.sop (max_value1, min_value2, p)]
		if Util.rangeIntersection (
			min_value1, max_value1,
			min_value2, max_value2) in [3, 4, 5, 6]:
			extrema.append (0)
		min_value = min (extrema)
		max_value = max (extrema)
		
		self.p = p

		Operations.__init__ (self, min_value, max_value,
			(min_value1, max_value1),
			(min_value2, max_value2))
	def op (self, value1, value2):
		Operations.op (self, value1, value2)
		ret = PowerDifference.sop (value1, value2, self.p)
		self.validateOp (ret)
		return ret