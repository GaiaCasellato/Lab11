import networkx as nx
from database.DAO import DAO


class Model:
    def __init__(self):
        self._grafo = nx.Graph()
        self._idMap = {}



    def getColors(self):
        return DAO.getAllColors()

    def creaGrafo(self,colore):
        self._idMap = {}
        self._grafo.clear()
        self.nodi = DAO.getProducts_color(colore)
        self._grafo.add_nodes_from(self.nodi)
        print("fatto")
        print(self._grafo)

    def getNumNodes(self):
        return len(self._grafo.nodes)






