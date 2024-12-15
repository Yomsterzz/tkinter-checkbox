import tkinter as tk

def show():
    data = []
    if option1.get():
        data.append("Yes, I like dogs.")
    if option2.get():
        data.append("Yes, I like cats.")
    if option3.get():
        data.append("Yes, I like fish.")
    
    print(data)

window = tk.Tk()
window.title("Checkboxes")
window.geometry("800x800")

option1 = tk.BooleanVar(value = False)
option2 = tk.BooleanVar(value = True)
option3 = tk.BooleanVar(value = True)

check1 = tk.Checkbutton(window, text="Do you like dogs?", variable=option1, font=("Arial", 20))
check1.pack()

check2 = tk.Checkbutton(window, text="Do you like cats?", variable=option2, font=("Arial", 20))
check2.pack()

check3 = tk.Checkbutton(window, text="Do you like fish?", variable=option3, font=("Arial", 20))
check3.pack()

show_results = tk.Button(window, text="Show All", font=("Arial", 20), command=show)
show_results.pack()


window.mainloop()