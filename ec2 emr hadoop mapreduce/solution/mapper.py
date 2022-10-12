#!/usr/bin/env python
def mapper() :
    
    M =[]
    N =[]
    X = []
    mname = "M.txt"
    nnme = "N.txt"
    xname = "X.txt"   
    
    with open( mname ) as f:
      for line in f:
        val = line.strip().split(", ")[ 2: ]
        M.append(val )

    with open( nnme ) as f:
      for line in f:
        val = line.strip().split(", ")[ 2: ]
        N.append( val ) 

    with open( xname ) as f:
      for line in f:
        val = line.strip().split(", ")[ 2: ]
        X.append( val )       
      
    return M, N , X 
