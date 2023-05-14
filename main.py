from tkinter import Tk, Frame, Scrollbar, Label, END, Entry, Text, VERTICAL, Button, font
from tkinter.scrolledtext import ScrolledText
import random

# Chatbot responses
bot_responses = [
    "Hello!",
    "How are you?",
    "Tell me more.",
    "That's interesting.",
    "I'm sorry to hear that.",
    "What do you think about that?",
    "I'm glad you shared that with me."
]



# Function to send a message
def send_message(event=None):
    message = entry_box.get()
    chat_log.config(state='normal')
    chat_log.insert(END, "You: " + message + "\n")
    chat_log.see(END)

    bot_response = random.choice(bot_responses)
    chat_log.insert(END, "Bot: " + bot_response + "\n")
    chat_log.see(END)

    chat_log.config(state='disabled')
    entry_box.delete('0', 'end')


# Function to reset the conversation
def reset_conversation():
    chat_log.config(state='normal')
    chat_log.delete('1.0', END)
    chat_log.config(state='disabled')


# Creating the main window
window = Tk()
window.title("Chatbox")

# Styling
window.configure(bg="#F2F2F2")
window.geometry("400x500")
window.resizable(width=False, height=False)
window.option_add("*Font", "Helvetica 11")

# Creating the chat log display
chat_log = ScrolledText(window, width=50, height=20, bg="#FFFFFF", fg="#333333", relief="flat",
                        font=font.Font(family="Helvetica", size=11))
chat_log.pack(pady=10)

# Creating the message entry box
entry_frame = Frame(window, bg="#F2F2F2")
entry_frame.pack(fill='x', padx=10, pady=10)
entry_box = Entry(entry_frame, bg="#FFFFFF", relief="flat", font=font.Font(family="Helvetica", size=11))
entry_box.pack(side='left', fill='x', expand=True)
entry_box.bind("<Return>", send_message)
send_button = Button(entry_frame, text="Send", command=send_message, bg="#2196F3", fg="#FFFFFF",
                     relief="flat", font=font.Font(family="Helvetica", size=11, weight="bold"))
send_button.pack(side='right')

# Adding a chat log title
chat_log_title = Label(window, text="Chat Log", bg="#F2F2F2", font=font.Font(family="Helvetica", size=12, weight="bold"))
chat_log_title.pack()

# Adding a separator line
separator = Frame(window, height=2, bd=1, relief="sunken", bg="#CCCCCC")
separator.pack(fill='x')

# Creating the reset button
reset_button = Button(window, text="Reset Conversation", command=reset_conversation, bg="#F44336", fg="#FFFFFF",
                      relief="flat", font=font.Font(family="Helvetica", size=11, weight="bold"))
reset_button.pack(pady=10)

# Running the main window loop
window.mainloop()
