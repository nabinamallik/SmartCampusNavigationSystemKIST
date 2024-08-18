import json

class NodeManager:
    def __init__(self, nodes_file):
        with open(nodes_file, 'r') as file:
            self.nodes = json.load(file)

    def get_position(self, node):
        return self.nodes.get(node)

    def get_all_nodes(self):
        return self.nodes
