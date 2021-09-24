#14/3/2021:
'''def virus():
  import tkinter
  import tkinter.font
  #Create window:
  window = tkinter.Tk()
  window.title('Nam')
  window.geometry('640x360+0+0')
  window.config(bg='#000000')
  #Create label:
  label = tkinter.Label(master=window, text='Tinder Virus :D')
  label.config(bg='#ffffff',font=('Times',49))
  label.pack()
  #Run window:
  window.mainloop()
#Create virus:
while 1:(
  virus()'''

#21/3/2021:
#Import Tkinter:
'''from tkinter import *
from tkinter import messagebox

#Create window:
window = Tk()
window.geometry("200x200")
window.title('Login window')

#Create login form:
  #Create "Username" section:
def section_un():
  label_un = Label(master=window,text="Username:")
  label_un.pack()
  box_un = Entry(master=window)
  box_un.pack()
  global box_un

  #Create "Password" section:
def section_p():
  label_p = Label(master=window,text="Password:")
  label_p.pack()
  box_p = Entry(master=window,show='*')
  box_p.pack()
  global box_p

#Show login form section:
section_un()
section_p()

#Create button:
def msg():
  un = box_un.get()
  p = box_p.get()
  messagebox.showinfo('Login completed','Successful!',"Username:",un,"\nPassword:",p)
login = Button(master=window,text='Login',command=msg)
login.pack()

window.mainloop()'''

#28/03/2021:
'''#Import Tkinter library:
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox

#Create UI (window):
w = Tk()
w.geometry('650x100+0+0')
w.title('Sign up')
l = Label(w, text='Fill in your info:')
l.grid(row=0,column=2)

#Create info:
l_n = Label(w, text='Username:')
l_n.grid(row=1,column=0)
b_n = Entry(w)
b_n.grid(row=1,column=1)

l_a = Label(w, text='Age:')
l_a.grid(row=1,column=3)
b_a = Entry(w)
b_a.grid(row=1,column=4)

l_e = Label(w, text='Email:')
l_e.grid(row=2,column=0)
b_e = Entry(w)
b_e.grid(row=2,column=1)

l_c = Label(w, text='Country:')
l_c.grid(row=2,column=3)
c = ['','Việt Nam','China','Japỏn','Sỉngapoẻ','Thái','Láo','Cầm bô đi ỉa','Môngolịa']
cmb = Combobox(w, values=c)
cmb.current(0)
cmb.grid(row=2,column=4)

#Get and show info:
def get_inf():
  name = b_n.get()
  age = b_a.get()
  email = b_e.get()
  country = cmb.get()
  info = 'Username: ' + name + '\nAge: ' + age + '\nEmail: ' + email + '\nCountry: ' + country
  messagebox.showinfo('Successful!', info)

#Create button:
btn = Button(w, text='Register', command=get_inf)
btn.grid(row=3,column=2)
#Run:
w.mainloop()'''

'''from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
window = Tk()
window.title("Register Form")
window.geometry("300x400+500+250")

name_label = Label(window, text="Name: ")
name_label.pack()
name_entry = Entry(window)
name_entry.pack()

date_label = Label(window, text="Date: ")
date_label.pack()
date_entry = Entry(window)
date_entry.pack()

address_label = Label(window, text="Address: ")
address_label.pack()
address_entry = Entry(window)
address_entry.pack()

email_label = Label(window, text="Email: ")
email_label.pack()
email_entry = Entry(window)
email_entry.pack()

phone_label = Label(window, text="Phone: ")
phone_label.pack()
phone_entry = Entry(window)
phone_entry.pack()

country_label = Label(window, text="Country: ")
country_label.pack()
countries = ['Viet Nam', 'Laos', 'Cambodia', 'Thailands', 'Singapore', 'Philippines', 'Malaysia', 'Indonesiasubmit', 'Myanmar', 'TimoLeste', "Brunei"]
country_combobox = Combobox(window)
country_combobox['values'] = countries
country_combobox.current(0)
country_combobox.pack()

def get_country():
    name = name_entry.get()
    date = date_entry.get()
    address = address_entry.get()
    email = email_entry.get()
    phone = phone_entry.get()
    country = country_combobox.get()

    notion = name + date + address + email + phone + country
    messagebox.showinfo("Show Country", notion)
submit_btn = Button(window, text="Submit")
submit_btn['command'] = get_country
submit_btn.pack()

window.mainloop()'''

