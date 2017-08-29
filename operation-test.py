from Operation.sumop  import SumOp
from Operation.cntop  import CntOp
from Operation.prodop import ProdOp
from Operation.minop  import MinOp
from Operation.maxop  import MaxOp
from Operation.CentralTendency.arithmeticmean import ArithmeticMean
from Operation.CentralTendency.geometricmean  import GeometricMean
from Operation.CentralTendency.harmonicmean   import HarmonicMean
from Operation.CentralTendency.midrange import MidRange
from Operation.CentralTendency.GeneralizedMean.quadraticmean \
import QuadraticMean
from Operation.CentralTendency.GeneralizedMean.cubicmean \
import CubicMean
from Operation.CentralTendency.GeneralizedMean.generalizedmean \
import GeneralizedMean

if __name__ == '__main__':
	l = list (xrange (10))
	print len (l)
	print min (l)
	print max (l)
	
	sumop = SumOp (len (l), min (l), max (l))
	map (sumop.update, l)
	sumop.finish ()
	sumop.validate ()
	print sumop.value
	
	cntop = CntOp (len (l), min (l), max (l))
	map (cntop.update, l)
	cntop.finish ()
	cntop.validate ()
	print cntop.value
	
	sumop = SumOp (len (l), min (l), max (l))
	cntop = CntOp (len (l), min (l), max (l))
	am = ArithmeticMean (len (l), min (l), max (l))
	map (am.update, l)
	am.finish ()
	am.validate ()
	print am.value
	
	l1 = map (lambda x: x + 1, l)
	gm = GeometricMean (len (l1), min (l1), max (l1))
	map (gm.update, l1)
	gm.finish ()
	gm.validate ()
	print gm.value - 1
	
	prodop = ProdOp (len (l1), min (l1), max (l1))
	cntop = CntOp (len (l1), min (l1), max (l1))
	hm = HarmonicMean (len (l1), min (l1), max (l1))
	map (hm.update, l1)
	hm.finish ()
	hm.validate ()
	print hm.value - 1
	
	assert am.value >= gm.value - 1
	assert gm.value >= hm.value
	
	# TODO trimean

	minop = MinOp (len (l), min (l), max (l))
	map (minop.update, l)
	minop.finish ()
	minop.validate ()
	print minop.value
	
	maxop = MaxOp (len (l), min (l), max (l))
	map (maxop.update, l)
	maxop.finish ()
	maxop.validate ()
	print maxop.value
	
	minop = MinOp (len (l), min (l), max (l))
	maxop = MaxOp (len (l), min (l), max (l))
	mr = MidRange (len (l), min (l), max (l))
	map (mr.update, l)
	mr.finish ()
	mr.validate ()
	print mr.value
	
	qm = QuadraticMean (len (l), min (l), max (l))
	map (qm.update, l)
	qm.finish ()
	qm.validate ()
	print qm.value
	
	cm = CubicMean (len (l), min (l), max (l))
	map (cm.update, l)
	cm.finish ()
	cm.validate ()
	print cm.value
	
	gm = GeneralizedMean (len (l), min (l), max (l))
	map (gm.update, l)
	gm.finish ()
	gm.validate ()
	print gm.value
	
	sqm = GeneralizedMean (len (l), min (l), max (l), .5)
	map (sqm.update, l)
	sqm.finish ()
	sqm.validate ()
	print sqm.value