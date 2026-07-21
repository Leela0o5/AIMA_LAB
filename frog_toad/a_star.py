'''
Logic:
1. Create the root node using the initial state.
2. Insert the root node into the frontier (Priority Queue).
3. Repeat until the frontier becomes empty:
       a. Remove the node with lowest f(n) = g(n) + h(n) from priority queue.
       b. Check if it is the goal state.
       c. Mark it as explored.
       d. Generate all successor states (slide and jump moves).
       e. Calculate f(n) for each successor.
       f. Add unexplored successors to the frontier.
4. If frontier becomes empty, no solution exists.

Data Structure Used:
    Priority Queue (min-heap)

Justification:
    - Uses heuristic to guide search towards goal.
    - Finds optimal solution efficiently.
    - Expands fewer nodes than uninformed search.
    - Combines actual cost g(n) and heuristic h(n).

Time Complexity:
    O(b^d)

Space Complexity:
    O(b^d)

where
    b = branching factor
    d = solution depth
'''
import heapq
start = "BBB_WWW"
goal = "WWW_BBB"

class Node:
    def __init__(self, state, parent=None, move=None, depth=0):
        self.state = state
        self.parent = parent
        self.move = move
        self.depth = depth

    def __lt__(self, other):
        return self.depth < other.depth
    
def find_empty(state):
    return state.index("_")

def test_goal(state):
    return state == goal

def get_successors(state):
    moves = []
    empty_index = find_empty(state)
    for i in range(len(state)):
        if state[i] != "_":
            # Slide move
            if abs(i - empty_index) == 1:
                new_state = list(state)
                new_state[empty_index], new_state[i] = new_state[i], new_state[empty_index]
                moves.append(((i, empty_index), ''.join(new_state)))
            # Jump move
            elif abs(i - empty_index) == 2:
                if state[(i + empty_index) // 2] != "_":
                    new_state = list(state)
                    new_state[empty_index], new_state[i] = new_state[i], new_state[empty_index]
                    moves.append(((i, empty_index), ''.join(new_state)))
    return moves

def print_solution(node):
    path = []
    while node:
        path.append(node)
        node = node.parent
    path.reverse()
    print("\nSolution Path:\n")
    for step in path:
        print(step.state)


def heuristic(state):
    goal = "WWW_BBB"
    h = 0

    for i in range(len(state)):
        if state[i] != "_" and state[i] != goal[i]:
            h += 1

    return h

def a_star(start):
    pq = []
    start_node = Node(start, depth=0)
    heapq.heappush(pq, (heuristic(start), start_node))
    visited = set()
    nodes_generated = 0

    while pq:
        f_n, current_node = heapq.heappop(pq)
        
        if test_goal(current_node.state):
            print(f"Nodes generated: {nodes_generated}")
            print_solution(current_node)
            return
        
        if current_node.state in visited:
            continue
        
        visited.add(current_node.state)
        
        for move, new_state in get_successors(current_node.state):
            if new_state not in visited:
                nodes_generated += 1
                g_n = current_node.depth + 1
                h_n = heuristic(new_state)
                f_n = g_n + h_n
                child_node = Node(new_state, current_node, move, g_n)
                heapq.heappush(pq, (f_n, child_node))
    
    print("No solution found.")

a_star(start)
