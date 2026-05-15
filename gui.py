import tkinter as tk
from tkinter import ttk, scrolledtext
from datetime import datetime
from chatbot_logic import analyze_input

def send_message():
    user_input = entry.get()
    if not user_input:
        return

    chat_box.config(state=tk.NORMAL)
    chat_box.insert(tk.END, "You: " + user_input + "\n", "user")
    chat_box.config(state=tk.DISABLED)
    entry.delete(0, tk.END)

    response = analyze_input(user_input.lower())

    if response == "exit":
        chat_box.config(state=tk.NORMAL)
        chat_box.insert(tk.END, "Bot: Goodbye!\n", "bot")
        chat_box.config(state=tk.DISABLED)
        auto_scroll()
        root.after(1000, root.destroy)
        return

    chat_box.config(state=tk.NORMAL)
    chat_box.insert(tk.END, "Bot: " + response + "\n", "bot")
    chat_box.config(state=tk.DISABLED)
    auto_scroll()

def auto_scroll():
    chat_box.see(tk.END)

# Window
root = tk.Tk()
root.title("AI Chatbot")
root.geometry("500x600")
root.config(bg="#1a1a1a")

# Bot avatar/title frame
header_frame = tk.Frame(root, bg="#2a2a2a", height=80)
header_frame.pack(fill=tk.X, pady=(0, 10))
header_frame.pack_propagate(False)

# Bot avatar (using a simple text representation)
avatar_label = tk.Label(header_frame, text="🤖", font=("Arial", 24), bg="#2a2a2a", fg="white")
avatar_label.pack(side=tk.LEFT, padx=20, pady=20)

# Bot title
title_label = tk.Label(header_frame, text="AI Assistant", font=("Arial", 16, "bold"), bg="#2a2a2a", fg="white")
title_label.pack(side=tk.LEFT, pady=20)

# Chat display with scrollbar
chat_frame = tk.Frame(root, bg="#1a1a1a")
chat_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

chat_box = scrolledtext.ScrolledText(
    chat_frame, 
    height=20, 
    width=60,
    bg="black", 
    fg="white",
    font=("Arial", 10),
    wrap=tk.WORD,
    state=tk.DISABLED
)
chat_box.pack(fill=tk.BOTH, expand=True)

# Configure text tags for different colors
chat_box.tag_config("user", foreground="#00ff00", font=("Arial", 10, "bold"))
chat_box.tag_config("bot", foreground="#00bfff", font=("Arial", 10))

# Input frame
input_frame = tk.Frame(root, bg="#1a1a1a")
input_frame.pack(fill=tk.X, padx=10, pady=(0, 10))

entry = tk.Entry(input_frame, width=40, bg="#2a2a2a", fg="white", font=("Arial", 10))
entry.pack(side=tk.LEFT, padx=(0, 10), fill=tk.X, expand=True)

send_btn = tk.Button(input_frame, text="Send", command=send_message, bg="#4a4a4a", fg="white", font=("Arial", 10, "bold"))
send_btn.pack(side=tk.LEFT)

# Welcome message
chat_box.config(state=tk.NORMAL)
chat_box.insert(tk.END, "Bot: Hello! I'm your AI assistant. How can I help you today?\n", "bot")
chat_box.config(state=tk.DISABLED)

root.mainloop()