'''from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
w = Tk()
w.geometry('640x480')
w.title('Program')
m = Menu(master=w)
w.config(menu=m)
#Create command:
def cmd(act):
    print(act)

#Menu "Menu":
m_m = Menu(master=m,tearoff=0)
m.add_cascade(label='Menu',menu=m_m)
m_m.add_command(label='Open')
m_m.add_command(label='New')
m_m.add_command(label='Save')
m_m.add_command(label='Undo')
m_m.add_command(label='Redo')

#Menu "Options":
m_o = Menu(master=m,tearoff=0)
m.add_cascade(label='Options',menu=m_o)
m_o.add_command(label='Appearance & layout')
m_o.add_command(label='Preferences & tools')
m_o.add_command(label='Settings & configuration')

#Menu "Help":
m_h = Menu(master=m,tearoff=0)
m.add_cascade(label='Help',menu=m_h)
m_h.add_command(label='Guide')
m_h.add_command(label='Documentation')
m_h.add_command(label='About',command=lambda: cmd('ADU DẢK WÁ BỦH BỦH LMAO'))

w.mainloop()'''

'''from tkinter import *
w = Tk()
w.geometry("300x500")
w.title("Calculator")

f_1 = Frame(w, bg="#222", width=300, height=100)
f_1.propagate(0)
f_1.pack()
s = Entry(f_1, font=("Consolas",30))
s.pack()
f_2 = Frame(w, bg="#555", width=300, height=400)
f_2.grid_propagate(0)
f_2.pack()

def ins(var):
    s.insert(END,var)
def cal():
    result = None
    

b = Button(f_2, text='1')
b['command'] = lambda: ins('1')
b.grid(row=0,column=0)
b = Button(f_2, text='2')
b['command'] = lambda: ins('2')
b.grid(row=0,column=1)
b = Button(f_2, text='3')
b['command'] = lambda: ins('3')
b.grid(row=0,column=2)
b = Button(f_2, text='4')
b['command'] = lambda: ins('4')
b.grid(row=1,column=0)
b = Button(f_2, text='5')
b['command'] = lambda: ins('5')
b.grid(row=1,column=1)
b = Button(f_2, text='6')
b['command'] = lambda: ins('6')
b.grid(row=1,column=2)
b = Button(f_2, text='7')
b['command'] = lambda: ins('7')
b.grid(row=2,column=0)
b = Button(f_2, text='8')
b['command'] = lambda: ins('8')
b.grid(row=2,column=1)
b = Button(f_2, text='9')
b['command'] = lambda: ins('9')
b.grid(row=2,column=2)
b = Button(f_2, text='0')
b['command'] = lambda: ins('0')
b.grid(row=3,column=1)
b = Button(f_2, text='+')
b['command']
b.grid(row=3,column=0)
b = Button(f_2, text='-')
b['command']
b.grid(row=4,column=0)
b = Button(f_2, text='x')
b['command']
b.grid(row=3,column=2)
b = Button(f_2, text=':')
b['command']
b.grid(row=4,column=2)
b = Button(f_2, text='=')
b['command']
b.grid(row=4,column=1)

w.mainloop()'''

