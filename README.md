# A-With-Pygame

**A-With-Pygame** is a Python project focused on visualizing the **A\*** (A-Star) search algorithm using the **Pygame** library.  
The core objective is to create an interactive grid environment where the A\* algorithm can find the shortest path between a starting point and an end point.

---

## Key Implementation Details

### A\* Pathfinding Core
The project will implement the A\* algorithm, which prioritizes nodes based on the function:

\[
f(n) = g(n) + h(n)
\]

where:
- \( g(n) \) is the cost from the start node to the current node \( n \),
- \( h(n) \) is the estimated cost from the current node \( n \) to the goal node.

---

### Heuristic Function (\( h(n) \))
The implementation will specifically use the **Manhattan Distance heuristic**.  
This function calculates the sum of the absolute differences between the coordinates of the current spot and the goal spot.  

This heuristic is standard for movement restricted to four directions (up, down, left, right), typically found in **grid-based environments and mazes**.

---

### Future Maze Generation
The choice of the Manhattan Distance heuristic aligns with a future goal: **integrating a maze generation algorithm** (e.g., **Kruskal’s** or **Prim’s** algorithm) into the project.  
This addition will allow the A\* algorithm to be tested dynamically on **newly created, complex maze structures**.

---

### Pygame Visualization
**Pygame** will be used to:
- Render the grid.
- Visually distinguish different states of the grid cells (e.g., *unvisited*, *open set*, *closed set*, *obstacle*, *path*, *start*, and *end*).
- Provide an **interactive display** for observing the pathfinding process in real time.
