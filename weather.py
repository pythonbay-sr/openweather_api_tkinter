import requests, json
import tkinter
from tkinter import *
from PIL import ImageTk, Image
import pyglet


#Set up the Program

root = tkinter.Tk()
root.title("Weather")
root.geometry("1152x700")
root.resizable(width=False, height=False)
root.configure(bg="#323999")

img = ImageTk.PhotoImage(Image.open(r"C:\\Users\\Nikola Kostic\\Desktop\\weather_template.png"))
panel = Label(root, image = img)
panel.place(x=0, y=0)

pyglet.font.add_file(r"C:\\Users\\Nikola Kostic\\Desktop\\Poppins-Regular.ttf")

#OpenWeather API

def check():
    # API base URL
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"

    # City Name
    CITY = Text_Entry.get()

    # Your API key
    API_KEY = "63b6494c53ed8a38142f66dfd26eb59f"

    # updating the URL
    URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY

    # Sending HTTP request
    response = requests.get(URL)

    # checking the status code of the request
    if response.status_code == 200:
            
        # retrieving data in the json format
        data = response.json()
        
        # take the main dict block
        main = data['main']
        
        # getting temperature
        temperature = main['temp']
        # getting feel like
        temp_feel_like = main['feels_like']  
        # getting the humidity
        humidity = main['humidity']
        # getting the pressure
        pressure = main['pressure']
        
        # weather report
        weather_report = data['weather']
        # wind report
        wind_report = data['wind']
        
        City_Label = Label(root, text=(f"City: {CITY}") , font=("Poppins", 20), fg="#fff", bg="#A5A8B0")
        City_Label.place(x=210, y=180)

        Temperature_Label = Label(root, text=(f"Temperature: {temperature}"), font=("Poppins", 20), fg="#fff", bg="#A5A8B0")
        Temperature_Label.place(x=210, y=230)

        Feels_Like_Label = Label(root, text=(f"Feels like: {temp_feel_like}") , font=("Poppins", 20), fg="#fff", bg="#A5A8B0")
        Feels_Like_Label.place(x=210, y=280)

        Humidity_Label = Label(root, text=(f"Humidity: {humidity}") , font=("Poppins", 20), fg="#fff", bg="#A5A8B0")
        Humidity_Label.place(x=210, y=330)

        Pressure_Label = Label(root, text=(f"Pressure: {pressure}") , font=("Poppins", 20), fg="#fff", bg="#A5A8B0")
        Pressure_Label.place(x=520, y=180)

        Weather_Report_Label = Label(root, text=(f"Weather Report: {weather_report[0]['description']}") , font=("Poppins", 20), fg="#fff", bg="#A5A8B0")
        Weather_Report_Label.place(x=520, y=230)

        Wind_Speed_Label = Label(root, text=(f"Wind Speed: {wind_report['speed']}") , font=("Poppins", 20), fg="#fff", bg="#A5A8B0")
        Wind_Speed_Label.place(x=520, y=280)
    else:
        # showing the error message
        print("Error in the HTTP request")


#City Question Label

City_Question_Label = Label(root, text="Enter the name of the city : " , font=("Poppins", 20), fg="#fff", bg="#A5A8B0")
City_Question_Label.place(x=225, y=420)


#Text Entry

Text_Entry = Entry(root, font=("Century Gothic", 15), width=30)
Text_Entry.place(x=230, y=490)


#Enter Button

Enter_Button = Button(root, text="Enter", font=("Century Gothic", 15), fg="#fff", bg="#7b7b7b", width=10, command=check, relief=FLAT)
Enter_Button.place(x=590, y=485)


#Root Mainloop

root.mainloop()
