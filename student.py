# -*- coding: utf-8 -*-
"""
Created on Sun Jul  2 09:30:22 2023

@author: pramo
"""

from tkinter import messagebox
from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
import mysql.connector
import cv2


class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face_Recognition_System")
        
        #*********************VARIABLE*********************************
         
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()
          

        #frist Image
        img=Image.open(r"C:\Users\pramo\OneDrive\Desktop\FRA_Project\Images\img2.jfif")
        img=img.resize((500,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)
        
        #Second Image
        img1=Image.open(r"C:\Users\pramo\OneDrive\Desktop\FRA_Project\Images\IMG1.jfif")
        img1=img1.resize((500,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=130)
        
        #third Image
        img2=Image.open(r"C:\Users\pramo\OneDrive\Desktop\FRA_Project\Images\IMG3.jfif")
        img2=img2.resize((500,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=500,height=130)
############################################################################################   
   
      #BG Image
        img3=Image.open(r"C:\Users\pramo\OneDrive\Desktop\FRA_Project\Images\BG1.jfif")
        img3=img3.resize((1500,710),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
 
        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1500,height=710)

        title_lbl=Label(bg_img,text="FACE RECOGNITION BASED ATTENDENCE SYSTEM",font=("times new roman",35,"bold"),bg="skyblue",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        main_frame = Frame(bg_img, bd=2)
        main_frame.place(x=5, y=55, width=1500, height=600)

        # LEFT LABLE FRAME
        Left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE,text="student Details", font=("times new roman", 12, "bold"))
        Left_frame.place(x=10, y=10, width=730, height=580)

        img_l = Image.open(r"Images\bok.jpg")
        img_l = img_l.resize((720, 130), Image.ANTIALIAS)
        self.photoimg_l = ImageTk.PhotoImage(img_l)

        b1 = Button(Left_frame, image=self.photoimg_l, cursor="hand2")
        b1.place(x=5, y=0, width=715, height=130)

        # Current Course Information
        current_course = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE,text="Current Course", font=("times new roman", 12, "bold"))
        current_course.place(x=14, y=155, width=720, height=130)

        # Department
        dep_lable = Label(current_course, text="Department", font=("times new roman", 12, "bold"), bg="white")
        dep_lable.grid(row=0, column=0, padx=10, sticky=W)

        dep_combo = ttk.Combobox(current_course,textvariable=self.var_dep,font=("times new roman", 12, "bold"), state="readonly")
        dep_combo["values"] = ("Select Department","computer", "IT", "Civil", "Mechanical", "MCA")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        # Course
        course_lable = Label(current_course, text="Course", font=("times new roman", 12, "bold"), bg="white")
        course_lable.grid(row=0, column=2, padx=10, sticky=W)

        course_combo = ttk.Combobox(current_course,textvariable=self.var_course, font=("times new roman", 12, "bold"), state="readonly")
        course_combo["values"] = ("Select Course", "FY", "SY", "TY", "LY")
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=2, pady=10, sticky=W)

        # year
        year_lable = Label(current_course,text="Year", font=("times new roman", 12, "bold"), bg="white")
        year_lable.grid(row=1, column=0, padx=10, sticky=W)

        year_combo = ttk.Combobox(current_course,textvariable=self.var_year, font=("times new roman", 12, "bold"), state="readonly")
        year_combo["values"] = ("Select Year", "2021-22","2022-23", "2023-24", "2024-25", "2025-26")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=2, pady=10, sticky=W)

        # Semester
        semester_lable = Label(current_course,text="Semester", font=("times new roman", 12, "bold"), bg="white")
        semester_lable.grid(row=1, column=2, padx=10, sticky=W)

        semester_combo = ttk.Combobox(current_course,textvariable=self.var_semester,font=("times new roman", 12, "bold"), state="readonly")
        semester_combo["values"] = ("Select Semester", "frist", "Second", "Third", "Fourth", "Fifth", "Sixth")
        semester_combo.current(0)
        semester_combo.grid(row=1, column=3, padx=2, pady=10, sticky=W)

        # Class Student Information
        class_Student_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE,text="Class Student Info", font=("times new roman", 12, "bold"))
        class_Student_frame.place(x=14, y=285, width=720, height=300)

        # Student ID
        StudentID_label = Label(class_Student_frame, text="StudentID:", font=("times new roman", 13, "bold"), bg="white")
        StudentID_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        StudentID_entry = ttk.Entry(class_Student_frame,textvariable=self.var_std_id, width=20, font=("times new roman", 12, "bold"))
        StudentID_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        # Student Name
        StudentName_label = Label(class_Student_frame, text="Student Name:", font=("times new roman", 13, "bold"), bg="white")
        StudentName_label.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        StudentName_entry = ttk.Entry(class_Student_frame,textvariable=self.var_std_name, width=20, font=("times new roman", 12, "bold"))
        StudentName_entry.grid(row=0, column=3, padx=10, pady=5, sticky=W)

        # Student DIVISION
        class_div_label = Label(class_Student_frame, text="Class Division:", font=("times new roman", 13, "bold"), bg="white")
        class_div_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)

        
        div_combo = ttk.Combobox(class_Student_frame,textvariable=self.var_div,font=("times new roman", 10, "bold"), state="readonly")
        div_combo["values"] = ("Select Division","A", "B","C")
        div_combo.current(0)
        div_combo.grid(row=1, column=1, padx=10, pady=5, sticky=W)


        # ROLL NO
        Roll_No_label = Label(class_Student_frame, text="Roll No:", font=("times new roman", 13, "bold"), bg="white")
        Roll_No_label.grid(row=1, column=2, padx=10, pady=5, sticky=W)

        Roll_No_entry = ttk.Entry(class_Student_frame,textvariable=self.var_roll, width=20, font=("times new roman", 12, "bold"))
        Roll_No_entry.grid(row=1, column=3, padx=10, pady=5, sticky=W)

        # Email_id
        Email_id_label = Label(class_Student_frame, text="Email ID:", font=("times new roman", 13, "bold"), bg="white")
        Email_id_label.grid(row=3, column=0, padx=10, pady=5, sticky=W)

        Email_id_entry = ttk.Entry(class_Student_frame,textvariable=self.var_email, width=20, font=("times new roman", 12, "bold"))
        Email_id_entry.grid(row=3, column=1, padx=10, pady=5, sticky=W)

        # GENDER
        Gender_label = Label(class_Student_frame, text="Gender:", font=("times new roman", 13, "bold"), bg="white")
        Gender_label.grid(row=2, column=0, padx=10, pady=5, sticky=W)

        
        gender_combo = ttk.Combobox(class_Student_frame,textvariable=self.var_gender,font=("times new roman", 10, "bold"), state="readonly")
        gender_combo["values"]=("Select Gender","Male","Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=2, column=1, padx=10, pady=10, sticky=W)

        # DOB
        dob_label = Label(class_Student_frame, text="Date Of Birth:", font=("times new roman", 13, "bold"), bg="white")
        dob_label.grid(row=2, column=2, padx=10, pady=5, sticky=W)

        dob_entry = ttk.Entry(class_Student_frame,textvariable=self.var_dob, width=20,font=("times new roman", 12, "bold"))
        dob_entry.grid(row=2, column=3, padx=10, pady=5, sticky=W)

        # Phone NO
        phone_label = Label(class_Student_frame, text="Phone No:", font=("times new roman", 13, "bold"), bg="white")
        phone_label.grid(row=3, column=2, padx=10, pady=5, sticky=W)

        phone_entry = ttk.Entry(class_Student_frame,textvariable=self.var_phone, width=20, font=("times new roman", 12, "bold"))
        phone_entry.grid(row=3, column=3, padx=10, pady=5, sticky=W)

        # Address
        address_label = Label(class_Student_frame, text="Address:", font=("times new roman", 13, "bold"), bg="white")
        address_label.grid(row=4, column=0, padx=10, pady=5, sticky=W)

        address_entry = ttk.Entry(class_Student_frame,textvariable=self.var_address, width=20, font=("times new roman", 12, "bold"))
        address_entry.grid(row=4, column=1, padx=10, pady=5, sticky=W)

        # Teacher Name
        teacher_label = Label(class_Student_frame, text="Teacher Name:", font=("times new roman", 13, "bold"), bg="white")
        teacher_label.grid(row=4, column=2, padx=10, pady=5, sticky=W)

        teacher_entry = ttk.Entry(class_Student_frame,textvariable=self.var_teacher, width=20, font=("times new roman", 12, "bold"))
        teacher_entry.grid(row=4, column=3, padx=10, pady=5, sticky=W)

        # radio Button
        self.var_radio1=StringVar()
        radionbtn1 = ttk.Radiobutton(class_Student_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        radionbtn1.grid(row=6, column=0)

        
        radionbtn2 = ttk.Radiobutton(class_Student_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
        radionbtn2.grid(row=6, column=1)

        # bbutton frame
        btn_frame = Frame(class_Student_frame, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=200, width=715, height=35)

        save_btn = Button(btn_frame, text="Save",command=self.add_data, width=17, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        save_btn.grid(row=0, column=0)

        update_btn = Button(btn_frame, text="Update",command=self.update_data, width=17, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        update_btn.grid(row=0, column=1)

        delete_btn = Button(btn_frame, text="Delete",command=self.delete_data, width=17, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        delete_btn.grid(row=0, column=2)

        reset_btn = Button(btn_frame, text="Reset",command=self.reset_data,width=17, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        reset_btn.grid(row=0, column=3)

        btn_frame1 = Frame(class_Student_frame, bd=2, relief=RIDGE)
        btn_frame1.place(x=0, y=235, width=715, height=35)

        take_photo_btn = Button(btn_frame1, text="Take Photo Sample",command=self.generate_dataset, width=35, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        take_photo_btn.grid(row=0, column=0)

        update_photo_btn = Button(btn_frame1, text="Update Photo Sample", width=35, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        update_photo_btn.grid(row=0, column=1)

        # Right LABLE FRAME
        right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE,text="student Details", font=("times new roman", 12, "bold"))
        right_frame.place(x=750, y=10, width=730, height=580)

        img_R = Image.open(r"Images\BG2.jfif")
        img_R = img_R.resize((720, 130), Image.ANTIALIAS)
        self.photoimg_R = ImageTk.PhotoImage(img_R)

        b1 = Button(right_frame, image=self.photoimg_R, cursor="hand2")
        b1.place(x=5, y=0, width=715, height=130)

        # **************************Search System**********************

        Search_frame = LabelFrame(right_frame, bd=2, bg="white", relief=RIDGE,text="Search Systems", font=("times new roman", 12, "bold"))
        Search_frame.place(x=5, y=135, width=715, height=70)

        search_label = Label(Search_frame, text="Search By:", font=("times new roman", 15, "bold"), bg="red", fg="white")
        search_label.grid(row=0, column=0, padx=5, pady=10, sticky=W)

        search_combo = ttk.Combobox(Search_frame, font=("times new roman", 12, "bold"), state="readonly")
        search_combo["values"] = ("Select ", "Roll_No", "Phone_No")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        search_entry = ttk.Entry(Search_frame, width=12, font=("times new roman", 12, "bold"))
        search_entry.grid(row=0, column=2, padx=10, pady=5)

        search_btn = Button(Search_frame, text="Search", width=14, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        search_btn.grid(row=0, column=3, padx=4)

        showAll_btn = Button(Search_frame, text="Show All", width=12, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        showAll_btn.grid(row=0, column=4, padx=4)

        # ****************************TABLE FRAME***************************************

        table_frame = Frame(right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=5, y=210, width=715, height=350)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame, columns=("dep","course","year","sem","id","name","div","roll","gender","dob","email","phone", "address", "teacher", "photo"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_x.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="StudentID")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("roll",text="RollNo")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="Photos")
        self.student_table["show"]="headings"
       
       
        
        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=100)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
        
        #*****************************Function Decleration********************************
    
    
    def add_data(self):
         if self.var_dep.get() == 'Select Department' or self.var_std_name.get() =="" or self.var_std_id.get() =="":
             messagebox.showerror("Error", "All Fields required", parent=self.root)
         else:
            try:
                 conn = mysql.connector.connect(host="localhost",
                                                user="root", 
                                                password="W@2915djkq#",
                                                database="face_recognition")
                 my_cursor = conn.cursor()
                 my_cursor.execute("INSERT INTO student value(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                                                self.var_dep.get(),
                                                self.var_course.get(),
                                                self.var_year.get(),
                                                self.var_semester.get(),
                                                self.var_std_id.get(),
                                                self.var_std_name.get(),
                                                self.var_div.get(),
                                                self.var_roll.get(),
                                                self.var_gender.get(),
                                                self.var_dob.get(),
                                                self.var_email.get(),
                                                self.var_phone.get(),
                                                self.var_address.get(),
                                                self.var_teacher.get(),
                                                self.var_radio1.get()
                                        )) 
                 conn.commit()
                 self.fetch_data()
                 conn.close()
                 messagebox.showinfo("Success", "Student Detail has been added successfully", parent=self.root)
            except Exception as es:
               messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root) 
               
               
               
    def fetch_data(self):
                conn = mysql.connector.connect(host="localhost",user="root",password="W@2915djkq#",database="face_recognition")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from student ")
                data = my_cursor.fetchall()
                if len(data) != 0:
                      self.student_table.delete(*self.student_table.get_children())
                      for i in data:
                           self.student_table.insert("",END,values=i)
                      conn.commit()
                conn.close()

    
    def get_cursor(self, event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content['values']
    
        self.var_dep.set(data[0])
        self.var_course.set(data[1])
        self.var_year.set(data[2])
        self.var_semester.set(data[3])
        self.var_std_id.set(data[4])
        self.var_std_name.set(data[5])
        self.var_div.set(data[6])
        self.var_roll.set(data[7])
        self.var_gender.set(data[8])
        self.var_dob.set(data[9])
        self.var_email.set(data[10])
        self.var_phone.set(data[11])
        self.var_address.set(data[12])
        self.var_teacher.set(data[13])
        self.var_radio1.set(data[14])


   ####Update#############
   
    
    def update_data(self):
          if self.var_dep.get() == 'Select Department' or self.var_std_name.get() == '' or self.var_std_id.get() == '':
              messagebox.showerror("Error","All Fields required",parent=self.root)
          else:
           try:
                Update = messagebox.askyesno("Update","Do you want to update this student detail",parent=self.root) 
                if Update >0 :
                    conn = mysql.connector.connect(host="localhost",user="root",password="W@2915djkq#",database="face_recognition")
                    my_cursor = conn.cursor()
                    my_cursor.execute("update student set Dep=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email= %s, Phone = %s, Address = %s,Teacher = %s,PhontoSample = %s where Student_id =%s ",(
                          self.var_dep.get(),
                          self.var_course.get(),
                          self.var_year.get(),
                          self.var_semester.get(),
                          self.var_std_name.get(),
                          self.var_div.get(),
                          self.var_roll.get(),
                          self.var_gender.get(),
                          self.var_dob.get(),
                          self.var_email.get(),
                          self.var_phone.get(),
                          self.var_address.get(),
                          self.var_teacher.get(),
                          self.var_radio1.get(),
                          self.var_std_id.get()
                    ))
               
                else:
                 if not Update:
                      return  
                messagebox.showinfo("Success","Student Detail successfully update",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
           except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root) 
 
        
    def delete_data(self):
         if self.var_std_id.get() == "":
              messagebox.showerror("Error","Student is must be required",parent=self.root)
         else:
              try:
                   delete = messagebox.askyesno("Student Delete Page", "Do you want to delete this student",parent=self.root)
                   if delete >0:
                        conn = mysql.connector.connect(host="localhost",user="root",password="W@2915djkq#",database="face_recognition")
                        my_cursor = conn.cursor()
                        sql="delete from student where student_id=%s"
                        val=(self.var_std_id.get(),)
                        my_cursor.execute(sql,val)
                   else:
                       if not delete:
                        return
                   conn.commit()
                   self.fetch_data()
                   conn.close()
                   messagebox.showinfo("Delete","Student deleted successfully",parent=self.root)
              except Exception as es:
                   messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root) 


    def reset_data(self):
        self.var_dep.set("Select Department"),
        self.var_course.set("Select Course"),
        self.var_year.set("Select Semester"),
        self.var_semester.set(""),
        self.var_std_id.set(""),
        self.var_std_name.set(""),
        self.var_div.set(""),
        self.var_roll.set(""),
        self.var_gender.set(""),
        self.var_dob.set(""),
        self.var_email.set(""),
        self.var_phone.set(""),
        self.var_address.set(""),
        self.var_teacher.set(""),
        self.var_radio1.set("")
        self.var_std_id.set("")
    
    
    #***********GeNARATE DATABASE*****************************
              
    def generate_dataset(self):
          if self.var_dep.get() == 'Select Department' or self.var_std_name.get() == '' or self.var_std_id.get() == '':
              messagebox.showerror("Error","All Fields required",parent=self.root)
          else:
              try:
                    conn = mysql.connector.connect(host="localhost",user="root",password="W@2915djkq#",database="face_recognition")
                    my_cursor = conn.cursor()
                    my_cursor.execute("select * from student ")
                    myresult= my_cursor.fetchall()
                    id=0
                    for i in myresult:
                        id +=1
                    my_cursor.execute("update student set Dep=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email= %s, Phone = %s, Address = %s,Teacher = %s,PhontoSample = %s where Student_id =%s ",(
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_std_name.get(),
                        self.var_div.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_teacher.get(),
                        self.var_radio1.get(),
                        self.var_std_id.get()==id+1
                        ))
                    conn.commit()
                    self.fetch_data()
                    self.reset_data()
                    conn.close() 
              
                    
     
                    
                     ################# Load predifined data on face frontals from opencv

                    face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                    def face_cropped(img):
                        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                        faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                        # scaling factor = 1.3
                        # minimum neighbor = 5
                    
                        for (x, y, w, h) in faces:
                            face_cropped = img[y:y + h, x:x + w]
                            return face_cropped
                    
                    cap = cv2.VideoCapture(1)
                    img_id = 0
                    while True:
                        ret, my_frame = cap.read()
                        if face_cropped(my_frame) is not None:
                            img_id += 1
                            face = cv2.resize(face_cropped(my_frame), (450, 450))
                            face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                            file_name_path = "data/user." + str(id) + "." + str(img_id) + ".jpg"
                            cv2.imwrite(file_name_path, face)
                            cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                            cv2.imshow("Cropped Face", face)
                    
                        if cv2.waitKey(1) == 13 or int(img_id) == 100:
                            break
                    
                    cap.release()
                    cv2.destroyAllWindows()
                    messagebox.showinfo("Result", "Generating dataset completed")
 
              except Exception as es:
                   messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root) 

                    
if __name__ == "__main__" :
   root=Tk()
   obj=Student(root)
   root.mainloop()