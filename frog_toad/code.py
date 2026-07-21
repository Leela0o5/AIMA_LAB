'''
Logic:
This file implements multiple search algorithms for solving the Frogs and Toads puzzle:

1. BFS (Breadth-First Search):
   - Uses Queue (FIFO) to explore states level by level
   - Guarantees shortest solution
   
2. DFS (Depth-First Search):
   - Uses Stack (LIFO) to explore one branch completely before backtracking
   - Uses less memory than BFS
   
3. IDS (Iterative Deepening Search):
   - Combines benefits of DFS and BFS
   - Runs depth-limited searches with increasing depth limits
   - Guarantees shortest solution with memory efficiency of DFS

Problem:
   - Move all B pieces (left) past all W pieces (right)
   - B piece can slide/jump right, W piece can slide/jump left
   - Slide: move to adjacent empty space
   - Jump: jump over exactly one piece into empty space

Data Structures Used:
   - BFS: Queue (FIFO)
   - DFS: Stack (LIFO)
   - IDS: Stack with depth limit

Justification:
   - BFS finds optimal solution but uses more memory
   - DFS uses less memory but doesn't guarantee optimality
   - IDS combines benefits of both approaches

Time Complexity:
   - BFS: O(b^d)
   - DFS: O(b^m)
   - IDS: O(b^d)

Space Complexity:
   - BFS: O(b^d)
   - DFS: O(bm)
   - IDS: O(bd)

where
    b = branching factor (maximum possible moves)
    d = solution depth
    m = maximum depth of search tree
'''
from collections import deque
import heapq
start = "BBB_WWW"
goal = "WWW_BBB"

'''
A B piece can move  to the right or left.
A W piece can move  to the left or right.A piece may:

Slide into the adjacent empty space.
Jump over exactly one piece (of either color) into the empty space.
'''
class Node:
    def __init__(self, state, parent=None, move=None, cost=0):
        self.state = state
        self.parent = parent
        self.move = move
        self.cost = cost

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

def bfs(start):
    queue = deque([Node(start)])
    visited = set()
    visited.add(start)
    nodes_generated = 0

    while queue:
        current_node = queue.popleft()
        if test_goal(current_node.state):
            print(f"Nodes generated: {nodes_generated}")
            print_solution(current_node)
            return
        for move, new_state in get_successors(current_node.state):
            if new_state not in visited:
                nodes_generated += 1
                visited.add(new_state)
                queue.append(Node(new_state, current_node, move))
    print("No solution found.")
   

def dfs(start):
    stack = [Node(start)]
    visited = set()
    visited.add(start)
    nodes_generated = 0

    while stack:
        current_node = stack.pop()
        if test_goal(current_node.state):
            print(f"Nodes generated: {nodes_generated}")
            print_solution(current_node)
            return
        for move, new_state in get_successors(current_node.state):
            if new_state not in visited:
                visited.add(new_state)
                nodes_generated += 1
                stack.append(Node(new_state, current_node, move))
    print("No solution found.")


def depth_limited_search(start, limit):
    stack = [Node(start, depth=0)]
    visited = set()
    nodes_generated = 0
    nodes_visited = 1

    while stack:
        current_node = stack.pop()
        if test_goal(current_node.state):
            print(f"Nodes generated: {nodes_generated}")
            print_solution(current_node)
            return
        if current_node.depth < limit:
            visited.add(current_node.state)
            for move, new_state in get_successors(current_node.state):
                if new_state not in visited:
                    nodes_generated += 1
                    stack.append(Node(new_state, current_node, move, current_node.depth + 1))
    print("No solution found.")

def iterative_deepening_search(start):
    depth = 0
    while True:
        print(f"\nSearching with depth limit = {depth}")
        depth_limited_search(start, depth)
        depth += 1


bfs(start)
dfs(start)
iterative_deepening_search(start)
