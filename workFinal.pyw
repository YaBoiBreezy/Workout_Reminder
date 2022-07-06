from time import time, sleep
import tkinter as tk
from tkinter import ttk
import random
import winsound

NORM_FONT= ("Verdana", 10)
BIG_FONT= ("Verdana", 12)
toDo=['50 pushups','50 pushups',
'15 pullups','15 chinups','15 reverse-chinups',
'30 dips','30 dips',
'60s planking F+B','60s planking sides']
done=[]

#pushups
#chinups - 3 kinds
#dips - 2 kinds
#planking - 4 kinds

#lifts
#overhead lifts
#dumbbell pushups
#curls - 3 kinds

def popupmsg(done, notDone, msg):
    popup = tk.Tk()
    popup.geometry("510x220")
    tk.Label(popup, text='DONE', font=BIG_FONT).grid(row=1,column=1,sticky='W') 
    tk.Label(popup, text='TODO', font=BIG_FONT).grid(row=1,column=3,sticky='E') 
    tk.Label(popup, text=' ', font=BIG_FONT).grid(row=1,column=2) 
    tk.Label(popup, text=' ', font=BIG_FONT).grid(row=2,column=2) 
    tk.Label(popup, text=' ', font=BIG_FONT).grid(row=3,column=2) 
    tk.Label(popup, text=' ', font=BIG_FONT).grid(row=4,column=2) 
    tk.Label(popup, text=msg, font=BIG_FONT).grid(row=5,column=2) 
    for x in range(len(done)):
        tk.Label(popup, text=done[x], font=NORM_FONT).grid(row=x+2,column=1,sticky='W') 
    for x in range(len(notDone)):
        tk.Label(popup, text=notDone[x], font=NORM_FONT).grid(row=x+2,column=3,sticky='E') 
    popup.grid_columnconfigure(1, minsize=170)
    popup.grid_columnconfigure(2, minsize=170)
    popup.grid_columnconfigure(3, minsize=170)
    popup.title('New Exercise: '+msg)
    popup.attributes("-topmost", True)
    popup.eval('tk::PlaceWindow . center')
    popup.mainloop()

while True:
    sleep(1800 - time() % 1800)
    next=toDo[random.randint(0,len(toDo)-1)]
    winsound.PlaySound("SystemAsterisk", winsound.SND_ALIAS)
    toDo.remove(next)
    popupmsg(done,toDo,next)
    done.append(next)
    if 'planking' in next:
        sleep(10)
        winsound.Beep(700,800)
        sleep(int(next[:2]))
        winsound.Beep(600,800)
        sleep(int(next[:2])+2)
        winsound.Beep(500,800)
