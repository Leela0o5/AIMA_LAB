from collections import deque
'''
  The problem is usually stated as follows.
    Three missionaries and three cannibals are on one side of a river, 
    along with a boat that can hold one or two people. Find a way to get 
    everyone to the other side without ever leaving a group of missionaries 
    in one place outnumbered by the cannibals in that place.

'''
boat_capacity = 2
m = 3
c = 3
# true is right side, false is left side
start = (m, c, False)  # (missionaries, cannibals, boat_side) 
goal = (0, 0, True)  # (missionaries, cannibals, boat_side)


class Node:
    def __init__(self,state,parent=None,move=None,cost=0):
        self.state=state
        self.parent=parent
        self.move=move
        self.cost=cost

def goal_test(state,goal):
    return state==goal

def print_solution(node):
    path=[]
    while node:
        path.append(node.state)
        node=node.parent
    for state in reversed(path):
        print(state)
    
def is_valid(state):
    m, c, _ = state
    if m < 0 or c < 0 or m > 3 or c > 3:
        return False
    if m > 0 and m < c:
        return False
    if m < 3 and (3 - m) < (3 - c):
        return False
    return True

def get_successors(state):

    left_m, left_c, boat = state

    right_m = 3 - left_m
    right_c = 3 - left_c

    successors = []

    for move_m in range(boat_capacity + 1):
        for move_c in range(boat_capacity + 1):

            if move_m + move_c == 0 or move_m + move_c > boat_capacity:
                continue

            # Boat is on the LEFT bank
            if boat == False:

                # Cannot move more people than available on the left
                if move_m > left_m or move_c > left_c:
                    continue

                new_state = (
                    left_m - move_m,
                    left_c - move_c,
                    True
                )

            # Boat is on the RIGHT bank
            else:

                # Cannot move more people than available on the right
                if move_m > right_m or move_c > right_c:
                    continue

                new_state = (
                    left_m + move_m,
                    left_c + move_c,
                    False
                )

            if is_valid(new_state):
                successors.append(new_state)

    return successors


def bfs(start, goal):
    frontier = deque([Node(start)])
    explored = set()
    node_genrated = 1
    node_visited = 0
    while frontier:
        node = frontier.popleft()
        node_visited += 1

        if goal_test(node.state, goal):
            print_solution(node)
            print(f"Number of nodes generated: {node_genrated}")
            print(f"Number of nodes visited: {node_visited}")
            return
        explored.add(node.state)
        for child_state in get_successors(node.state):
            if child_state not in explored and all(child.state != child_state for child in frontier):
                child_node = Node(child_state, node)
                frontier.append(child_node)
                node_genrated += 1
    print("No solution found.")

bfs(start, goal)
            
            
        