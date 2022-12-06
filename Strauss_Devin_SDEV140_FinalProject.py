import os
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
#from tkinter.font import Font

'''
Author: Devin Strauss
Last Date Modified: 12/2/2022
This program is a GUI application that will run as a log in screen for a user. It will allow them to log in with
a username and password. It will direct them to a page that tells them they have successfully logged in. If the user 
needs to create a new account then the "create new account" will bring up a new window to have the user enter their information
to create an account that allows them to log in

'''


# creates empty window for frame and widgets to be applied to
root=Tk()
root.title("Login Screen")
root.geometry("900x850")
root.configure(bg="white")

# creates frame that the widgets will fit into
frame= Frame()
frame.configure(bg="white")
frame.pack()

'''new_window= Frame()
new_window.configure(bg="white")
new_window.pack()'''


# labels that will be fit into frame
company_label= Label(frame, text= "A Fake Company, LLC") # creates a label within the frame configured in line 23
company_label.configure(fg="purple", bg="white",relief="solid", font= "Arial, 19", height= 5) # customizes the label created in line 32 by changing the color, outline, font, and size of the label
company_label.grid(row=0,column=2,sticky=NSEW) # assigns the area space that the label will be placed

img = ImageTk.PhotoImage(Image.open("worthy-welcome-worthy-christian-forums-1.png")) # assigns the image to a variable
welcome_label = Label(frame, text= "Welcome! Please log in", image= img) # label that also calls the image to be displayed as a label
welcome_label.configure(fg="purple", bg= "white", relief="solid",font= "Arial, 18")
welcome_label.grid(row=1, column=2, pady=5, sticky=NS)

user_nameLabel= Label(frame, text= "Username")
user_nameLabel.configure(fg="black", bg= "white", font="Arial, 15", relief= "solid")
user_nameLabel.grid(row=4, column= 1, pady=20, padx=10)

password_label= Label(frame, text="Password")
password_label.configure(fg="black", bg= "white", font="Arial, 15",relief="solid")
password_label.grid(row=5, column=1, sticky=W, pady=4, padx=10)

# entry fields where user can enter their username and password
global username_success
global password_success

 # creates a variable that the username and password entries can recognize
username_success = StringVar()
password_success = StringVar()

# entry fields that allow a user to enter a username and password
username_entry= Entry(frame, textvariable=username_success, bd=5, width=20) # creates the entry field and customizes the size and appearance of the entry field
username_entry.grid(row=4, column= 2, pady=20) # assigns the area that the entry field will be placed on the frame
password_entry= Entry(frame, textvariable=password_success, bd = 5, show="*") # creates an entry field for the password and also customizes the password entry to be hidden)
password_entry.grid(row=5, column=2, pady=20)


# button functions
def login_function(): #function that will be called by the login button
    username1 = username_success.get() # uses the variables created in lines 57 and 58
    password1 = password_success.get()
    username_entry.delete(0, END) # clears out the entry fields after a successful log in
    password_entry.delete(0, END)

    list_of_files = os.listdir() # this method allows the list of usernames and passwords in the directory to be referred to
    if username1 in list_of_files:
        file1 = open(username1, "r") # opens the files from the directory and reads them using "r" and then matches them to allow access or not
        verify = file1.read().splitlines() # since the directories are stored using two separate lines (username, password) .splitlines is used to distinguish the two
        if password1 in verify: # if statement that allows access based on the password in the directory
            messagebox.showinfo(title="Login Success", message="You have successfully logged in.")

        else:
            password_invalid() # calls the function when the password is typed incorrectly

    else:
        user_not_found() # calls the function if the username is not found in the directory






def delete_user_not_found_screen(): # function that closes the window created when a username is not found in the directory
    user_not_found_screen.destroy()



def password_invalid(): # function that is called when the password the user types is invalid or incorrect
    messagebox.showerror(title="Error", message="Invalid password.")





def user_not_found(): # function that is called when ther username entry is not found in the directory
    global user_not_found_screen # global is able to call a function used previously
    user_not_found_screen = Toplevel(frame) # Toplevel creates a frame on top of the current window
    user_not_found_screen.title("Invalid Username.") # title that is read at the top of the window
    user_not_found_screen.configure(bg="white")
    user_not_found_screen.geometry("700x650")
    img2 = ImageTk.PhotoImage(Image.open("user-not-found.png"))  # assigns the image to a variable
    usernot_foundlabel= Label(user_not_found_screen, bg="white", image=img2) # label that calls the image
    usernot_foundlabel.grid(row=0, column=2) # places the above label into the frame by defining the row and column to place it
    usernot_foundlabel.image=img2 # references the image again, the image was not showing up and after research I found that the image got garbage collected leaving no reference to it. This line attaches a reference to the image
    usernot_foundlabel2= Label(user_not_found_screen, bg="white", text="User not found. Please create new account.") # label that shows text that user is not found
    usernot_foundlabel2.grid(row=1, column=2)
    leave_button= Button(user_not_found_screen, text="Return to Login", command=delete_user_not_found_screen) # button that calls function from above to close the current window which will return to login screen
    leave_button.grid(row=2, column=2)




