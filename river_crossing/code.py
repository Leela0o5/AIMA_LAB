'''
Logic:
1. Create the root node using the initial state.
2. Insert the root node into the frontier (Queue).
3. Repeat until the queue becomes empty:
      a. Remove the front node.
      b. Check if it is the goal state.
      c. Mark it as explored.
      d. Generate all legal successor states.
      e. Insert unexplored successor states into the queue.
4. If the queue becomes empty, no solution exists.

Data Structure Used:
    Queue (FIFO)

Time Complexity:
    O(b^d)

Space Complexity:
    O(b^d)
'''

from collections import deque


start = (False, False, False, False)
goal = (True, True, True, True)
# farmer, wolf, goat, cabbage

conflict = {
    (1,2),
    (2,3)
}

class Node:
    def __init__(self, state, parent=None, move=None, cost=0):
        self.state = state
        self.parent = parent
        self.move = move
        self.cost = cost

def test_goal(state, goal):
    return state == goal

def print_solution(node):
    path = []
    while node:
        path.append(node)
        node = node.parent
    path.reverse()
    for step in path:
        print(step.state)
        if step.move:
            print("Move:", step.move)
        print()

def is_valid(state):
    for a, b in conflict:
        if state[a] == state[b] and state[0] != state[a]:
            return False
    return True

def legal_moves(state):
    moves = []
    farmer_side = state[0]
    new_state = list(state)
    # farmer moves alone
    new_state[0] = not farmer_side
    if is_valid(tuple(new_state)):
        moves.append(("Farmer Alone", tuple(new_state)))
    names = ["farmer", "wolf", "goat", "cabbage"]
    for i in range(1, 4):
        # farmer moves with item i
        if state[i] == farmer_side:
            new_state = list(state)
            new_state[0] = not farmer_side
            new_state[i] = not farmer_side
            if is_valid(tuple(new_state)):
                moves.append((f"Farmer + {names[i]}", tuple(new_state)))
    return moves

def bfs(start, goal):
    root = Node(start)
    frontier = deque([root])
    explored = set()
    nodes_generated = 1
    nodes_visited = 0

    while frontier:
        current = frontier.popleft()
        nodes_visited += 1
        if test_goal(current.state, goal):
            print("Goal Found!\n")

            print_solution(current)
            print("Cost :", current.cost)
            print("Nodes Generated :", nodes_generated)
            print("Nodes Visited :", nodes_visited)
            return current

        explored.add(current.state)

        successors = legal_moves(current.state)

        for move,state in successors:

            if state not in explored and \
               all(state != node.state for node in frontier):

                child = Node(
                    state=state,
                    parent=current,
                    move=move,
                    cost=current.cost + 1
                )

                frontier.append(child)

                nodes_generated += 1

    print("No Solution Found.")


bfs(start, goal)

        
            

    