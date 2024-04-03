from tkinter import *
from bcrypt import checkpw, gensalt, hashpw
from tkinter import messagebox
import mysql.connector


window = Tk()
background = "#06283D"
framebg = "#EDEDED"
framefg = "#06283D"

window.title("Signup System")
window.geometry("700x600+210+100")
window.config(bg = background)
icon = PhotoImage(file="icons/upload3.png")
window.iconphoto(False, icon)


############################  Function for Sign Up ##################################
def signup():
    username = usernameEntry.get()
    password = passwordEntry.get()

    if (username=="" or username == "Username") or (password=="" or password == "Password"):
        messagebox.showerror("Entry error", "Please fill all entries!")

    else:
        try:
            conn = mysql.connector.connect(host='localhost',
                                           user='root',
                                           database='SRS_Login',
                                           password='nupakilawaki5207')
            mycursor = conn.cursor()
            print("Connected to database")

            mycursor.execute("SELECT * FROM login WHERE username = %s", (username,))
            existing_user = mycursor.fetchone()
            if existing_user:
                messagebox.showerror("Error", "Username already exist!!")


        except:
            messagebox.showerror("Error", "Database connection not establish!!")
            return

        query = "USE SRS_Login"
        mycursor.execute(query)

        query = "INSERT INTO login (username, password) VALUES (%s, %s)"
        mycursor.execute(query, (username, password))

        if username != "" and password != "":
            messagebox.showinfo("Success", "Successfully Signed up!!!")
        else:
            messagebox.showwarning("Warning", "Something went wrong. Please fill the entries!!")
        conn.commit()

def to_login():
    window.destroy()
    import Login


frame = LabelFrame(window, width=450, height=400, bg="#0095B6")
frame.place(x = 130, y = 40)

Label(frame, text="SIGN UP", font=("Colonna MT", 25, 'bold'), bg="#0095B6", fg=framefg).place(x = 150, y = 30)

Label(frame, text="Username:", font=('Times New Roman', 15, 'bold'), bg='#0095B6',
      fg="#FFFDD0").place(x=85, y=120)

Label(frame, text="Password:", font=('Times New Roman', 15, 'bold'), bg='#0095B6',
      fg="#FFFDD0").place(x=90, y=190)


######################  User entry ###############################
def username_enter(e):
    usernameEntry.delete(0, "end")

def username_leave(e):
    username = usernameEntry.get()
    if username == "":
        usernameEntry.insert(0, "Username")

usernameEntry = Entry(frame, width=20, bd=2, bg="#EFDECD", font="Arial 14")
usernameEntry.insert(0, "enter username")
usernameEntry.bind("<FocusIn>", username_enter)
usernameEntry.bind("<FocusOut>", username_leave)
usernameEntry.place(x=190, y=125)


def password_enter(e):
    passwordEntry.delete(0, "end")

def password_leave(e):
    password = passwordEntry.get()
    if password == "":
        passwordEntry.insert(0, "Password")

passwordEntry = Entry(frame, width=20, bd=2, bg="#EFDECD", font="Arial 14")
passwordEntry.insert(0, "enter password")
passwordEntry.bind("<FocusIn>", password_enter)
passwordEntry.bind("<FocusOut>", password_leave)
passwordEntry.place(x=190, y=195)


########################  Button   ############################
signupButton = Button(frame, text="Sign Up", font=('Times New Roman', 13, 'bold'), width=8,
      bg='#0095B6', fg="#FFFDD0", activeforeground=framefg, activebackground='#0095B6', command=signup)
signupButton.place(x=165, y=270)

Label(frame, text="Do you have an account?", font=('Times New Roman', 13, 'bold'),
      bg='#0095B6', fg="#FFFDD0").place(x=20, y=330)

loginButton = Button(frame, text="Login", font=('Times New Roman', 13, 'bold'), border=0,
      bg='#0095B6', fg=framefg, activeforeground="#FFFDD0", activebackground='#0095B6', relief=FLAT, command=to_login)
loginButton.place(x=200, y=328)


window.mainloop()
