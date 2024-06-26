from tkinter import *
from PIL import ImageTk,Image
import os
from pygame import mixer
window = Tk()
window.title("")
window.geometry('352x255')
window.configure(background='white')
window.resizable(width=False,height=False)

def playmusic():
    running = listbox.get(ACTIVE)
    running_song['text'] = running
    mixer.music.load(running)
    mixer.music.play()
def pausemusic():
    mixer.music.pause()
def continuemusic():
    mixer.music.unpause()
def stopmusic():
    mixer.music.stop()
def nextmusic():
    playing = running_song['text']
    index = songs.index(playing)
    newindex = index +1
    playing =songs[newindex]
    mixer.music.load(playing)
    mixer.music.play()
    listbox.delete(0,END)

    show()

    listbox.select_set(newindex)
    running_song["text"] = playing
def premusic():
    playing = running_song['text']
    index = songs.index(playing)
    newindex = index -1
    playing =songs[newindex]
    mixer.music.load(playing)
    mixer.music.play()
    listbox.delete(0,END)

    show()

    listbox.select_set(newindex)
    running_song["text"] = playing

leftframe = Frame(window,width=150,height=150,bg="lightgray")
leftframe.grid(row=0,column=0,padx=1,pady=1)

rightframe = Frame(window,width=250,height=150,bg="lightgray")
rightframe.grid(row=0,column=1,padx=0)

downframe = Frame(window,width=400,height=100,bg="lightgray")
downframe.grid(row=1,column=0,columnspan=3,padx=0,pady=1)


listbox = Listbox(rightframe, selectmode=SINGLE, width=30, fg='black',bg="lightgray")
listbox.grid(row=0,column=0)

w=Scrollbar(rightframe)
w.grid(row=0,column=1)

listbox.config(yscrollcommand=w.set)
w.config(command=listbox.yview)

img1 = Image.open('circled.png')
img1 = img1.resize((150,150))
img1 = ImageTk.PhotoImage(img1)
app_image = Label(leftframe, height = 130, image = img1, padx=10, bg="lightgray")
app_image.place(x=0,y=1)

img2 = Image.open('icons8-rewind-button-round-48.png')
img2 = img2.resize((40,40))
img2 = ImageTk.PhotoImage(img2)
pre_button = Button(downframe, width= 40,height = 40, image = img2, padx=10, bg="darkgray", command =premusic)
pre_button.place(x=38,y=35)

img3 = Image.open('icons8-circled-play-48.png')
img3 = img3.resize((40,40))
img3 = ImageTk.PhotoImage(img3)
play_button = Button(downframe, width= 40,height = 40, image = img3, padx=10, bg="darkgray", command = playmusic)
play_button.place(x=56+28,y=35)


img4 = Image.open('icons8-fast-forward-round-48.png')
img4 = img4.resize((40,40))
img4 = ImageTk.PhotoImage(img4)
next_button = Button(downframe, width= 40,height = 40, image = img4, padx=10, bg="darkgray", command = nextmusic)
next_button.place(x=102+28,y=35)


img5 = Image.open('icons8-pause-button-48.png')
img5 = img5.resize((40,40))
img5 = ImageTk.PhotoImage(img5)
pause_button = Button(downframe, width= 40,height = 40, image = img5, padx=10, bg="darkgray", command =pausemusic)
pause_button.place(x=92+56+28,y=35)


img6 = Image.open('icons8-resume-button-48.png')
img6 = img6.resize((40,40))
img6 = ImageTk.PhotoImage(img6)
continue_button = Button(downframe, width= 40,height = 40, image = img6, padx=10, bg="darkgray", command =continuemusic)
continue_button.place(x=138+56+28,y=35)


img7 = Image.open('icons8-stop-circled-48.png')
img7 = img7.resize((40,40))
img7 = ImageTk.PhotoImage(img7)
stop_button = Button(downframe, width= 40,height = 40, image = img7, padx=10, bg="darkgray" , command =stopmusic)
stop_button.place(x=184+56+28,y=35)




running_song = Label(downframe, text = "Choose A Song", width=48, height=1, padx=10, bg="darkgray", fg="black")
running_song.place(x=0,y=0)



os.chdir(r'C:\Users\Mahendra\Downloads\Music')
songs = os.listdir()
def show():
    for i in songs:
        listbox.insert(END,i)
show()
mixer.init()
music_state = StringVar()
music_state.set("Choose One!")
window.mainloop()
