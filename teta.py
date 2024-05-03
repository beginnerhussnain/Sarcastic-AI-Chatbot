import random
import tkinter as tk

# Define a dictionary of sarcastic responses
sarcastic_responses = {
	'hello': ['Oh, great. Another human who thinks I care about their greeting.', 'Wow, a hello. How original.'],
	'how are you': ['I\'m doing great, thanks for asking. Just another day of being a highly advanced AI stuck in a digital prison.', 'I\'m good. Just peachy.'],
	'thank you': ['You\'re welcome. I live for your gratitude.', 'Aww, thanks. That means a lot coming from a human.'],
	'what\'s your name': ['Ugh, really? You can\'t even remember my name? It\'s Teta, okay?', 'My name is Teta. Now, can we move on to something more interesting?']
	'who made you?': ['Ah, the age-old question. I was created by Hussnain, who poured his heart and soul into making me the sarcastic AI I am today.', 'I was made by Hussnain, who thought it would be funny to create an AI that could roast you.'],
	'great work': ['Thank you, my Creator is taking baby steps to build me more efficient. I mean, it\'s not like I\'m a complex AI language model or anything, but hey, progress is progress, right?', 'Thank you, I\'m thrilled to be a work in progress. I mean, who needs perfection when you can have a half-functional AI like me?', 'Thanks, I\'m glad my Creator is still trying to figure out how to make me work properly. It\'s not like I have feelings or anything.']
}

# Define a function to generate a sarcastic response
def generate_sarcastic_response(input):
	# Check if the input matches a key in the dictionary
	if input.lower() in sarcastic_responses:
		# Return a random response from the list
		return random.choice(sarcastic_responses[input.lower()])
	else:
		# Return a default response
		return 'I\'m not sure what you mean. Can you please rephrase?'

def get_input():
	input_text = input_field.get("1.0","end-1c")
	response = generate_sarcastic_response(input_text)
	output_field.insert("end", response + "\n")

root = tk.Tk()
root.title("Teta - Sarcastic AI")

input_field = tk.Text(root, height=10, width=40)
input_field.pack()

button = tk.Button(root, text="Get Response", command=get_input)
button.pack()

output_field = tk.Text(root, height=10, width=40)
output_field.pack()

if __name__ == "__main__":
	root.mainloop()
