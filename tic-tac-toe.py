from tkinter import *
import random
root = Tk()
root.title('Criss-cross')
game_run = True
field = []
cross_count = 0

def new_game():
    global game_run
    for row in range(3):
        for col in range(3):
            field[row][col]['text'] = ' '
            field[row][col]['background'] = 'lavender'    
    game_run = True

def click(row, col):
    global player
    if player ==1:
        if game_run and field[row][col]['text'] == ' ':            
            field[row][col]['text'] = 'X'                
            check_win('X')
            player=2             
    elif player == 2:
        if game_run and field[row][col]['text'] == ' ':
            field[row][col]['text'] = 'O'                
            check_win('O') 
            player=1

def check_win(smb):
    for n in range(3):
        check_line(field[n][0], field[n][1], field[n][2], smb)
        check_line(field[0][n], field[1][n], field[2][n], smb)
    check_line(field[0][0], field[1][1], field[2][2], smb)
    check_line(field[2][0], field[1][1], field[0][2], smb)

def check_line(a1,a2,a3,smb):
    if a1['text'] == smb and a2['text'] == smb and a3['text'] == smb:
        a1['background'] = a2['background'] = a3['background'] = 'green'
        global game_run
        game_run = False

player = 1
for row in range(3):
    line = [] 
    for col in range(3):        
        button = Button(root, text=' ', width=4, height=2, 
                    font=('Verdana', 20, 'bold'),
                    background='lavender',
                    command= lambda row=row, col=col: click(row,col))
        button.grid(row=row, column=col, sticky='nsew')
        line.append(button)
    field.append(line)

new_button = Button(root, text='new game', command=new_game)
new_button.grid(row=3, column=0, columnspan=3, sticky='nsew')
root.mainloop()
