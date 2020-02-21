# ENPM661 - 8 Puzzle Problem

This is the readme file explaining the woriking of the code to solve 8-Puzzle Problem.

## Dependencies
- Python
- Numpy

## Code Details
- The scrip `Sandeep_Kota_Project1.py` contains a class `Node` which contains the details about its current state, current node ID, parent node ID, index location of the blank tile, and the list of actions available.

- The `Node` class has the member functions `MoveLeft`, `MoveRight`, `MoveUp`, and `MoveDown` to get the state the update state of the node if the move is possible.

- The script also contains the `showMatrix()` method which prints the array into a matrix form. **Importany Note: The matrix is printed row-wise and not column wise.**

- The `isSolvable()` method checks the solvability of the start state.

- The `BFS()` Method checks the solvability of the start state and records the path in the text files.

-  The start state is defined in the main function and the BFS method is called in the main function.

- The file `Nodes.txt` contains the list of all the states that have been checked.**Importany Note: The matrix is printed row-wise and not column wise.**
- The file `NodesInfo.txt` contains the list of all the node ID's and their corresponding parent node ID's.**Importany Note: The matrix is printed row-wise and not column wise.**
- The file `nodePath.txt` contains the list of all the states of the optimal path.**Importany Note: The matrix is printed row-wise and not column wise.**


## Instructions to run the Code
- Give the start state in the variable `Start` in the main function.

- Run the script in a temrinal with the following command.
```
python3 Sandeep_Kota_Project1.py
```
