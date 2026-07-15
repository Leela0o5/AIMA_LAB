'''
Logic:
1. Create the root node using the initial state.
2. Insert the root node into the frontier (Stack).
3. Repeat until the frontier becomes empty:
       a. Remove the top node from the stack.
       b. Check if it is the goal state.
          - If yes, print the solution and stop.
       c. Mark the current state as explored.
       d. Generate all valid successor states.
       e. Add unexplored successor nodes to the stack.
4. If the stack becomes empty, no solution exists.

Data Structure Used:
    Stack (LIFO)

Justification:
    - Explores one branch completely before backtracking.
    - Uses less memory than BFS.
    - Does not guarantee the shortest path.
    - Complete only for finite search spaces (like the 8-puzzle).

Time Complexity:
    O(b^m)

Space Complexity:
    O(bm)

where
    b = Branching Factor
    m = Maximum depth of the search tree

'''
start = ((1, 2, 3), (4, 0, 5), (7, 8, 6))
goal = ((1, 2, 3), (4, 5, 6), (7, 8, 0))


class Node:
      def __init__(self,state,parent=None,move=None,cost=0):
            self.state=state
            self.parent=parent
            self.move=move
            self.cost=cost

def print_state(state):
    for row in state:
            print(row)
    print()

def goal_test(state,goal):
      return state==goal

def print_solution(node):
        path=[]
        current = node
        while current is not None:
             path.append(current)
             current = current.parent
        path.reverse()
        for node in path:
            print_state(node.state)

def find_blank(state):
      for i in range(3):
            for j in range(3):
                  if state[i][j]==0:
                        return (i,j)
      return None

def get_possible_moves(state):
        moves=[]
        row,col=find_blank(state)
        if row>0:
                moves.append('up')
        if row<2:
                moves.append('down')
        if col>0:
                moves.append('left')
        if col<2:
                moves.append('right')
        return moves

def move(state,direction):
        row,col=find_blank(state)
        new_state=[list(r) for r in state]
        if direction=='up':
                new_row=row-1
                new_col=col
        elif direction=='down':
                new_row=row+1
                new_col=col
        elif direction=='left':
                new_row=row
                new_col=col-1
        elif direction=='right':
                new_row=row
                new_col=col+1
        else:
                return None
        new_state[row][col],new_state[new_row][new_col]=new_state[new_row][new_col],new_state[row][col]
        return tuple(tuple(r) for r in new_state)

def expand(node):
        children=[]
        for move_direction in get_possible_moves(node.state):
                new_state=move(node.state,move_direction)
                if new_state is not None:
                        child_node=Node(new_state,node,move_direction,node.cost+1)
                        children.append(child_node)
        return children


def dfs(start,goal):
        node_generated = 1
        stack=[Node(start)]
        visited=set()
        while stack:
                node=stack.pop()
                if goal_test(node.state,goal):
                    print("Solution found!")
                    print("Number of nodes generated:", node_generated)
                    print("Cost of the solution:", node.cost)
                    print_solution(node)
                    return node
                visited.add(node.state)
                for child in expand(node):
                        if child.state not in visited and \
   all(child.state != n.state for n in stack):
                            stack.append(child)
                            node_generated += 1
                            
        print("No solution found.")


dfs(start, goal)

