# PySimpleGUI Basic Usage Demo
# Mr. Scott
# Nov 15, 2023
# Input/Output using pop-up windows (PySimpleGUI)

# Import The PySimpleGUI Module
import PySimpleGUI as sg  #sg → simplegui

# Getting a string from the user.   sg. → look inside the sg library, and run...
name = sg.popup_get_text("Please enter a name:")
if name == None:
    print("pressed cancel or X")
    
# How to display some text in a popup window:
greeting = "Hello there, " + name + ". Nice to see you!"
sg.popup(greeting)
sg.popup(greeting, title="TEST", background_color="black")



