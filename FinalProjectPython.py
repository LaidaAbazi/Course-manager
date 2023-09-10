import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.ttk import Combobox
import csv
from tkinter import filedialog


class Courses:
    def __init__(self,root):
        self.data = []
        FilePathLbl=Label(root,width=15)
        FilePathLbl.config(text="Provide data path",bg="white")
        FilePathLbl.grid(row=0,column=0,padx=(5,10),pady=(20,0))

        self.PathEntry=Entry(root)
        self.PathEntry.grid(row=0, column=1, padx=(0,0),pady=(20,0),columnspan=2, sticky=W + E)

        YearLbl=Label(root,width=15)
        YearLbl.config(text="Year",bg="white")
        YearLbl.grid(row=1,column=0,padx=(5,10),pady=(20,0),sticky=W+E)

        self.n=tk.StringVar()
        self.YearBox=ttk.Combobox(root,width=5,textvariable=self.n)
        self.YearBox['values']=('1','2','3','4','5')
        self.YearBox.grid(column=1,row=1,padx=(5,10),pady=(20,0),sticky=W + E)
        self.YearBox.current()

        DepLbl=Label(root)
        DepLbl.config(text="Department",bg="white")
        DepLbl.grid(row=1,column=3,padx=(5,10),pady=(20,0),sticky=W+E)

        self.d = tk.StringVar()
        self.DepBox = ttk.Combobox(root, width=5, textvariable=self.d)
        self.DepBox['values'] = ('CS', 'ECE', 'ECON', 'EECS', 'ENGR','FRE','GER','IE','ISE','LIFE','MATH','MGT','UNI')
        self.DepBox.grid(column=4, row=1, padx=(5, 10), pady=(20, 0), sticky=W + E)
        self.DepBox.current()


        DspBtn=Button(root,command=self.enter_file_dir)
        DspBtn.config(text="Display",bg="white")
        DspBtn.grid(column=0, row=2, padx=(0, 10), pady=(50,0), sticky=E)

        ClrBtn=Button(root)
        ClrBtn.config(text="Clear",bg="white",command=self.delete_items)
        ClrBtn.grid(row=2,column=1,padx=(0,10),pady=(50,0),sticky=W+E)

        SaveBtn=Button(root,command=self.enter_file_dir)
        SaveBtn.config(text="Save",bg="White")
        SaveBtn.grid(row=2,column=2,padx=(0,10),pady=(50,0),sticky=W+E)

        def buttonClick(self, event):

            pass

        SlcCoursesLbl=Label(root)
        SlcCoursesLbl.config(text="Selected courses", bg="white")
        SlcCoursesLbl.grid(row=5,column=0,columnspan=5,padx=(10,0),pady=(50,0),ipadx=5,sticky=W)

        self.SlcCoursesLbx=Listbox(root,width=20)
        self.SlcCoursesLbx.grid(row=6,column=0,columnspan=5,padx=(10,0),pady=(15,0),sticky=W)

        CrsLbl=Label(root)
        CrsLbl.config(text="Courses",bg="white")
        CrsLbl.grid(row=5, column=2, columnspan=10, padx=(0, 0), pady=(50, 0), sticky=W+E)

        self.CrsLbx=Listbox(root,width=50)
        self.CrsLbx.grid(row=6,column=2,columnspan=10,padx=(0,0),pady=(15,0),sticky=W+E)
        self.CrsLbx.bind("<<ListboxSelect>>",self.onSelect)


#C:\\Users\\Laida\\Downloads\\sampledata.csv
    def enter_file_dir(self):

        filepath=self.PathEntry.get()
        if self.CrsLbx.size() > 0:
            self.CrsLbx.delete(first=0, last=END)
        with open(filepath,"r",encoding="utf-8",errors="ignore") as file:
            for i in file:
                self.data.clear()
                if self.d.get() == i.split(",")[0].split(" ")[0] and i.split(",")[0].split(" ")[1].startswith(self.n.get()):
                    print(self.data.append(i))
                    self.CrsLbx.insert("end",i)
    def delete_items(self):
        self.CrsLbx.delete(0,END)
        self.SlcCoursesLbx.delete(0,END)

    def onSelect(self,val):
        sender=val.widget
        idx=sender.curselection()
        value=sender.get(idx)
        print(value)
        if self.SlcCoursesLbx.size() > 0:
            if self.SlcCoursesLbx.size() == 6:
                return
            else:
                for i in self.SlcCoursesLbx.get(0, END):
                    print(type(i))
                    a = i.split(",")
                    b = value.split(",")
                    if a[2] == b[2] and a[3] == b[3]:
                        return
                    if a[1] == b[1]:
                        return
                self.SlcCoursesLbx.insert("end", value)

        else:
            self.SlcCoursesLbx.insert("end",value)


x=Tk()
root=Courses(x)
x.resizable(0,0)
x.geometry("520x500+400+200")
x.wm_title(" " * 50+"Project")
x.configure(background='LightSkyBlue4')
x.mainloop()
