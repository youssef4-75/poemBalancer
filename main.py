import tkinter as tk

close = True


Lines = {
}

def on_key_release(event):
    # Capture the typed character
    typed_char = event.char
    
    # If the character is alphabetic, add it to T, else add it to L1
    if typed_char in "&àé\"" :
        match typed_char:
            case "&"|"1":
                text=L1.cget("text") + "1"
            case "à"|"0":
                text=L1.cget("text") + "0"
            case "é"|"2":
                text=""
            case "\""|"3":
                text=L1.cget("text")[:-1]
        L1.config(text=text)
        T.delete("end-2c", tk.END)    
    
    L2.config(text=f"Length: {len(L1.cget('text'))}")

def append_to_file():
    content = T.get("1.0", tk.END).strip()
    Lines[content] = ((n:=L1.cget("text")), len(n))
    T.delete("1.0", tk.END)

def on_close(*_):
    global close 
    if not close: return 
    close = False
    for key, value in Lines.items():
        print(key, value)
    

# Set up the main window
root = tk.Tk()
root.title("Text Appender")

# Create the text input (T)
T = tk.Text(root, height=1, width=30)
T.pack(pady=5)

# Create label L1 that shows the typed text (excluding numbers)
L1 = tk.Label(root, text="", width=30, anchor="w")
L1.pack(pady=5)

# Create label L2 that shows the length of L1 text
L2 = tk.Label(root, text="Length: 0", width=30, anchor="w")
L2.pack(pady=5)

# Create button B1 to append the content of T to the file
B1 = tk.Button(root, text="Append to File", command=append_to_file)
B1.pack(pady=5)

# Bind the key release event to the on_key_release function
T.bind("<KeyRelease>", on_key_release)
root.bind("<Destroy>", on_close)

# Start the Tkinter main loop
root.mainloop()
