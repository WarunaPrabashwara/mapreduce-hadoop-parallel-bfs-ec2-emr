#!/usr/bin/env python

import reducer

from mapper import  graph
map = graph()


visited = [] # List to keep track of visited nodes.

# Driver Code


orderedlet , distances = reducer.bfs(visited, map, '1')
#print( orderedlet )
#print( distances )

def output():
  outputfile =  "output.txt"
  f = open(outputfile , "w")
  key = 0
  for i in orderedlet :
    f.write( i + ":" +" " + str(distances[key])  + "\n" )
    key = key +1
  f.close()


output() 