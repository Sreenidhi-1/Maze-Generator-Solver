def DijkstraRoute(visit_cell,row,col,walls):
    d=visit_cell[row-1][col-1]
    coordinate=[[row-1,col-1]] #finish to top right
    while(coordinate[0]!=[0,0]):
        if(walls[coordinate[0][1]][coordinate[0][0]][0]==0):
            if(visit_cell[coordinate[0][1]][coordinate[0][0]-1]==d-1):
                coordinate.insert(0,[coordinate[0][0]-1,coordinate[0][1]])
                d=d-1
        if(walls[coordinate[0][1]][coordinate[0][0]][1]==0):
            if(visit_cell[coordinate[0][1]+1][coordinate[0][0]]==d-1):
                coordinate.insert(0,[coordinate[0][0],coordinate[0][1]+1])
                d=d-1    
        if(walls[coordinate[0][1]][coordinate[0][0]][2]==0):
            if(visit_cell[coordinate[0][1]][coordinate[0][0]+1]==d-1):
                coordinate.insert(0,[coordinate[0][0]+1,coordinate[0][1]])
                d=d-1
        if(walls[coordinate[0][1]][coordinate[0][0]][3]==0):
            if(visit_cell[coordinate[0][1]-1][coordinate[0][0]]==d-1):
                coordinate.insert(0,[coordinate[0][0],coordinate[0][1]-1])
                d=d-1  
    return(coordinate)