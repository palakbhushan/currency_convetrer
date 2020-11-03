#!/usr/bin/env python
# coding: utf-8

# In[1]:

from firebase import firebase
import mysql.connector  # imported sql.connector for using mysql
from tkinter import *  # imported tkinter module for GUI
import json
import requests  # imported JSON and request module for handling data from API's
from tkinter import ttk  # specially for combobox function for dropdown menus
from tkinter import messagebox as tmsg  # for using message box in GUI
from PIL import Image, ImageTk  # PIL for using image formats in tkinter like jpg,jpeg etc...


class GUI(Tk):  # CLASS GUI

    def __init__(self):

        super().__init__()  # Calling super class's ('TK') constructor
        self.user = StringVar()
        self.passwd = StringVar()
        self.db = StringVar()
        self.db_variable = IntVar()

        try:
            self.conn = mysql.connector.connect(host="localhost", user="root", passwd="7070134898aA$", database="pygui")
            cursor = self.conn.cursor()
            cursor.execute('show tables')
            tables = cursor.fetchall()
            print(tables)
            if ('login',) in tables:
                cursor.execute('select Email from login')
                self.email_list = cursor.fetchall()
                print("Email list:\n", self.email_list)
                # print("table present")
            else:
                cursor.execute('Create table login(Firstname VARCHAR(50) NOT NULL, lastname VARCHAR(50) NOT NULL,'
                               ' Email VARCHAR(50) NOT NULL, Password VARCHAR(50) NOT NULL, PRIMARY KEY(Email))')
                self.email_list = cursor.fetchall()
                print("Email list:\n", self.email_list)
                print("table not present, so created one.")
        except:

            self.fyrebase = firebase.FirebaseApplication("https://currency-converter-test.firebaseio.com/", None)
            result = self.fyrebase.get("/currency-converter-test/:login", '')
            self.rows = result.values()
            self.email_list = []
            for row in self.rows:
                self.email_list.append(row['Email'])
            print(self.email_list)

        # gui-geometry
        self.geometry("1200x800")
        self.title("Currency Converter- Login / Signup")
        self.minsize(1200, 800)
        self.maxsize(1200, 800)
        #self['background'] = 'black'
        self.image = Image.open('background4.jpeg')
        resized = self.image.resize((1200, 800), Image.ANTIALIAS)
        self.photo = ImageTk.PhotoImage(resized)
        self.label = Label(self, image=self.photo)
        self.wm_iconbitmap("logo.ico")

        self.label.place(x=0, y=0)

        self.heading = Label(self,
                             text="CURRENCY CONVERTER",
                             font=("times new roman", 15, "bold"),
                             padx=100,
                             pady=15,
                             fg="black",
                             bg="LightSteelBlue1",
                             relief=SOLID).place(x=330, y=20)

        self.heading = Label(self,
                             text="LOGIN / SIGNUP",
                             font=("times new roman", 15, "bold"),
                             padx=200,
                             pady=10,
                             fg="black",
                             bg="white").place(x=270, y=120)

        # signup
        # light blue/2/3/4 cadet blue1/2/3/4
        signup_frame = Frame(self, width=460, height=500, bg="LightSteelBlue")
        signup_frame.place(x=650, y=220)

        # variable

        self.firstnamevar = StringVar()
        self.firstnamevar.set("")
        self.lastnamevar = StringVar()
        self.firstnamevar.set("")

        self.emailvar = StringVar()
        self.firstnamevar.set("")

        self.passwordvar = StringVar()
        self.firstnamevar.set("")

        # entry
        Entry(signup_frame, textvariable=self.firstnamevar, justify=CENTER, width=20, borderwidth=2,
              font=("times new roman", 15, "bold")).place(x=1, y=210)

        Entry(signup_frame, textvariable=self.lastnamevar, justify=CENTER, width=20, borderwidth=2,
              font=("times new roman", 15, "bold")).place(x=250, y=210)

        Entry(signup_frame, textvariable=self.emailvar, justify=CENTER, width=20, borderwidth=2,
              font=("times new roman", 15, "bold")).place(x=1, y=315)

        Entry(signup_frame, textvariable=self.passwordvar, justify=CENTER, width=20, borderwidth=2,
              font=("times new roman", 15, "bold")).place(x=250, y=315)

        # labels
        Label(signup_frame,
              text="                        SIGN UP                        ",
              padx=10,
              pady=10,
              bg="purple",
              fg="black",
              font=("times new roman", 20, "bold"),
              justify=CENTER).place(x=0, y=30)
        Label(signup_frame,
              padx=10,
              pady=10,
              text=" FIRST NAME ",
              bg="light blue3",
              fg="black",
              font=("times new roman", 17, "bold"),
              justify=CENTER).place(x=0, y=145)

        Label(signup_frame,
              padx=30,
              pady=10,
              text="LAST NAME",
              bg="light blue3",
              fg="black",

              font=("times new roman", 17, "bold"),
              justify=CENTER).place(x=270, y=145)

        Label(signup_frame,
              padx=10,
              pady=10,
              text=" EMAIL  ",
              bg="light blue3",
              fg="black",
              font=("times new roman", 17, "bold"),
              justify=CENTER).place(x=0, y=250)
        Label(signup_frame,
              text="PASSOWRD",
              bg="light blue3",
              fg="black",
              padx=10,
              pady=10,
              font=("times new roman", 17, "bold"),
              justify=CENTER).place(x=305, y=250)

        Button(
            signup_frame,
            text="REGISTER",
            padx=10,
            pady=10,
            width=12,
            bg="light green",
            fg="black",
            font=("times new roman", 17, "bold"),
            command=self.register).place(x=150, y=410)

        # login
        login_frame = Frame(self, width=340, height=500, bg="LightSteelBlue")
        login_frame.place(x=100, y=220)
        # Label(self, text="", bg="black", padx=10, width=200, pady=50).place(x=2, y=720)
        Button(
            login_frame,
            text="SIGN IN",
            padx=10,
            pady=10,
            width=12,
            bg="light green",
            fg="black",
            font=("times new roman", 15, "bold"),
            command=self.login).place(x=75, y=410)

        Label(login_frame,
              text="                LOGIN                ",
              padx=10,
              pady=10,
              bg="purple",
              fg="black",
              font=("times new roman", 20, "bold"),
              justify=CENTER).place(x=0, y=30)

        Label(login_frame,
              text=" EMAIL ",
              padx=10,
              pady=10,
              bg="brown2",
              fg="black",
              font=("times new roman", 18, "bold"),
              justify=CENTER).place(x=0, y=130)

        Label(login_frame,
              text=" PASSWORD ",
              padx=10,
              pady=10,
              bg="brown2",
              fg="black",
              font=("times new roman", 18, "bold"),
              justify=CENTER).place(x=0, y=270)

        self.verifyemail = StringVar()
        self.verifyemail.set("")
        self.verifypassword = StringVar()
        self.verifypassword.set("")

        Entry(login_frame, textvariable=self.verifyemail, justify=CENTER, width=25, borderwidth=2,
              font=("times new roman", 16, "bold")).place(x=1, y=200)

        Entry(login_frame, textvariable=self.verifypassword, justify=CENTER, width=25, borderwidth=2,
              font=("times new roman", 16, "bold")).place(x=1, y=340)

        # coverpage..
        # USING TWO API's 1. 'http://data.fixer.io/api/'
        # 2. 'https://api.exchangerate-api.com/v4/latest/USD'

    def makeconnection(self, access_key, url):  # Because of request limits....

        try:  # trying API-1 ('https://data.fixer.io/api/')
            self.access_key = access_key
            self.url = url
            self.mainurl = self.url + 'latest?access_key=' + self.access_key  # api syntax
            self.response = requests.get(self.mainurl)  # storing the response of the api
            self.data = self.response.json()  # converting into json format if not already
            self.currencies = self.data['rates']
            self.date = self.data['date']
            # print(self.currencies)

        # if API_1 does not works because of per day request limits then
        # this except part for API-2('https://api.exchangerate-api.com/v4/latest/USD')
        except:
            self.response = requests.get('https://api.exchangerate-api.com/v4/latest/USD')
            self.data = self.response.json()
            # self.currencies-dictionary containing currency codes as key
            #                     and exchange rate as their values respectively
            self.currencies = self.data['rates']
            self.date = self.data['date']
            # print(self.currencies)

    def register(self):
        if self.firstnamevar.get() == "":
            tmsg.showinfo('Register', 'Firstname is required')
        elif self.lastnamevar.get() == "":
            tmsg.showinfo('Register', 'Lastname is required')
        elif self.emailvar.get() == "" and self.firstnamevar.get() != "":
            tmsg.showinfo('Register', 'Email is required')
        elif self.passwordvar.get() == "":
            tmsg.showinfo('Register', "Password is required")
        elif (self.emailvar.get(),) in self.email_list:
            tmsg.showinfo('Email error', 'User Already Exists')
        elif "@" not in self.emailvar.get() and "." not in self.emailvar.get():
            tmsg.showerror('Error', 'Invalid email')
        else:
            try:
                cursor = self.conn.cursor()
                cursor.execute('INSERT INTO login values(%s, %s, %s, %s)',
                                   (self.firstnamevar.get(),
                                    self.lastnamevar.get(), self.emailvar.get(), self.passwordvar.get()))

                self.conn.commit()
                self.fyrebase = firebase.FirebaseApplication("https://currency-converter-test.firebaseio.com/", None)
                data = {

                    "Firstname": f"{self.firstnamevar.get()}",
                    "Lastname": f"{self.lastnamevar.get()}",
                    "Email": f"{self.emailvar.get()}",
                    "Password": f"{self.passwordvar.get()}"
                }

                self.fyrebase.post("/currency-converter-test/:login", data)
                tmsg.showinfo('Success', 'User created successfully')
            except:
                data = {

                    "Firstname": f"{self.firstnamevar.get()}",
                    "Lastname": f"{self.lastnamevar.get()}",
                    "Email": f"{self.emailvar.get()}",
                    "Password": f"{self.passwordvar.get()}"
                }

                self.fyrebase.post("/currency-converter-test/:login", data)
                tmsg.showinfo('Success', 'User created successfully')

    def login(self):
        if self.verifyemail.get() == "":
            tmsg.showinfo('Login', 'Email is required')
        elif self.verifypassword.get() == "":
            tmsg.showinfo('Login', 'Password is required')

        elif self.verifypassword.get() == "admin" and self.verifyemail.get() == "admin":
            tmsg.showinfo('Success', 'You are logged in successfully.')
            self.firstpage()

        else:
            try:
                cursor = self.conn.cursor()
                cursor.execute(f'select Password from login where Email = "{self.verifyemail.get()}"')
                password = cursor.fetchall()
                print(type(password))
                print(password)

                if (self.verifypassword.get(),) in password:
                    tmsg.showinfo('Success', 'You are logged in successfully.')
                    self.firstpage()
                else:
                    tmsg.showinfo('login', "Incorrect Username or Password")

            except:
                self.fyrebase = firebase.FirebaseApplication("https://currency-converter-test.firebaseio.com/", None)
                result = self.fyrebase.get("/currency-converter-test/:login", '')
                self.rows = result.values()
                self.email_list = []
                for row in self.rows:
                    self.email_list.append(row['Email'])

                if self.verifyemail.get() in self.email_list:
                    for row in self.rows:
                        if row['Email'] == self.verifyemail.get():
                            if row['Password'] == self.verifypassword.get():
                                tmsg.showinfo('Success', 'You are logged in successfully.')
                                self.firstpage()
                                break
                            else:
                                tmsg.showinfo('login', "Incorrect Password")
                        else:
                            print()
                else:
                    tmsg.showinfo('login', "User doesn't exist.")

    def firstpage(self):
        self.geometry("1000x800")  # GUI window of size 1000x800
        self.maxsize(1000, 800)  # max, min size fixed
        self.minsize(1000, 800)  # so that user won't be able to increase or decrease size beyond that limit...
        self.title("Currency Converter")
        self.wm_iconbitmap("logo.ico")  # LPU_ICON

        # self['background']='#856ff8'

        # using PIL
        self.image = Image.open('newpic.jpg')

        self.photo = ImageTk.PhotoImage(self.image)
        self.label = Label(image=self.photo)

        self.label.place(x=0, y=0)

        # variables
        introvar = StringVar()
        self.user = StringVar()
        self.user.set("")
        self.passwd = StringVar()
        self.passwd.set("")
        self.db = StringVar()
        self.db.set("")
        import datetime
        now = datetime.datetime.now()
        time = now.strftime('%H')
        if "0" <= time < "12":
            introvar.set(" GOOD MORNING EVERYONE ")  # setting the default value of string variable 'intro-var'
        elif "12" <= time < "16":
            introvar.set(" GOOD AFTERNOON EVERYONE ")  # setting the default value of string variable 'intro-var'
        else:
            introvar.set(" GOOD EVENING EVERYONE ")  # setting the default value of string variable 'intro-var'

        sbar = Label(self, textvariable=introvar,
                     font="comicsansms 21 bold ",
                     bg="black", fg="white",
                     padx=10,


                     pady=15, justify=CENTER)
        sbar.place(x=200, y=20)
        sbar.update()

        import time  # importing time module
        time.sleep(4)  # to add delay of 4 seconds in the execution of program.
        introvar.set("WELCOME TO CURRENCY CONVERTER")  # changed to new value; attempt of making transition...

        # course code and course name LABEL..
        f = Frame(self, width=800, height=300, bg="black").place(x=100, y=440)

        self.course_name_label = Label(text="INT-213 PYTHON",
                                       font="comicsansms 15 bold",
                                       bg="light green",
                                       fg="black",
                                       padx=10,
                                       pady=10,
                                       relief=RAISED,
                                       justify=CENTER)
        self.course_name_label.place(x=220, y=145)

        # group-no LABEL...
        self.group_name_label = Label(text="GROUP-20",
                                      font="comicsansms 15 bold",
                                      bg="red3",
                                      fg="black",
                                      padx=10,
                                      pady=10,

                                      justify=CENTER)
        self.group_name_label.place(x=220, y=200)

        # group members LABEL..
        self.group_member_label = Label(text="GROUP-MEMBERS \nAbhishek Kumar Singh\nPalak Bhushan\nKaran Singh Naruka",
                                        font="comicsansms 15 bold",
                                        bg="cadet blue2",
                                        fg="black",
                                        padx=10,
                                        pady=10,
                                        justify=CENTER)
        self.group_member_label.place(x=220, y=260)
        self.group_member_label = Label(text="GUIDED BY:",
                                        font="comicsansms 15 bold",
                                        bg="red3",
                                        fg="black",
                                        padx=10,
                                        pady=10,
                                        justify=CENTER)
        self.group_member_label.place(x=600, y=200)
        self.group_member_label = Label(text="CHAVI MAM",
                                        font="comicsansms 15 bold",
                                        bg="cadet blue2",
                                        fg="black",
                                        padx=10,
                                        pady=10,
                                        justify=CENTER)
        self.group_member_label.place(x=600, y=260)

        self.databasetitle_label = Label(text="DATABASE LOGIN",
                                         font=("times new roman", 15, "bold"),
                                         bg="LightSteelBlue1",
                                         fg="black",
                                         padx=40,
                                         pady=10,
                                         justify=CENTER)
        self.databasetitle_label.place(x=380, y=450)
        # user_LABEL..

        self.user_label = Label(text="Username:",
                                bg="brown2",
                                fg="white",
                                padx=100,
                                pady=5,

                                justify=CENTER,
                                font=("times new roman", 15, "bold"))
        self.user_label.place(x=100, y=520)

        # passwd_LABEL...
        self.passwd_label = Label(text="Password:",
                                  bg="brown2",
                                  fg="white",
                                  justify=CENTER,
                                  font=("times new roman", 15, "bold"),
                                  padx=103,
                                  pady=5)
        self.passwd_label.place(x=100, y=570)

        # database_name LABEL..
        self.database = Label(text="Database :",
                              bg="brown2",
                              fg="white",
                              justify=CENTER,
                              font=("times new roman", 15, "bold"),
                              padx=100,
                              pady=5)
        self.database.place(x=100, y=620)

        # entries..
        # user entry

        self.user_entry = Entry(self, textvariable=self.user,
                                width=38,
                                relief=RIDGE,
                                justify=CENTER,
                                font=("times new roman", 15, "bold"),
                                )
        self.user_entry.place(x=500, y=520)

        # password entry

        self.passwd_entry = Entry(self, textvariable=self.passwd,
                                  width=38,
                                  relief=RIDGE,
                                  justify=CENTER,
                                  font=("times new roman", 15, "bold"),
                                  )
        self.passwd_entry.place(x=500, y=570)

        # database entry

        self.db_entry = Entry(self, textvariable=self.db,
                              width=38,
                              relief=RIDGE,
                              justify=CENTER,
                              font=("times new roman", 15, "bold"),
                              )
        self.db_entry.place(x=500, y=620)

        # connect _button..
        self.sql_button = Button(self, text="CONNECT",
                                 bg="light green",
                                 fg="black",
                                 font="comicsans 15 bold",
                                 command=self.sql)
        self.sql_button.place(x=340, y=685)

        # open app button
        Button(self, text="OPEN APP",
               bg="light green",
               fg="black",
               font="comicsansms 15 bold",
               command=self.app_gui).place(x=520, y=685)

        Label(self, text="INT_213",
              bg="black",
              fg="yellow",
              justify="center").place(anchor=S)
        # coverpage ends...

    def sql(self):
        # sql connection...
        # connecting to database..

        self.db_variable.set(0)
        try:

            self.conn = mysql.connector.connect(host="localhost", user=self.user.get(), passwd=self.passwd.get())
            self.cursor = self.conn.cursor()  # creating a cursor object
            self.cursor.execute('show databases')
            databases = self.cursor.fetchall()
            if (self.db.get(),) in databases:  # use database if exists already
                self.cursor.execute(f'use {self.db.get()}')
                self.sql_button["text"] = "CONNECTED"
            else:  # otherwise create database entered by user...
                self.cursor.execute(f'create database {self.db.get()}')
                self.cursor.execute(f'use {self.db.get()}')

                self.sql_button["text"] = "CONNECTED"

                self.conn.commit()
            # creating table and deleting table if exists already...
            self.cursor.execute('drop table if exists counts')
            self.cursor.execute('CREATE TABLE counts(DATE TEXT, FROM_CURRENCY TEXT, TO_CURRENCY TEXT, AMOUNT TEXT,'
                                ' RESULT TEXT)')
            self.cursor.close()
            self.db_variable.set(1)
        except Exception as e:  # prompt warning if unable to connect.. either username or password entered is wrong..

            tmsg.askretrycancel(title="Warning", message="Invalid Username or Password")

    # GUI PART
    def app_gui(self):

        # using pillow for opening jpg images, as we can't use jpg or jpeg images directly in tkinter
        # open
        image = Image.open('background.jpeg')
        # resize
        resized = image.resize((1000, 800), Image.ANTIALIAS)
        self.photo = ImageTk.PhotoImage(resized)
        self.label = Label(image=self.photo)
        self.label.place(x=0, y=0)

        # creating gui for converter

        self.geometry("1000x800")  # fixed size of the window
        self.maxsize(1000, 800)
        self.minsize(1000, 800)
        self.title("Currency Converter")
        self.wm_iconbitmap("logo.ico")  # LPU_ICON instead of default tkinter icon

        # GUI widgets, variables and labels...

        # HEADING
        Label(text="    CURRENCY   CONVERTER    ",
              font=("times new roman", 18, "bold"),
              bg="black",
              fg="white",
              padx=40,
              pady=10,
              justify=CENTER).place(x=305, y=4)

        # DATE LABEL
        self.date_label = Label(self,
                                text=f"Date : {self.data['date']}",  # used 'f string'

                                borderwidth=5,
                                font="courier,10")
        self.date_label.place(x=420, y=80)

        # variables...
        self.result = 0.0  # creating result variable and initializing it to 0.0
        self.from_ = StringVar()  # from_ variable of type string to store the currency code
        self.from_.set("USD")  # setting it to USD by default

        self.amount = DoubleVar()  # amount variable for storing input amount from the user..
        self.to = StringVar()  # to_ variable of type string to store the currency code to be  convert into
        self.to.set("INR")  # by default setting it to INR

        Label(text=" FROM ",
              font=("times new roman", 15, "bold"),
              bg="LightSteelBlue1",
              fg="black",
              padx=50,
              pady=10,
              justify=CENTER).place(x=200, y=200)

        Label(text=" TO ",
              font=("times new roman", 15, "bold"),
              bg="LightSteelBlue1",
              fg="black",
              padx=60,
              pady=10,
              justify=CENTER).place(x=650, y=200)


        # DROPDOWN MENUs...

        self.from_currency_dropdown = ttk.Combobox(self, textvariable=self.from_,
                                                   values=list(self.currencies.keys()),
                                                   font=("times new roman", 18, "bold"),
                                                   state='readonly', width=11,
                                                   justify=CENTER)
        self.from_currency_dropdown.place(x=210, y=270)

        self.to_currency_dropdown = ttk.Combobox(self, textvariable=self.to,
                                                 values=list(self.currencies.keys()),
                                                 font=("times new roman", 18, "bold"),
                                                 state='readonly',
                                                 width=10,
                                                 justify=CENTER)
        self.to_currency_dropdown.place(x=660, y=270)

        # ENTRY..
        self.from_amount = Entry(self, textvariable=self.amount,
                                 width=18,
                                 bg='grey',
                                 relief=SUNKEN,
                                 justify=CENTER,
                                 border=2,
                                 font=("times new roman", 18, "bold")
                                 ).place(x=175, y=340)

        # OUTPUT LABEL...
        self.converted_amount_field_label = Label(self, text='0.0',
                                                  fg='black',
                                                  bg='grey',

                                                  relief=SUNKEN,
                                                  justify=CENTER,
                                                  width=15,
                                                  font=("times new roman", 18, "bold"))
        self.converted_amount_field_label.place(x=625, y=340)

        # BUTTONS...

        # clear button...
        Button(text="CLEAR",
               padx=15,
               pady=10,
               width=12,
               bg="light green",
               fg="black",
               font=("times new roman", 10, "bold"),
               command=self.clear).place(x=300, y=490)

        # convert button - calls conversion function on click
        Button(text="CONVERT",
               padx=10,
               pady=10,
               width=15,
               bg="light green",
               fg="black",
               font=("times new roman", 10, "bold"),
               command=self.conversion).place(x=600, y=490)

        # save button -  calls save function
        Button(text="SAVE",
               padx=10,
               pady=10,
               width=12,
               bg="dark turquoise",
               fg="black",
               font=("times new roman", 10, "bold"),
               command=self.save).place(x=290, y=570)

        # show data button - calls show function..
        Button(text="SHOW DATA",
               padx=10,
               pady=10,
               width=15,
               bg="dark turquoise",
               fg="black",
               font=("times new roman", 10, "bold"),
               command=self.showdata).place(x=610, y=570)

        # exit button - destroys the gui
        Button(text="EXIT",
               padx=10,
               pady=10,
               width=10,
               bg="brown2",
               fg="black",
               font=("times new roman", 10, "bold"),
               command=self.exit).place(x=455, y=570)
        Button(text="BACK", padx=20,
               pady=11,
               bg="black",
               fg="white",
               font="comicsansms 9 bold",
               command=self.firstpage).place(x=5, y=4)

    # CONVERSION FUNCTION

    def conversion(self):
        try:  # conversion part if user enters valid input
            rate_from = self.data['rates'][self.from_.get()]
            rate_to = self.data['rates'][self.to.get()]
            self.result = (self.amount.get() * rate_to) / rate_from
            self.result = round(self.result, 2)
            self.converted_amount_field_label.config(text=str(self.result))

        except Exception as e:  # EXCEPTION FOR INVALID INPUTs like characters, expressions etc...

            tmsg.showerror("Error", "Invalid Input.")  # WARNING MESSAGE_BOX FOR INVALID INPUT

    def clear(self):
        self.amount.set(0.0)
        self.converted_amount_field_label.config(text="0.0")

    # SAVE FUNCTION

    def save(self):  # mysql queries to insert data...
        if self.db_variable.get() == 1:
            try:
                self.cursor = self.conn.cursor()

                self.cursor.execute('''insert into counts values(%s , %s , %s , %s , %s)''',
                                    (self.date, self.from_.get(), self.to.get(), self.amount.get(), str(self.result)))

                self.conn.commit()  # committing the transactions in db..
                self.cursor.close()
            except:
                tmsg.showerror('Input Error', 'Invalid Input for Amount')
        else:
            tmsg.showerror('Database Error', 'Please Connect Database')

            # SHOW DATA FUNCTION...

    def showdata(self):
        if self.db_variable.get() == 1:
            self.cursor = self.conn.cursor()  # again creating the cursor object -'self.cursor'
            self.cursor.execute('select * from counts')
            self.mydata = self.cursor.fetchall()  # 'fetchall()'-to retrieve all the rows of the table...

            root = Tk()
            root.geometry("300x300")
            root.title("GUI-SHOWDATA")
            root.wm_iconbitmap("logo.ico")
            TextArea = Text(root, bg="light green",
                            fg="black",
                            font="lucida 10")
            TextArea.pack(expand=True, fill=BOTH)
            TextArea.insert(1.0, "                YOUR TABLE\n\n")
            TextArea.insert(END, "('  DATE','   FROM','  TO','AMOUNT','RESULT')\n\n")
            for data in self.mydata:
                TextArea.insert(END, f"{data}\n")
            self.cursor.close()
        else:
            tmsg.showerror('Database', 'Database not connected. Try connecting Database')

    def exit(self):
        qanswer = tmsg.askquestion("ASK", "Did you like it ?")
        print(qanswer)
        if qanswer == "yes":
            tmsg.showinfo('Message', 'Thank You Very Much.')
        else:
            tmsg.showinfo('Message', 'Oops! Sorry :(')
        answer = tmsg.askokcancel('Error', 'Are you sure you want to exit Currency Converter?')
        if answer:
            self.destroy()


if __name__ == '__main__':  # entry point of the program...
    baseurl = 'http://data.fixer.io/api/'
    accesskey = 'd8bb0828eecaa42b3119f51bc492c06b'  # access_key= key for accessing the api

    converter = GUI()  # GUI class called and converter object created
    # converter.firstpage()
    converter.makeconnection(accesskey, baseurl)
    mainloop()

