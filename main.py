import tkinter as tk
from tkinter import PhotoImage
from PIL import Image, ImageTk
import subprocess

def start_game_pyfile(pyfile_name):
    root.withdraw()
    root.update()
    subprocess.run(["python", pyfile_name])
    root.deiconify()

# Ana pencere
root = tk.Tk()
root.title("Mini Game Hub")
root.geometry("600x700")
root.resizable(False, False)

# Arka plan resmi
background_image = Image.open("assets/background.jpg")
background_photo = ImageTk.PhotoImage(background_image.resize((600, 700)))

background_label = tk.Label(root, image=background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Başlık
title = tk.Label(root, text="🎮 Mini Game Hub 🎮", font=("Comic Sans MS", 32, "bold"), bg="#000000", fg="white")
title.pack(pady=30)

# Buton için ikonlar
snake_icon = ImageTk.PhotoImage(Image.open("assets/snake_icon.jpeg").resize((40, 40)))
pong_icon = ImageTk.PhotoImage(Image.open("assets/pong_icon.jpeg").resize((40, 40)))
tictactoe_icon = ImageTk.PhotoImage(Image.open("assets/tictactoe_icon.jpeg").resize((40, 40)))

# Buton Stili
def create_game_button(parent, text, icon, file_name):
    btn = tk.Button(
        parent,
        text=f"  {text}",
        image=icon,
        compound="left",
        font=("Arial", 20),
        bg="#4CAF50",
        fg="white",
        activebackground="#45a049",
        padx=10,
        pady=10,
        bd=0,
        width=300,
        anchor="w",
        cursor="hand2",
        command=lambda: start_game_pyfile(file_name)
    )
    def on_enter(e): btn.config(bg="#388E3C")
    def on_leave(e): btn.config(bg="#4CAF50")
    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)
    btn.pack(pady=15)

# Oyun Butonları
create_game_button(root, "Snake", snake_icon, "snake.py")
create_game_button(root, "Pong", pong_icon, "pong.py")
create_game_button(root, "Tic Tac Toe", tictactoe_icon, "tictactoe.py")

# Çıkış
exit_button = tk.Button(
    root,
    text="Çıkış",
    font=("Arial", 20),
    bg="#f44336",
    fg="white",
    activebackground="#e53935",
    padx=10,
    pady=10,
    bd=0,
    width=300,
    cursor="hand2",
    command=root.quit
)
exit_button.pack(pady=30)

root.mainloop()
