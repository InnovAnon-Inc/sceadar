from Operation.operation import Operation

class CentralTendency (Operation):
	def __init__ (self, length, min_value, max_value):
		if length is 0: raise Exception ("length is 0")
		Operation.__init__ (self, length, min_value, max_value)