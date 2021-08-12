import cv2
from tkinter import *
import PIL
from PIL import Image,ImageTk
root=Tk()
root.geometry("700x640")
root.configure(bg="goldenrod2")
Label(root,text="my tkcam").pack()
f1=LabelFrame(root,bg="red")
f1.pack()
l1=Label(f1,bg="red")
l1.pack()
cap=cv2.VideoCapture(0)
while True:

    img=cap.read()[1]
    img1=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    try:
        img = ImageTk.PhotoImage(Image.fromarray(img1))
    except:
        break
    l1["image"]=img
    root.update()
