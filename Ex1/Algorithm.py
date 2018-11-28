
class Algorithm(object):
    """
    An abstract class for different search algorithms
    """
    def __init__(self):
        self.open_set = []
        self.developed_nodes = 0

    def create_path(self, node):
        """
        create the path from a given state to goal state
        :param node
        :return: path
        """
        path = list()
        # run loop until reaching the root
        while getattr(node, "parent") is not None:
            move = getattr(node, "move")
            node = getattr(node, "parent")
            path.append(move)
        path.reverse()
        return path