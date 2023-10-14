import cv2
import mysql.connector
from tkinter import messagebox
from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk


class Help:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face_Recognition_System")
        
        img_top=Image.open(r"Images\help.jpg")
        img_top=img_top.resize((1560,820),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=1560,height=820)
        
        dev_lable = Label(f_lbl, text="warankarmayuri99@gmail.com", font=("times new roman", 20, "bold"), bg="white")
        dev_lable.place(x=50,y=50)
        
        dev_lable = Label(f_lbl, text="pramodchavhanm@gmail.com", font=("times new roman", 20, "bold"), bg="white")
        dev_lable.place(x=50,y=100)
        
          
if __name__ == "__main__" :
    root=Tk()
    obj=Help(root)
    root.mainloop()
