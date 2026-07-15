'''
----------------------------------------------------------
Algorithm : Iterative Deepening Search (IDS)

Logic:
1. Start with depth limit = 0.
2. Perform Depth-Limited Search (DLS).
3. If the goal is found, print the solution and stop.
4. Otherwise, increase the depth limit by 1.
5. Repeat until the goal is found or the maximum depth is reached.

Data Structure Used:
    Stack (LIFO)

Justification:
    - Combines the advantages of BFS and DFS.
    - Uses less memory than BFS.
    - Finds the shortest solution like BFS when step costs are equal.
    - Complete and Optimal for the 8-puzzle.

Time Complexity:
    O(b^d)

Space Complexity:
    O(bd)

where
    b = Branching Factor
    d = Depth of the shallowest goal
----------------------------------------------------------
'''

start = (
    (1, 2, 3),
    (4, 0, 5),
    (7, 8, 6)
)

goal = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 0)
)



class Node:

    def __init__(self, state, parent=None, move=None, cost=0, depth=0):
        self.state = state
        self.parent = parent
        self.move = move
        self.cost = cost
        self.depth = depth


def print_state(state):

    for row in state:
        print(row)

    print()




def goal_test(state, goal):
    return state == goal




def print_solution(node):
    path = []
    while node:
        path.append(node.state)
        node = node.parent
    for state in reversed(path):
        print_state(state)



def find_blank(state):

    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j




def get_possible_moves(state):

    moves = []

    row, col = find_blank(state)

    if row > 0:
        moves.append("up")

    if row < 2:
        moves.append("down")

    if col > 0:
        moves.append("left")

    if col < 2:
        moves.append("right")

    return moves



def move(state, direction):

    row, col = find_blank(state)

    board = [list(r) for r in state]

    if direction == "up":
        new_row, new_col = row - 1, col

    elif direction == "down":
        new_row, new_col = row + 1, col

    elif direction == "left":
        new_row, new_col = row, col - 1

    elif direction == "right":
        new_row, new_col = row, col + 1

    board[row][col], board[new_row][new_col] = \
        board[new_row][new_col], board[row][col]

    return tuple(tuple(r) for r in board)


def expand(node):

    children = []

    for direction in get_possible_moves(node.state):

        child_state = move(node.state, direction)

        child = Node(
            child_state,
            parent=node,
            move=direction,
            cost=node.cost + 1,
            depth=node.depth + 1
        )

        children.append(child)

    return children



def depth_limited_search(start, goal, limit):

    stack = [Node(start)]

    visited = set()

    nodes_generated = 1
    nodes_visited = 0

    while stack:

        current = stack.pop()

        nodes_visited += 1

        if goal_test(current.state, goal):
            return current, nodes_generated, nodes_visited

        visited.add(current.state)

        if current.depth < limit:

            children = expand(current)

            for child in reversed(children):

                if child.state not in visited and \
                   all(child.state != n.state for n in stack):

                    stack.append(child)

                    nodes_generated += 1

    return None, nodes_generated, nodes_visited



def ids(start, goal, max_depth):

    total_generated = 0
    total_visited = 0

    for limit in range(max_depth + 1):

        print("Searching with Depth Limit =", limit)

        result, generated, visited = depth_limited_search(
            start,
            goal,
            limit
        )

        total_generated += generated
        total_visited += visited

        if result:

            print("\nGoal Found!\n")

            print_solution(result)

            print("Depth Limit :", limit)
            print("Nodes Generated :", total_generated)
            print("Nodes Visited :", total_visited)

            return

    print("Goal Not Found")



ids(start, goal, 20)