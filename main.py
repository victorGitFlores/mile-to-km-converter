from tkinter import *

FACTOR_KM = 1.60934

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=500, height=300)
window.config(pady=30, padx=30)

# Row 0
#label_plc1 = Label(text="__________ ")
#label_plc1.grid(row=0, column=0)

entry = Entry(width=5)
entry.grid(row=0, column=1)
# text to get the party started...
entry.insert(END, string="0")

label = Label(text="   Miles")
label.grid(row=0, column=2)

# Row 1
lbl_is_eq = Label(text="is equal to ")
lbl_is_eq.grid(row=1, column=0)

lbl_result = Label(text="0")
lbl_result.grid(row=1, column=1)

lbl_km = Label(text="Km")
lbl_km.grid(row=1, column=2)


# Row 2
def doit():
    # print("Well, do it!")
    # get the miles:
    miles = int(entry.get())
    # convert to k:
    km = round(miles * FACTOR_KM, 1)
    #update result with....km
    lbl_result.config(text=str(km))


button = Button(text="Calculate", command=doit)
button.grid(row=2, column=1)




















# this shld be the last line of code in program:
window.mainloop()   #this keeps the window on the screen...listening
