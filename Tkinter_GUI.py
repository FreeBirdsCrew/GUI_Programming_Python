from tkinter import *

window = Tk()
window.title("ItsExceptional")
window.geometry("300x200")
window.config(background = "black", pady=10)

lb1 = Label(window, text = "Login Form", bg = "black", fg="white", font=20)
lb1.place(x=110, y=5)

lb2_u = Label(window, text = "Username - ", bg="black", fg="white")
lb2_u2 = Entry(window)
lb2_u.place(x=10, y=40)
lb2_u2.place(x=110, y=40)

lb2_p = Label(window, text = "Password - ", bg="black", fg="white")
lb2_p2 = Entry(window)
lb2_p.place(x=10, y=80)
lb2_p2.place(x=110,y=80)


display = Label(window, text="Access : ", bg="black")

bt = Button(window, text="Login")

def dis():
    user = lb2_u2.get()
    pas = lb2_p2.get()
    filo = open('register.txt').readlines()
    for lino in filo:
        if user == lino.split()[2]:
            display.config(bg="green",fg="white", text="Access :Granted")
            break
        else:
            display.config(bg="red",fg="white", text="Access :Denied")

bt.config(command=dis)
bt.place(x=110, y=120)

def newsign():
    sign=Tk()
    sign.title("SignUp")
    sign.geometry("300x200")
    sign.config(background = "black", pady=10)

    lbs = Label(sign, text = "SignUp", bg = "black", fg="white", font=20)
    lbs.place(x=110, y=5)

    lb2_s = Label(sign, text = "Username - ", bg="black", fg="white")
    lb2_s2 = Entry(sign)
    lb2_s.place(x=10, y=40)
    lb2_s2.place(x=110, y=40)

    lb2_ps = Label(sign, text = "Password - ", bg="black", fg="white")
    lb2_ps2 = Entry(sign)
    lb2_ps.place(x=10, y=80)
    lb2_ps2.place(x=110,y=80)

    dis = Label(sign, text ="", bg="black", fg="white")
    
    def reg():
        username = lb2_s2.get()
        pas = lb2_ps2.get()
        
        file =  open("register.txt","a")
        fiIn = open('register.txt').readlines()

        l=[] 
        for lines in fiIn:
            l.append(lines.split()[1])

        if username in l:
            print("Exists")
            dis.config(text="User Exists", bg="green")

        else:
            print("not Exists")
            file.write("Username = "+username+"\n")
            file.write("Password = "+pas+"\n")
            file.close()
            dis.config(text = "Registered", bg="green")
                    
    bts = Button(sign, text="Register", command=reg)
    bts.place(x=110, y=120)
    dis.place(x=100, y=150)

    window.destroy()

bt2 = Button(window, text="SignUp", command=newsign)
bt2.place(x=170, y=120)

display.place(x=110, y=155)
