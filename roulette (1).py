#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import time
import random
import Roulette_functions as rf
import FreeSimpleGUI as fsg

# Create GUI
layout = [
    [fsg.Text("Enter your name:"), fsg.InputText(key="name_input")],
    [fsg.Text("Add Money:"), fsg.InputText(key="money_input")],
    [fsg.Text("Choose a number between 1 and 12:"), fsg.InputText(key="num_input")],
    [fsg.Text("Choose red or black:"), fsg.InputOptionMenu(["red", "black"], key="color_input")],
    [fsg.Button("Play", button_color=(None, "green"))],
    [fsg.Text("", key="number_output")],  # Display generated random number
    [fsg.Text("", key="color_output")],   # Display generated random color
    [fsg.Text("", key="result_output")],  # Empty Text element for displaying results
]

window = fsg.Window("Roulette", layout)

while True:
    event, values = window.read()
    if event == fsg.WINDOW_CLOSED:
        break
    elif event == "Play":
        rf.play_roulette(window,values)

window.close()

