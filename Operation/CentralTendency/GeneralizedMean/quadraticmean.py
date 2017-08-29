from Operation.CentralTendency.GeneralizedMean.generalizedmean \
import GeneralizedMean

class QuadraticMean (GeneralizedMean):
	def __init__ (self, length, min_value, max_value):
		GeneralizedMean.__init__ (self, length, min_value, max_value, 2)