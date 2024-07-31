from numpy import array
from time import sleep
from random import randint
from os import system

cute_emojis = [
"❤︎"
]

def create_matrix(rows, cols):
    return array([[" "]*cols]*rows)

def display(matrix):
    for row in matrix:
        print("\t"*8, *row,)
    print("\n"*2)


        
def show_stat(matrix,c):
    if c == 0:
        print("\n"*3)
        print("\t"*12,"    Filled Matrix : ",len(matrix),"x",len(matrix[0]))
        print("\n"*1)
    else:
        print("\n"*3)
        print("\t"*12,"    Matrix : ",len(matrix),"x",len(matrix[0]))
        print("\n"*1)
        
def update(matrix,cells,load):
    for i in range(cells):
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
    while not (rows >= 10 and cols >= 10):
            rows = int(input("Matrix Rows: "))
            cols = int(input("Matrix Cols: "))
            
    Matrix=create_matrix(rows,cols)
    
    while not (full(Matrix," ") ):
        system("cls")
        show_stat(Matrix,None)
        update(Matrix,20,cute_emojis)
        display(Matrix)
        sleep(0.05)

    system("cls")    
    show_stat(Matrix,0)
    display(Matrix)
    exit()
        

main()