# Ashesi Campus Navigation System

### Introduction
Ashesi University is a private, non-profit university located in Berekuso, Ghana. The university is situated on about one hundred acres of land 
in the Eastern region. The various university departments, student dorms, cafeterias, and recreational facilities cover the scope of this area. 
Due to the large size of the institution navigation can be a bit problematic, especially for newcomers and visitors. Students frequently 
get lost on the way to class or meetings, and occasionally find themselves being late. 
The goal of this project is to provide effective campus navigation by using the knowledge acquired in artificial intelligence over the course 
of the semester to determine the shortest path between two points on the university campus and display that route to the user.

### Approach
A summary of the tasks derived:
- Formulation and representation of the problem
- Implementation the A* search algorithm with an appropriate heuristic function, 
- Display of the path found on an aerial view of the institution.
# 
The first task involved formulating the problem definition by representing the campus as a graph using an adjacency list, with each landmark represented by a vertex and connected by edges representing paths between them. The second task was to implement the A* search algorithm with an appropriate heuristic function. A set was used to represent the explored structure, a priority queue with a node's associated value as its priority was used for the frontier, and dictionaries were used to store transition costs and predecessors. The Euclidean distance formula was used as the heuristic function. Finally, the Open CV library was used to trace over pixel locations of the path found and display it to the user.
