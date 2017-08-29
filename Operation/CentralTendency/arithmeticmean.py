from Operation.CentralTendency.centraltendency import CentralTendency

from Util.util import Util

from Operation.sumop import SumOp
from Operation.cntop import CntOp

class ArithmeticMean (CentralTendency):
	def __init__ (self, length, min_value, max_value):
		self.sumOp = SumOp (length, min_value, max_value)
		self.cntOp = CntOp (length, min_value, max_value)
		self.s   = 0
		#self.cnt = 0
		CentralTendency.__init__ (self, length, min_value, max_value)
	def update (self, elem):
		#CentralTendency.update (self, elem / float (self.length))
		CentralTendency.update (self, elem)
		self.s += elem
		self.sumOp.update (elem)
		self.cntOp.update (elem)
	def finish (self):
		self.value = float (self.s) / float (self.length)
		self.sumOp.finish ()
		self.cntOp.finish ()
		CentralTendency.finish (self)
	def validate (self):
		CentralTendency.validate (self)
		self.sumOp.validate ()
		self.cntOp.validate ()
		#if self.s is not self.sumOp.value: raise Exception (
		if not Util.approxEqual (self.s, self.sumOp.value): raise Exception (
			"s:%s is not sumOp:%s" % (self.s, self.sumOp.value))
		if self.length is not self.cntOp.value: raise Exception (
			"length:%s is not cntOp:%s" % (self.length, self.cntOp.value))
		quot = float (self.sumOp.value) / float (self.cntOp.value)
		if self.value != quot: raise Exception (
			"value:%s is not quot:%s" % (self.value, quot))
	def cupdates (self, elem): return CentralTendency.cupdates (self, elem)