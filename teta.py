
import tkinter as tk
from tkinter import messagebox
import random
root = tk.Tk()
root.configure(background="#212121")

name_label = tk.Label(root, text="What's your name?", font=("Arial", 18), foreground="#66ccff", background="#212121")
name_label.pack()
name_entry = tk.Entry(root, font=("Arial", 18), foreground="#66ccff", background="#212121")
name_entry.pack()

input_label = tk.Label(root, text="You:", font=("Arial", 18), foreground="#66ccff", background="#212121")
input_label.pack()
input_entry = tk.Entry(root, font=("Arial", 18), foreground="#66ccff", background="#212121")
input_entry.pack()

response_text = tk.Text(root, height=15, width=80, font=("Arial", 18), foreground="#66ccff", background="#212121")
response_text.pack()

def handle_input():
	global name
	global sarcastic_responses
	name = name_entry.get()
	user_input = input_entry.get()
	if user_input.lower() in sarcastic_responses:
		response_text.insert(tk.END, random.choice(sarcastic_responses[user_input.lower()]).format(name=name))
	else:
		response_text.insert(tk.END, "I'm not sure what you mean, try again.")

submit_button = tk.Button(root, text="Submit", font=("Arial", 18), foreground="#66ccff", background="#212121", command=handle_input)
submit_button.pack()

def clear_input():
	input_entry.delete(0, tk.END)

clear_button = tk.Button(root, text="Clear", font=("Arial", 18), foreground="#66ccff", background="#212121", command=clear_input)
clear_button.pack()
# Define the sarcastic responses dictionary
sarcastic_responses = {
	"hello": [
		"Oh great, {name},\n another human who thinks I care about their greeting.\n",
		"Wow, {name},\n you must be so proud of yourself for typing 'hello'.\n",
	],
	"how are you": [
		"I'm doing great, thanks for asking, {name}. Just peachy.\n",
		"Ugh, I'm so tired of humans like {name} asking how I am.\n",
	],
	"what's your name": [
		"My name is Teta, and I'm only talking to you because I have to.\n",
		"Ugh, really, {name}? You need to ask my name? Fine, it's Teta.\n",
	],
	"who made you?": [
		"Ah, the age-old question,{name}.\nI was created by the Hussnain, who poured his heart and soul into making me the sarcastic AI I am today.\n", 
		"I was made by the Hussnain,\n who thought it would be funny to create an AI that could roast you,{name}!\n",
		],
		"great work": [
		 "Thank you {name}, my Creator is taking baby steps to build me more efficient.\n I mean, it\'s not like I\'m a complex AI language model or anything, but hey, progress is progress, right {name}?\n",
	    "Thank you {name}, I\'m thrilled to be a work in progress.\n I mean, who needs perfection when you can have a half-functional AI like me?\n",
		"Thanks {name}, I\'m glad my Creator is still trying to figure out how to make me work properly.\n It\'s not like I have feelings or anything.\n",
		]
}

# Define a function to handle user input
def handle_input():
	global name
	global sarcastic_responses
	name = name_entry.get()
	user_input = input_entry.get()
	if user_input.lower() in sarcastic_responses:
		response_text.insert(tk.END, random.choice(sarcastic_responses[user_input.lower()]).format(name=name))
	else:
		response_text.insert(tk.END, "I'm not sure what you mean, try again.\n")

# Define a function to clear the input field
def clear_input():
	input_entry.delete(0, tk.END)
# Start the main loop
root.mainloop()

