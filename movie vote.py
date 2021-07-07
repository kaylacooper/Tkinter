from tkinter import *
from tkinter import messagebox

def votebutton():
    totalvotes= cb1.get()+cb2.get()+cb3.get()+cb4.get()
    if totalvotes == 1:
        messagebox.showinfo("Voting message", \
            "Thank you for voting for a movie!")
        main_window.destroy()
    else:
        messagebox.showerror("Voting message", \
            "You voted for " +str(totalvotes) +
                             "\nPlease vote for one movie!")
   
main_window = Tk()
main_window.title('Main window')
main_window.geometry("400x200+200+100")

title = Label(main_window,text="Movie Voting Form",\
  font=("Helvetica", 16),justify=CENTER).grid(row=0,columnspan=3)
directions = Label(main_window,\
  text="Please vote for one " \
          +"of the following movies",\
       font=("Helvetica", 14),fg="pink"). \
          grid(row=1,columnspan=2)

cb1 = IntVar()
cb2 = IntVar()
cb3 = IntVar()
cb4 = IntVar()



button1=Checkbutton(main_window,text="Legally Blonde", variable=cb1,\
              font=("Helvetica", 14)).grid(row=2, column=0)
button2=Checkbutton(main_window,text="Avengers: End Game", variable=cb2,\
              font=("Helvetica", 14)).grid(row=3, column=0)
button3=Checkbutton(main_window,text="Gone Girl", variable=cb3,\
              font=("Helvetica", 14)).grid(row=2, column=1)
button4=Checkbutton(main_window,text="Molly's Game", variable=cb4,\
              font=("Helvetica", 14)).grid(row=3, column=1)


cancelbutton=Button(main_window,text="Cancel",\
                command=main_window.destroy,width=10,height=2)\
                .grid(row=2,column=2)
submit=Button(main_window,\
                text="Submit",command = votebutton,width=10,height=2)\
                .grid(row=4,column=2)

main_window.mainloop()
