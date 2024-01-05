#generating maze

import random

def summing(node):
    total=0
    for i in node:
        total=total+sum(i)
    return total


def maze_generating(row,col):    #maze generator
    walls=[[[1,1,1,1] for i in range(row)] for j in range(col)]
    cell_sum=0 #visited cells
    visit_cell=[[0 for i in range(row)] for j in range(col)]
    x=0
    y=0
    current_node=[x,y]
    visit_cell[x][y]=1 #1st cell is visited
    visit=[[x,y]]
    n=0
    while(cell_sum!=(row*col)):
        choice=[0,0,0,0]  #choice of wall to break
        if(x!=0):
            if(visit_cell[y][x-1]==0):
                choice[0]=1  #can break left wall
        if(y!=0):
            if(visit_cell[y-1][x]==0):
                choice[3]=1  #can break below wall
        if(x!=(row-1)):
            if(visit_cell[y][x+1]==0):
                choice[2]=1  #can break right  wall
        if(y!=(col-1)):
            if(visit_cell[y+1][x]==0):
                choice[1]=1  #can break above wall
        #backtracking
        if(choice==[0,0,0,0]):
            current_node=visit[n-1]
            x=current_node[0]
            y=current_node[1]
            n=n-1
        else:
            found=False
            while(found==False):
                w=random.randint(0,3)  #generating randomly a wall to break
                if(choice[w]==1):
                    if(w==0):   #breaking left wall nd moving to left cell
                        next_node=[current_node[0]-1,current_node[1]]
                        walls[current_node[1]][current_node[0]][0]=0 #removed wall
                        walls[next_node[1]][next_node[0]][2]=0
                    elif(w==1):   #breaking below wall nd moving to down cell
                        next_node=[current_node[0],current_node[1]+1]
                        walls[current_node[1]][current_node[0]][1]=0 #removed wall
                        walls[next_node[1]][next_node[0]][3]=0
                    elif(w==2):   #breaking right wall nd moving to right cell
                        next_node=[current_node[0]+1,current_node[1]]
                        walls[current_node[1]][current_node[0]][2]=0 #removed wall
                        walls[next_node[1]][next_node[0]][0]=0
                    else:   #breaking above wall nd moving to top cell
                        next_node=[current_node[0],current_node[1]-1]
                        walls[current_node[1]][current_node[0]][3]=0 #removed wall
                        walls[next_node[1]][next_node[0]][1]=0
                    n=n+1
                    visit.insert(n,next_node)
                    current_node=next_node
                    visit_cell[current_node[1]][current_node[0]]=1
                    x=current_node[0]
                    y=current_node[1]
                    found=True
        cell_sum=summing(visit_cell) 
    return (walls)
            





            
    
 