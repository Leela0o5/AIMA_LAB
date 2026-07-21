import heapq

start = (0, 1, 2, 3, 4, 5, 6, 7)


class Node:
    def __init__(self, state, parent=None, move=None, cost=0):
        self.state = state
        self.parent = parent
        self.move = move
        self.cost = cost  # g(n)

    def __lt__(self, other):
        return self.cost < other.cost


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
    return heuristic(state) == 0


def heuristic(state):
    attacks = 0

    for i in range(8):
        for j in range(i + 1, 8):

            if state[i] == state[j]:
                attacks += 1

            elif abs(state[i] - state[j]) == abs(i - j):
                attacks += 1

    return attacks


def get_successors(state):
    successors = []

    for col in range(8):

        current = state[col]

        for row in range(8):

            if row != current:
                new_state = list(state)
                new_state[col] = row
                successors.append(((col, row), tuple(new_state)))

    return successors


def print_solution(node):
    path = []

    while node:
        path.append(node)
        node = node.parent

    path.reverse()

    print("\nSolution Path:\n")

    for node in path:
        if node.move:
            print("Move:", node.move)
        print_board(node.state)


def a_star(start):

    pq = []

    start_node = Node(start)

    heapq.heappush(pq, (heuristic(start), start_node))

    visited = set()

    nodes_generated = 1
    nodes_visited = 0

    while pq:

        f, current = heapq.heappop(pq)

        if current.state in visited:
            continue

        visited.add(current.state)
        nodes_visited += 1

        if goal_test(current.state):

            print("Solution Found!\n")
            print_solution(current)
            print("Cost:", current.cost)
            print("Nodes Generated:", nodes_generated)
            print("Nodes Visited:", nodes_visited)
            return

        successors = get_successors(current.state)

        for move, state in successors:

            if state not in visited:

                child = Node(
                    state,
                    current,
                    move,
                    current.cost + 1
                )

                g = child.cost
                h = heuristic(state)
                f = g + h

                heapq.heappush(pq, (f, child))
                nodes_generated += 1

    print("No Solution Found")


a_star(start)
