import sys # for the "maxsize" of an int for representing infinity
import matplotlib.pyplot as plt
import networkx as nx
from graph import Graph
from vertex import Vertex
from binary_heap import BinaryHeap
from scanner import Scanner
from collections import deque

def main():
    actors = Scanner('actors.txt')
    movies = Scanner('movies.txt')
    movie_actors = Scanner('movie-actors.txt')
    g = create_map(actors, movies, movie_actors)
    new_g = bfs(g.get_vertex('Kevin Bacon'))
    per = input('Enter the name of an actor: ')
    v = new_g.get_vertex(per)
    lines = []
    kb = 0
    nx_g = nx.Graph()
    graph_components = []
    while v.get_ID() != 'Kevin Bacon':
        a = v.get_ID()
        b = " appeared in "
        x = v.get_connections()
        v2 = list(x)[0]
        c = v.get_weight(v2)
        d = " with "
        e = v2.get_ID()
        v=v2 
        z = a+b+c+d+e
        lines.append(z)
        kb += 1
        
        lst = []
        lst.append(a)
        lst.append(e)
        lst.append(c)
        graph_components.append(lst)
        
    print(per + " 's Bacon number is " + str(kb))
    for line in lines:
        print(line)
        
    edges = []
    for lst in graph_components:
        edges.append([lst[0], lst[1]])

    nx_g.add_edges_from(edges)

    pos = nx.spring_layout(nx_g)
    nx.draw(nx_g,pos, with_labels='True')
    

def create_map(actor_file, movie_file, movie_actors_file):

    #dictionary lookup for actor ID
    actors = {}
    all_actors = []
    while True:
        current = actor_file.readline().strip()
        if current == '':
            break
        actors[current.split('|')[0]] = current.split('|')[1]
        all_actors.append(current.split('|')[1])

    #dictionary lookup for movie ID
    movies = {}
    while True:
        current = movie_file.readline().strip()
        if current == '':
            break
        movies[current.split('|')[0]] = current.split('|')[1]

    #adding every actor as a vertex
    g = Graph()
    for i in range(len(all_actors)):
        g.add_vertex(all_actors[i])

    #adding edges
    last = ''
    curr_actors = []
    while True:
        current = movie_actors_file.readline().strip()
        if current != '':
            curr_list = current.split('|')
            if not curr_actors:
                curr_actors.append(curr_list[1])
                last = curr_list
            
            elif curr_list[0] == last[0]:
                curr_actors.append(curr_list[1])
                last = curr_list

        if curr_list != last or current == '':
            for i in range(len(curr_actors) - 1):
                for j in range(i+1, len(curr_actors)):
                    g.add_edge(actors[curr_actors[i]],actors[curr_actors[j]],movies[last[0]])
                    g.add_edge(actors[curr_actors[j]],actors[curr_actors[i]],movies[last[0]])
            curr_actors = []
            curr_actors.append(curr_list[1])
            last = curr_list
        if current == '':
            break
    return g

def bfs(start):
    T = Graph()
    Q = deque()
    Q.append(start)
    T.add_vertex(start.get_ID())
    while Q:
        V_des = Q.popleft()
        for V_src in V_des.get_connections():
            if not T.contains(V_src.get_ID()):
                T.add_edge(V_src.get_ID(), V_des.get_ID(), V_src.get_weight(V_des))
                Q.append(V_src)
    return T

main()