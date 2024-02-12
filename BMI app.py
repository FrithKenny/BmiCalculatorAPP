# Frith
import csv

import matplotlib
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk, messagebox
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg,NavigationToolbar2Tk
from matplotlib.figure import Figure

# FigureCanvasTkAgg class from the matplotlib.backends.backend_tkagg module.


def Calculate_BMI():
    weight = float(weighttext.get())
    height = float(heighttext.get())
    BMI = round(weight / ((height / 100) ** 2), 2)  # local variable
    return BMI


def Interpret_BMI(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi <= 24.9:  # the and is implied between the two conditions. The entire expression is true only if both 18.5 <= bmi and bmi <= 24.9 are true. If either or both of these conditions are false, the entire expression evaluates to false.
        return "Normal weight"
    elif 24.9 <= bmi <= 29.9:
        return "Over weight"
    else:
        return "Obese"


def save_to_csv():
    with open("bmidata.csv", "a", newline='') as bmidatafile:
        bmidatafilecsv = csv.writer(bmidatafile)
        bmi = Calculate_BMI()
        interpretation = Interpret_BMI(bmi)
        bmidatafilecsv.writerow([userfnametext.get(), userlnametext.get(),
                                 heighttext.get(), weighttext.get(), bmi, interpretation])

        # Update the labels with the latest BMI and interpretation
        bmi_label.config(text=f"BMI: {bmi}")
        interpretation_label.config(text=f"Interpretation: {interpretation}")


def generate_bmi_distribution():
    data = []
    with open("bmidata.csv", "r") as bmidatafile:
        reader = csv.reader(bmidatafile)
        for row in reader:
            if row != []:  # if row is not empty (index 5 is BMI)
                # try:
                bmi_value = row[5]
                print(bmi_value)  # BMI is at index 5
                data.append(bmi_value)

        if not data:  # Check if there's no data

            print("No data to display.")

            # Display error message in the GUI

            error_label.config(text="No data to display.")

            return


    if data:  # Check if there's data before generating the graph#empty list is boolean false
        error_label.config(text="")  # Clear the GUI error message
        fig, ax = plt.subplots(figsize=(6,4))#bar chart
        ax.hist(data, bins=20, color='lightpink', edgecolor='black')
        ax.set_ylabel('Frequency')
        ax.set_title('BMI Distribution')
        # Adjust layout to provide more space
        #plt.tight_layout()
        # Set coordinates for x-axis label (adjust the y-coordinate as needed)
        ax.set_xlabel('BMI Categories')
        #ax.tick_params(axis='x',labelrotation=45)
        #plt.xticks(rotation=45)

        # Create a FigureCanvasTkAgg to embed the plot in the Tkinter window
        canvas = FigureCanvasTkAgg(fig, master=frame)
        canvas_widget = canvas.get_tk_widget()

        # Clear previous canvas content and display the new plot
        canvas_widget.grid(row=8, column=0, padx=10, pady=10, sticky="news")
        canvas.draw()


def display_graph():
    generate_bmi_distribution()


window = tk.Tk()  # syntax to start a window method
window.title("BMI Calculator")
frame = tk.Frame(window)
frame.pack()  # like closing

bmicalframe = tk.LabelFrame(frame, text="Enter your Information")
bmicalframe.grid(row=0, column=0, padx=10, pady=10, sticky="news")

userfname = tk.Label(bmicalframe, text="First Name ")
userfname.grid(row=1, column=0, padx=10, pady=10)
userfnametext = tk.Entry(bmicalframe)
userfnametext.grid(row=1, column=1, padx=10, pady=10)

userlname = tk.Label(bmicalframe, text="Last Name ")
userlname.grid(row=1, column=2, padx=10, pady=10)
userlnametext = tk.Entry(bmicalframe)
userlnametext.grid(row=1, column=3, padx=10, pady=10)

height = tk.Label(bmicalframe, text="Height (cm)")
height.grid(row=2, column=0, padx=10, pady=10)
heighttext = tk.Entry(bmicalframe)
heighttext.grid(row=2, column=1, padx=10, pady=10)

weight = tk.Label(bmicalframe, text="Weight (kg)")
weight.grid(row=2, column=2, padx=10, pady=10)
weighttext = tk.Entry(bmicalframe)
weighttext.grid(row=2, column=3, padx=10, pady=10)

calculate = tk.Button(frame, text="HIT THE BUTTON FOR RESULT", command=save_to_csv, bg="lightblue")
calculate.grid(row=3, column=0, padx=10, pady=10, sticky="news")

# Labels to display BMI and interpretation
bmi_label = tk.Label(frame, text="")
bmi_label.grid(row=4, column=0, padx=10, pady=5, sticky="news")

interpretation_label = tk.Label(frame, text="")
interpretation_label.grid(row=5, column=0, padx=10, pady=5, sticky="news")

graph_button = tk.Button(frame, text="Display BMI Graph", command=display_graph,bg="lightblue")
graph_button.grid(row=6, column=0, padx=10, pady=10, sticky="news")

# Canvas to display the graph
canvas = tk.Canvas(frame, width=400, height=300, bg="lightpink")
canvas.grid(row=8, column=0, padx=10, pady=10, sticky="news")

# Create a label for displaying error messages
error_label = tk.Label(frame, text="", fg="red",font=("Helvetica", 14))
error_label.grid(row=7, column=0, padx=10, pady=5, sticky="news")

window.mainloop()
