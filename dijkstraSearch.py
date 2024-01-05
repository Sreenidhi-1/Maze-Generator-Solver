import oppositenode
def DijkstraSearch(walls,row,col):
    visit_cell=[[0 for i in range(row)] for j in range(col)]
    visit_cell[0][0]=1   #checking visiting of cell
    c_node=[[0,0]]
    new=True
    while(new==True):
        new=False
        for i in range(len(c_node)): 
            current_node=c_node[0]
            for j in range(4): #check walls
                if(walls[current_node[1]][current_node[0]][j]==0):
                    node=oppositenode.opposite_node(j,current_node)
                    if(visit_cell[node[1]][node[0]]==0): #check if visited
                        visit_cell[node[1]][node[0]]=visit_cell[current_node[1]][current_node[0]]+1
                        c_node.append(node) #adds new node to list
                        new=True
            c_node.remove(current_node)  #removes previously visited node
    return(visit_cell)