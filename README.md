8Puzzle-Solver-AStar

__Project Overview__ -

This project implements a solution to the 8-puzzle problem using the A* (A-star) search algorithm. The 8-puzzle consists of a 3x3 grid where each tile can be moved into an adjacent empty space. The objective is to arrange the tiles in a specified goal configuration, starting from an initial state. This project utilizes the A* algorithm, which is an informed search algorithm that combines the cost to reach a node (g) and a heuristic function (h) to determine the most optimal path to the goal state.

__Key Features__ -

- A Algorithm Implementation*: Solves the 8-puzzle problem by finding the optimal path using a heuristic (Manhattan Distance).

- State Validation: Checks if the state is valid, ensuring the puzzle follows the rules of the 8-puzzle.

- Solvability Check: Determines if a given puzzle configuration is solvable using the inversion count method.

- Path Reconstruction: Displays the solution path in reverse order from the goal state to the initial state, including each state’s heuristic and number of moves.

- Priority Queue: Uses a priority queue (min-heap) to efficiently explore states with the lowest cost (f = g + h).


__Technologies Used__ -

- Python: The core language used for implementing the algorithm and solving the 8-puzzle problem.

- Heapq: A Python library used to implement the priority queue in the A* algorithm.

- List, Tuple, Dictionary: Data structures used to represent the puzzle state, track visited nodes, and manage the solution path.


__How it Works__ -

1. Initial Setup:  The puzzle state is represented as a list of integers where each number corresponds to a tile in the puzzle. A value of 0 denotes the empty space.
  The goal state is dynamically determined based on the number of non-zero tiles in the input state, ensuring the state follows the rules of the 8-puzzle.

2. A Search*: The A* algorithm explores possible puzzle states by evaluating both the cost to reach the current state (g) and the heuristic value (h), which is the sum of Manhattan distances of tiles from their goal positions. A priority queue (min-heap) is used to select the state with the lowest f-value, which is the sum of g and h.

3. State Expansion: The algorithm generates all valid successor states by swapping the 0 tile with its neighboring tiles (up, down, left, right).
It then checks if the new state has been visited and whether it has a lower cost than previously recorded. If so, it updates the state in the priority queue.

4. Goal Check and Path Reconstruction: When the goal state is reached, the solution path is reconstructed by backtracking from the goal state using a dictionary that stores the cost and parent state for each visited state.
The solution path is then displayed, showing the sequence of states, along with the corresponding heuristic values and move count.

5. Solvability: The puzzle is first checked for solvability using the inversion count method. If the puzzle is not solvable, the algorithm prints False. If solvable, it proceeds to solve the puzzle and prints the solution path.
