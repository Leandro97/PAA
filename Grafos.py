from collections import namedtuple
##########################################################################
#this array will stock the nodes
vet = []

#initializing a adjacence list of a graph with 5 nodes
nodes = 5
graph = [[0 for x in range(0)] for y in range(nodes)] 

#Node definition
Node = namedtuple("node", ["id", "status"])

#Node creation
def createNode(id):
  vet.append(Node(id, 0))

#Node status modification
def newStatus(vet, id, s):
  vet[id] = vet[id]._replace(status = s)  

#Edge creation (bidirectional)
def createEdge(n1, n2):
  graph[n1.id].append(n2.id)
  graph[n2.id].append(n1.id)

####################################Test##################################  
#creation of 5 nodes
createNode(0)
createNode(1)
createNode(2)
createNode(3)
createNode(4)

#creation of biderectional edges (0,1), (1,2), (1,3), (2,3), (3,4) 
createEdge(vet[0], vet[1])
createEdge(vet[1], vet[2])
createEdge(vet[1], vet[3])
createEdge(vet[2], vet[3])
createEdge(vet[3], vet[4])

#printing adjacence list
print(graph)