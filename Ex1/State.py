
class State(object):
    """
    State comprise of the followings:
    board size, initialize state, heuristic value (manhattan) and g value (distance from init state)
    """
    def __init__(self, board_size, state, parent=None, move=None):
        self.board_size = board_size
        self.state = state.split('-')
        self.parent = parent
        self.move = move
        self.time_stamp = 0
        self.cost = 1
        self.h = 0
        self.g = 0


    def change_state(self, zero_state, mid_state, nodes):
        """
        return the new state after swap the zero node with other node
        :param zero_state: comprise of zero_row and zero_col
        :param mid_state: comprise of mid_row and mid_col
        :param nodes: all nodes in the problem
        :return: new state after replacing the nodes
        """
        (zero_row, zero_col) = zero_state
        (swap_row, swap_col) = mid_state
        temp_node = nodes[swap_row * self.board_size + swap_col]
        nodes[swap_row * self.board_size + swap_col] = '0'
        nodes[zero_row * self.board_size + zero_col] = temp_node
        new_state = '-'.join(nodes)
        return new_state


    def get_all_children(self):
        """
        create a list of all potential states of a certain node
        :return: list of states
        """
        all_children = list()
        zero_index = self.state.index('0')
        zero_row = int(zero_index / self.board_size)
        zero_col = zero_index % self.board_size
        # move up
        if zero_row != self.board_size - 1:
            new_state = self.change_state((zero_row, zero_col), (zero_row + 1, zero_col), list(self.state))
            all_children.append(State(self.board_size, new_state, self, 'U'))
        # move down
        if zero_row != 0:
            new_state = self.change_state((zero_row, zero_col), (zero_row - 1, zero_col), list(self.state))
            all_children.append(State(self.board_size, new_state, self, 'D'))
        # move left
        if zero_col != self.board_size - 1:
            new_state = self.change_state((zero_row, zero_col), (zero_row, zero_col + 1), list(self.state))
            all_children.append(State(self.board_size, new_state, self, 'L'))
        # move right
        if zero_col != 0:
            new_state = self.change_state((zero_row, zero_col), (zero_row, zero_col - 1), list(self.state))
            all_children.append(State(self.board_size, new_state, self, 'R'))
        return all_children
    
    
    def is_equal(self, state):
        """
        compare between 2 states by their state member
        :param state
        :return: true if both states are equal, else return false
        """
        return self.state == state.state


    def heuristic(self):
        """
        calculate manhattan's distance for this state to the goal state
        :return: value of the heuristic function for h value
        """
        h_value = 0
        # run through all nodes accept 0
        for index, item in enumerate(self.state):
            node_value = int(item)
            if node_value != 0:
                # current values
                cur_row = int(index / self.board_size)
                cur_col = index % self.board_size
                # goal values
                goal_row = int((node_value-1) / self.board_size)
                goal_col = (node_value-1) % self.board_size
                h_value += abs(goal_row - cur_row) + abs(goal_col - cur_col)
        return h_value


    def __lt__(self, other):
        """
        compare two nodes by their g value and h value
        :param other: the node to compare with
        :return: bigger node
        """
        # if value of f is equal return by time_stamp value
        if (self.g + self.h) == (other.g + other.h):
            return self.time_stamp < other.time_stamp
        return (self.g + self.h) < (other.g + other.h)