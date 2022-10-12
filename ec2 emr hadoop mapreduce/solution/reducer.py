#!/usr/bin/env python
 
def  reducer(   M,N,X ) :
    M =M
    N =N 
    X = X
    
    checker =0
    result =[]
    if len( M ) != len( N[0]) or len( N ) != len( M[0])  or len( N[0]) != len( X[0]) or len( M ) != len( X )  :
        return  1
    
    else :
        for i in range(len(M)):
            row =[]
            val = 0
            for j in range(len(N[0])):
                for k in range(len(N)):
                    val += int( M[i][k] ) * int( N[k][j] ) 
                val = int( X[i][j] ) - val
                row.append( val )
                val = 0    
            result.append(row)
            row =[]
        return result    


