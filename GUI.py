#Import All Required Packages
#----------------------------------------->
from tkinter import *
from PIL import Image,ImageTk
from winsound import *
import random
#CREATED BY BISWARUP BHATTACHARJEE
from face_smaple_collects import fsc
from model_traning import mt
from  Recognizer import recog

import os
def AllFilesDelete():
    dir = 'faces/'
    for f in os.listdir(dir):
        os.remove(os.path.join(dir, f))
        print("RESETTING ALL IMAGES IN FACES FOLDER...")


clicklist=["click.wav","click2.wav"]
#------------------------------------------->
#Canvas Window Creation
#-------------------------------------------->
#play clicking tune
clicked = lambda: PlaySound(random.choice(clicklist),SND_FILENAME)
#--------------------------------------------->
root = Tk()
root.geometry("675x500+120+120")
root.minsize(675,395)
root.maxsize(675,395)
rootwalpaper=Image.open("rootwallpaper.jpg")
bgimg=ImageTk.PhotoImage(rootwalpaper)
canvas=Canvas(root,width=675,height=500)
canvas.pack()
canvas.create_image(335,195,image=bgimg)
root.title("HANDWRITTING RECOGNITION SYSTEM")
root.iconbitmap("icon.ico")
#------------------------------------------------->
#Buttons Section
#-------------------------------------------------->
#Button1---->Hand Written Digits Recognition
#Button2---->OCR
#Button3---->Credits
#Button4---->Exit
b1=Button(root,text="FACIAL \n SAMPLES \n COLLECTS",font=("BankGothic Md BT",13,"bold"),fg="aquamarine",pady=5,padx=5,relief=RAISED,bg="black",command=lambda:[clicked(),fsc()])
#place the b1 button
b1_placing=canvas.create_window(222,120,window=b1)
b2=Button(root,text=" MODEL TRAINING ",font=("BankGothic Md BT",10,"bold"),fg="aquamarine",padx=26,pady=18,relief=RAISED,bg="black",command=lambda:[clicked(),mt()])
#place the b2 button
b2_placing=canvas.create_window(450,120,window=b2)
b3=Button(root,text=" RECOGNIZER ",font=("BankGothic Md BT",12,"bold"),fg="yellow",pady=20,padx=4,relief=RAISED,bg="black",command=lambda:[clicked(),recog()])
#place the b3 button
b3_placing=canvas.create_window(452,250,window=b3)
b4=Button(root,text=" RESET ",font=("BankGothic Md BT",15,"bold"),fg="red",padx=31,pady=3,relief=SUNKEN,command=lambda:[clicked(),AllFilesDelete()],bg="black")
#place the b4 button
b4_placing=canvas.create_window(220,250,window=b4)
#------------------------------------------------->
#main function
if __name__ == '__main__':
    root.mainloop()
