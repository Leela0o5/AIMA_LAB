from collections import deque
'''

Logic:
1. Create the root node using the initial state.
2. Insert the root node into the frontier (Queue).
3. Repeat until the frontier becomes empty:
       a. Remove the front node from the queue.
       b. Check if it is the goal state.
          - If yes, print the solution and stop.
       c. Mark the current state as explored.
       d. Generate all valid successor states.
       e. Add unexplored successor nodes to the queue.
 4. If the queue becomes empty, no solution exists.

Data Structure Used:
    Queue (FIFO)

Justification:
    - Explores the search tree level by level.
    - Guarantees the shortest path when each move has equal cost.
    - Complete and Optimal for the 8-puzzle.

Time Complexity:
    O(b^d)

Space Complexity:
    O(b^d)

where
    b = Branching Factor
    d = Depth of the shallowest goal

'''
start = (
    (1, 2, 3),
    (4, 0, 6),
    (7, 5, 8)
)

goal = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 0)
)

class Node:
    def __init__(self, state, parent=None,move=None,cost=0):
        self.state = state
        self.parent = parent
        self.move = move
        self.cost = cost


def print_state(state):
    for row in state:
        print(row)
    print()


def goal_test(state,goal):
    return state == goal

def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return (i, j)
    return None

def get_possible_moves(state):
    moves=[]
    row,col = find_blank(state)
    if row > 0:
        moves.append('up')
    if row < 2:
        moves.append('down')
    if col > 0:
        moves.append('left')
    if col < 2:
        moves.append('right')
    return moves

def move(state, direction):
    row, col = find_blank(state)
    new_state = [list(r) for r in state]  
    if direction == 'up':
        new_row = row - 1
        new_col = col
    elif direction == 'down':
        new_row = row + 1
        new_col = col
    elif direction == 'left':
        new_row = row
        new_col = col - 1
    elif direction == 'right':
        new_row = row
        new_col = col + 1
    new_state[row][col], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[row][col]
    return tuple(tuple(r) for r in new_state)

def generate_successors(state):
    successors = []
    possible_moves = get_possible_moves(state)
    for direction in possible_moves:
        successors.append((direction, move(state, direction)))
    return successors

def print_solution(node):
    path = []
    while node:
        path.append(node.state)
        node = node.parent
    for state in reversed(path):
        print_state(state)
    
def bfs(start, goal):
    root = Node(start)
    frontier = deque([root])
    explored = set()
    nodes_visited = 0
    nodes_generated = 0
    while frontier:
        current_node = frontier.popleft()
        nodes_visited += 1
        if goal_test(current_node.state, goal):
            print("Goal reached!")
            print_solution(current_node)
            print(f"Nodes Visited: {nodes_visited}")
            print(f"Nodes Generated: {nodes_generated}")
            return
        explored.add(current_node.state)
        successors = generate_successors(current_node.state)
        for direction, child in successors:
            if child not in explored and all(child != node.state for node in frontier):
                child_node = Node(child, current_node, direction, current_node.cost + 1)
                frontier.append(child_node)
                nodes_generated += 1
    print("No solution found.")

bfs(start, goal)











    