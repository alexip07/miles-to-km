import tkinter as tk


# window sett

window = tk.Tk()
window.title("Mile to Km Converter")
window.minsize()
window.config(padx=20, pady=20)
# label sett

miles_label = tk.Label(text="Miles")
miles_label.grid(column=2, row=0)

my_label = tk.Label(text="is equal to")
my_label.grid(column=0, row=1)

km_label = tk.Label(text="Km")
km_label.grid(column=2, row=1)

km_label_results = tk.Label(text="0")
km_label_results.grid(column=1, row=1)

# entry sett

input_value = tk.Entry(width=7)
input_value.grid(column=1, row=0)

# button sett


def convert():
    miles = float(input_value.get())
    km = miles * 1.609
    km_label_results.config(text=f"{km}")


conv_button = tk.Button(text="Calculate", command=convert)
conv_button.grid(column=1, row=2)
window.mainloop()
