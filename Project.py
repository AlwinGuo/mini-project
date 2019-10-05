from tkinter import *
from Functions import *

root = Tk()
root.geometry("600x400")
root.resizable(False,False)
Main_page = Frame(root)
Main_page.place(relheight=1,relwidth=1)

main = PhotoImage(file="main.png")
label = Label(Main_page,image=main)
label.place(x=0,y=0)

def todays_menu():
    Main_page.destroy()
    todays_menu = Frame(root)
    todays_menu.place(relwidth=1,relheight=1)
    label = Label(todays_menu, text = "Stores")
    label.place(rely=0.1)
    

label_title = Label(Main_page, text = "NTU Canteen Menu System",font=('Courier','30'))
label_title.place(relx=0.02,rely=0.02, relheight = 0.1, relwidth =0.97)


Button_today = Button(Main_page, text="Today's Menu", command = todays_menu)
Button_today.place(relx=0.1,rely=0.4, relheight = 0.1, relwidth =0.8)

#Button for other dates
Button_other_dates = Button(Main_page, text="View stores by other dates")
Button_other_dates.place(relx=0.1,rely=0.6, relheight = 0.1, relwidth =0.8)

exit_button = Button(Main_page, text="Exit")
exit_button.place(relx=0.1,rely=0.8, relheight = 0.1, relwidth =0.8)

root.mainloop()



