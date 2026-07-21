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
