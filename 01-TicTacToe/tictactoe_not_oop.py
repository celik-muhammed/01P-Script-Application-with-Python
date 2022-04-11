import tkinter as tk
from tkinter import messagebox

root = tk.Tk()

# configure the root window
root.title("Tic Tac Toe")

# set window size
root.geometry('450x450')

#set window color
root.configure(bg='orange')
#root['bg']='green'
#root.configure(background='yellow')
#root['background']='#856ff8'
  

# InputFrame InputFrame top frame - with add 2 button X, O  
InputFrame = tk.Frame(root)
InputFrame.pack()

# select first player from - radio button
rbtn_player_variable_String = tk.StringVar()
cur_player = None
msg_label = None

# adding Label the root window
msg_label = tk.Label(
            InputFrame, 
            text ="   Welcome Allen's Game\n\t  firstly select PLAYER   ", 
            justify= tk.LEFT,
            font = "50") 
msg_label.pack()


def show_choice():

    global cur_player, msg_label
    choice  = rbtn_player_variable_String.get()
    cur_player = choice
    msg_label.config(text = f'Selected {cur_player}')
    
    for child in InputFrame.winfo_children():
        child.configure(state='disable')
    
    for child in ButtonFrame.winfo_children():
        child.configure(state='active')


# Radiobutton
rbtn1 = tk.Radiobutton(
            InputFrame, 
            text='Player X', 
            value='Player X', 
            padx=1, 
            width=12, 
            variable=rbtn_player_variable_String)

rbtn1['command'] = lambda: show_choice()
rbtn1.pack(anchor=tk.CENTER)  # side=tk.LEFT

tk.Radiobutton(
            InputFrame, 
            text='Player O', 
            value='Player O', 
            padx=1, width=12, 
            variable=rbtn_player_variable_String, 
            command=lambda: show_choice()).pack(anchor=tk.CENTER)  # side=tk.LEFT



# adding ButtonFrame after InputFrame for gaming - with add 2 button X, O  
ButtonFrame = tk.Frame(root)
ButtonFrame.pack( side = tk.BOTTOM )

button_img_o = tk.PhotoImage(file='res/circle.png')
button_img_x = tk.PhotoImage(file='res/xmark.png') 
#button_img_red = tk.PhotoImage(file='red.png')

board_button_list = [None] * 9
set_btn_variable_Int = get_btn_variable_Int = [None] * 9  # bellekte aynı yeri gösterir
 

def onclick_button():
    global get_btn_variable_Int, button_img_o, button_img_x

    # check which button clicked and add player name
    for i in range(9):
        if set_btn_variable_Int[i].get() == 1:
            get_btn_variable_Int[i] = tk.StringVar(value=cur_player)
    
    # check which button clicked and add picture - button_img_o or button_img_x
    for j in range(9):
        if get_btn_variable_Int[j].get() == 'Player X':
            board_button_list[j].config(image=button_img_x)
            board_button_list[j].config(state='disable')
        elif get_btn_variable_Int[j].get() == 'Player O':
            board_button_list[j].config(image=button_img_o)
            board_button_list[j].config(state='disable')

    win_check()

def win_check():
    global cur_player
    show = None

    while True:
        if get_btn_variable_Int[0].get() == cur_player \
                and get_btn_variable_Int[1].get() == cur_player \
                and get_btn_variable_Int[2].get() == cur_player:

            show = messagebox.showinfo(title='Greetings', message='WINNER --> ' + cur_player)

        elif get_btn_variable_Int[3].get() == cur_player \
                and get_btn_variable_Int[4].get() == cur_player \
                and get_btn_variable_Int[5].get() == cur_player:
            show = messagebox.showinfo(title='Greetings', message='WINNER --> ' + cur_player)
        elif get_btn_variable_Int[6].get() == cur_player \
                and get_btn_variable_Int[7].get() == cur_player \
                and get_btn_variable_Int[8].get() == cur_player:
            show = messagebox.showinfo(title='Greetings', message='WINNER --> ' + cur_player)
        elif get_btn_variable_Int[0].get() == cur_player \
                and get_btn_variable_Int[3].get() == cur_player \
                and get_btn_variable_Int[6].get() == cur_player:
            show = messagebox.showinfo(title='Greetings', message='WINNER --> ' + cur_player)
        elif get_btn_variable_Int[1].get() == cur_player \
                and get_btn_variable_Int[4].get() == cur_player \
                and get_btn_variable_Int[7].get() == cur_player:
            show = messagebox.showinfo(title='Greetings', message='WINNER --> ' + cur_player)
        elif get_btn_variable_Int[2].get() == cur_player \
                and get_btn_variable_Int[5].get() == cur_player \
                and get_btn_variable_Int[8].get() == cur_player:
            show = messagebox.showinfo(title='Greetings', message='WINNER --> ' + cur_player)
        elif get_btn_variable_Int[0].get() == cur_player \
                and get_btn_variable_Int[4].get() == cur_player \
                and get_btn_variable_Int[8].get() == cur_player:
            show = messagebox.showinfo(title='Greetings', message='WINNER --> ' + cur_player)
        elif get_btn_variable_Int[2].get() == cur_player \
                and get_btn_variable_Int[4].get() == cur_player \
                and get_btn_variable_Int[6].get() == cur_player:
            show = messagebox.showinfo(title='Greetings', message='WINNER --> ' + cur_player)
        break
    
    # Winner Message Check Game end make not clikable remaining buttons
    if show is not None:
        for load in range(9):
            board_button_list[load].config(state='disable')
        return show    
    
    # if no winner Continue - change player - and go game
    if cur_player == 'Player X': cur_player = 'Player O'
    elif cur_player == 'Player O': cur_player = 'Player X'


# butonlar için int variable listesi olustur
for i in range(9):
    set_btn_variable_Int[i] = tk.IntVar()


# buton olustur - buton listesini güncelle
for k in range(9):
    board_button_list[k] = tk.Checkbutton(
                            ButtonFrame,                            
                            text=f'Click!\n{k}',
                            variable=set_btn_variable_Int[k], 
                            onvalue=1, 
                            offvalue=0, 
                            pady=35, padx=36,
                            indicatoron=False, 
                            state='disable',
                            command=lambda: onclick_button())


# gridleyerek (row, col) - matris frame_2 ye ekliyoruz
index = 0
for row in range(3):
    for col in range(3):
        board_button_list[index].grid(row=row, column=col)  # sticky=tk.W
        index += 1

root.mainloop()