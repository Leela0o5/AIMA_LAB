start = (0,1,2,3,4,5,6,7)

class Node:
    def __init__(self, state, parent=None, move=None, cost=0):
        self.state = state
        self.parent = parent
        self.move = move
        self.cost = cost

def print_board(state):
    print("State:", state)
    for row in range(8):
        for col in range(8):
            if state[col] == row:
                print('Q', end=' ')
            else:
                print('.', end=' ')
        
        print()
    print()


def goal_test(state):
    n = 8
    for i in range(n):
        for j in range(i + 1, n):
            # same row or same diagonal
            if state[i] == state[j] or abs(state[i] - state[j]) == abs(i - j):
                return False
    return True

def get_successors(state):
    n =  8 
    successors = []
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
    for node in path:
        print_board(node.state)
    print("Total Moves:", len(path) - 1)

def dfs(start):
    stack = [Node(start)]
    visited = set()
    while stack:
        current_node = stack.pop()
        if goal_test(current_node.state):
            print_solution(current_node)
            return current_node
        visited.add(current_node.state)
        for move, new_state in get_successors(current_node.state):
            if new_state not in visited and not any(node.state == new_state for node in stack):
               child = Node(
                     new_state,
                     parent=current_node,
                     move=move,
                     cost=current_node.cost + 1
                    )
               stack.append(child)
    print("No solution found.")

dfs(start)