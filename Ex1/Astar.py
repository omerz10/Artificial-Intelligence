from Algorithm import Algorithm
import State
import heapq

class Astar(Algorithm):
    """
    the class solves different problems by running Astar algorithm
    """
    def run(self, init_state, goal_state):
        time_stamp = 0
        # use open set as a priority queue for costs of nodes
        heapq.heapify(self.open_set)
        self.enqueue(init_state)
        while self.open_set:
            node = self.dequeue()
            # we have reach to requested goal state
            if goal_state.is_equal(node):
                # create the path to this state
                path = self.create_path(node)
                return path, self.developed_nodes, getattr(node, "g")
            # run through all children of this node
            for child in node.get_all_children():
                time_stamp += 1
                setattr(child, "time_stamp", time_stamp)
                # set the g value of this child by his parent g value + cost of move
                child_g = getattr(node, "g") + getattr(node, "cost")
                setattr(child, "g", child_g)
                # set the h value of this child by his heuristic function
                setattr(child, "h", child.heuristic())
                # enqueue child into open list and compare it with other children by the priority queue
                self.enqueue(child)


    def enqueue(self, node):
        """
        push node into priority queue (the open_set)
        :param node: a given node
        :return:
        """
        return heapq.heappush(self.open_set, node)


    def dequeue(self):
        """
        pop node from priority queue (the open_set) and add count for developed nodes
        :return: a node from priority queue with the highest value
        """
        self.developed_nodes += 1
        return heapq.heappop(self.open_set)