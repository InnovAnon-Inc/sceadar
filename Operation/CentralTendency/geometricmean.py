from math import log, exp

from Util.util import Util

from Operation.CentralTendency.centraltendency import CentralTendency

from Operation.prodop import ProdOp
from Operation.cntop import CntOp

class GeometricMean (CentralTendency):
	@staticmethod
	def doop (elem, length):
		if length % 2 is not 0: elem = abs (elem)
		return elem ** (1.0 / length)
	def __init__ (self, length, min_value, max_value):
		self.prodOp = ProdOp (length, min_value, max_value)
		self.cntOp = CntOp (length, min_value, max_value)
		self.p = 1
		self.s = 0
		if 0 in xrange (min_value, max_value + 1): raise Exception (
			"0 in [%s, %s]" % (min_value, max_value))
		CentralTendency.__init__ (self, length, min_value, max_value)
	def update (self, elem):
		CentralTendency.update (self, elem)
		#elem = abs (elem) # TODO verify correctness
		#tfe = elem ** (1.0 / float (self.length))
		tfe = GeometricMean.doop (elem, self.length)
		#CentralTendency.update (self, tfe)
		self.p *= tfe
		self.s += log (elem)
		self.prodOp.update (elem)
		self.cntOp.update (elem)
	def finish (self):
		self.value = self.p
		self.v2 = exp (float (self.s) / float (self.length))
		self.prodOp.finish ()
		self.cntOp.finish ()
		CentralTendency.finish (self)
	def validate (self):
		CentralTendency.validate (self)
		self.prodOp.validate ()
		self.cntOp.validate ()
		if not Util.approxEqual (self.value, self.v2): raise Exception (
			"value:%s is not v2:%s" % (self.value, self.v2))
		#quot = self.prodOp.value ** (1.0 / float (self.cntOp.value))
		quot = GeometricMean.doop (self.prodOp.value, self.cntOp.value)
		if not Util.approxEqual (self.value, quot): raise Exception (
			"value:%s is not quot: %s" % (self.value, quot))
	def cupdates (self, elem): return CentralTendency.cupdates (self, elem)