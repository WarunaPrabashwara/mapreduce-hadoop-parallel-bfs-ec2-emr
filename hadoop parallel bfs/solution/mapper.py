#!/usr/bin/env python

def graph(  ):
    graph = { }
    filename = "graph.txt"
    with open( filename ) as f:
      for line in f:
        val = []
        if line.split(":")[1].split()[0] != 'none' : 
            val =  line.split(":")[1].split()
        (k, v) = [ line.split(":")[0] , val  ]
        graph[str(k)] = v

    return graph 