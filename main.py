from tkinter import *
import random
game=Tk()
game.title("paper_rock_scissor")
color="#5c98ff"
game.configure(bg =color)
#=========================================frame=================
Top_first=Frame(game,width=400,height=50,bg=color)
Top_first.pack(side="top")
Top_second=Frame(game,width=400,height=50,bg=color)
Top_second.pack(side="top")
Top_third=Frame(game,width=400,height=50,bg=color)
Top_third.pack(side="top")
Top_forth=Frame(game,width=400,height=50,bg=color)
Top_forth.pack(side="top")
Top_five=Frame(game,width=400,height=50,bg=color)
Top_five.pack(side="top")
Top_six=Frame(game,width=400,height=50,bg=color)
Top_six.pack(side="top")
Top_seven=Frame(game,width=400,height=50,bg=color)
Top_seven.pack(side="top")
Top_eight=Frame(game,width=400,height=50,bg=color)
Top_eight.pack(side="top")
#=================================================butten=======================
btn_1=Button(Top_first,text="ROCK",width=30,highlightbackground=color,command=lambda: Rock() )
btn_1.pack(side=LEFT,padx=5,pady=5)
btn_2=Button(Top_second,text="paper",width=30,highlightbackground=color,command=lambda: paper() )
btn_2.pack(side=LEFT,padx=5,pady=5)
btn_3=Button(Top_third,text="scissor",width=30,highlightbackground=color,command=lambda: scissor() )
btn_3.pack(side=LEFT,padx=5,pady=5)
btn_4=Button(Top_five,text="",width=30,highlightbackground=color)
btn_4.pack(side=LEFT,padx=5,pady=5)
btn_5=Button(Top_seven,text="",width=30,highlightbackground=color)
btn_5.pack(side=LEFT,padx=5,pady=5)
btn_6=Button(Top_eight,text="creator",width=5,highlightbackground=color,command=lambda: creator() )
btn_6.pack(side=LEFT,padx=5,pady=5)
btn_7=Button(Top_eight,text="clear",width=5,highlightbackground=color,command=lambda: clear() )
btn_7.pack(side=LEFT,padx=5,pady=5)
#=================================================================
def Rock():
    z=random.randint(0,2)
    if z==0:

        btn_4["text"]="Rock"
        btn_5["text"]="Tie"
    elif  z==1:

        btn_4["text"] = "paper"
        btn_5["text"] = "you lose"
    elif  z==2:

        btn_4["text"] = "scissor"
        btn_5["text"] = "you win"
def paper():
    z = random.randint(0, 2)
    if z == 0:

        btn_4["text"] = "Rock"
        btn_5["text"] = "you win"
    elif z == 1:

        btn_4["text"] = "paper"
        btn_5["text"] = "Tie"
    elif z == 2:

        btn_4["text"] = "scissor"
        btn_5["text"] = "you lose"

def scissor():
    z = random.randint(0, 2)
    if z == 0:

        btn_4["text"] = "Rock"
        btn_5["text"] = "you lose"
    elif z == 1:

        btn_4["text"] = "paper"
        btn_5["text"] = "you win"
    elif z == 2:

        btn_4["text"] = "scissor"
        btn_5["text"] = "Tie"
def clear():
    btn_4["text"] = ""
    btn_5["text"] = ""
#===============================================================

game.mainloop()