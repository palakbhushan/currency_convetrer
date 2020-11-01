import mysql.connector  # imported sql.connector for using mysql
from tkinter import *  # imported tkinter module for GUI
import json, requests  # imported JSON and request module for handling data from API's
from tkinter import ttk  # specially for combobox function for dropdown menus
from tkinter import messagebox as tmsg  # for using message box in GUI
from PIL import Image, ImageTk  # PIL for using image formats in tkinter like jpg,jpeg etc...


class GUI(Tk):  # CLASS GUI

    def __init__(self, url, access_key):

        super().__init__()  # Calling super class's ('TK') constructor

        # USING TWO API's 1. 'http://data.fixer.io/api/'
        # 2. 'https://api.exchangerate-api.com/v4/latest/USD'

        # Because of request limits....

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

        # coverpage..

    def firstpage(self):
        self.geometry("700x526")  # GUI window of size 700x526
        self.maxsize(700, 526)  # max, min size fixed
        self.minsize(700, 526)  # so that user won't be able to increase or decrease size beyond that limit...
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
        self.passwd = StringVar()
        self.db = StringVar()

        introvar.set(" GOOD MORNING EVERYONE..")  # setting the default value of string variable 'intro-var'
        sbar = Label(self, textvariable=introvar,
                     font="comicsansms 21 bold ",
                     bg="black", fg="white",
                     relief=RAISED,
                     pady=15, justify=CENTER)
        sbar.place(x=70, y=10)
        sbar.update()

        import time  # importing time module
        time.sleep(4)  # to add delay of 4 seconds in the execution of program.
        introvar.set("WELCOME TO CURRENCY CONVERTER")  # changed to new value; attempt of making transition...

        # course code and course name LABEL..

        self.course_name_label = Label(text="INT-213 PYTHON",
                                       font="comicsansms 15 underline",
                                       bg="purple",
                                       fg="white",
                                       relief=RAISED,
                                       justify=CENTER)
        self.course_name_label.place(x=70, y=100)

        # group-no LABEL...
        self.group_name_label = Label(text="Group-20",
                                      font="comicsansms 15 underline",
                                      bg="purple",
                                      fg="white",
                                      relief=RAISED,
                                      justify=CENTER)
        self.group_name_label.place(x=70, y=130)

        # group members LABEL..
        self.group_member_label = Label(text="Group Members:-\nAbhishek Kumar Singh\nPalak Bhushan\nKaran Singh Naruka",
                                        font="comicsansms 15 italic",
                                        bg="yellow", fg="black",
                                        relief=RAISED,
                                        justify=LEFT)
        self.group_member_label.place(x=70, y=180)

        # roll_number LABEL...
        self.roll_label = Label(text="Roll Number\n15\n27\n26",
                                font="comicsansms 15 italic",
                                bg="yellow",
                                fg="black",
                                relief=RAISED, justify=CENTER)
        self.roll_label.place(x=500, y=180)

        # user_LABEL..
        self.user_label = Label(text="Username:",
                                bg="purple",
                                fg="white",
                                relief="raised",
                                justify=CENTER,
                                font="comicsansms 14 bold")
        self.user_label.place(x=70, y=305)

        # passwd_LABEL...
        self.passwd_label = Label(text="Password:",
                                  bg="purple",
                                  fg="white",
                                  relief="raised",
                                  justify=CENTER,
                                  font="comicsansms 14 bold")
        self.passwd_label.place(x=70, y=340)

        # database_name LABEL..
        self.database = Label(text="Database :",
                              bg="purple",
                              fg="white",
                              relief="raised",
                              justify=CENTER,
                              font="comicsansms 14 bold")
        self.database.place(x=70, y=375)

        # entries..
        # user entry

        self.user_entry = Entry(self, textvariable=self.user,
                                width=30,
                                relief=RIDGE,
                                justify=CENTER,
                                font="comicsansms 12 bold",
                                borderwidth=1)
        self.user_entry.place(x=210, y=305)

        # password entry

        self.passwd_entry = Entry(self, textvariable=self.passwd,
                                  width=30,
                                  relief=RIDGE,
                                  justify=CENTER,
                                  font="comicsansms 12 bold",
                                  borderwidth=1)
        self.passwd_entry.place(x=210, y=340)

        # database entry

        self.db_entry = Entry(self, textvariable=self.db,
                              width=30,
                              relief=RIDGE,
                              justify=CENTER,
                              font="comicsansms 12 bold",
                              borderwidth=1)
        self.db_entry.place(x=210, y=375)

        # connect _button..
        self.sql_button = Button(self, text="CONNECT",
                                 bg="yellow",
                                 fg="black",
                                 font="comicsans 15 bold",
                                 command=self.sql)
        self.sql_button.place(x=210, y=435)

        # open app button
        Button(self, text="OPEN APP",
               bg="red",
               fg="black",
               font="comicsansms 15 bold",
               command=self.app_gui).place(x=360, y=435)

        Label(self, text="INT_213",
              bg="black",
              fg="yellow",
              justify="center").place(anchor=S)
        # coverpage ends...

    def sql(self):
        # sql connection...
        # connecting to database..
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
        except Exception as e:  # prompt warning if unable to connect.. either username or password entered is wrong..
            tmsg.askretrycancel(title="Warning", message="Invalid Username or Password")

    # GUI PART
    def app_gui(self):

        # using pillow for opening jpg images, as we can't use jpg or jpeg images directly in tkinter

        self.image = Image.open('newpic.jpg')
        self.photo = ImageTk.PhotoImage(self.image)
        self.label = Label(image=self.photo)
        self.label.place(x=0, y=0)

        # creating gui for converter

        self.geometry("700x526")  # fixed size of the window
        self.maxsize(700, 526)
        self.minsize(700, 526)
        self.title("Currency Converter")
        self.wm_iconbitmap("logo.ico")  # LPU_ICON instead of default tkinter icon

        # GUI widgets, variables and labels...

        # HEADING
        Label(text="    CURRENCY   CONVERTER    ",
              font="comicsansms 21 bold",
              bg="black",
              fg="white",
              relief=RAISED,
              pady=15,
              justify=CENTER).place(x=135, y=0)

        # DATE LABEL
        self.date_label = Label(self,
                                text=f"Date : {self.data['date']}",  # used 'f string'
                                relief=SOLID,
                                borderwidth=5,
                                font="courier,10")
        self.date_label.place(x=275, y=80)

        # variables...
        self.result = 0.0  # creating result variable and initializing it to 0.0
        self.from_ = StringVar()  # from_ variable of type string to store the currency code
        self.from_.set("USD")  # setting it to USD by default

        self.amount = DoubleVar()  # amount variable for storing input amount from the user..
        self.to = StringVar()  # to_ variable of type string to store the currency code to be  convert into
        self.to.set("INR")  # by default setting it to INR

        # DROPDOWN MENUs...

        self.from_currency_dropdown = ttk.Combobox(self, textvariable=self.from_,
                                                   values=list(self.currencies.keys()),
                                                   font="comicsansms 18 bold",
                                                   state='readonly', width=10,
                                                   justify=CENTER)
        self.from_currency_dropdown.place(x=100, y=150)

        self.to_currency_dropdown = ttk.Combobox(self, textvariable=self.to,
                                                 values=list(self.currencies.keys()),
                                                 font="comicsansms 18 bold",
                                                 state='readonly',
                                                 width=10,
                                                 justify=CENTER)
        self.to_currency_dropdown.place(x=460, y=150)

        # ENTRY..
        self.from_amount = Entry(self, textvariable=self.amount,
                                 width=17,
                                 relief=RIDGE,
                                 justify=CENTER,
                                 font="comicsansms 12 bold",
                                 borderwidth=3).place(x=100, y=210)

        # OUTPUT LABEL...
        self.converted_amount_field_label = Label(self, text='0.0',
                                                  fg='black',
                                                  bg='white',
                                                  relief=RIDGE,
                                                  justify=CENTER,
                                                  width=15,
                                                  borderwidth=3,
                                                  font="comicsansms 12 bold")
        self.converted_amount_field_label.place(x=460, y=210)

        # BUTTONS...

        # convert button - calls conversion function on click
        Button(text="CONVERT",
               padx=10,
               pady=10,
               width=15,
               bg="red",
               fg="black",
               font="comicsansms 10 bold",
               command=self.conversion).place(x=360, y=310)

        # clear button...
        Button(text="CLEAR",
               padx=10,
               pady=10,
               width=12,
               bg="red",
               fg="black",
               font="comicsansms 10 bold",
               command=self.clear).place(x=220, y=310)

        # save button -  calls save function
        Button(text="SAVE",
               padx=10,
               pady=8,
               width=10,
               bg="yellow",
               fg="black",
               font="comicsansms 9 bold",
               command=self.save).place(x=185, y=390)

        # show data button - calls show function..
        Button(text="SHOW DATA",
               padx=10,
               pady=8,
               width=10,
               bg="yellow",
               fg="black",
               font="comicsansms 9 bold",
               command=self.showdata).place(x=435, y=390)

        # exit button - destroys the gui
        Button(text="EXIT",
               padx=10,
               pady=8,
               width=10,
               bg="black",
               fg="yellow",
               font="comicsansms 9 bold",
               command=self.destroy).place(x=305, y=390)
        Button(text="BACK", padx=10,
               pady=8,
               bg="black",
               fg="white",
               font="comicsansms 9 bold",
               relief=FLAT,
               command=self.firstpage).place(x=5, y=0)

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
        try:
            self.cursor = self.conn.cursor()

            self.cursor.execute('''insert into counts values(%s , %s , %s , %s , %s)''',
                                (self.date, self.from_.get(), self.to.get(), self.amount.get(), str(self.result)))

            self.conn.commit()  # committing the transactions in db..

            self.cursor.close()

        except Exception as e:
            tmsg.showerror('Input Error', 'Invalid input or Database not connected.')

            # SHOW DATA FUNCTION...

    def showdata(self):
        try:
            self.cursor = self.conn.cursor()  # again creating the cursor object -'self.cursor'
            self.cursor.execute('select * from counts')
            self.mydata = self.cursor.fetchall()  # 'fetchall()'-to retrieve all the rows of the table...


            root = Tk()
            root.geometry("300x300")
            root.title("GUI-SHOWDATA")
            root.wm_iconbitmap("logo.ico")
            TextArea = Text(root, bg="yellow", fg="white", font="lucida 10")
            TextArea.pack(expand=True, fill=BOTH)
            TextArea.insert(1.0, "                YOUR TABLE\n")
            TextArea.insert(END, "('  DATE','   FROM','  TO','AMOUNT','RESULT')\n")
            for data in self.mydata:
                TextArea.insert(END, f"{data}\n")
            self.cursor.close()
        except Exception as e:
            tmsg.showerror('Input Error', 'Invalid input or Database not connected.')


if __name__ == '__main__':  # entry point of the program...
    baseurl = 'http://data.fixer.io/api/'
    accesskey = 'd8bb0828eecaa42b3119f51bc492c06b'  # access_key= key for accessing the api

    converter = GUI(baseurl, accesskey)  # GUI class called and converter object created
    converter.firstpage()
    mainloop()
