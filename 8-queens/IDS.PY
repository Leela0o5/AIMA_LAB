'''
Logic:
1. Create the root node using the initial board.
2. Perform iterative deepening with increasing depth limits.
3. For each depth limit, run depth-first search:
       a. Remove the top node from the stack.
       b. Check if it is the goal state.
       c. If depth limit not reached, mark it as explored.
       d. Generate all successor states.
       e. Add unexplored successors to the frontier.
4. If solution not found at current depth, increase limit and repeat.
5. Continue until a solution is found or all depths exhausted.

Data Structure Used:
    Stack (LIFO) with depth limit

Justification:
    - Combines benefits of DFS (memory efficiency) and BFS (optimality).
    - Guarantees finding the shallowest goal.
    - Uses less memory than BFS.
    - Finds solution with minimum number of moves.

Time Complexity:
    O(b^d)

Space Complexity:
    O(bd)

where
    b = 56 (maximum successors)
    d = solution depth
'''
start = (0, 1, 2, 3, 4, 5, 6, 7)


class Node:
    def __init__(self, state, parent=None, move=None, cost=0, depth=0):
        self.state = state
        self.parent = parent
        self.move = move
        self.cost = cost
        self.depth = depth


def print_board(state):
    print("State:", state)
    for row in range(8):
        for col in range(8):
            if state[col] == row:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()
    print()


def goal_test(state):
    n = 8
    for i in range(n):
        for j in range(i + 1, n):
            # Same row or same diagonal
            if state[i] == state[j] or abs(state[i] - state[j]) == abs(i - j):
                return False
    return True


def get_successors(state):
    successors = []
    n = 8

    for col in range(n):
        current_row = state[col]

        for new_row in range(n):
            if new_row != current_row:
                new_state = list(state)
                new_state[col] = new_row
                successors.append(((col, new_row), tuple(new_state)))

    return successors


def print_solution(node):
    path = []

    while node:
        path.append(node)
        node = node.parent

    path.reverse()

    print("\nSolution Path:\n")

    for node in path:
        if node.move is not None:
            print("Move:", node.move)
        print_board(node.state)


def depth_limited_search(start, limit):
    stack = [Node(start, depth=0)]
    visited = set()

    nodes_generated = 0
    nodes_visited = 1

    while stack:

        current_node = stack.pop()

        if goal_test(current_node.state):
            return current_node, nodes_generated, nodes_visited

        if current_node.depth < limit:

            visited.add(current_node.state)

            successors = get_successors(current_node.state)

            # Reverse so DFS explores first successor first
            for move, new_state in reversed(successors):

                if (
                    new_state not in visited
                    and all(new_state != node.state for node in stack)
                ):

                    child = Node(
                        state=new_state,
                        parent=current_node,
                        move=move,
                        cost=current_node.cost + 1,
                        depth=current_node.depth + 1,
                    )

                    stack.append(child)
                    nodes_generated += 1

            nodes_visited += 1

    return None, nodes_generated, nodes_visited


def iterative_deepening_search(start):
    depth = 0

    total_generated = 0
    total_visited = 0

    while True:

        print(f"\nSearching with depth limit = {depth}")

        result, generated, visited = depth_limited_search(start, depth)

        total_generated += generated
        total_visited += visited

        if result:
            print("\nSolution Found!\n")

            print_solution(result)

            print("Depth:", result.depth)
            print("Cost:", result.cost)
            print("Total Nodes Generated:", total_generated)
            print("Total Nodes Visited:", total_visited)

            return result

        depth += 1


# Driver Code
iterative_deepening_search(start)