import pandas as pd
import ephem
import tkinter as tk

def calculate_twilights():
    entered_position = enter_location.get()
    string_position = entered_position.split('/')
    position = [float(x) for x in string_position]
    
    date = enter_date.get()
    date = pd.Timestamp(date) + pd.Timedelta(12, "h") # date is at midnight by default, by moving to noon "next rising" is the day after
    
    earth = ephem.Observer()
    earth.lat = str(position[0])
    earth.lon = str(position[1])
    earth.date = date

    sun = ephem.Sun()
    sun.compute()
    
    earth.horizon = "-18"

    # ephem throws an "AlwaysUpError" when there is no astronomical twilight (which occurs in Summer in nordic countries)
    try:
        evening_twilight = ephem.localtime(earth.next_setting(sun))
        evening["text"] = evening_twilight
    except ephem.AlwaysUpError:
        evening["text"] = "never!"

    try:    
        morning_after_twilight = ephem.localtime(earth.next_rising(sun))
        morning["text"] = morning_after_twilight

    except ephem.AlwaysUpError:
        morning["text"] = "never!"

# create window and resize it
window = tk.Tk()
window.title("Astronomical twilight calculator")
window.resizable(width = True, height = False)
window.geometry("1200x500")

# create date fields and add text 
date_entry = tk.Frame(master=window)
enter_date = tk.Entry(master=date_entry, width=20, font=('Calibri',25))
date_label = tk.Label(master=date_entry, text="Date (yyyy-mm-dd): ", font=('Calibri',25))

# create location fields and add text 
location_entry = tk.Frame(master=window)
enter_location = tk.Entry(master=location_entry, width=20, font=('Calibri',25))
location_label = tk.Label(master=location_entry, text="Location (lat/lon): ", font=('Calibri',25))

# position date and location labels (operating on objects tk.Frame)
enter_date.grid(row=0, column=1, sticky="e")
date_label.grid(row=0, column=0, sticky="w")
enter_location.grid(row=0, column=1, sticky="e")
location_label.grid(row=0, column=0, sticky="w")

# create button to calculate
button = tk.Button(
    master=window,
    text="Calculate night!",
    command=calculate_twilights,
    font=('Calibri',25)
)

# create results labels for evening start and morning end of night
evening_label = tk.Label(master=window, text="Full dark night starts at: ", font=('Calibri',25))
morning_label = tk.Label(master=window, text="Full dark night ends at: ", font=('Calibri',25))
evening = tk.Label(master=window, text="", font=('Calibri',25))
morning = tk.Label(master=window, text="", font=('Calibri',25))

# position all labels on window (operating on object tk.Tk())
date_entry.grid(row=0, column=0, padx=10)
location_entry.grid(row=1, column=0, padx=10)
button.grid(row=2, column=0, pady=10)
evening_label.grid(row=3, column=0, sticky="w")
evening.grid(row=3, column=1, padx=10)
morning_label.grid(row=4, column=0, sticky="w")
morning.grid(row=4, column=1, padx=10)

window.mainloop()