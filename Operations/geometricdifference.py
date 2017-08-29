from math import sqrt

from Util.util import Util

from Operations.operations import Operations

class GeometricDifference (Operations):
	@staticmethod
	def sop (value1, value2): return sqrt (value1 * value2)
	def __init__ (self,
		min_value1, max_value1,
		min_value2, max_value2):
		if 0 in xrange (min_value1, max_value1 + 1): raise Exception (
			"0 in [%s, %s]" % (min_value1, max_value1))
		if 0 in xrange (min_value2, max_value2 + 1): raise Exception (
			"0 in [%s, %s]" % (min_value2, max_value2))
		
		min_value = GeometricDifference.sop (min_value1, min_value2)
		max_value = GeometricDifference.sop (max_value1, max_value2)

		Operations.__init__ (self, min_value, max_value,
			(min_value1, max_value1),
			(min_value2, max_value2))
	def op (self, value1, value2):
		Operations.op (self, value1, value2)
		ret = GeometricDifference.sop (value1, value2)
		self.validateOp (ret)
		return ret