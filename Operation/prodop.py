from math import log, exp

from Util.util import Util

from Operation.operation import Operation

class ProdOp (Operation):
	@staticmethod
	def doop (elem, length): return elem ** length
	def __init__ (self, length, min_value, max_value):
		self.p = 1
		self.c = 0
		if 0 in xrange (min_value, max_value + 1): raise Exception (
			"0 in [%s, %s]" % (min_value, max_value + 1))
		Operation.__init__ (self, length,
			#min_value ** length, max_value ** length)
			ProdOp.doop (min_value, length), ProdOp.doop (max_value, length))
	def update (self, elem):
		Operation.update (self, elem)
		#Operation.update (self, elem * self.length)
		self.p *= elem
		self.c += log (elem)
	def finish (self):
		self.value = self.p
		self.v2 = exp (self.c)
		Operation.finish (self)
	def validate (self):
		Operation.validate (self)
		if not Util.approxEqual (self.value, self.v2): raise Exception (
			"value: %s is not v2: %s" % (self.value, self.v2))
	def cupdates (self, elem): return Operation.cupdates (self,
		#elem ** self.length)
		ProdOp.doop (elem, self.length))