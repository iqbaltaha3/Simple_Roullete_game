#!/usr/bin/env python
# coding: utf-8

# In[ ]:
import time
import random
import FreeSimpleGUI as fsg

def generate_random_number():
    time.sleep(5)
    return random.randint(1, 12)

def generate_random_color():
    colors = ["red", "black"]
    time.sleep(5)
    return random.choice(colors)

def calculate_earnings(money, color, num, chosen_color, random_num):
    if color == chosen_color and num == random_num:
        return money * 100
    elif color == chosen_color and num != random_num:
        return round(money * 0.48)
    elif color != chosen_color and num == random_num:
        return round(money * 0.98)
    else:
        return 0
    
def play_roulette(window,values):
    
    name = window["name_input"].get()
    try:
        money = int(window["money_input"].get())
    except ValueError:
        fsg.error("Please enter an integer for money.")
        return
    
    try:
        num = int(window["num_input"].get())
        if num < 1 or num > 12:
            raise ValueError("Please choose a number between 1 and 12.")
    except ValueError:
        fsg.error("Please enter a number between 1 and 12.")
        return
    
    color = values["color_input"]
    
    # Display "Generating random number..." on the window
    window["number_output"].update("Generating random number...")
    window.refresh()
    
    # Generate random number
    random_num = generate_random_number()
    
    # Display the generated random number on the window
    window["number_output"].update(f"Generated random number: {random_num}")
    window.refresh()
    time.sleep(1)
    
    # Display "Generating random color..." on the window
    window["color_output"].update("Generating random color...")
    window.refresh()
    
    # Generate random color
    chosen_color = generate_random_color()
    
    # Display the generated random color on the window
    window["color_output"].update(f"Generated random color: {chosen_color}")
    window.refresh()
    time.sleep(1)
    
    # Check if number or color matches
    if num == random_num and color == chosen_color:
        result_message = "Congratulations, you won! Both number and color matched."
        text_color = "green"
    elif num == random_num:
        result_message = "Only Number matched."
        text_color = "Yellow"
    elif color == chosen_color:
        result_message = "Only Color matched."
        text_color = "Yellow"
    else:
        result_message = "Sorry, you didn't win. Try again."
        text_color = "red"
    
    total_earnings = calculate_earnings(money, color, num, chosen_color, random_num)
    
    # Update the text of the result_output Text element with the result
    window["result_output"].update(f"{result_message}\n{name}, your total earnings are {total_earnings}", text_color=text_color)  
    

