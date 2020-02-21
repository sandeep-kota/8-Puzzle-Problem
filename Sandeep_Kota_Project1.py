import numpy as np
import sys

class Node:
    """
    This class describes a node.
    """
    def __init__(self,state,parent,current):
        self.current = current
        self.state = state
        self.blank_index = np.argwhere(self.state==0)
        self.parent = parent
        self.action_available = []
        # Up
        if self.blank_index > 2:
            self.action_available.append(self.MoveUp())
            
        # Right
        if self.blank_index%3 != 2:
            self.action_available.append(self.MoveRight())
            
        # Down
        if self.blank_index < 6:
            self.action_available.append(self.MoveDown())
            
        # Left
        if self.blank_index%3 != 0:
            self.action_available.append(self.MoveLeft())

    def MoveLeft(self):
        """
        Move the node left 
    
        :returns:    Updated State 
        :rtype:      Numpy Array 
        """
        if (self.blank_index%3!=0):
            new_state = self.state.copy()
            new_state[self.blank_index], new_state[self.blank_index-1] = new_state[self.blank_index-1],new_state[self.blank_index]
            return new_state
        else:
            print("Error: Action Left Not Possible")
            return False


    def MoveRight(self):
        """
        Move the node right 
    
        :returns:    Updated State 
        :rtype:      Numpy Array 
        """
        if (self.blank_index%3!=2):
            new_state = self.state.copy()
            new_state[self.blank_index], new_state[self.blank_index+1] = new_state[self.blank_index+1],new_state[self.blank_index]
            return new_state
        else:
            print("Error: Action Right Not Possible")
        return False

    def MoveUp(self):
        """
        Move the node up 
    
        :returns:    Updated State 
        :rtype:      Numpy Array 
        """
        if (self.blank_index>2):
            new_state = self.state.copy()
            new_state[self.blank_index], new_state[self.blank_index-3] = new_state[self.blank_index-3],new_state[self.blank_index]
            return new_state
        else:
            print("Error: Action Up Not Possible")
        return False

    def MoveDown(self):
        """
        Move the node Down 
    
        :returns:    Updated State 
        :rtype:      Numpy Array 
        """
        if (self.blank_index<6):
            new_state = self.state.copy()
            new_state[self.blank_index], new_state[self.blank_index+3] = new_state[self.blank_index+3],new_state[self.blank_index]
            return new_state
        else:
            print("Error: Action Down Not Possible")
        return False        

def showMatrix(state):
    """
    Shows the matrix.

    :param      state:  The state
    :type       state:  Array
    """
    print(np.reshape(state,(3,3)))

def BFS(start):
    """
    Breadth First Search

    :param      start:  The start
    :type       start:  Array

    :returns:   If the element is found or not
    :rtype:     Bool
    """
    goal = np.array([1,2,3,4,5,6,7,8,0])
    
    solve = isSolvable(start)

    # Check for solvability
    if solve == False:
        print("The puzzle is not solvable!")
        return False

    if solve == True:
        # Number of steps
        n_steps = 0
        s = np.append(start,n_steps)
        
        # Append Parent ID to start
        parent_id = 0
        s = np.append(s,parent_id)

        # Make an empty queue and append initial state
        queue = []
        queue.append(s)
      
        # Empty list for Visited Nodes
        visited = []
        while isSolvable(start):
            # Pop the Parent Node
            v = queue.pop(0)
            p,c,v_n = v[-1],v[-2],v[:-2]

            #Store the first element as visited
            visited.append(v)

            # Pop the first element
            current_node = Node(v_n,parent_id,n_steps)
            print("Current Node ID:", current_node.current)
            print ("Current State: ")
            showMatrix(current_node.state)

            # Check for Goal State
            if np.array_equal(current_node.state,goal):
                print("Start state is goal state")
                return True

            # If Goal available in Possible Actions
            print("Avilable States")
            for i in range(0,len(current_node.action_available)):
                
                # Check for goal state
                if np.array_equal(current_node.action_available[i],goal):
                    print("Goal Reached in ", n_steps, " steps")
                    showMatrix(current_node.action_available[i])
                    visited = np.array(visited)
                    
                    # Saving the paths
                    np.savetxt("Nodes.txt",visited[:,0:-2],fmt='%i')
                    
                    # Saving the parent and child node ID
                    np.savetxt("NodesInfo.txt",visited[:,-2:],fmt='%i')

                    # Back Tracking the path from Goal
                    optimal_path = []
                    optimal_path.append(goal)
                    optimal_path.append(current_node.state)
                    p = visited[:,-1][-1]
                    while p>0:

                        path = visited[p]
                        optimal_path.append(path[0:-2])
                        p = path[-1]
                        print("Path",path) 
                    optimal_path.append(start)   
                    np.savetxt("nodePath.txt",optimal_path,fmt='%i')   
                    return True

                # If Goal state not available in Possible Actions
                if np.array_equal(current_node.action_available[i],goal)==False:
                    saw = False 

                    # Check if action state is visited
                    for j in range(0,len(visited)):
                        if np.array_equal(current_node.action_available[i],visited[j][:-2]):
                            saw = True
                    
                    # If not append to the BFS
                    if saw==False:
                        # print("Parent ID",current_node.parent)
                        showMatrix(current_node.action_available[i])
                        n_steps+=1  
                        qa = np.append(current_node.action_available[i],n_steps)
                        qa = np.append(qa,parent_id)
                        # print("Appended ", qa)
                        queue.append(qa)
                        print("--")
                        

            print("___________")
            parent_id +=1

def isSolvable(start):
    """
    Determines whether the specified start is solvable.

    :param      start:  The start
    :type       start:  Array

    :returns:   True if the specified start is solvable, False otherwise.
    :rtype:     boolean
    """
 
    inverse = 0
    for i in range(0,len(start)):
        for j in range(i+1,len(start)):
            # print("Si,Sj:",start[i],start[j])
            if start[j]!=0 and start[j]!=0:
                if start[i]>start[j]:
                    inverse+=1
                    # print("inv")
    if inverse%2 == 0:
        return True
    if inverse%2 == 1:
        return False

def main():
    """
    Main Function
    """

    # Start state 
    start = np.array([0,2,3,1,5,6,4,7,8])
    """
    Equivalent to 
    |0 2 3|
    |1 5 6|
    |4 7 8|
    """
    print("Start Main:")
    showMatrix(start)
    print("Goal Main:")
    showMatrix(start)
    print(BFS(start))

if __name__ == "__main__":
   main() 