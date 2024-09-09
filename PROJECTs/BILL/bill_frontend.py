from tkinter import*
class Bill_App: 
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")#("widthxheight+x+y")x&y is position--
        self.root.title("Billing Software")
        bg_color="blue"
        title=Label(self.root,text="Invoice",bd=12,relief=GROOVE,bg=bg_color,fg="white",font=("times new roman",30,"bold"),pady=3).pack(fill=X)
        
        #========Customber details Frame=========#
        
        F1=LabelFrame(self.root,text="Customber Details",bg=bg_color,fg="gold",font=("times new roman",15,"bold"),bd=10,relief=GROOVE,padx=0)

        F1.place(x=0,y=80,relwidth=1)
        
        cname_lbl=Label(F1,text="Customber Name",font=("times new roman",20,"bold"),fg="white",bg=bg_color).grid(row=0,column=0,padx=20,pady=5)
       
        cname_txt=Entry(F1,width=15,font="arial 15",bd=7,relief=SUNKEN,textvariable=self).grid(row=0,column=1,pady=5,padx=10)
            
        cmob_lbl=Label(F1,text="Mobile No.",font=("times new roman",20,"bold"),fg="white",bg=bg_color).grid(row=0,column=2,padx=20,pady=5)
       
        cmob_txt=Entry(F1,width=15,font="arial 15",bd=7,relief=SUNKEN,textvariable=self).grid(row=0,column=3,pady=5,padx=10)
        
        cbill_lbl=Label(F1,text="Bill No.",font=("times new roman",20,"bold"),fg="white",bg=bg_color).grid(row=0,column=4,padx=20,pady=5)
       
        cbill_txt=Entry(F1,width=15,font="arial 15",bd=7,relief=SUNKEN,textvariable=self).grid(row=0,column=5,pady=5,padx=10)
        
        bill_btn=Button(F1,text="Search",width=10,bd=7,relief=GROOVE,font="arial 15 bold").grid(row=0,column=6,pady=10,padx=10)
