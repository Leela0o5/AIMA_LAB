from collections import deque
'''
Logic:
1. Create the root node using the initial board.
2. Insert the root node into the frontier (Queue).
3. Repeat until the frontier becomes empty:
       a. Remove the front node.
       b. Check if it is the goal state.
       c. Mark it as explored.
       d. Generate all successor states.
       e. Add unexplored successors to the frontier.
4. If queue becomes empty, no solution exists.

Data Structure Used:
    Queue (FIFO)

Justification:
    - Explores the search space level by level.
    - Finds the solution with minimum number of queen moves.

Time Complexity:
    O(b^d)

Space Complexity:
    O(b^d)

where
    b = 56 (maximum successors)
    d = solution depth
'''
start = (0,1,2,3,4,5,6,7)

class Node:
    def __init__(self,state,parent=None,move=None,cost=0):
        self.state=state
        self.parent=parent
        self.move=move
        self.cost=cost

def print_board(state):
    for row in range(8):
        for col in range(8):
            if state[col] == row:
                print('Q', end=' ')
            else:
                print('.', end=' ')
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
    path=[]
    while node:
        path.append(node)
        node=node.parent
    path.reverse()
    for node in path:
        print_board(node.state)
    print("Total Moves:", len(path)-1)

def bfs(start):
    root = Node(start)
    frontier = deque([root])
    explored = set()
    nodes_visited = 0
    nodes_generated = 1
    while frontier:
        current_node = frontier.popleft()
        nodes_visited += 1
        print("Visited:", nodes_visited)
        if goal_test(current_node.state):
            print_solution(current_node)
            print(f"Number of nodes generated: {nodes_generated}")
            print(f"Number of nodes visited: {nodes_visited}")
            return
        explored.add(current_node.state)
        successors = get_successors(current_node.state)
        for move, new_state in successors:
            if new_state not in explored and all(child.state != new_state for child in frontier):
                child_node = Node(new_state, current_node, move, current_node.cost + 1)
                frontier.append(child_node)
                nodes_generated += 1
    print("No solution found.")

bfs(start)