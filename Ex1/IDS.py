from Algorithm import Algorithm

class IDS(Algorithm):
    """
    the class solves different problems by running IDS algorithm
    """
    def run(self, init_state, goal_state, max_depth):
        """
        run IDS algorithm on a given problem
        :param init_state: the initial state of the problem
        :param goal_state: the requsted goal state fo the problem
        :return: the path to the goal state and number fo developed nodes
        """
        # run through all levels in graph
        for level in range(max_depth):
            # run DFS algorithm until a given depth's level
            goal_found, path = self.dfs_algo(init_state, goal_state, level)
            # there is a  path to goal_state
            if goal_found:
                return path, self.developed_nodes, level
            # continue next iteration and nullify developed nodes
            self.developed_nodes = 0

    def dfs_algo(self, init_state, goal_state, level):
        """
        run dfs algorithm until reaching to a certain level
        :param init_state: the initial state of the problem
        :param goal_state: the requested goal state fo the problem
        :param level: the level of which the algorithm can run to
        :return:
        """
        self.developed_nodes += 1
        # stop condition - init_state is goal_state node
        if goal_state.is_equal(init_state):
            path = self.create_path(init_state)
            return True, path
        # stop condition - level is a non negative number
        if level <= 0:
            return False, None
        # For each child of the current tree process
        for child in init_state.get_all_children():
            # Call recursively to search util with new subtree to explore with lower depth
            found, path = self.dfs_algo(child, goal_state, level - 1)
            # Is processed subtree found path, so return it
            if found:
                return True, path
        # goal state was not found
        return False, None
