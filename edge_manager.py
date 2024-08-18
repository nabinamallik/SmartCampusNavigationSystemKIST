import json

class EdgeManager:
    def __init__(self, edges_file):
        with open(edges_file, 'r') as file:
            self.edges = json.load(file)

    def get_edges(self):
        return self.edges

    def get_weight(self, from_node, to_node):
        return self.edges.get(from_node, {}).get(to_node)
