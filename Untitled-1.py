from tkinter import *
import phonenumbers
from phonenumbers import carrier
from phonenumbers import geocoder
from opencage.geocoder import OpenCageGeocode
import folium
import webbrowser

root = Tk()
root.title("Phone Number Tracker")
root.geometry("385x595+300+200")
root.resizable(False, False)
root.configure(bg="black")
key = "d2b3af88e38b4b5bb6e04f77a89e39f3"

def track():
    enter_nb = entry.get()
    number = phonenumbers.parse(enter_nb)

    location = geocoder.description_for_number(number, "en")
    country.config(text=location)

    service = carrier.name_for_number(number, "en")
    sim.config(text=service)

    query = str(location)
    results = OpenCageGeocode(key).geocode(query)

    lat = results[0]['geometry']['lat']
    lng = results[0]['geometry']['lng']

    myMap = folium.Map(location=[lat, lng], zoom_start=9)

    folium.Marker([lat, lng], popup=location).add_to(myMap)
    myMap.save("mylocation.html")

def show_map():
    webbrowser.open("mylocation.html")

# Create a colored box instead of an image
canvas = Canvas(root, width=100, height=100, bg="blue")
canvas.place(x=130, y=40)

heading = Label(root, text="Phone Number Tracker", font=("arial", 15, "bold"), bg="black", fg="white")
heading.place(x=100, y=190)

entry = StringVar()
enter_nb = Entry(root, textvariable=entry, font=("arial", 15), width=15, bd=5, relief=GROOVE)
enter_nb.place(x=100, y=250)

search_button = Button(root, text="Search", font=("arial", 15, "bold"), bg="black", fg="white", relief=GROOVE, command=track)
search_button.place(x=150, y=300)

country = Label(root, text="Country", font=("arial", 15, "bold"), bg="black", fg="white")
country.place(x=150, y=350)

sim = Label(root, text="Service Provider", font=("arial", 15, "bold"), bg="black", fg="white")
sim.place(x=150, y=400)

open_map_btn = Button(root, text="Open in Map", font=("arial", 15, "bold"), bg="black", fg="white", relief=GROOVE, command=show_map)
open_map_btn.place(x=120, y=450)

root.mainloop()