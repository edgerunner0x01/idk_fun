from numpy import array
from time import sleep
from random import randint
from os import system

cute_emojis = ["#"]


def create_matrix(rows, cols, main_cell):
    return array([[main_cell]*cols]*rows)

def display(matrix):
    for row in matrix:
        print("\t",*row,)
    print("\n"*2)


        
def show_stat(matrix,c,time,speed,main_cell):
    if c == 0:
        print("\n"*3)
        print("\t","Filled Matrix : ",len(matrix),"x",len(matrix[0]),"- Refresh Rate:",time,"ms","- Fill Speed:",speed,"- Main Cell: \'",main_cell,"\'")
        print("\n"*1)
    else:
        print("\n"*3)
        print("\t","Matrix:",len(matrix),"x",len(matrix[0]),"- Refresh Rate:",time,"ms","- Fill Speed:",speed,"- Main Cell: \'",main_cell,"\'")
        print("\n"*1)
        
def update(matrix,cells,load):
    for i in range(cells):
        if not matrix[randint(0,len(matrix)-1)][randint(0,len(matrix[0])-1)] in load:
            matrix[randint(0,len(matrix)-1)][randint(0,len(matrix[0])-1)]=str(load[len(load)-1])

def full(Matrix,cell):
    test=True
    i=0
    while (test==True and i < len(Matrix)):
        if cell in Matrix[i]:
            test=False
        else:
            i+=1
    if test==True:
        return True
    else:
        return False
        
def main():
    
    rows = int(input("Matrix Rows: "))
    cols = int(input("Matrix Cols: "))
    rr = int(input("Refrech Rate in ms: "))
    speed = int(input("Fill Speed: "))
    main_cell=str(input("Main Cell: "))
    while not (rows >= 10 and cols >= 10 and 0<=rr<=1000 and 1<=speed<=10000):
            rows = int(input("Matrix Rows: "))
            cols = int(input("Matrix Cols: "))
            rr = int(input("Refrech Rate in ms: "))
            speed = int(input("Main Cell: "))
            
    Matrix=create_matrix(rows,cols,main_cell)
    show_stat(Matrix,None,rr,speed,main_cell)
    display(Matrix);input()
    while not ( full(Matrix,main_cell) ):
        system("cls")
        show_stat(Matrix,None,rr,speed,main_cell)
        update(Matrix,speed,cute_emojis)
        display(Matrix)
        sleep(rr/1000)

    system("cls")    
    show_stat(Matrix,0,rr,speed,main_cell)
    display(Matrix)
    exit()
        
if __name__=="__main__":
    main()