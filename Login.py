from tkinter import *
from tkinter import messagebox
from bcrypt import checkpw, gensalt, hashpw
import mysql.connector

background = "#06283D"
framebg = "#EDEDED"
framefg = "#06283D"

window = Tk()
window.title("Login System")
window.config(bg=background)
window.geometry("700x550+210+100")
icon = PhotoImage(file="icons/upload3.png")
window.iconphoto(False, icon)
# window.resizable(False, False)

######################### All Functions Apply in Login System ####################
trial_no = 0


def trial():
    global trial_no

    trial_no += 1
    if trial_no == 3:
        messagebox.showwarning("Warning", "You have tried more than limit!!")
        window.destroy()


def login():
    username = usernameEntry.get()
    password = password_entry.get()

    if (username == '' or username == 'UserID') or (password == '' or password == 'password'):
        messagebox.showerror("Entry error", "Please enter Username or password!")
    else:
        try:
            conn = mysql.connector.connect(host='localhost',
                                           user='root',
                                           database='SRS_Login',
                                           password='nupakilawaki5207')

            mycursor = conn.cursor()
            print("Connected to database")

        except:
            messagebox.showerror("Error", "Database connection not establish!!")
            return

        query = "use SRS_Login"
        mycursor.execute(query)
        query = "SELECT * FROM login WHERE username = %s and password = %s"
        mycursor.execute(query, (username, password))
        result = mycursor.fetchone()
        print(result)

        if result == None:
            messagebox.showinfo("Invalid", "Invalid Username or password!")
            trial()
        else:
            messagebox.showinfo("Login", "Successfully login!!")
            window.destroy()
            import studentregistrationsystem2




######################### Sign Up ###################################
def signup():
    window.destroy()
    import Signup


###########  Create Frame
LoginFrame = LabelFrame(window, bg="#0095B6", bd=2, width=420, height=400, relief=GROOVE)
LoginFrame.place(x=140, y=80)

Label(LoginFrame, text="LOGIN", font=("Colonna MT", 28, 'bold'), bg='#0095B6',
      fg=framefg).place(x=135, y=10)

Label(LoginFrame, text="Username:", font=('Times New Roman', 15, 'bold'), bg='#0095B6',
      fg="#FFFDD0").place(x=50, y=70)

Label(LoginFrame, text="Password:", font=('Times New Roman', 15, 'bold'), bg='#0095B6',
      fg="#FFFDD0").place(x=50, y=150)


############### User entry ########################
def user_enter(e):
    usernameEntry.delete(0, 'end')


def user_leave(e):
    name = usernameEntry.get()
    if name == "":
        usernameEntry.insert(0, 'Username')


usernameEntry = Entry(LoginFrame, width=20, bd=2, font='arial 14')
usernameEntry.insert(0, "enter username")
usernameEntry.bind("<FocusIn>", user_enter)
usernameEntry.bind("<FocusOut>", user_leave)
usernameEntry.place(x=150, y=75)


####################### Password entry ####################################
def password_enter(e):
    password_entry.delete(0, 'end')


def password_leave(e):
    if password_entry.get() == "":
        password_entry.insert(0, 'password')


password_entry = Entry(LoginFrame, width=20, bd=2, font='arial 14')
password_entry.insert(0, "enter password")
password_entry.bind("<FocusIn>", password_enter)
password_entry.bind("<FocusOut>", password_leave)
password_entry.place(x=150, y=150)

###################  Hide eye and show button ############################
button_mode = True


def hide():
    global button_mode

    if button_mode:
        eyeButton.config(image=closeeye, activebackground='white')
        password_entry.config(show='*')
        button_mode = False
    else:
        eyeButton.config(image=openeye, activebackground='white')
        password_entry.config(show='')
        button_mode = True


openeye = PhotoImage(file="icons/openeye.png")
closeeye = PhotoImage(file="icons/closeeye.png")
eyeButton = Button(LoginFrame, image=openeye, border=0, bg='white', command=hide)
eyeButton.place(x=352, y=152)

loginButton = Button(LoginFrame, text="Login", font=('Times New Roman', 15, 'bold'), bg='#0095B6',
                     fg="#FFFDD0", width=8, activebackground='#0095B6', activeforeground=framefg, command=login)
loginButton.place(x=150, y=200)

Label(LoginFrame, text="Don't have an account?", font=('Times New Roman', 13, 'bold'),
      bg='#0095B6', fg="#FFFDD0").place(x=50, y=250)

signUpButton = Button(LoginFrame, text="Sign Up", font=('Times New Roman', 13, 'bold'), border=0,
                      bg='#0095B6', fg=framefg, activeforeground="#FFFDD0", activebackground='#0095B6', relief=FLAT,
                      command=signup)
signUpButton.place(x=220, y=248)

window.mainloop()
