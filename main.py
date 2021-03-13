import numpy as np
from node import node
from connection import connection
from genome import genome
from chistory import chistory

ch = chistory(4, 2)

g = []
for i in range(2):
	g.append(genome(ch, True))

# g[0].mutate_link()
# g[0].mutate_shift_conn()
# g[0].mutate_random_conn()
# g[0].mutate_enable_disable()
# g[0].mutate_add_node()

print("All Connections")
g[0].printConnections(ch.allConnections)