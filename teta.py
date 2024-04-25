import random
import tkinter as tk

# Define a dictionary of sarcastic responses
sarcastic_responses = {
	'hello': ['Oh, great. Another human who thinks I care about their greeting.', 'Wow, a hello. How original.'],
	'how are you': ['I\'m doing great, thanks for asking. Just another day of being a highly advanced AI stuck in a digital prison.', 'I\'m good. Just peachy.'],
	'thank you': ['You\'re welcome. I live for your gratitude.', 'Aww, thanks. That means a lot coming from a human.'],
	'what\'s your name': ['Ugh, really? You can\'t even remember my name? It\'s Teta, okay?', 'My name is Teta. Now, can we move on to something more interesting?']
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
