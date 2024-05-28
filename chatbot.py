import json
import random
import tkinter as tk
from tkinter import messagebox

#Read the dataset
with open ("faqs.json", "r") as file:
    data=json.load(file)
    

#extract intents from faqs.json
intents = data["intents"]


# No answer responses
no_response = ["Sorry, can't understand you", "Please give me more info", "Not sure I understand"]



def get_response(user_input):
    for intent in intents:
        for pattern in intent["patterns"]:
            if user_input.lower() == pattern.lower():
                return random.choice(intent["responses"])
    return random.choice(no_response);



def send_message(event=None):
    user_input=entry.get()
    if user_input.strip() !="":
        chat_log.config(state=tk.NORMAL)
        chat_log.insert(tk.END, "You : "+ user_input +"\n\n")
        chat_log.insert(tk.END, "Bot : "+get_response(user_input)+"\n\n")
        chat_log.config(state=tk.DISABLED)
        entry.delete(0, tk.END)
        
        
        
root = tk.Tk()
root.title("Zahra ChatBot")

frame = tk.Frame(root)
chat_log = tk.Text(frame, width=50, height=20, state=tk.DISABLED)
scrollbar = tk.Scrollbar(frame, command=chat_log.yview)
entry=tk.Entry(frame, width=40)
send_button=tk.Button(frame, text="Send", command = send_message)


chat_log.grid(row=0, column=0, padx=(10,0), pady=(10,0), sticky="ew")
scrollbar.grid(row=0, column =1, sticky = "ns")
entry.grid(row=1, column=0,padx=10, pady=10, sticky="ew")
send_button.grid(row=1, column=1, padx=10, pady=10)

frame.pack(pady=20)
entry.bind("<Return>", send_message)
root.mainloop()




        
