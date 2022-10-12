#!/usr/bin/env python3
from reducer import * 
from mapper import mapper 

# mehemai . mewage map eke n reducer eka wa th reducer eken map ekawath import kaloth kelwa wenawa wage i guess . e nisa driver eken import kala .mokada nArrham map run wela reducer eka run wenne nArhi case ehema enwa 
def output( object ):
  outputfile =  "output.txt"
  f = open(outputfile , "w")
  for i in range( len( object ) ) :
    for j in  range( len( object[i] ) ):
      # print( str(i) +" " + str(j) +" "+ str( object[i][j] ) )
      f.write(  str(i) +" " + str(j) +" "+ str( object[i][j] ) +"\n"  )
  f.close()

M, N , X = mapper()
object = reducer( M, N , X )
if  object == 1 :
    print(" please provide valid inputs to input arrays . otherwise it is not possible to do the calculations ")
else :
    output( object )



