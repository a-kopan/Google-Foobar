#the matrix is a matrix with 0's for passable tiles, and 1's for walls
#you can destroy 1 wall
#start and end are always 0
#moves only up/down/left/right
#path length includes both start and end
#the point is to return the shortest path length from (0,0) to (w-1,h-1)

import heapq
def solution(matrix):
    START = (0,0)
    END = (len(matrix)-1,len(matrix[0])-1)
    DIRECTIONS = [(0,1),(1,0),(-1,0),(0,-1)]
    #((flag,(x,y)),(flag,(x,y)))
    visited = set()
    
    #queue for all temp spaces
    queue = [(1,False,START)]

    #while the distance of end point wasn't established
    while queue:
        current = heapq.heappop(queue)
        for diff_x, diff_y in DIRECTIONS:
            x,y = current[2][0]+diff_x, current[2][1]+diff_y
            wall_broken = current[1]

            if x<0 or x>=len(matrix) or y<0 or y>=len(matrix[0]): continue
            elif (x,y)==END: return current[0]+1
            elif wall_broken and matrix[x][y]==1: continue
            elif (False,(x,y)) in visited: continue
            elif (True,(x,y)) in visited and matrix[x][y]==1: continue
            elif (True,(x,y)) in visited and wall_broken: continue
            else:
                if wall_broken and matrix[x][y]==0:
                    heapq.heappush(queue,(current[0]+1,True,(x,y)))
                    visited.add((True,(x,y)))
                elif not wall_broken and matrix[x][y]==1:
                    heapq.heappush(queue,(current[0]+1,True,(x,y)))
                    visited.add((True,(x,y)))
                else:
                    heapq.heappush(queue,(current[0]+1,False,(x,y)))
                    visited.add((False,(x,y)))