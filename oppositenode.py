def opposite_node(j,current_node):
    if(j==0):
        opposite_node=[current_node[0]-1, current_node[1]]
    elif(j==1):
        opposite_node=[current_node[0], current_node[1]+1]   
    elif(j==2):
        opposite_node=[current_node[0]+1, current_node[1]]
    else:
        opposite_node=[current_node[0], current_node[1]-1]
    return (opposite_node)