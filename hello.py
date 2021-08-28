import tkinter as tk
from face1 import fuck
root=tk.Tk()
root.title("face-detection")
root.geometry("500x400")
root.configure(bg="black")
root.resizable(False,False)

label2=tk.Label(text="Welcome to Face-Detection !",bg="black",foreground="green",font=("Arial",25))
label2.pack()
label1=tk.Label(text="For exit press 'a' ",bg="black",foreground="green",font=("Arial",25))
label1.pack()
def lab():
    label=tk.Label(text="hi")
    label.pack()
def close():
    root.destroy()
bttn_frame=tk.Frame(root,background="black",highlightbackground="red",highlightthickness=1,bd=2)
image=tk.PhotoImage(file="start2.png")

button=tk.Button(bttn_frame,image=image ,command=fuck)
button.pack(padx=20,pady=30)

button1=tk.Button(bttn_frame,text="Close",bg="#034B03",foreground="#90EE90",font=("Arial",20),command=close)
button1.pack(padx=40,pady=100)
bttn_frame.pack()
label2=tk.Label(text="Note: here you will use the face-detection app and press a when face-detection window is opened",foreground="green",bg="black",font=("Arial",20))
label2.pack()
root.wm_attributes('-fullscreen','True')#for full screen 
root.mainloop()
