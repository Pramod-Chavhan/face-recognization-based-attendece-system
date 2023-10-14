import cv2
import mysql.connector
from tkinter import messagebox
from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk


class Developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face_Recognition_System")
        
        
        title_lbl = Label(self.root,text="DEVELOPER", font=("times new roman", 35, "bold"), bg="white", fg="skyblue")
        title_lbl.place(x=0, y=0, width=1530, height=45)
        
        img_top=Image.open(r"Images\devG.jpg")
        img_top=img_top.resize((1530,820),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=45,width=1530,height=820)
        
        # ===============frame
        main_frame = Frame(f_lbl, bd=2,bg="white")
        main_frame.place(x=1080, y=0, width=470, height=750)
        
        #developer images
        
        img_top1=Image.open(r"Images\dev2.png")
        img_top1=img_top1.resize((450,250),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img_top1)

        f_lbl=Label(main_frame,image=self.photoimg1)
        f_lbl.place(x=0,y=0,width=450,height=250)
        
        img_top2=Image.open(r"Images\dev1.png")
        img_top2=img_top2.resize((450,250),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img_top2)
        f_lbl=Label(main_frame,image=self.photoimg2)
        f_lbl.place(x=0,y=252,width=450,height=250)
        
        img_top3=Image.open(r"Images\dev3.png")
        img_top3=img_top3.resize((450,250),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img_top3)
        f_lbl=Label(main_frame,image=self.photoimg3)
        f_lbl.place(x=0,y=504,width=450,height=250)
        
      
if __name__ == "__main__" :
    root=Tk()
    obj=Developer(root)
    root.mainloop()

