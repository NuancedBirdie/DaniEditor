import tkinter as tk
import os
import playsound
from gtts import gTTS
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename

def open_file():
    """Open a file for editing."""
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    ent.delete("1.0", tk.END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        ent.insert(tk.END, text)
    window.title(f"Dani's Editor - {filepath}")

def save_file():
    """Save the current file as a new file."""
    filepath = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text = ent.get("1.0", tk.END)
        output_file.write(text)
    window.title(f"Dani's Editor - {filepath}")

def readfunc():
    tts = gTTS(text =ent.get("1.0", tk.END), lang='en')
    filename="DaniTemp.mp3"
    tts.save(filename)    
    playsound.playsound(filename)
    os.remove(filename)

def light():
    ent.configure({"bg": "white", "fg": "black"})

def dark():
    ent.configure({"bg":"black", "fg":"white"})

window = tk.Tk()
window.title("Dani's Editor")

ent = tk.Text(relief=tk.SUNKEN, fg="black", bg="white")
ent.pack(side=tk.BOTTOM)

btn_opn = tk.Button(text="Open", fg="pink", bg="black", padx=3, master=window, relief=tk.RAISED, command=open_file)
btn_opn.pack(side=tk.LEFT)

btn_save = tk.Button(text="Save", fg="pink", bg="black", padx=3, master=window, relief=tk.RAISED, command=save_file)
btn_save.pack(side=tk.LEFT)

btn_read = tk.Button(text="Read", fg="pink", bg="black", padx=3, master=window, relief=tk.RAISED, command=readfunc)
btn_read.pack(side=tk.LEFT)

btn_light = tk.Button(text="light", fg="pink", bg="black", padx=3, master=window, relief=tk.RAISED, command=light)
btn_light.pack(side=tk.RIGHT)

btn_dark = tk.Button(text="Dark", fg="pink", bg="black", padx=3, master=window, relief=tk.RAISED, command=dark)
btn_dark.pack(side=tk.RIGHT)

window.resizable(False,False)
window.wm_iconbitmap('Danicon2.ico')
window.mainloop()