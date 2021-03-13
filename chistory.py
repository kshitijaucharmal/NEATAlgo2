import numpy as np

class chistory(object):
	def __init__(self, inputs, outputs):
		self.inputs = inputs
		self.outputs = outputs
		self.allConnections = []
		self.global_inno = 0
		pass

	def exists(self, n1, n2):
		for x in self.allConnections:
			if (n1 == x.inode.number) and (n2 == x.onode.number):
				return x.inno
		return None