import sys
from State import State
from BFS import BFS
from IDS import IDS
from Astar import Astar


def read_from_file():
    """
    extract data from input file
    :return: parameters from file (algo, borad size, init state)
    """
    # parse data from file
    fp = open('input.txt')
    lines = fp.readlines()
    algo = int(lines[0].strip())
    bz = int(lines[1].strip())
    ins = lines[2].strip()
    fp.close()
    return [algo, bz, ins]


def create_goal_state(size):
    """
    create goal state by size of board
    :param size: Size of the board
    :return: String representation of goal state
    """
    goal_state = list()
    for i in range(1, size * size):
        goal_state.append(str(i))
    goal_state.append('0')
    res = '-'.join(goal_state)
    return res


if __name__ == "__main__":

    # extract data fro, input file
    algorithm, board_size, init_state_t = read_from_file()
    # set problem's parameters
    init_state = State(board_size, init_state_t)
    goal_state = State(board_size, create_goal_state(board_size))

    dm = ''
    sp = ' '
    # run algorithm and write result in output file
    output_f = open('output.txt', 'w')

    # run problem by IDS algorithm
    if algorithm == 1:
        path, developed_nodes, depth = IDS().run(init_state, goal_state, 100)
        output_data = dm.join(path) + sp + str(developed_nodes) + sp + str(depth)
        output_f.write(output_data)

    # run problem by BFS algorithm
    elif algorithm == 2:
        path, developed_nodes = BFS().run(init_state, goal_state)
        output_data = dm.join(path) + sp + str(developed_nodes) + sp + str(0)
        output_f.write(output_data)

        # run problem by Astar algorithm
    elif algorithm == 3:
         path, developed_nodes, cost = Astar().run(init_state, goal_state)
         output_data = dm.join(path) + sp + str(developed_nodes) + sp + str(cost)
         output_f.write(output_data)