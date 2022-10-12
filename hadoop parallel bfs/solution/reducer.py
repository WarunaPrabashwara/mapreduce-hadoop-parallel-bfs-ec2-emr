#!/usr/bin/env python
def bfs(visited, graph, node):
  distances =[]
  queue = []     #Initialize a queue
  orderedlet = []
  visited.append(node) 
  queue.append(node) # here the global queue is not modified gloally . instead , it modifies a copy of the array came to the namespace of this function . It is okay as we don't use it externally once again 
  upperlevel = []
  lowerlevel = []
  distances.append(0)
  dist = 0
  queueI = 0
  while queue:
    queueI = queueI +1 
    s = queue.pop(0)
    orderedlet.append(s)
    if node == s :
      for neighbour in graph[s]:
        if neighbour not in visited:
          visited.append(neighbour)
          queue.append(neighbour)
          upperlevel.append(neighbour)
          dist = 1

    else:
      if len(graph[s]) == 0 :
        if s not in upperlevel :
          upperlevel = list( lowerlevel )   
          lowerlevel = []
          dist = dist + 1

      for neighbour in graph[s]:
        if neighbour not in visited:
          visited.append(neighbour)
          queue.append(neighbour)
          if s in upperlevel :
            lowerlevel.append(neighbour)
          if s not in upperlevel :
            upperlevel = list( lowerlevel )   
            lowerlevel = []
            lowerlevel.append( neighbour )
            dist = dist + 1

      distances.append(dist)

    
  return orderedlet , distances 