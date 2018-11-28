from Algorithm import Algorithm

class BFS(Algorithm):
    """
    the class solves different problems by running BFS algorithm
    """
    def run(self, init_state, goal_state):
        """
        run BFS algorithm on a given problem
        :param init_state: the initial state of the problem
        :param goal_state: the requsted goal state fo the problem
        :return: the path to the goal state and number fo developed nodes
        """
        self.enqueue(init_state)
        # for each node develop his successors
        while self.open_set:
            node = self.dequeue()
            # we have reach to requested goal state
            if goal_state.is_equal(node):
                # create the path to this state
                path = self.create_path(node)
                return path , self.developed_nodes
            # run through all children of this node
            for child in node.get_all_children():
                # add child to the future path
                self.enqueue(child)

    def enqueue(self, node):
        """
        append node to the end of the queue
        :param a node
        :return:
        """
        self.open_set.append(node)

    def dequeue(self):
        """
        pop first node at the end of queue and add count of developed nodes
        :return: new node
        """
        self.developed_nodes += 1
        return self.open_set.pop(0)


