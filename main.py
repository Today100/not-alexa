from tkinter import *
from replit import audio
import time
# import sys
root = Tk()
root.attributes('-fullscreen', True)
lab = Label(root, text="Hello! Welcome to this fun \"Alexa\" smart home simulator!\n\nIt is just simple program build with python.\n\nThis program did not use machine learning technology.\n\nSo commands are stable. If you change the word, program cannot identify what you mean.\n\nYou can type help to see a list of command and exit for exit the program.\n\nPRESS the START BUTTON to START")
lab.pack()



def setup():
  lab.forget()
  starts.forget()
  global can, l
  can = Canvas(root)
  can.pack(fill=BOTH)
  can.create_oval(0, 0, 50, 80, fill="yellow", outline="grey", width=4, tag='lighton')
  can['bg'] = 'white'
  
  l = can.create_text(100,100,text="light is on!")
  
  ask = Label(root, text="What Should I do?")
  ask.pack()
  ins = Entry(root)
  ins.pack()
  ins.bind("<Return>", run)
  global la
  la = can.create_text(120, 200, text=' ')
  global cur
  cur = can.create_rectangle(
    250, 10, 370, 150,
    outline="#fb0",
    fill="#fb0")
  line = can.create_line(230, 30, 390, 30, fill='black')
  run(n='help')

starts = Button(root, text='START', command=setup)

starts.place(x=300, y=500)
starts.pack()

def f():
  can.itemconfig(la, text='  ')

lights = 'on'
def light(x):
  global lights, win, win1, win2, win3
  if x =='true':
    lights = 'on'
    can.create_oval(0, 0, 50, 80, fill="yellow", outline="#DDD", width=4, tag='lighton')
    can['bg'] = 'white'
    can.itemconfig(l, text="light is on!", fill='black')
    can.itemconfig(cur, fill='#fb0', outline='#fb0')
    try:
      can.itemconfig(win, outline='#fb0')
      can.itemconfig(win1, outline='#fb0')
      can.itemconfig(win2, outline='#fb0')
      can.itemconfig(win3, outline='#fb0')
    except:
      pass
  else:
    lights = 'off'
    can.create_oval(0, 0, 50, 80, fill="black", outline="grey", width=4, tag='lighton')
    can['bg'] = 'black'
    can.itemconfig(l, text="light is off!", fill='white')
    can.itemconfig(cur, fill='black', outline='black')

k = 0


def run(e=None, n='none'):
  global win, win1, win2, win3
  try:
    n = e.widget.get()
    e.widget.delete(0, END)
  except:
    pass
  if n == "help":
    global k
    k += 1
    if k == 2:
      f()
      k = 0
      return
    can.itemconfig(la, text="""  help  =  see all the command
    exit  =  exit the program
    light on = turn the light on
    light off = turn the light OFF
    curtain on = open curtain
    curtain off = close curtain
    music = music (might not work)
    type help again to close help
    """, fill='red')
    
  elif "light" in n and "on" in n or "light" in n and "open" in n:
    light('true')
  elif "light" in n and 'off' in n or "light" in n and "close" in n :
    light('off')
    can.itemconfig(win, outline='black')
    can.itemconfig(win1, outline='black')
    can.itemconfig(win2, outline='black')
    can.itemconfig(win3, outline='black')
    
  elif "curtain" in n and "off" in n or "curtain" in n and "close" in n:
    can.coords(cur, 250, 10, 370, 150)
    try:
      if lights == 'on':
        can.itemconfig(win, outline='#fb0')
        can.itemconfig(win1, outline='#fb0')
        can.itemconfig(win2, outline='#fb0')
        can.itemconfig(win3, outline='#fb0')
      else:
        can.itemconfig(win, outline='black')
        can.itemconfig(win1, outline='black')
        can.itemconfig(win2, outline='black')
        can.itemconfig(win3, outline='black')
    except:
      pass
  elif "curtain" in n and "on" in n or "curtain" in n and "open" in n:
    can.coords(cur, 250, 10, 260, 150)
    
    win = can.create_rectangle(290, 50, 310, 70, outline='black')
    win1 = can.create_rectangle(290, 70, 310, 90, outline='black')
    win2 = can.create_rectangle(310, 50, 330, 70, outline='black')
    win3 = can.create_rectangle(310, 70, 330, 90, outline='black')
  elif "music" in n:
    source = audio.play_tone(0.5, 500, 3)
    time.sleep(0.5)
    source = audio.play_tone(0.5, 440, 1)
    time.sleep(0.5)
    source = audio.play_tone(0.5, 390, 2)
    time.sleep(0.5)
    source = audio.play_tone(0.5, 360, 2)
    time.sleep(0.5)
    source = audio.play_tone(0.5, 300, 1)
    time.sleep(0.5)
    source = audio.play_tone(0.5, 360, 2)
    time.sleep(0.5)
    source = audio.play_tone(0.5, 200, 2)
    time.sleep(0.5)
    source = audio.play_tone(0.5, 500, 3)
    time.sleep(0.5)
    source = audio.play_tone(0.5, 440, 1)
    time.sleep(0.5)
    source = audio.play_tone(0.5, 390, 2)
    return
  elif n == "exit":
    root.quit()
    root.destroy()
    return
 
# b = Button(root, image='light_on.jpg')
# # b.pack()

mainloop()