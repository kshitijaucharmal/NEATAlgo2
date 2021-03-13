import numpy as np
from node import node
from connection import connection

class genome(object):
	def __init__(self, ch, create):
		self.ch = ch
		self.inputs = ch.inputs
		self.outputs = ch.outputs

		self.tempConnections = []
		self.usableConnections = []
		self.nodes = []

		self.start_per = 0.1

		if(create):
			self.createNetwork()

		return

	def createNetwork(self):
		for i in range(self.inputs):
			self.nodes.append(node(i))
			self.nodes[i].type = 0

		for i in range(self.outputs):
			self.nodes.append(node(self.inputs + i))
			self.nodes[self.inputs + i].type = 1

		for i in range(self.inputs):
			for j in range(self.outputs):
				self.tempConnections.append(connection(self.nodes[i], self.nodes[self.inputs + j]))

		for i in range(len(self.tempConnections)):
			if np.random.random() < self.start_per:
				x = self.ch.exists(self.tempConnections[i].inode.number, self.tempConnections[i].onode.number)
				if x != None:
					self.tempConnections[i].inno = x
					self.usableConnections.append(self.tempConnections[i])
				else:
					self.tempConnections[i].inno = self.ch.global_inno
					self.ch.global_inno += 1
					self.ch.allConnections.append(self.tempConnections[i])
					self.usableConnections.append(self.tempConnections[i])


		for i in range(len(self.usableConnections)):
			for j in range(i+1, len(self.usableConnections)):
				if self.usableConnections[i].inno > self.usableConnections[j].inno:
					self.usableConnections[i], self.usableConnections[j] = self.usableConnections[j], self.usableConnections[i]

		print("Usable Connections")
		self.printConnections(self.usableConnections)

	def printConnections(self, conns):
		print("-----------------------------------------------")
		for c in conns:
			c.printConn()
		print("-----------------------------------------------")