import maze_generator
import maze_printing 
import dijkstraSearch
import dijkstraRoute
import displayRoute 
#import mtTkinter
#from PIL import ImageTk,Image
from tkinter import *
def dhiv():
  row=int(e1.get())
  col=int(e2.get())
  print(row,col)
  startx=-380
  starty=startx
  gridsize=(2*(-starty))/col
  walls=maze_generator.maze_generating(row,col)
  maze_printing.printing(row, col, walls)
  visit_cell=dijkstraSearch.DijkstraSearch(walls,row,col)
  coordinate=dijkstraRoute.DijkstraRoute(visit_cell,row,col,walls)
  displayRoute.displayroute(coordinate,startx,starty,gridsize)  
  

top = Tk()  
top.geometry("1000x800")
top.configure(bg='black')
name = Label(top, text = "Rows",fg="cyan",bg='black',font=('Comic Sans MS',24)).place(x = 550,y = 308)
email = Label(top, text = "Columns",fg="cyan",bg='black',font=('Comic Sans MS',24)).place(x = 550, y = 368)   
sbmitbtn = Button(top, text = "Generate and Solve",font=('Comic Sans MS',20),activebackground = "palegreen",command=dhiv, activeforeground = "black").place(x = 580, y = 460)    
e1 = Entry(top,width=10, font=('Arial 20'))
e1.place(x = 730, y = 320)   
e2 = Entry(top,width=10,font=('Arial 20'))
e2.place(x = 730, y = 380)
"""frame=Frame(top,width=20,height=20)
frame.pack()
frame.place(anchor='left',relax=0.5,rely=0.5)
imag=ImageTk.PhotoImage(Image.open("maze.jpeg"))
label=Label(top,image=imag)
label.pack()"""
top.mainloop()  