#=========Cosmetics========

        F2=LabelFrame(self.root,bd=10,relief=GROOVE,text="Cosmetic:",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F2.place(x=5,y=195,height=375,width=325)
        
        #Bath Soap
        bath_lbl=Label(F2,text="Bath Soap",font=("times new roman",16,"bold"),bg=bg_color,fg="aqua",).grid(row=0,column=0,pady=10,padx=10,sticky="w")
        bath_qua=Entry(F2,width=10,font=("times new roman",16,"bold"),bd=10,relief=SUNKEN).grid(row=0,column=1,padx=5,pady=5)
        
        #Face Cream
        
        face_cream_lbl=Label(F2,text="Face Cream",font=("times new roman",16,"bold"),bg=bg_color,fg="aqua",).grid(row=1,column=0,pady=10,padx=10,sticky="w")
        bface_cream_qua=Entry(F2,width=10,font=("times new roman",16,"bold"),bd=10,relief=SUNKEN).grid(row=1,column=1,padx=5,pady=5)
        
        #Face Wash
        
        face_Wash_lbl=Label(F2,text="Face Wash",font=("times new roman",16,"bold"),bg=bg_color,fg="aqua",).grid(row=2,column=0,pady=10,padx=10,sticky="w")
        face_Wash_qua=Entry(F2,width=10,font=("times new roman",16,"bold"),bd=10,relief=SUNKEN).grid(row=2,column=1,padx=5,pady=5)
        
        #Hair Oil
        
        hair_oil_lbl=Label(F2,text="Hair Oil",font=("times new roman",16,"bold"),bg=bg_color,fg="aqua",).grid(row=3,column=0,pady=10,padx=10,sticky="w")
        hair_oil_qua=Entry(F2,width=10,font=("times new roman",16,"bold"),bd=10,relief=SUNKEN).grid(row=3,column=1,padx=5,pady=5)
        
        #Body Lotion
        
        body_lotion_lbl=Label(F2,text="Body Lotion",font=("times new roman",16,"bold"),bg=bg_color,fg="aqua",).grid(row=4,column=0,pady=10,padx=10,sticky="w")
        body_lotion_qua=Entry(F2,width=10,font=("times new roman",16,"bold"),bd=10,relief=SUNKEN).grid(row=4,column=1,padx=5,pady=5)
        
        #Hair Dye
        
        hair_dye_lbl=Label(F2,text="Hair Dye",font=("times new roman",16,"bold"),bg=bg_color,fg="aqua",).grid(row=5,column=0,pady=10,padx=10,sticky="w")
        hair_dye_qua=Entry(F2,width=10,font=("times new roman",16,"bold"),bd=10,relief=SUNKEN).grid(row=5,column=1,padx=5,pady=5)
#=========Cosmetics========

        F3=LabelFrame(self.root,bd=10,relief=GROOVE,text="Grocery:",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F3.place(x=10+325,y=195,height=375,width=325)
        
        #Rice
        rice_lbl=Label(F3,text="Rice",font=("times new roman",16,"bold"),bg=bg_color,fg="aqua",).grid(row=0,column=0,pady=10,padx=10,sticky="w")
        rice_qua=Entry(F3,width=10,font=("times new roman",16,"bold"),bd=10,relief=SUNKEN).grid(row=0,column=1,padx=5,pady=5)
        
        #Food Oil
        
        food_oil_lbl=Label(F3,text="Food Oil",font=("times new roman",16,"bold"),bg=bg_color,fg="aqua",).grid(row=1,column=0,pady=10,padx=10,sticky="w")
        food_oil_qua=Entry(F3,width=10,font=("times new roman",16,"bold"),bd=10,relief=SUNKEN).grid(row=1,column=1,padx=5,pady=5)
        
        #Pulses
        
        pluses_lbl=Label(F3,text="Pulses",font=("times new roman",16,"bold"),bg=bg_color,fg="aqua",).grid(row=2,column=0,pady=10,padx=10,sticky="w")
        pluses_qua=Entry(F3,width=10,font=("times new roman",16,"bold"),bd=10,relief=SUNKEN).grid(row=2,column=1,padx=5,pady=5)
        
        #Wheat
        
        wheat_lbl=Label(F3,text="Wheat",font=("times new roman",16,"bold"),bg=bg_color,fg="aqua",).grid(row=3,column=0,pady=10,padx=10,sticky="w")
        wheat_qua=Entry(F3,width=10,font=("times new roman",16,"bold"),bd=10,relief=SUNKEN).grid(row=3,column=1,padx=5,pady=5)
        
        #Sugar
        
        sugar_lbl=Label(F3,text="Sugar",font=("times new roman",16,"bold"),bg=bg_color,fg="aqua",).grid(row=4,column=0,pady=10,padx=10,sticky="w")
        sugar_qua=Entry(F3,width=10,font=("times new roman",16,"bold"),bd=10,relief=SUNKEN).grid(row=4,column=1,padx=5,pady=5)
        
        #Tea
        
        tea_lbl=Label(F3,text="Tea",font=("times new roman",16,"bold"),bg=bg_color,fg="aqua",).grid(row=5,column=0,pady=10,padx=10,sticky="w")
        tea_qua=Entry(F3,width=10,font=("times new roman",16,"bold"),bd=10,relief=SUNKEN).grid(row=5,column=1,padx=5,pady=5)
#=========Cold Drinks========

        F4=LabelFrame(self.root,bd=10,relief=GROOVE,text="Cold Drinks:",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F4.place(x=665,y=195,height=375,width=325)
        
        #Mazza
        mazza_lbl=Label(F4,text="Mazza",font=("times new roman",16,"bold"),bg=bg_color,fg="aqua",).grid(row=0,column=0,pady=10,padx=10,sticky="w")
        mazza_qua=Entry(F4,width=10,font=("times new roman",16,"bold"),bd=10,relief=SUNKEN).grid(row=0,column=1,padx=5,pady=5)
        
        #Coke
        
        coke_cream_lbl=Label(F4,text="Coke",font=("times new roman",16,"bold"),bg=bg_color,fg="aqua",).grid(row=1,column=0,pady=10,padx=10,sticky="w")
        coke_cream_qua=Entry(F4,width=10,font=("times new roman",16,"bold"),bd=10,relief=SUNKEN).grid(row=1,column=1,padx=5,pady=5)
        
        #Frooti
        
        frooti_lbl=Label(F4,text="Frooti",font=("times new roman",16,"bold"),bg=bg_color,fg="aqua",).grid(row=2,column=0,pady=10,padx=10,sticky="w")
        frooti_qua=Entry(F4,width=10,font=("times new roman",16,"bold"),bd=10,relief=SUNKEN).grid(row=2,column=1,padx=5,pady=5)
        
        #Thumbs Up
        
        thumbsup_lbl=Label(F4,text="Thumbs Up",font=("times new roman",16,"bold"),bg=bg_color,fg="aqua",).grid(row=3,column=0,pady=10,padx=10,sticky="w")
        thumbsup_qua=Entry(F4,width=10,font=("times new roman",16,"bold"),bd=10,relief=SUNKEN).grid(row=3,column=1,padx=5,pady=5)
        
        #Limca
        
        limca_lbl=Label(F4,text="Limca",font=("times new roman",16,"bold"),bg=bg_color,fg="aqua",).grid(row=4,column=0,pady=10,padx=10,sticky="w")
        limca_qua=Entry(F4,width=10,font=("times new roman",16,"bold"),bd=10,relief=SUNKEN).grid(row=4,column=1,padx=5,pady=5)
        
        #Sprite
        
        sprite_lbl=Label(F4,text="Sprite",font=("times new roman",16,"bold"),bg=bg_color,fg="aqua",).grid(row=5,column=0,pady=10,padx=10,sticky="w")
        sprite_qua=Entry(F4,width=10,font=("times new roman",16,"bold"),bd=10,relief=SUNKEN).grid(row=5,column=1,padx=5,pady=5)
         
        #Bill Area 
        F5=Frame(self.root,bd=10,relief=GROOVE)
        F5.place(x=1000,y=195,width=350,height=375)
        
        bill_title=Label(F5,text="Billing Area",font="arial 16 bold",bd=5,relief=GROOVE).pack(fill=X)
        
        scrol_y=Scrollbar(F5,orient=VERTICAL)
        self.txtarea=Text(F5,yscrollcommand=scrol_y.set)
        scrol_y.pack(side="right",fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill="both",expand=1)
         
        #Button Area
        F6 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Bill Menu ", font=("times new roman", 15, "bold"),fg="gold", bg=bg_color)
        F6.place(x=0,y=510)
        
        
         
root=Tk()
obj = Bill_App(root)
root.mainloop()