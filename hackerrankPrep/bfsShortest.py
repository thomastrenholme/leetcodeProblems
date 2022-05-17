    ##start = s
    ##edges = [1,2], [1,3], [3,4]
    ##each edge is 6 distance
    ##unreachable is -1
    ##n = numNodes
    ##m = numEdges

from collections import defaultdict


def bfs(n, m, edges, s):

    distances = [-1]*n

    
    edgesFirstToSecond = defaultdict(list)

    edgesSecondToFirst = defaultdict(list)

    edgesIdxDict={}
    idxCtr=0

    for edge in edges:
        edgesFirstToSecond[edge[0]].append(edge[1])

        edgesSecondToFirst[edge[1]].append(edge[0])

        print(str(edge))
        edgesIdxDict[tuple(edge)]=idxCtr
        idxCtr+=1


    
    neighbors=edgesFirstToSecond.get(s)
    fts=True
    if neighbors is None:
        fts=False
        neighbors=edgesSecondToFirst.get(s)
        stf=True
        if neighbors is None:
            return distances

    ctr=0
    dist=6
    visitedDict={}
    neighborsQueue=[]
    currStartPtr=s
    while neighbors is not None:
        
        print("Curr Node: " + str(currStartPtr) + " Curr neighbors: " + str(neighbors))
        for neighbor in neighbors:

            if (neighbor, currStartPtr) not in visitedDict:
                edgeIdx = edgesIdxDict[(currStartPtr, neighbor)]
                distances[edgeIdx] = dist
                neighborsQueue.append(neighbor)
                visitedDict[(currStartPtr, neighbor)] = True
        dist+=6
        
        if len(neighborsQueue) > 0:
            currStartPtr=neighborsQueue.pop()
            
            if fts:
                fts=False
                stf=True
                neighbors=edgesSecondToFirst.get(currStartPtr)
            else:
                stf=False
                fts=True
                neighbors=edgesFirstToSecond.get(currStartPtr)
        else:
            break
    
    return distances


    
