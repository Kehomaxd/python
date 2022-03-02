from  tkinter import *
import time

#Hour
def times():
	current_time=time.strftime("%H:%M:%S") 
	clock.config(text=current_time,bg="white",fg="black",font="Arial 50 bold")
	clock.after(200,times)
	
#Window
root=Tk()
root.geometry("500x180")
root.title("Reloj digital con Tkinter")
clock=Label(root,font=("times",50,"bold"))

clock.grid(row=2,column=1,pady=25,padx=100)
times()

root.mainloop()