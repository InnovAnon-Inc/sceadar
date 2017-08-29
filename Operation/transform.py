from Operation.operation import Operation

class Transform (Operation):
	def __init__ (self, length, min_value, max_value,
		tf, untf, Delegate, *dargs):
		if filter (
			lambda x: x is not untf (tf (x)), [min_value, max_value]):
			raise Exception (
				"tf:%s is not inv of untf:%s" % (tf, untf))
		tfl = map (tf, [min_value, max_value])
		self.tf  = tf
		self.untf = untf
		mintf = min (tfl)
		maxtf = max (tfl)
		self.delegate = Delegate (length, mintf, maxtf, *dargs)
		#Operation.__init__ (self, length, mintf, maxtf)
		Operation.__init__ (self, length, min_value, max_value)
	def update (self, elem):
		Operation.update (self, elem)
		tfe = self.tf (elem)
		self.delegate.update (tfe)
	def finish (self):
		self.delegate.finish ()
		untfl = map (self.untf, [self.min_value, self.max_value])
		#self.min_value = min (untfl)
		#self.max_value = max (untfl)
		self.value = self.untf (self.delegate.value)
		Operation.finish (self)
	#def validate (self):
	#	Operation.validate (self)
	def cupdates (self, elem):
		tfe = self.tf (elem)
		tfcupdates = self.delegate.cupdates (tfe)
		return self.untf (tfcupdates)