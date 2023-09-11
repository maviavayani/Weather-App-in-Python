import tkinter
from tkinter import*
from tkinter import ttk
import requests      # request module run the API or URL in Python File

def data_get():
    city = city_name.get()
    data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=2163710a5aff97785936139a3ac13171").json()   #Weather API jo list or dictionary ki form main ha
    w_label1.config(text=data["weather"][0]["main"])
    wd_label1.config(text=data["weather"][0]["description"])
    temp_label1.config(text=str(int(data["main"]["temp"]-273.15)))
    pre_label1.config(text=data["main"]["pressure"])
    Humidity_label1.config(text=data["main"]["humidity"])

win = Tk()
win.title("Weather App")
win.config(bg="lightblue")
win.geometry("500x650")


name_label = Label(win,text="Weather App",font=("Arial",35,"bold"))
name_label.place(x=25,y=50,height=50,width=450)

city_name = StringVar()
list_txt = ["Karachi","Lahore","Faisalabad","Rawalpindi","Gujranwala","Peshawar","Multan","Saidu Sharif","Hyderabad","Islamabad","Murree","Quetta","Cantonment"]
com = ttk.Combobox(win,values=list_txt,font=("Arial",15,"bold"),textvariable=city_name)
com.place(x=25,y=120,height=50,width=450)
com.set("Karachi")

done_button = Button(win,text="Done",font=("Arial",30,"bold"),command=data_get)
done_button.place(x=200,y=190,height=50,width=100)

w_label = Label(win,text="Weather Climate",font=("Arial",17))
w_label.place(x=25,y=260,height=50,width=210)
w_label1 = Label(win,text="",font=("Arial",17))
w_label1.place(x=250,y=260,height=50,width=210)

wd_label = Label(win,text="Weather Description",font=("Arial",17))
wd_label.place(x=25,y=330,height=50,width=210)
wd_label1 = Label(win,text="",font=("Arial",17))
wd_label1.place(x=250,y=330,height=50,width=210)

temp_label = Label(win,text="Temperature",font=("Arial",17))
temp_label.place(x=25,y=400,height=50,width=210)
temp_label1 = Label(win,text="",font=("Arial",17))
temp_label1.place(x=250,y=400,height=50,width=210)

pre_label = Label(win,text="Pressure",font=("Arial",17))
pre_label.place(x=25,y=470,height=50,width=210)
pre_label1 = Label(win,text="",font=("Arial",17))
pre_label1.place(x=250,y=470,height=50,width=210)


Humidity_label = Label(win,text="Humidity",font=("Arial",17))
Humidity_label.place(x=25,y=540,height=50,width=210)
Humidity_label1 = Label(win,text="",font=("Arial",17))
Humidity_label1.place(x=250,y=540,height=50,width=210)




tkinter.mainloop()