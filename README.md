Graph-Based Actor Connectivity Analyzer
A Python program that calculates the Bacon number of any actor using Dijkstra’s Algorithm and a binary heap priority queue for efficient shortest path calculations. It processes a dataset of 11,000+ actors and 7,000+ movies to determine the degrees of separation from Kevin Bacon.

Features - 
Computes shortest paths efficiently using Dijkstra’s Algorithm
Processes large datasets with binary heap optimization
Interactive command-line interface for user input
Supports 11,000+ actors and 7,000+ movies


Usage - 
Run the program and enter an actor's name to compute their Bacon number:

bash
Copy
Edit
python bacon_number.py
Example:

vbnet
Copy
Edit
Enter actor's name: Tom Hanks  
Bacon Number: 1  
(Tom Hanks → Apollo 13 → Kevin Bacon)

How It Works - 
Graph Representation: Actors and movies are modeled as a graph where edges connect actors who have appeared in the same film.
Shortest Path Algorithm: Uses Dijkstra’s Algorithm with a binary heap priority queue to quickly find the shortest path between actors.
Data Processing: Parses a dataset containing actor-movie relationships to construct the graph dynamically.
