import numpy as np
from node import node

class connection(object):
	def __init__(self, inode, onode):
		self.inode = inode
		self.onode = onode
		self.weight = np.random.random() * 4 - 2
		self.enabled = True
		self.inno = -1

		pass

	def printConn(self):
		print(f"{self.inno}. {self.inode.number} -> {self.onode.number} weight : {self.weight} {self.enabled}")