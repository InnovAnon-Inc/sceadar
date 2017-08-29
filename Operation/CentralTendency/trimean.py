from Operation.operation import Operation

from Operation.CentralTendency.arithmeticmean import ArithmeticMean
from Operation.CentralTendency.geometricmean  import GeometricMean
from Operation.CentralTendency.harmonicmean   import HarmonicMean

class TriMean (Operation):
	def __init__ (self, am, gm, hm):
		if not isinstance (am, ArithmeticMean): raise Exception (
			"am:%s is not ArithmeticMean" % am)
		if  not isinstance (gm,          GeometricMean) \
		and not isinstance (gm.delegate, GeometricMean): raise Exception (
			"gm:%s is not GeometricMean" % gm)
		if  not isinstance (hm,          HarmonicMean) \
		and not isinstance (hm.delegate, HarmonicMean): raise Exception (
			"hm:%s is not HarmonicMean" % hm)
		if am.min_value is not gm.min_value: raise Exception (
			"am.min:%s is not gm.min:%s" % (am.min_value, gm.min_value))
		if am.min_value is not hm.min_value: raise Exception (
			"am.min:%s is not hm.min:%s" % (am.min_value, hm.min_value))
		if am.max_value is not gm.max_value: raise Exception (
			"am.max:%s is not gm.max:%s" % (am.max_value, gm.max_value))
		if am.max_value is not hm.max_value: raise Exception (
			"am.max:%s is not hm.max:%s" % (am.max_value, gm.max_value))
		if am.length    is not gm.length:    raise Exception (
			"am.length:%s is not gm.length:%s" % (am.length, gm.length))
		if am.length    is not hm.length:    raise Exception (
			"am.length:%s is not hm.length:%s" % (am.length, hm.length))
		self.am = am
		self.gm = gm
		self.hm = hm
		self.l = [am, gm, hm]
		Operation.__init__ (self, am.length,
			(am.min_value, gm.min_value, hm.min_value),
			(am.max_value, gm.max_value, hm.max_value))
	def update (self, elem):
		Operation.update (self, elem)
		
		#self.am.update (elem)
		#self.gm.update (elem)
		#self.hm.update (elem)
		map (lambda m: m.update (elem), self.l)
		
		am = self.am.cupdates (elem)
		gm = self.gm.cupdates (elem)
		hm = self.hm.cupdates (elem)
		# TODO
		#map (lambda m: ? = m.cupdates (elem), self.l)
		if am < gm: raise Exception (
			"am:%s < gm:%s" % (am, gm))
		if gm < hm: raise Exception (
			"gm:%s < hm:%s" % (gm, hm))
	def finish (self):
		#self.am.finish ()
		#self.gm.finish ()
		#self.hm.finish ()
		map (lambda m: m.finish (), self.l)
		self.value = (self.am.value, self.gm.value, self.hm.value)
		Operation.finish (self)
	def validate (self):
		Operation.validate (self)
		#self.am.validate ()
		#self.gm.validate ()
		#self.hm.validate ()
		map (lambda m: m.validate (), self.l)
		if self.am.value < self.gm.value: raise Exception (
			"am.value:%s >= gm.value:%s" % (am.value, gm.value))
		if self.gm.value < self.hm.value: raise Exception (
			"gm.value:%s >= hm.value:%s" % (gm.value, hm.value))
	def cupdates (self, elem): #return (
		#self.am.cupdates (elem),
		#self.gm.cupdates (elem),
		#self.hm.cupdates (elem))
		return Operation.cupdates (self,
			tuple (map (lambda m: m.cupdates (elem), self.l)))