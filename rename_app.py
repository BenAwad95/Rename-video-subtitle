
from tkinter import *
from tkinter import filedialog
import glob
import os

def select_folder():
	filename = filedialog.askdirectory()
	e4.delete(0,END)
	e4.insert(END,filename)




def show_files():
	e3.delete(0,END)
	folder_path = folder_path_variable.get().strip()
	video_extension = video_extension_varible.get()
	subtitle_extension = subtitle_extension_varible.get()
	for v,s in zip(glob.glob1(folder_path, f"*.{video_extension}"), glob.glob1(folder_path, f"*.{subtitle_extension}")):
		e3.insert(END,v)
		e3.insert(END,s)
	l3 = Label(app,text="If the Videos files goes correct with the subs order, prss Rename to make the changes")
	l3.grid(row=5,column=3)
	b4 = Button(app,text="Rename",command=rename)
	b4.grid(row=6,column=3)

def rename():
	folder_path = folder_path_variable.get()
	video_extension = video_extension_varible.get()
	subtitle_extension = subtitle_extension_varible.get()
	for v,s in zip(glob.glob1(folder_path, f"*.{video_extension}"), glob.glob1(folder_path, f"*.{subtitle_extension}")):
		print(v)
		new_name = v.replace(video_extension,subtitle_extension)
		os.rename(f"{folder_path}/{s}",f"{folder_path}/{new_name}")


app = Tk()





app.minsize(700,300)
app.wm_title("Rename files")
l1 = Label(app,text="Video extension")
l1.grid(row=1,column=1)
video_extension_varible = StringVar()
e1 = Entry(app,textvariable=video_extension_varible)
e1.grid(row=1,column=2,pady=10)

l2 = Label(app,text="Sub extension")
l2.grid(row=2,column=1,pady=10)
subtitle_extension_varible = StringVar()
e2 = Entry(app,textvariable=subtitle_extension_varible)
e2.grid(row=2,column=2)

b3 = Button(app,text="Selsct folder",command=select_folder)
b3.grid(row=3,column=1,pady=10)


folder_path_variable = StringVar()
e4 = Entry(app,textvariable=folder_path_variable)
e4.grid(row=3,column=2,ipadx=50)
e3 = Listbox(app)
e3.grid(row=1,column=3,rowspan=4,padx=20,ipadx=150,pady=10)

e3.bind('<<ListboxSelect>>')
       
scro = Scrollbar(app)
scro.grid(row=1,column=4,rowspan=4,columnspan=2)
e3.configure(yscrollcommand = scro.set)
scro.configure(command=e3.yview)


b1 = Button(app,text="Show Files",command=show_files)
b1.grid(row=4,column=1)

b2 = Button(app,text="Exit",command=app.destroy)
b2.grid(row=4,column=2,ipadx=20)


app.mainloop()