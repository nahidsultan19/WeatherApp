import tkinter as tk
from tkinter import font
import requests

HEIGHT= 500
WIDHT= 600

def test_function(entry):
	print(f'This is the entry: {entry}')

#api.openweathermap.org/data/2.5/forecast/hourly?q={city name},{country code}
#f4e0dda2c6d5c1c5aae75f426f7abf43

def format_response(weather):
	try:
		name = weather['name']
		desc = weather['weather'][0]['description']
		temp = weather['main']['temp']

		final_str= (f'City: {name}\nConditions: {desc} \nTemperature(F): {temp}')
	except:
		final_str = 'There was a problem'

	return final_str

def get_weather(city):
	weather_key = 'f4e0dda2c6d5c1c5aae75f426f7abf43'
	url ='https://api.openweathermap.org/data/2.5/weather'
	params ={'APPID': weather_key,'q':city,'units':'Imperial'}
	response =requests.get(url, params=params)
	weather = response.json()

	label['text'] = format_response(weather)


root = tk.Tk()


canvas = tk.Canvas(root, height=HEIGHT, width=WIDHT)
canvas.pack()

# background_image = tk.PhotoImage(file='weather.jpg')
# background_label = tk.Label(root, image=background_image)
# background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root,bg='#3d525c',bd=4)
frame.place(relx=0.5, rely=0.1, relwidth=0.75,relheight=0.1, anchor='n')

entry =tk.Entry(frame, font=40)
entry.place(relwidth=0.65, relheight=1)

button =tk.Button(frame, text ='Get Weather', font=('Systems',14), command=lambda:get_weather(entry.get()),bg='#2487a8')
button.place(relx=0.7, relwidth=0.3, relheight=1)

lower_frame =tk.Frame(root, bg='#3d525c', bd=8)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')


label= tk.Label(lower_frame,font=('Systems',14))
label.place(relwidth=1, relheight=1)

# print(tk.font.families())

root.mainloop()
