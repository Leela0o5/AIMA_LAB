import heapq
'''
Algorithm : A* Search

Logic:
1. Create the root node using the initial state.
2. Compute the heuristic (Manhattan Distance).
3. Insert the root node into the priority queue.
4. Repeat until the priority queue becomes empty:
       a. Remove the node with the lowest f(n).
       b. Check if it is the goal state.
          - If yes, print the solution and stop.
       c. Mark the current state as explored.
       d. Generate all valid successor states.
       e. Compute f(n) = g(n) + h(n).
       f. Insert unexplored successor nodes into the priority queue.
5. If the priority queue becomes empty, no solution exists.

Data Structure Used:
    Priority Queue (Min Heap)

Justification:
    - Expands the most promising node first.
    - Uses the evaluation function f(n)=g(n)+h(n).
    - Complete and Optimal when using an admissible heuristic
      such as Manhattan Distance.

Time Complexity:
    O(b^d) (Worst Case)

Space Complexity:
    O(b^d)

where
    b = Branching Factor
    d = Depth of the optimal solution

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
    def __init__(self, state, parent=None, move=None, cost=0, heuristic=0):
            self.state = state
            self.parent = parent
            self.move = move
            self.cost = cost  # g(n)
            self.heuristic = heuristic  # h(n)
    
    def f(self):
        return self.cost + self.heuristic # f(n) = g(n) + h(n)
    
    def __lt__(self, other):
        return self.f() < other.f()  # For priority queue comparison when f values are equal
    

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


def print_solution(node):
    path = []
    while node:
        path.append(node.state)
        node = node.parent
    for state in reversed(path):
        print_state(state)

def manhattan_distance(state, goal):
    distance = 0
    for i in range(3):
        for j in range(3):
            value = state[i][j]
            if value != 0:
                for x in range(3):
                       for y in range(3):
                            if goal[x][y] == value:
                                distance += abs(x - i) + abs(y - j)
    return distance

def expand(node):
    children = []
    possible_moves = get_possible_moves(node.state)
    for direction in possible_moves:
        new_state = move(node.state, direction)
        h = manhattan_distance(new_state, goal)
        child_node = Node(state=new_state, parent=node, move=direction, cost=node.cost + 1, heuristic=h)
        children.append(child_node)
    return children

def a_star(start, goal):
    root = Node(state=start, cost=0, heuristic=manhattan_distance(start, goal))
    frontier = []
    heapq.heappush(frontier, root)
    explored = set()
    node_generated = 1
    node_visited = 0
    while frontier:
        current_node = heapq.heappop(frontier)
        node_visited += 1
        if goal_test(current_node.state, goal):
            print("Goal Found!")
            print_solution(current_node)
            print(f"Nodes Generated: {node_generated}")
            print(f"Nodes Visited: {node_visited}")
            return
        explored.add(current_node.state)
        children = expand(current_node)
        for child in children:
            if child.state not in explored and all(child.state != node.state for node in frontier):
                heapq.heappush(frontier, child)
                node_generated += 1
    print("no solution found")

a_star(start, goal)