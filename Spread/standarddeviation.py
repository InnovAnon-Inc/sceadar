from Spread.stddevct import StdDevCT
from Operations.differencepower import DifferencePower

from Spread.generalizedvariance import GeneralizedVariance

class StandardDeviation (GeneralizedVariance):
	def __init__ (self, length, min_value, max_value, arithmetic_mean):
		GeneralizedVariance.__init__ (self, length, min_value, max_value,
			StdDevCT, DifferencePower, arithmetic_mean)
	#def update (self, elem):
	#def finish (self):
	#	GeneralizedVariance.finish (self)
	#	self.value = sqrt (self.ct.value)
		#self.ct.finish ()
		#self.value = sqrt (self.ct.value)
		#Spread.finish (self)
	#def validate (self):
	#def cupdates (self, elem):