'''import tkinter

window = tkinter.Tk()
window.geometry("300x400")
window.title("Calculator")

frame_1 = tkinter.Frame(window, bg="#333", width=300, height=100)
frame_1.propagate(0)
frame_1.pack()

screen_entry = tkinter.Entry(frame_1, font=("Arial", 30))
screen_entry.pack()

frame_2 = tkinter.Frame(window, bg="#666", width=300, height=300)
frame_2.grid_propagate(0)
frame_2.pack()

number_1 = None
number_2 = None
operator = None
result = None


def insert_button(value):
    screen_entry.insert(tkinter.END, value)

def computer():
    result = None
    if operator == "+":
        result = number_1 + number_2
    elif operator == "-":
        result = number_1 - number_2
    elif operator == "x":
        result = number_1 * number_2
    elif operator == ":":
        result = number_1 / number_2
    return result


def calculate(new_operator):
    global number_1, number_2, operator
    screen_value = screen_entry.get()

    if number_1 == None:
        number_1 = int(screen_value)
    elif number_2 == None:
        number_2 = int(screen_value)

    if operator == None:
        operator = new_operator
        screen_entry.delete(0,tkinter.END)
        return

    if operator != None:
        number_1 = computer()
        number_2 = None
        screen_entry.delete(0,tkinter.END)
        screen_entry.insert(0, number_1)

    operator = new_operator
    if new_operator == "=":
        operator = None 

button = tkinter.Button(frame_2, text="1")
button['command'] = lambda: insert_button("1")
button.grid(row=0,column=0)

button = tkinter.Button(frame_2, text="2")
button['command'] = lambda: insert_button("2")
button.grid(row=0,column=1)

button = tkinter.Button(frame_2, text="3")
button['command'] = lambda: insert_button("3")
button.grid(row=0,column=2)

button = tkinter.Button(frame_2, text="4")
button['command'] = lambda: insert_button("4")
button.grid(row=1,column=0)

button = tkinter.Button(frame_2, text="5")
button['command'] = lambda: insert_button("5")
button.grid(row=1,column=1)

button = tkinter.Button(frame_2, text="6")
button['command'] = lambda: insert_button("6")
button.grid(row=1,column=2)

button = tkinter.Button(frame_2, text="7")
button['command'] = lambda: insert_button("7")
button.grid(row=2,column=0)

button = tkinter.Button(frame_2, text="8")
button['command'] = lambda: insert_button("8")
button.grid(row=2,column=1)

button = tkinter.Button(frame_2, text="9")
button['command'] = lambda: insert_button("9")
button.grid(row=2,column=2)

button = tkinter.Button(frame_2, text="0")
button['command'] = lambda: insert_button("0")
button.grid(row=3,column=0)

button = tkinter.Button(frame_2, text="=")
button['command'] = lambda: calculate("=")
button.grid(row=3,column=1)

button = tkinter.Button(frame_2, text="+")
button['command'] = lambda: calculate("+")
button.grid(row=3,column=2)

button = tkinter.Button(frame_2, text="-")
button['command'] = lambda: calculate("-")
button.grid(row=4,column=0)

button = tkinter.Button(frame_2, text="x")
button['command'] = lambda: calculate("x")
button.grid(row=4,column=1)

button = tkinter.Button(frame_2, text=":")
button['command'] = lambda: calculate(":")
button.grid(row=4,column=2)

window.mainloop()'''

'''import tkinter 

color = {
    'background': '#062F33',
    'question_bg': '#DFE9EA',
    'score_bg': '#575A5B',
    'text': 'white'
}



font_1 = ('Consolas', 30)
font_2 = ('Consolas', 10)

window = tkinter.Tk()
window.title("Ai la trieu phu")
window.geometry("800x500")
window.propagate(0)

# ===============================================================
# game frame
game_frame = tkinter.Frame(window, width=500, height= 500, bg=color['question_bg'])
game_frame.grid(row=0,column=0)

# ===============================================================
# question frame
question_frame = tkinter.Frame(game_frame, width=500, height= 300, bg=color['question_bg'])
question_frame.propagate(0)
question_frame.pack()

def question_display(question):
    question_label = tkinter.Label(question_frame, text=question, font=font_2, bg=color['question_bg'])
    question_label.pack(pady=100)

# ===============================================================
# answers frame
ans_frame = tkinter.Frame(game_frame, width=500, height= 200, bg=color['background'])
ans_frame.grid_propagate(0)
ans_frame.pack()

def ans_display(ans_list):
    ans_1 = tkinter.Button(ans_frame, width=20, height=2, font=font_2, text=ans_list[0])
    ans_1.grid(row=0, column=0, padx=5, pady=10)

    ans_2 = tkinter.Button(ans_frame, width=20, height=2, font=font_2, text=ans_list[1])
    ans_2.grid(row=0, column=1, padx=60, pady=10)

    ans_3 = tkinter.Button(ans_frame, width=20, height=2, font=font_2, text=ans_list[2])
    ans_3.grid(row=1, column=0, padx=5, pady=10)

    ans_4 = tkinter.Button(ans_frame, width=20, height=2, font=font_2, text=ans_list[3])
    ans_4.grid(row=1, column=1, padx=60, pady=10)

question_list = [
    ["1. Viet Nam thuoc chau luc nao",["Chau Au","Chau A","Chau Phi","Chau My","Chau A"]],
    ["2. Con vat nao co bon chan",["Con ca","Con ran","Con cho","Con chim","Con cho"]],
]

current_question = 1

question_display(question_list[current_question][0])
ans_display(question_list[current_question][1])

# ===============================================================
# score frame
score_frame = tkinter.Frame(window, width=300, height= 500, bg=color['score_bg'])
score_frame.grid(row=0,column=1)

window.mainloop()'''