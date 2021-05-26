from tkinter import *
from LOGINPAGE import *
def sign():
    class signup:
        def __init__(self,root):
            self.root=root
            root.geometry=('700x700')
            root.maxsize(700,700)
            root.minsize(700,700)
            root.title('Sign Up')
            root.configure(bg='grey')
            signuplabel= Label(root, width=30, justify=CENTER, text='Welcome to Sign UP Page!', font=('Times New Roman', 15, 'bold',), bg='grey')
            signupbutton= Button(root, width=20, justify=CENTER, text='SIGN UP!', font=('Times New Roman', 15, 'bold',), bg='orange')
            frame1 = Frame(root, height=500, bg='grey')
            name_label = Label(frame1, width=10, justify=CENTER, text='User Name:', font=('Times New Roman', 15, 'bold'),bg='grey')
            self.name_entry = Entry(frame1, width=20, justify=CENTER, font=('Times New Roman', 15, 'bold'))
            roll_label = Label(frame1, width=10, justify=CENTER, text='Roll no:', font=('Times New Roman', 15, 'bold'),bg='grey')
            self.roll_entry = Entry(frame1, width=20, justify=CENTER, font=('Times New Roman', 15, 'bold'))

            frame2 = Frame(root, height=500, bg='grey')
            program_label = Label(frame2, width=10, justify=CENTER, text='Program Name:', font=('Times New Roman', 15, 'bold'),bg='grey')
            self.program_entry = Entry(frame2, width=20, justify=CENTER, font=('Times New Roman', 15, 'bold'))
            semester_label = Label(frame2, width=10, justify=CENTER, text='Semester no:', font=('Times New Roman', 15, 'bold'),bg='grey')
            self.semester_entry = Entry(frame2, width=20, justify=CENTER, font=('Times New Roman', 15, 'bold'))

            frame3 = Frame(root, height=500, bg='grey')
            city_label = Label(frame3, width=10, justify=CENTER, text='City Name:', font=('Times New Roman', 15, 'bold'), bg='grey')
            self.city_entry = Entry(frame3, width=20, justify=CENTER, font=('Times New Roman', 15, 'bold'))
            phone_label = Label(frame3, width=10, justify=CENTER, text='Phone no:', font=('Times New Roman', 15, 'bold'), bg='grey')
            self.phone_entry = Entry(frame3, width=20, justify=CENTER, font=('Times New Roman', 15, 'bold'))

            frame4 = Frame(root, height=500, bg='grey')
            password_label = Label(frame4, width=10, justify=CENTER, text='Password:', font=('Times New Roman', 15, 'bold'),bg='grey')
            self.password_entry = Entry(frame4, width=15, justify=CENTER, font=('Times New Roman', 15, 'bold'))
            pass2_label = Label(frame4, width=15, justify=CENTER, text='Confirm Password:', font=('Times New Roman', 15, 'bold'),bg='grey')
            self.pass2_entry = Entry(frame4, width=15, justify=CENTER, font=('Times New Roman', 15, 'bold'))

            signuplabel.pack(side=TOP, pady=10, padx=100)
            signupbutton.pack(side=BOTTOM, pady=20, padx=30)

            frame1.pack(side=TOP, fill=BOTH, expand=1)
            name_label.pack(side=LEFT, pady=5, padx=10)
            self.name_entry.pack(side=LEFT, pady=5, padx=10)
            roll_label.pack(side=LEFT, pady=5, padx=10)
            self.roll_entry.pack(side=LEFT, pady=5, padx=10)

            frame2.pack(side=TOP, fill=BOTH, expand=1)
            program_label.pack(side=LEFT, pady=5, padx=10)
            self.program_entry.pack(side=LEFT, pady=5, padx=10)
            semester_label.pack(side=LEFT, pady=5, padx=10)
            self.semester_entry.pack(side=LEFT, pady=5, padx=10)

            frame3.pack(side=TOP, fill=BOTH, expand=1)
            city_label.pack(side=LEFT, pady=5, padx=10)
            self.city_entry.pack(side=LEFT, pady=5, padx=10)
            phone_label.pack(side=LEFT, pady=5, padx=10)
            self.phone_entry.pack(side=LEFT, pady=5, padx=10)

            frame4.pack(side=TOP, fill=BOTH, expand=1)
            password_label.pack(side=LEFT, pady=5, padx=10)
            self.password_entry.pack(side=LEFT, pady=5, padx=10)
            pass2_label.pack(side=LEFT, pady=5, padx=10)
            self.pass2_entry.pack(side=LEFT, pady=5, padx=10)

        def erase(self):
            self.name_entry.delete(0,END)
            self.roll_entry.delete(0,END)
            self.phone_entry.delete(0,END)
            self.city_entry.delete(0,END)
            self.password_entry.delete(0,END)
            self.pass2_entry.delete(0,END)

        def confirmmation(self,password,pass2):
            if password == pass2:
                self.erase()
                root.destroy()
                main()
            else:
                root.destroy()
                sign()

    root= Tk()
    signup(root)
    mainloop()

sign()