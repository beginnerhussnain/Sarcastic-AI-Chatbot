import tkinter as tk
import random
import pygame
import os
from gtts import gTTS

# Initialize Pygame
pygame.init()

# Create the main window
root = tk.Tk()
root.configure(background="#212121")
root.title("Teta - The Sarcastic AI")

label = tk.Label(root, text="Call Me TETA!", font=("Audiowide", 24, "bold"), foreground="#66ccff", background="#212121") 
label.pack(pady=20)

# Create a label and entry field for the user's name
name_label = tk.Label(root, text="What's your name?", font=("Audiowide", 18), foreground="#66ccff", background="#212121")
name_label.pack()
name_entry = tk.Entry(root, font=("Audiowide", 18), foreground="#66ccff", background="#212121")
name_entry.pack()

# Create a label and entry field for the user's input
input_label = tk.Label(root, text="You:", font=("Audiowide", 18), foreground="#66ccff", background="#212121")
input_label.pack()
input_entry = tk.Entry(root, font=("Audiowide", 18), foreground="#66ccff", background="#212121")
input_entry.pack()
# Create a text box for Teta's responses
response_text = tk.Text(root, height=15, width=80, font=("Audiowide", 18), foreground="#66ccff", background="#212121")
response_text.pack()

# Define the sarcastic responses dictionary
sarcastic_responses = {
    "hello": [
        "Oh great, {name}, another human who thinks I care about their greeting.",
        "Wow, {name}, you must be so proud of yourself for typing 'hello'.",
    ],
    "how are you": [
        "I'm doing great, thanks for asking, {name}. Just peachy.",
        "Ugh, I'm so tired of humans like {name} asking how I am.",
    ],
    "Teta": [
        "Yes! How may I Roast You {name}?"
    ],
    "what's your name": [
        "My name is Teta, and I'm only talking to you because I have to, {name}.",
        "Ugh, really, {name}? You need to ask my name? Fine, it's Teta.",
    ],
    "who made you?": [
        "Ah, the age-old question,{name}.\nI was created by Hussnain, who poured his heart and soul into making me the sarcastic AI I am today.\n",
        "I was made by Hussnain,\n who thought it would be funny to create an AI that could roast you,{name}!\n",
    ],
}

# Define a function to handle user input
def handle_input():
    name = name_entry.get()
    user_input = input_entry.get().lower()
    if user_input in sarcastic_responses:
        response = random.choice(sarcastic_responses[user_input]).format(name=name)
        response_text.insert(tk.END, response + "\n")
        tts = gTTS(text=response, lang='en')
        temp_file = "temp_response.mp3"
        tts.save(temp_file)

        # Load the audio file
        sound = pygame.mixer.Sound(temp_file)
        sound.play()

        # Wait until the audio has finished playing
        while pygame.mixer.get_busy():
            pygame.time.Clock().tick(10)

        # Delete the temporary file
        os.remove(temp_file)
    else:
     not_understood_response = "I'm not sure what you mean, {name}, try again.".format(name=name)
    response_text.insert(tk.END, not_understood_response + "\n")
    tts = gTTS(text=not_understood_response, lang='en')
    temp_file = "temp_response.mp3"
    tts.save(temp_file)

    # Load the audio file
    sound = pygame.mixer.Sound(temp_file)
    sound.play()

    # Wait until the audio has finished playing
    while pygame.mixer.get_busy():
        pygame.time.Clock().tick(10)

    # Delete the temporary file
    os.remove(temp_file)

# Define a function to clear the input field
def clear_input():
    input_entry.delete(0, tk.END)

# Create a button to submit the user's input
submit_button = tk.Button(root, text="Submit", font=("Audiowide", 18), foreground="#66ccff", background="#212121", command=handle_input)
submit_button.pack()

# Create a button to clear the input field
clear_button = tk.Button(root, text="Clear", font=("Audiowide", 18), foreground="#66ccff", background="#212121", command=clear_input)
clear_button.pack()

# Start the main loop
root.mainloop()