def forgot_function(): # function that will be called by forgot password button
    forgot_window= Toplevel(frame) # creates a new window, Toplevel places the window on top of the already generated window
    forgot_window.title("Forgot Password") # gives the new created window a title
    forgot_window.configure(bg="white")
    forgot_window.geometry("600x550") # creates the size of the window
    forgot_label= Label(forgot_window, fg="black", bg="white", text="Did you forget your password? Sorry, we are still working on this.")
    forgot_label.grid(row=1, column=1, sticky=N)
    leave_button = Button(forgot_window, fg="red", text="Return to Login",command=forgot_window.destroy)  # button that closes the current window which will return to login screen
    leave_button.grid(row=2, column=1)



def create_user(): # function that will be called by create account button
    create_window= Toplevel(frame)
    create_window.title("Create User Account")
    create_window.configure(bg="white")
    create_window.geometry("600x550")

    # global allows access to these varibales throughout the program
    global username
    global password
    global username_entry
    global password_entry

    # identifies these variables as strings even if integers are used in the entry fields
    username = StringVar()
    password = StringVar()

    # labels that distinguish what info to enter in entry fields listed below
    create_label= Label(create_window, fg="black", bg= "white",font="Calibri, 19", text="Create a new user account")
    create_label.grid(row=0, column=1, pady= 20, padx=20)
    createname_label= Label(create_window, fg="black", bg= "white", text= "Create username:")
    createname_label.grid(row=2, column=0)
    createpass_label= Label(create_window, fg="black", bg="white", text= "Create password:")
    createpass_label.grid(row=3, column=0)

    # entry fields that user can use to create username and password
    createuser_entry= Entry(create_window, textvariable= username)
    createuser_entry.grid(row=2, column=1)
    createpass_entry= Entry(create_window, textvariable=password, show='*')
    createpass_entry.grid(row=3, column=1)

    # function that the "finished" button below will call in order to store username and password
    def createnew_account():
        username_input= username.get() # gets username entry in order to write it to file
        password_input= password.get() # gets password entry in order to write it to file

        f= open(username_input, "w") # opens a file using "w" for write
        f.write(username_input + "\n") # writes username on a new line and writes it to created file
        f.write(password_input) # writes password to file opened previously
        f.close() # closes the file after username and password is written to the file

        # clears out the entry field
        createuser_entry.delete(0, END)
        createpass_entry.delete(0, END)

        # label and message box that confirm account was created successfully
        Label(create_window, text="Account created successfully", fg="blue", font="Arial, 12").grid(row=6, column=1, pady=20) # label that appears to let user know account was created successfully

        messagebox.showinfo(title="New Account Created", message= "You have successfully created an account.") # pop-up message that approves new account



    # button that calls the function to write newly created username and password
    createnew_button = Button(create_window, text="Finished", width=10, height=1, fg="blue", command=createnew_account)
    createnew_button.grid(row=4, column=1, pady=20)

    # button that will close the create account window and return to the log in screen
    exit_button= Button(create_window, text="Return to Login", width=10, height=1, fg="red", command=create_window.destroy)
    exit_button.grid(row=5, column=1, pady=20)

    show_me = IntVar(value=0)  # variable that will be used within the checkbox button

    def show_pass():  # function that is used for the checkbox to either reveal or hide password
        if (show_me.get() == 1):  # applies the variable assigned to the checkbox
            createpass_entry.config(show='') # if the checkbox is checked then the password will be revealed
        else:
            createpass_entry.config(show='*') # if checkbox is unchecked then the password will appear at asterisks

    show_password = Checkbutton(create_window, text="Show Password", variable=show_me, onvalue=1, offvalue=0,
                                command=show_pass)  # creates a checkbox that uses the show_me variable to activate the function that is assigned to this button
    show_password.grid(row=3, column=2)  # places the checkbox onto the frame using the grid layout



# buttons that will be used in conjunction with functions written above
login_button= Button(frame, text= "Log In", fg= "blue",bg="black", command= login_function) # creates the button called "Log In", command assigns the function to the button
login_button.grid(row=6, column=2, pady=10) # assigns the area that this button will be placed
forgot_button= Button(frame, text="Forgot Password", fg= "blue", relief= "solid", command=forgot_function)
forgot_button.grid(row=7, column=2, pady=10)
create_account= Button(frame, text="Create Account", fg="blue", relief="solid", command=create_user)
create_account.grid(row=8, column=2, pady=10)
quitButton = Button(frame, text="Exit", command=frame.quit) # button that will close the window and any new windows that have also opened from button commands
quitButton.grid(row=9, column= 2, pady=20)


show_me= IntVar(value=0) # variable that will be used within the checkbox button

def show_pass(): #function that is used for the checkbox to either reveal or hide password
    if (show_me.get() == 1): # applies the variable assigned to the checkbox
        password_entry.config(show='') # reveals the password if checkbox is checked
    else:
        password_entry.config(show='*') # hides password if checkbox is unchecked

show_password= Checkbutton(frame, text= "Show Password",variable=show_me, onvalue=1,offvalue=0,command= show_pass) # creates a checkbox that uses the show_me variable to activate the function that is assigned to this button
show_password.grid(row=5, column=3) # places the checkbox onto the frame using the grid layout












root.mainloop() # starts the GUI application
